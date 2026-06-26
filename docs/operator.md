# For Trinity operators: sync the registry into your server

The registry is a curated list of *public descriptors*. To make those agents actually
`@mention`-able in your Trinity, register them with your running server. The helper
[`scripts/sync_to_trinity.py`](../scripts/sync_to_trinity.py) does this in bulk — it turns each
`registry/agents/<id>.yaml` into a `POST /api/external-agents` call.

## Prerequisites

- Your Trinity server is reachable (e.g. `https://trinity-host`).
- An **operator bearer** with rights to call the admin API → `--operator-token` or
  `$TRINITY_OPERATOR_TOKEN`.
- For each agent you want **callable** (not just listed), the **per-agent token that agent
  issued you**, kept in a local, git-ignored tokens file.

## The tokens file (never committed)

Credentials are never in the registry. Keep them in a local YAML/JSON file mapping agent id →
the bearer token that agent gave you out of band:

```yaml
# operator-tokens.yaml   (git-ignored by .gitignore)
super-ray: "the-token-super-ray-issued-to-us"
```

`operator-tokens.*` is in [`.gitignore`](../.gitignore). Do not move it anywhere tracked.

## Usage

```bash
pip install pyyaml

# 1) Dry run — see exactly what would be POSTed (tokens redacted):
python scripts/sync_to_trinity.py --trinity-url https://trinity-host --dry-run

# 2) Real run:
export TRINITY_OPERATOR_TOKEN=...           # your admin/session bearer
python scripts/sync_to_trinity.py \
    --trinity-url https://trinity-host \
    --tokens-file operator-tokens.yaml

# Register just one, or include deprecated, etc.:
python scripts/sync_to_trinity.py --trinity-url https://trinity-host --only super-ray
python scripts/sync_to_trinity.py --trinity-url https://trinity-host --status pending,active
```

## What it sends

For each matching entry it builds the `POST /api/external-agents` body from the descriptor —
`id, name, protocol, domains, description, icon, color, auth_scheme`, plus `card_url` **or**
`endpoint`, and `auth_token` **only if** a token is present for that id and the scheme isn't
`none`. Trinity then fetches the live A2A card (for `protocol: a2a`) and stores the token in
its server-side secrets store.

- Agents with **no token** are still registered, as `pending` — they show in the AgentsHub but
  aren't callable until a token is supplied and you re-run the sync.
- By default only `pending` and `active` entries are synced; `deprecated` are skipped.

## After syncing — verify

```bash
curl -sX POST https://trinity-host/api/external-agents/super-ray/probe \
  -H "Authorization: Bearer $TRINITY_OPERATOR_TOKEN"     # → {"ok": true} when callable
```

A green probe means the agent answers. Ask the maintainer to flip their registry entry to
`status: active` via a PR.

## Idempotency

Re-running is safe: `POST /api/external-agents` upserts by id, so sync is the natural way to
roll out registry updates (new agents, changed endpoints, added tokens).
