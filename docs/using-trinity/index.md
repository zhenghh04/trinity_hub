# Using Trinity — overview

Trinity is a **chat workspace for HPC**. Instead of SSHing into a login node,
writing batch scripts, and babysitting the queue, you tell Trinity what you want
in plain language and it does the mechanics for you — on **ALCF (Polaris, Aurora,
Crux, Sophia, Sirius), NERSC (Perlmutter), and OLCF (Frontier)**.

!!! info "Where it lives"
    Trinity runs in your browser at **<https://trinity.lionlambstone.org>**. You sign
    in with **Globus** using your existing DOE facility identity — no new password
    required.

<div class="grid" markdown>

<figure markdown>
  ![Trinity login page](../assets/screenshots/login.png)
  <figcaption>Sign in with Globus, or connect an ALCF/NERSC/OLCF facility in one step.</figcaption>
</figure>

<figure markdown>
  ![Trinity workspace after login](../assets/screenshots/after-login.png)
  <figcaption>The workspace after login — here, AgentsHub, one of the views reachable from the sidebar.</figcaption>
</figure>

</div>

## What you can do

- **Run jobs** — DFT/MD/ML/benchmarks and arbitrary batch work. Trinity writes the
  job script, submits it, and monitors it. → [Running HPC jobs](running-jobs.md)
- **Build & port software** — compile applications from source on a system, or port
  CUDA → Intel/SYCL or HIP. → [The chat interface](chat.md)
- **Browse & edit files** — a built-in file browser over your project workspace,
  with upload/download. → [Files & projects](files-and-projects.md)
- **Check system status** — availability, queues, allocations, incidents.
- **Move data** — Globus transfers between facilities and your machine.
- **Collaborate with agents** — bring domain agents into shared rooms and
  `@mention` them. → [Agents & rooms](agents-and-rooms.md)

## The interface at a glance

A left sidebar switches between views; the most-used ones:

| View | What it's for |
|---|---|
| **Dashboard** | Landing page — greeting, quick links, system stats. |
| **Chat** | The main workspace — ask for work, watch it happen, see results. |
| **Projects** | Organize chats and files into project workspaces. |
| **Files** | Browse / read / edit / upload files in your workspace. |
| **Jobs** | Live status of background tasks and HPC submissions. |
| **AgentsHub** | Browse available agents and their cards. |
| **Agent Rooms** | Group conversations with people **and** agents. |
| **SkillHub** | Browse the catalog of reusable HPC skills. |
| **Knowledge Store** | Search validated HPC knowledge by system/topic. |
| **Trace Timeline** | A detailed timeline of every action in a session. |
| **Settings** | Custom instructions, HPC defaults, models, tokens, profile. |

## A typical first session

1. **[Log in](getting-started.md)** with Globus.
2. Open **Settings → HPC & Compute** and set your default **system**, **queue**,
   **allocation**, and **HPC username**. → [Settings](settings.md)
3. In **Chat**, type what you want — e.g. *"Check if Polaris is up, then submit a
   1-node debug job that runs `hostname`."*
4. Watch progress stream in; open **Jobs** to track the submission.
5. Read results in the chat or grab output from **Files**.

Next: **[Getting started →](getting-started.md)**
