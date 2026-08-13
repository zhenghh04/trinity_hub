# API access — talk to Trinity over HTTP

Everything you do in the chat window is also available over a small HTTP API, so
you can call Trinity from a script, a notebook, another agent, or CI. The endpoint
speaks the [A2A](https://google.github.io/A2A/) `message/send` and `message/stream`
shapes: you `POST` a text query and get either a single final answer (blocking) or
a live event stream (tokens + tool-call cards as they happen).

!!! info "Base URL"
    The hosted deployment is **`https://trinityscience.org`**. A self-hosted
    or local server is **`http://localhost:8765`**. Substitute your host in the
    examples below.

## 1. Get a token

Every call carries a **bearer token**. Mint one from a logged-in Trinity session —
it's scoped to calling an agent's `/query` endpoint and runs work **as you** ("talk
to *my* Trinity"):

```bash
# You need a Trinity user session cookie/JWT to mint an agent token.
curl -sX POST "https://trinityscience.org/api/agents/trinity/token" \
  -H "Authorization: Bearer $TRINITY_SESSION_JWT" \
  -H "Content-Type: application/json" \
  -d '{"ttl_hours": 168}'
```

Returns:

```json
{
  "access_token": "eyJhbGciOi...",
  "token_type": "Bearer",
  "expires_in": 604800,
  "scope": "agent:query agent:skills.read agent:knowledge.read",
  "jti": "44055a4f53064582847acdac66ee338b"
}
```

- `ttl_hours` defaults to 24, max 720 (30 days).
- Save the `access_token` — that's the value you pass as `Authorization: Bearer …`.
- The `jti` is the token's unique id; an operator can revoke this single token
  without rotating the server secret. Keep the token secret; treat it like a password.

Store it in an env var so you don't paste it into every command:

```bash
export TRINITY_TOKEN="eyJhbGciOi..."
```

## 2. Ask a question (blocking)

The default path blocks until the whole turn finishes, then returns **one JSON
envelope** with the final answer. Simplest to script, but for a long turn (an HPC
job, a build) the caller waits with no feedback.

```bash
curl -sX POST "https://trinityscience.org/api/agents/trinity/query" \
  -H "Authorization: Bearer $TRINITY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"parts":[{"kind":"text","text":"Which systems is LAMMPS built for in the catalog?"}]}'
```

Response:

```json
{
  "kind": "message",
  "status": "completed",
  "parts": [{"kind": "text", "text": "LAMMPS is supported on polaris, aurora, ..."}]
}
```

This returns only the final text — no intermediate tool calls.

## 3. Stream the response (recommended for interactive use)

Opt into **`message/stream`** to watch Trinity work in real time: token-by-token
text *and* a card for each tool call, over the same token and endpoint. No more
silent multi-minute wait.

Opt in **any** of three ways — `?stream=1` on the URL, an `Accept: text/event-stream`
header, or `"stream": true` in the body — and read with `curl -N` (unbuffered):

```bash
curl -N -X POST "https://trinityscience.org/api/agents/trinity/query?stream=1" \
  -H "Authorization: Bearer $TRINITY_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -d '{"parts":[{"kind":"text","text":"Which systems is LAMMPS built for in the catalog?"}]}'
```

You get a [Server-Sent Events](https://developer.mozilla.org/docs/Web/API/Server-sent_events)
stream — one `data:` line per frame — ending in `[DONE]`:

```
data: {"type":"session_id","id":"api-a1b2","task_id":"tk-9f3","project_id":"api"}
data: {"type":"thinking_start"}
data: {"type":"thinking_delta","text":"check the catalog first..."}
data: {"type":"tool_complete","name":"mcp__catalog__search_software","input":{"name":"lammps"},"result":"...","is_error":false}
data: {"type":"text_delta","text":"LAMMPS is supported on "}
data: {"type":"text_delta","text":"polaris, aurora, perlmutter, frontier, and crux."}
data: {"type":"done"}
data: [DONE]
```

| Frame `type` | Meaning |
|---|---|
| `session_id` | Sent first; carries the `task_id` and session `id`. |
| `thinking_start` / `thinking_delta` | Extended-reasoning tokens (if shown). |
| `tool_complete` | One card per tool call — `name`, `input`, `result`, `is_error`. |
| `text_delta` | A chunk of the answer, streamed as it's generated. |
| `done` | The turn finished (includes cost/turn totals). |
| `[DONE]` | Stream terminator. |

You'll also see `: keepalive` comment lines roughly every 15 s so a long tool call
isn't dropped by an intermediary, and on reconnect the server replays the backlog
so you don't miss frames.

## 4. Multi-turn conversations

Pass a **`conversation_id`** to thread follow-up turns — Trinity keeps the history
and replays it into each turn. Reuse the same id to continue; omit it for a fresh,
stateless one-shot each call.

```bash
curl -sX POST "https://trinityscience.org/api/agents/trinity/query" \
  -H "Authorization: Bearer $TRINITY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"conversation_id":"my-lammps-thread",
       "parts":[{"kind":"text","text":"And which of those use GPUs?"}]}'
```

- **No `conversation_id`** → fresh context, nothing persisted.
- **With `conversation_id`** → the turn is threaded and saved under your identity.

## Request envelope reference

The body is an A2A Query. Only `parts` is required.

| Field | Type | Notes |
|---|---|---|
| `parts` | list | `[{"kind":"text","text":"..."}]` — your message. Required. |
| `conversation_id` | string | Thread id for multi-turn (see above). |
| `stream` | bool | `true` to stream (equivalent to `?stream=1`). |
| `intent` | object | Optional structured intent (goal, stopping criteria) merged into the prompt. |
| `budget` | object | Optional cost/time budget hint merged into the prompt. |
| `message_id` | string | Echoed back as `in_reply_to` for correlation. |

## Troubleshooting

!!! warning "`502 Bad Gateway` or an empty stream from `localhost`"
    If `curl` returns 502 (even for `/api/health`) or the stream produces nothing,
    your machine likely has a **system-wide HTTP proxy** (common on lab-managed
    Macs / VPN setups) and `curl` is routing `localhost` through it. Bypass it:

    ```bash
    curl -N --noproxy '*' -X POST "http://localhost:8765/api/agents/trinity/query?stream=1" ...
    ```

    This only affects same-host calls behind a proxy; remote HTTPS calls don't need it.

- **`401 / not authenticated`** — the token is missing, expired, or from a different
  server. Mint a fresh one (step 1). Agent tokens carry `agent:query`; a token without
  it is rejected.
- **First call is slow (~10 s pause after `session_id`)** — Trinity's MCP tool servers
  are warming up on the first request; subsequent calls start faster.
- **`404 Agent not found`** — check the agent id in the path (`trinity` is the
  general-purpose front-door agent).
