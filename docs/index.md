---
title: Trinity Hub
hide:
  - navigation
  - toc
---

<div class="tx-hero">
  <svg class="tx-hero__orbits" viewBox="0 0 96 96" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <g fill="none" stroke-linecap="round" stroke-width="0.7">
      <ellipse cx="48" cy="34" rx="13" ry="26" transform="rotate(0 48 48)" stroke="#38bdf8"/>
      <ellipse cx="48" cy="34" rx="13" ry="26" transform="rotate(120 48 48)" stroke="#2dd4bf"/>
      <ellipse cx="48" cy="34" rx="13" ry="26" transform="rotate(240 48 48)" stroke="#a3e635"/>
    </g>
  </svg>
  <div class="tx-hero__inner">
    <div class="tx-hero__copy">
      <p class="tx-eyebrow">Argonne Leadership Computing Facility</p>
      <h1>Ask for science.<br><em>Trinity runs the supercomputer.</em></h1>
      <p class="tx-lead">Trinity is a multi-tenant workspace where scientists and AI agents collaborate on DOE leadership computing. Describe a task in plain language — Trinity plans it, submits and monitors the HPC jobs, moves the data, and reports back, all from a chat window.</p>
      <p class="tx-hero__actions">
        <a class="md-button md-button--primary" href="https://trinityscience.org">Open Trinity</a>
        <a class="md-button" href="using-trinity/getting-started/">Getting started</a>
      </p>
    </div>
    <div class="tx-hero__demo">
      <div class="tx-terminal" role="img" aria-label="Example Trinity session: a user asks for a Quantum ESPRESSO relaxation on Polaris; Trinity plans, submits, monitors, and returns the result.">
        <div class="tx-terminal__bar">
          <span class="tx-dot"></span><span class="tx-dot"></span><span class="tx-dot"></span>
          <span class="tx-terminal__title">trinity · room: polaris-dft</span>
        </div>
        <div class="tx-terminal__body">
          <p class="tx-line tx-line--you"><span class="tx-who">you</span><span>Relax this structure with Quantum ESPRESSO on Polaris.</span></p>
          <p class="tx-line"><span class="tx-tag tx-tag--plan">plan</span><span>pw.x vc-relax input + PBS script, debug queue</span></p>
          <p class="tx-line"><span class="tx-tag tx-tag--submit">submit</span><span>job 4182931 → Polaris · 1 node · 32 ranks</span></p>
          <p class="tx-line"><span class="tx-tag tx-tag--monitor">monitor</span><span>12 min · converged in 14 SCF steps</span></p>
          <p class="tx-line"><span class="tx-tag tx-tag--result">result</span><span>forces &lt; 10⁻⁴ Ry/bohr · outputs staged to your project</span></p>
          <p class="tx-line tx-line--done"><span class="tx-who">✓</span><span>done in 14 min<span class="tx-caret"></span></span></p>
        </div>
      </div>
    </div>
  </div>
  <div class="tx-stats">
    <div class="tx-stat"><span class="tx-stat__n" data-stat="apps">66</span><span class="tx-stat__l">applications</span></div>
    <div class="tx-stat"><span class="tx-stat__n" data-stat="systems">11</span><span class="tx-stat__l">HPC systems</span></div>
    <div class="tx-stat"><span class="tx-stat__n" data-stat="recipes">245</span><span class="tx-stat__l">verified recipes</span></div>
    <div class="tx-stat"><span class="tx-stat__n" data-stat="smoke">29/29</span><span class="tx-stat__l">smoke tests passing</span></div>
    <div class="tx-stat"><span class="tx-stat__n" data-stat="campaigns">40+</span><span class="tx-stat__l">documented campaigns</span></div>
  </div>
</div>

**Trinity Hub** (this site) is the open front door to that platform. It documents
**how to use Trinity** as a scientist, and **how to extend it** by publishing your
own agents and reusable skills.

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

<ul class="tx-facilities">
  <li><strong>ALCF</strong> Polaris · Aurora · Crux · Sophia · Sirius</li>
  <li><strong>NERSC</strong> Perlmutter</li>
  <li><strong>OLCF</strong> Frontier</li>
</ul>

See the full [supported-software dashboard](software/index.md) — which
applications are built, smoke-tested, and ready on each system.

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
