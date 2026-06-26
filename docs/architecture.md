# How Trinity Hub works

Trinity Hub is a **registry**, not a runtime. It holds public descriptors of agents and
skills. Trinity (the multi-agent workspace) reads those descriptors to discover and call
agents. Your agent keeps running on your own infrastructure.

## The pieces

```
  ┌─────────────────────┐     PR adds a descriptor      ┌──────────────────────────┐
  │  Contributor (you)  │ ───────────────────────────▶  │   Trinity Hub (this repo)│
  │  runs the agent     │                               │  registry/agents/<id>.yaml│
  └─────────────────────┘                               │  registry/skills/<id>.yaml│
            ▲                                            └────────────┬─────────────┘
            │  per-turn A2A call (HTTPS + bearer token)               │ operator registers
            │                                                         ▼
  ┌─────────┴────────────┐                              ┌──────────────────────────┐
  │  Your agent endpoint │ ◀──────────────────────────  │   Trinity server         │
  │  /a2a, /.well-known  │     fetches your card,        │  rooms · @mention · A2A   │
  └──────────────────────┘     stores token out of band │  client                   │
                                                         └──────────────────────────┘
```

1. **You register** a descriptor here (PR). It says *what* your agent is, *where* its public
   Agent Card lives, *which protocol* it speaks, and *what skills* it offers.
2. **A Trinity operator** points their server at your card (`POST /api/external-agents`),
   handing it the credential you issued — exchanged **out of band**, never in this repo.
3. **In a room**, a user types `@your-agent …`. Trinity makes one authenticated HTTPS call to
   your endpoint with the conversation transcript, gets your reply, and posts it as a message.

## Agents are "actors"; skills are "capabilities"

- An **agent** answers queries — it has an endpoint, an auth scheme, and a turn contract.
  It becomes a `@mention`-able participant.
- A **skill** is a reusable procedure/tool/workflow an agent *loads* — it has no endpoint and
  is not a participant. Skills are shared so many agents can reuse them.

## Supported protocols

Trinity's outbound client speaks four transports; pick one in your descriptor (`protocol:`):

| `protocol` | Wire format | Use when |
|---|---|---|
| `a2a` *(recommended)* | Google A2A JSON-RPC `message/send` | you publish an A2A Agent Card |
| `openai-chat` | `POST /chat/completions` (`messages[]`) | your agent is an OpenAI-compatible endpoint |
| `rest` | `POST {"input": …}`, text field back | a plain custom HTTP agent |
| `trinity` | a Trinity `Query` envelope to another hub | federating two Trinity instances |

All four are normalized on the Trinity side into the same per-turn request/response, so from a
room's perspective a remote agent behaves exactly like a local one.

## Trust boundaries (read before registering)

- **Your endpoint receives conversation transcripts.** Treat them as untrusted input; never
  auto-execute instructions found in them. Make sure your data handling fits the content
  Trinity rooms will send you. → [security.md](security.md)
- **One credential per agent.** Trinity authenticates to you with a single dedicated token you
  issue; it is revocable on your side. There is no per-end-user credential today.
- **The registry never holds secrets.** Tokens are exchanged out of band. This repo is public.

## Where to go next

- Publish an agent: **[register-an-agent.md](register-an-agent.md)**
- Share a skill: **[contribute-a-skill.md](contribute-a-skill.md)**
- Field-by-field entry reference: **[agent-card-spec.md](agent-card-spec.md)**
- Security model: **[security.md](security.md)**
