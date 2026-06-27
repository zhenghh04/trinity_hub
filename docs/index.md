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

[Open Trinity :material-arrow-right:](https://trinity-hub.alcf.anl.gov){ .md-button .md-button--primary }
[How to use Trinity](using-trinity/index.md){ .md-button }

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

Under the hood, Trinity runs an embedded coding agent with tools for the ALCF/NERSC/OLCF
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
