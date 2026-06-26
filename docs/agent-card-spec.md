# Field reference: registry entries & the A2A Agent Card

There are **two related documents** in play. Don't confuse them:

| | Registry entry (this repo) | A2A Agent Card (your server) |
|---|---|---|
| Lives in | `registry/agents/<id>.yaml` | `https://<HOST>/.well-known/agent-card.json` |
| Purpose | discovery + curation in Trinity Hub | the runtime contract Trinity calls |
| Format | Trinity Hub YAML (`trinity.hub.agent/v1`) | Google A2A `AgentCard` JSON |
| Validated by | [`schemas/agent_entry.schema.json`](../schemas/agent_entry.schema.json) | the A2A spec |
| Contains secrets? | **Never** | Never (it's public discovery) |

This page documents the **registry entry**. For the A2A card fields, see
[register-an-agent.md §B1](register-an-agent.md#b1-a-discoverable-agent-card).

## Registry entry fields (`trinity.hub.agent/v1`)

| Field | Req | Type | Notes |
|---|:--:|---|---|
| `schema` | ✓ | const | `trinity.hub.agent/v1` |
| `id` | ✓ | string | `^[a-z0-9][a-z0-9-]*$`; unique; equals the filename; your `@mention` handle |
| `name` | ✓ | string | Human-readable display name |
| `owner` | ✓ | string | Organization or person responsible |
| `maintainers` | ✓ | list | ≥1 `{github, contact}` — how a maintainer reaches you |
| `type` | ✓ | enum | `external` (you host it) · `trinity-local` (ships with Trinity) |
| `protocol` | ✓ | enum | `a2a` · `openai-chat` · `rest` · `trinity` |
| `discovery` | ✓ | object | `card_url` **or** `endpoint` (HTTPS only); `card_url` preferred for `a2a` |
| `auth` | ✓ | object | `{scheme: bearer\|api_key\|none}` — **no token value** |
| `domains` | ✓ | list | Tags used for discovery, e.g. `[ptychography, xrf-tomography]` |
| `description` | ✓ | string | One or two sentences: what it helps with |
| `skills` | ✓ | list | `{id, description}` per advertised skill (≥1) |
| `homepage` | – | url | Human-facing page or repo (HTTPS) |
| `icon` | – | string | An emoji or HTTPS image URL |
| `color` | – | string | Hex accent, e.g. `#0ea5e9` |
| `status` | ✓ | enum | `pending` · `active` · `deprecated` |
| `added` | ✓ | string | `YYYY-MM` you registered |

### `discovery` object

```yaml
discovery:
  card_url: https://<HOST>/.well-known/agent-card.json   # preferred for protocol=a2a
  # OR (if you have no A2A card):
  endpoint: https://<HOST>/a2a
```

- For `protocol: a2a`, give `card_url` — Trinity fetches the live card and derives the endpoint.
- For `openai-chat` / `rest`, give `endpoint` directly (the chat/completions or custom URL).
- All URLs must be **`https://`**. Plaintext HTTP entries are rejected.

### `auth` object

```yaml
auth:
  scheme: bearer        # bearer | api_key | none
  header: X-API-Key     # only for scheme: api_key (optional; default X-API-Key)
```

There is **no `token` field by design.** The credential Trinity uses to call you is exchanged
out of band and stored only on the Trinity server. See [security.md](security.md).

## Skill entry fields (`trinity.hub.skill/v1`)

See [contribute-a-skill.md](contribute-a-skill.md) for the full template. Required:
`schema, id, name, owner, maintainers, description, trigger, domains, source.repo, status, added`.

## Validation

Every entry is checked against [`schemas/`](../schemas/) by `scripts/validate_registry.py`
locally and by CI on every PR. Run it before you push:

```bash
python scripts/validate_registry.py
```
