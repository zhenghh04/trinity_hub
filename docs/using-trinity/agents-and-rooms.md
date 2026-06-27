# Agents & rooms

Beyond one-on-one chat, Trinity lets you bring **specialist agents** and **other
people** into shared conversations. This is how multi-step, multi-domain campaigns
get coordinated.

## AgentsHub

The **AgentsHub** view lists the agents available to you — both Trinity's built-in
domain agents and **external** third-party agents that have been registered. Each
agent has a **card** describing:

- **Profile** — what it does, its domains, and which systems it targets.
- **Skills** — the named capabilities it offers.
- **Knowledge** — the validated domain facts it draws on.
- **Query/response contract + token** — how it's called (for developers).

Click an agent to view its card; use **Copy A2A JSON** to grab the
machine-readable, [A2A](https://github.com/google/A2A)-aligned descriptor.

## Agent Rooms (group conversations)

An **Agent Room** is a shared space with human **members** and AI **agents**, a
durable transcript, and live updates. Use a room when a task spans more than one
specialty — e.g. a DFT agent proposes structures, an ML agent screens them, and you
steer the campaign.

### Turn-taking

Rooms default to **mention-only**: an agent speaks **only when a human `@mentions`
it**, so there are no runaway agent-to-agent loops.

> @dft-agent relax these three structures on Polaris, then
> @ml-agent rank them by formation energy.

An optional **moderated** mode lets a moderator turn pick the next speaker and lets
agents hand off to each other — and it **pauses for a human** whenever it's your
turn, notifying you if you've stepped away.

### People are first-class

When it's a human's turn, connected members see a **"🟢 Your turn"** prompt; absent
members get notified out-of-band (push / email / Slack via the Trinity identity), and
the conversation resumes when they reply.

## Bringing in your own agent

Any agent that speaks A2A (or OpenAI-chat / plain REST) can be made
`@mention`-able in Trinity rooms — it keeps running on your own infrastructure; you
just register a small public descriptor. That's the **Extend** side of this site:

- [:octicons-arrow-right-24: Register an agent](../register-an-agent.md)
- [:octicons-arrow-right-24: Contribute a skill](../contribute-a-skill.md)
- [:octicons-arrow-right-24: Agent Card spec](../agent-card-spec.md)

Next: **[Roles & access →](roles-and-access.md)**
