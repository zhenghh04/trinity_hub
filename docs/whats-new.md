# What's new

Dates below are when each feature reached the production Trinity server.
Subscribe via the [RSS feed](feed.xml) to get new entries in your reader.

<div class="tx-timeline" markdown>

## 2026-08-23 — Redesigned interface, attachments, artifact gallery & more

A large batch of updates reaches the production server:

- **Redesigned interface** — a rebuilt, faster web UI is now the default, with a
  consistent visual language across chat, Settings, and Admin, and a
  theme-following look throughout.
- **Attach files in the composer** — upload, drag-and-drop, or paste files
  straight into a message, the way you would in ChatGPT or Claude.
- **Artifact gallery** — plots, reports, and other files your session produces
  are collected per session so you can find and open them in one place, with
  inline preview for images and video.
- **Better file viewer** — LaTeX and Fortran syntax highlighting, optional
  one-click LaTeX compile, a line-wrap toggle, a collapsible file tree, and a
  manual refresh button.
- **Pick your model per chat** — a per-session model picker, plus the ability to
  register your own model providers (with write-only API keys) from Settings.
- **Smarter sidebar** — full-text search with ranked, highlighted snippets across
  folder names and conversation content; a *By Project* / *By Recent* toggle;
  activity ordering; and inline folder rename / move.
- **Sub-sessions** — work that a chat spawns in the background now appears as its
  own nested session under its parent, and status dots show when it's *your turn*
  versus a background agent still working.
- **Interrupted chats resume** — if a turn is cut off (a disconnect or restart),
  Trinity now safely picks it back up without re-running work it already did.
- **Reviews & scientist feedback** — campaign owners can invite reviewers, and a
  review dashboard lets scientists read runs and write structured feedback back.
- **Modernized terminal** — GPU-accelerated rendering, clickable links, in-terminal
  search, and automatic reconnect.
- **Monthly schedules** — schedule recurring tasks on a day-of-month interval.
- **API access** — mint a personal bearer token from Settings to call Trinity's
  `/query` endpoint from your own scripts. See [API access](using-trinity/api-access.md).
- **Customizable keyboard shortcuts** and a thinking-level control in the composer.

## 2026-07-29 — Trinity Hub launches

The community registry and this documentation site go live: register your own
agent or skill and make it `@mention`-able in any Trinity room without running
Trinity yourself. See [Register an agent](register-an-agent.md) and
[Contribute a skill](contribute-a-skill.md).

## 2026-07-11 — Usage tab, persistent sessions, opencode engine

- **Usage tab** — track token usage and estimated cost by day, project, and
  model from the dashboard.
- **Persistent, steerable sessions** — long-running chats survive reconnects,
  and you can steer a task while it's still running instead of waiting for it
  to finish.
- **opencode engine** — Trinity can drive non-Claude models (including
  open-weight models on ALCF inference endpoints) through the same chat
  interface.

## 2026-06-29 — Three-hub model

Trinity's backend reorganizes around three hubs — **Agent Hub**, **Skill
Hub**, and **Workflow Hub** — the foundation the community registry builds on.
See [How Trinity Hub works](architecture.md).

## 2026-06-19 — Group chat and mobile app

Shared rooms let multiple people and agents collaborate in one conversation;
a companion mobile app (Expo) brings Trinity to iOS and Android.

</div>

---

Have a request or found a bug? [Open an issue](https://github.com/zhenghh04/trinity_hub/issues)
or reach out to the maintainer.
