# Science Campaigns

Trinity isn't just a scheduler front-end — it's been run end-to-end on real scientific
and engineering work across ALCF, NERSC, and OLCF systems. This page is a record of
that work: the request as asked, what Trinity actually did (including the dead ends
and self-corrections), and what came out the other end.

Every entry below is backed by a full execution trace and, for auditability, a
provenance record of why each decision was made — the same "not just the agent said
so" standard described in [What Trinity is](../index.md#what-trinity-is). Where an
original prompt wasn't captured verbatim, the page says so plainly rather than
presenting a paraphrase as a quote — and partial, mixed, or negative results are
reported honestly, because a campaign that catches its own mistake is a better proof
of rigor than one that just reports success.

<div class="grid cards" markdown>

-   :material-chat-processing-outline: **Trinity runs**

    ---

    Campaigns run live through Trinity's chat interface — DFT, molecular dynamics, ML
    benchmarking, and infrastructure verification, each with a real execution trace.

    [:octicons-arrow-right-24: Browse Trinity runs](trinity-runs/index.md)

-   :material-flask-outline: **Autonomous science campaigns**

    ---

    A systematic study of 14 physics/chemistry/engineering campaigns across DOE
    systems, probing how well an autonomous agent self-corrects and knows when to
    trust its own result.

    [:octicons-arrow-right-24: Browse science campaigns](science-campaigns/index.md)

-   :material-chip: **Performance engineering case studies**

    ---

    Porting and performance work — moving code across GPU vendors, fixing GPU
    kernels, building software from source — with the debugging story and validated
    numbers, not just a final checkmark.

    [:octicons-arrow-right-24: Browse performance engineering case studies](engineering/index.md)

-   :material-file-document-check-outline: **Paper reproductions**

    ---

    Rebuilding the software, rerunning the calculation, and checking the numbers
    against what was published — one of the best stress tests of both a method and a
    workflow.

    [:octicons-arrow-right-24: Browse paper reproductions](papers/index.md)

</div>

## All campaigns

Every documented campaign in one place — filter by category or system, or search
by application, technique, or outcome.

<div class="sw-controls">
  <input type="search" id="ci-search" placeholder="Filter by title, application, system, outcome…" autocomplete="off">
  <select id="ci-category"><option value="">All categories</option></select>
  <select id="ci-system"><option value="">All systems</option></select>
</div>

<div id="ci-index">
  <div id="ci-table"></div>
  <p id="ci-empty" class="sw-empty" hidden>No campaigns match the current filters.</p>
  <noscript>This index needs JavaScript — browse the category pages above instead.</noscript>
</div>

## Have a campaign to add?

This page is curated from Trinity's own execution traces and campaign reports. If
you've run something interesting through Trinity and want it featured here, open an
issue on [trinity_hub](https://github.com/zhenghh04/trinity_hub/issues).
