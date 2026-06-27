# FAQ & troubleshooting

### How do I get access?

Go to **<https://trinity-hub.alcf.anl.gov>** and **Continue with Globus**. First
sign-in auto-provisions you as an **editor**. If your organization runs a private
Trinity, ask its administrator to add you.

### Do I need a new password?

No. Trinity uses **Globus single sign-on** with your existing DOE facility identity.

### Which systems can I use?

ALCF **Polaris, Aurora, Crux, Sophia, Sirius**; NERSC **Perlmutter**; OLCF
**Frontier**. ALCF works immediately; for OLCF/NERSC, connect compute once in
**Settings → Authentication**.

### My job is stuck "queued" — is something broken?

Usually not — that's the facility scheduler. Trinity submits to the queue you chose
(`debug`, `prod`, `preemptable`, …) and your job waits for nodes like any batch job.
Check the **Jobs** view for the live state; ask Trinity *"what's the queue on
&lt;system&gt;?"* to gauge the wait.

### Trinity says it can't submit a job / run a tool.

Three common causes:

1. **Capability** — your account may lack `submit_hpc_jobs` or `run_tools`. See
   [Roles & access](roles-and-access.md); ask an admin.
2. **Facility not connected** — for OLCF/NERSC, connect compute in
   **Settings → Authentication**.
3. **Missing defaults** — set your **system / queue / allocation / HPC username** in
   **Settings → HPC & Compute**, or name them in the message.

### Which system/queue should I pick?

Set sensible defaults in **Settings → HPC & Compute** and let Trinity use them. For
quick tests use a `debug` queue; for real runs use `prod`/`preemptable`. If unsure,
ask Trinity — *"which Polaris queue fits a 30-minute 2-node test?"*

### My OLCF/NERSC token expired.

Trinity refreshes tokens automatically, but if one lapses, reopen
**Settings → Authentication** and reconnect that facility.

### Are my chats and files private?

Yes. Trinity enforces **strict per-user isolation** — your sessions, files,
credentials, and traces are private to you. Only a read-only knowledge base and
reusable workflows are shared. High-impact actions are audited by operators.

### Will Trinity spend my allocation without asking?

It submits jobs under the **allocation you set**, which consumes real hours. Add a
**custom instruction** (Settings → Personalization) like *"always confirm node count
and walltime before submitting"* to keep a human in the loop. → [Settings](settings.md#personalization-custom-instructions)

### How do I get output files back?

Open the **Files** view to browse and download a run's outputs, or ask Trinity to
**Globus-transfer** them to another facility or your laptop. →
[Files & projects](files-and-projects.md)

### Can I bring my own agent into Trinity?

Yes — publish a small descriptor and your agent becomes `@mention`-able in rooms
while running on your own infrastructure. See
[Register an agent](../register-an-agent.md).

### Something else?

Use the **Trace Timeline** on a session to see exactly what Trinity did, export the
session as Markdown to share, or open an issue on
[GitHub](https://github.com/zhenghh04/trinity_hub/issues).
