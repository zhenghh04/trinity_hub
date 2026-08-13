# Trinity Hub

**Trinity is a multi-tenant, multi-agent workspace where scientists and AI agents
collaborate to run work on DOE leadership computing facilities.** You describe a
task in plain language — *"run a Quantum ESPRESSO relaxation on Polaris"*, *"build
LAMMPS on Aurora"*, *"is Frontier up?"* — and Trinity plans it, submits and
monitors the HPC jobs, moves the data, and reports back, all from a chat window in
your browser.

**Trinity Hub** (this site) is the open front door to that platform. It documents
**how to use Trinity** as a scientist, and **how to extend it** by publishing your
own agents and reusable skills.

[Open Trinity :material-arrow-right:](https://trinityscience.org){ .md-button .md-button--primary }
[How to use Trinity](using-trinity/index.md){ .md-button }

---

## What Trinity is

Built at the Argonne Leadership Computing Facility, Trinity runs on the
**Claude Agent SDK** for reasoning and tool use, and rides **Globus** for
identity, data movement, and compute — so one authenticated conversation can
reach every facility you're authorized to use.

It composes reusable building blocks rather than improvising from scratch each
time:

- **Agents** — domain specialists (DFT, molecular dynamics, performance
  engineering, storage benchmarking, and more) that plan and run multi-step
  campaigns, alone or together with people in a shared room.
- **Workflows** — curated, parameterized HPC pipelines for common tasks (builds,
  submissions, ports) that agents draw on instead of writing everything from
  scratch.
- **Skills** — atomic, reusable capabilities — a procedure, a tool wrapper, a
  known fix — that any agent can load.

Every action is recorded as **Knowledge** (validated domain facts that improve
future runs), **Traces** (a full timeline of tool calls and observations), and
**Provenance** (why a decision was made) — so results stay auditable and
reproducible, not just "the agent said so." See
[How it works](architecture.md) for the registry-vs-runtime split that lets
outside agents and skills plug in.

---

## Pick your path

<div class="grid cards" markdown>

-   :material-rocket-launch: **Use Trinity** *(scientists)*

    ---

    Log in with Globus, ask for compute work in natural language, and watch jobs
    run across ALCF, NERSC, and OLCF.

    [:octicons-arrow-right-24: Getting started](using-trinity/getting-started.md)

-   :material-robot: **Extend Trinity** *(agent & skill authors)*

    ---

    Publish your own agent so others can `@mention` it in a room, or share a
    reusable skill that any Trinity agent can load.

    [:octicons-arrow-right-24: Register an agent](register-an-agent.md)

-   :material-server-network: **Operate Trinity** *(deployers)*

    ---

    Understand the registry-vs-runtime split, sync the registry into a running
    server, and review the trust boundaries.

    [:octicons-arrow-right-24: How it works](architecture.md)

-   :material-flask-outline: **See it in action** *(anyone)*

    ---

    Real DFT, molecular dynamics, GPU porting, and paper-reproduction campaigns run
    end-to-end through Trinity — the prompt, what happened, and the result.

    [:octicons-arrow-right-24: Browse Science Campaigns](campaigns/index.md)

</div>

---

## What Trinity does

| You ask… | Trinity… |
|---|---|
| *"Relax this structure with Quantum ESPRESSO on Polaris."* | writes the input + PBS script, submits via the facility API, monitors to completion, returns results. |
| *"Build NekRS on Aurora."* | picks the right modules/toolchain and iterates the build on a compute node. |
| *"Train GPT-2 on 4 Aurora nodes."* | stages data, generates the distributed launch, submits, and tracks the run. |
| *"Is Perlmutter up? What's the queue?"* | queries facility status and reports availability and load. |
| *"Move these outputs to my laptop."* | runs a Globus transfer and reports the task status. |

Day to day, Trinity runs an embedded coding agent with tools for the ALCF/NERSC/OLCF
integrated research-infrastructure APIs, Globus transfer & compute, and experiment
tracking — but you never touch those directly. You stay in the chat.

## Supported facilities

- **ALCF** — Polaris, Aurora, Crux, Sophia, Sirius
- **NERSC** — Perlmutter
- **OLCF** — Frontier

## A platform built for many users

Trinity serves many scientists at once under **strict tenant isolation**: every
user has private sessions, files, credentials, and execution traces, while sharing
a read-only knowledge base and a library of reusable workflows. Access is by
**Globus single sign-on** — your existing DOE facility identity.

!!! tip "New here?"
    Start with **[Getting started](using-trinity/getting-started.md)** to log in,
    then skim **[The chat interface](using-trinity/chat.md)** to learn how to ask
    Trinity for work.

## Maintainer

Trinity and Trinity Hub are created and maintained by **Huihuo Zheng**
([@zhenghh04](https://github.com/zhenghh04)), Argonne Leadership Computing
Facility (ALCF) / Argonne National Laboratory. See
[GOVERNANCE.md](https://github.com/zhenghh04/trinity_hub/blob/main/GOVERNANCE.md)
for how contributions are reviewed, and
[CONTRIBUTING.md](https://github.com/zhenghh04/trinity_hub/blob/main/CONTRIBUTING.md)
to get involved.
