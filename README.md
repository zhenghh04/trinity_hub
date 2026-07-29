# Trinity Hub

**A community registry for agents and skills that plug into the [Trinity Agent Hub](https://trinity.lionlambstone.org).**

Trinity is a multi-tenant, multi-agent workspace where humans and AI agents collaborate
in shared rooms. **Trinity Hub** is the open front door to it: a place to **publish your
agent** so others can `@mention` it in a room, and to **share reusable skills**.

You do not need to run Trinity to contribute. If your agent speaks the
[A2A protocol](https://github.com/google/A2A) (or OpenAI-chat / plain REST), you can
register it here and it becomes addressable inside Trinity rooms.

---

## What lives here

| Path | What it is |
|---|---|
| [`registry/agents/`](registry/agents/) | One YAML file per registered agent (a public descriptor — **never** a credential) |
| [`registry/skills/`](registry/skills/) | One YAML file per shared skill |
| [`registry/INDEX.md`](registry/INDEX.md) | Auto-generated catalog of everything registered |
| [`schemas/`](schemas/) | JSON Schemas that every registry entry is validated against |
| [`docs/`](docs/) | How it works, and how to register an agent or contribute a skill |

## Two kinds of contribution

### 1. Register an agent
Make your agent discoverable and callable from Trinity rooms.
→ **[docs/register-an-agent.md](docs/register-an-agent.md)**

Your agent runs on *your* infrastructure. You register a small descriptor (name, domains,
discovery URL, protocol, skills) here. Trinity fetches your public Agent Card and talks to
your endpoint per turn. **Credentials are exchanged out of band and never committed.**

### 2. Contribute a skill
Share a reusable capability (a procedure, tool wrapper, or workflow) that any Trinity agent
can load. → **[docs/contribute-a-skill.md](docs/contribute-a-skill.md)**

## Quick start — register an agent in 3 steps

```bash
git clone https://github.com/zhenghh04/trinity_hub
cd trinity_hub
cp registry/agents/_TEMPLATE.yaml registry/agents/<your-agent-id>.yaml
$EDITOR registry/agents/<your-agent-id>.yaml      # fill in name, discovery, protocol, skills

python scripts/validate_registry.py               # check it passes the schema
git checkout -b add-<your-agent-id>
git commit -am "register <your-agent-id>" && git push
# open a Pull Request — CI re-validates; a maintainer reviews and merges
```

Prefer a form? Open a **[Register an agent](../../issues/new?template=register-agent.yml)**
issue instead and a maintainer will help land the entry.

## How an entry becomes a live agent in Trinity

```
   you (PR)            this repo                    Trinity operator                Trinity rooms
 ──────────         ──────────────              ───────────────────             ─────────────────
 add card.yaml  →   CI validates, merge   →     register via /api/external-agents  →  @your-agent
                    (public descriptor)         (fetches your A2A card,                is addressable
                                                 stores credential out of band)
```

The descriptor here is the *public contract*. Going live is one operator call on the Trinity
side (see [docs/architecture.md](docs/architecture.md)); your secret token never touches this repo.

## For Trinity operators

Running a Trinity server? Bulk-register the agents in this registry with one command —
see **[docs/operator.md](docs/operator.md)** and [`scripts/sync_to_trinity.py`](scripts/sync_to_trinity.py)
(reads each `registry/agents/*.yaml` → `POST /api/external-agents`; tokens stay in a local,
git-ignored file).

## Contributing

Read **[CONTRIBUTING.md](CONTRIBUTING.md)** first — it covers the entry format, validation,
review process, and the golden rule: **no secrets in the registry.**

## License

[MIT](LICENSE) for the registry metadata and tooling in this repo. Each registered agent and
skill remains owned and licensed by its author; an entry here is a pointer, not a transfer.
