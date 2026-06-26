# Contribute a skill

A **skill** is a reusable capability — a procedure, tool wrapper, or workflow — that any
Trinity agent can load to do something specific (e.g. "predict a XANES spectrum", "submit a
PBS job", "search the literature"). Unlike an agent, a skill has **no endpoint** and is not a
conversational participant; it's a unit an agent *uses*.

Registering a skill here advertises it and points to where it lives, so others can discover
and adopt it.

## 1. Add the descriptor

```bash
cp registry/skills/_TEMPLATE.yaml registry/skills/<id>.yaml
```

```yaml
schema: trinity.hub.skill/v1
id: xanes-analysis                 # lowercase [a-z0-9-]; unique
name: XANES Analysis
owner: ALCF / Argonne National Laboratory
maintainers:
  - github: your-handle
    contact: team@example.org
description: >-
  Predict and benchmark Ti K-edge XANES spectra with LightshowAI + Materials Project,
  including similarity metrics and energy-shift optimization.
trigger: >-
  "predict XANES for <material>", "benchmark XANES", "Ti K-edge spectrum"
domains: [materials-science, xanes, spectroscopy]
inputs: Material id or structure; absorbing element; optional reference spectrum.
outputs: Predicted spectrum, similarity metrics, optional plot.
source:
  repo: https://github.com/your-org/your-repo
  path: .claude/skills/xanes-analysis        # optional, where it lives in the repo
  license: MIT
requirements: >-
  Materials Project API key; LightshowAI MCP server (optional).
status: active                     # active | experimental | deprecated
added: "2026-06"
```

## 2. Validate and open a PR

```bash
pip install pyyaml jsonschema
python scripts/validate_registry.py
python scripts/build_index.py
git checkout -b add-skill-<id> && git commit -am "add skill <id>" && git push -u origin add-skill-<id>
```

## 3. What makes a good skill entry

- **A precise `trigger`.** This is how an agent (or a person) knows when to reach for it.
  Write the phrases that should invoke it.
- **Clear `inputs`/`outputs`.** A planner needs to know what to feed it and what comes back.
- **A real `source.repo`.** The skill itself lives in your repo (e.g. a `SKILL.md` plus
  scripts); the entry here is a pointer. List the `license` so adopters know the terms.
- **Honest `requirements`.** API keys, MCP servers, system access — say what's needed.
- **No secrets.** Same golden rule as agents: never commit keys or tokens.

## 4. Skill vs. agent — which am I contributing?

| | Skill | Agent |
|---|---|---|
| Has an endpoint? | No | Yes |
| `@mention`-able in a room? | No | Yes |
| What it is | a capability an agent *loads* | an actor that *answers* |
| Register via | `registry/skills/<id>.yaml` | `registry/agents/<id>.yaml` |

If your thing answers questions over an HTTP endpoint, it's an **agent** —
see [register-an-agent.md](register-an-agent.md).

## 5. Format conventions for the skill itself (recommendation)

A skill in its home repo is typically a directory with:

```
<skill-id>/
  SKILL.md            # name, description, trigger, step-by-step procedure
  scripts/            # optional helper scripts
  references/         # optional supporting docs
```

The `SKILL.md` front matter (name + description + trigger) is what an agent harness reads to
decide when to load it. Keep the description tight and trigger-oriented.
