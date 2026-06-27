# Roles & access

Trinity is multi-tenant: what you can do is governed by your **role** and a set of
fine-grained **capabilities**. Most scientists are **editors** and never need to
think about this — but here's the model.

## Roles

| Role | Can do |
|---|---|
| **admin** | Everything, including the **Admin** panel: manage users, roles, allocations, and capabilities. |
| **editor** *(default)* | Chat, run tools, **submit HPC jobs**, browse/read own files, terminal & proxy access. |
| **viewer** | Chat and read files only — no job submission or tool execution. |

New accounts auto-provision as **editor** on first Globus login. Roles are assigned
by an administrator.

## Capabilities

Roles expand into capability flags; an admin can also grant or revoke these
individually per user:

| Capability | Controls |
|---|---|
| `chat` | Access to the chat workspace. |
| `read_files` | Read files in your workspace. |
| `write_files` | Create / edit / upload / delete files. |
| `run_tools` | Let the agent execute tools (job submission, transfers, builds). |
| `submit_hpc_jobs` | Submit batch jobs to facilities. |
| `terminal_access` | Browser terminal sessions. |
| `proxy_access` | Same-origin access to experiment-tracking dashboards. |

An admin can also scope a user to specific **projects** and override their **HPC
username** and **allocation**.

## Isolation & auditing

- **Strict per-user isolation** — your sessions, files, credentials, and traces are
  private; users share only a read-only knowledge base and reusable workflows.
- **High-impact actions are audited** — sensitive operations are recorded so
  operators can review what ran and on whose behalf.

## Need more access?

If you can't submit jobs or reach a system you expect, you likely need a capability
or an OLCF/NERSC connection. See the [FAQ](faq.md) or ask your Trinity
administrator.

Next: **[FAQ →](faq.md)**
