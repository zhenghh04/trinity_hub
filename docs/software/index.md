# Supported software

*Auto-generated from Trinity's internal software cards on 2026-08-22T04:44:13Z. Do not edit
by hand — regenerate with `scripts/build_software_dashboard.py`.*

Trinity maintains verified build + run recipes ("software cards") for HPC
applications across DOE systems. This dashboard shows **66 applications** with
**269 recipes** across **11 systems**, and the **29 functional
smoke tests** (29 passing) that confirm an app doesn't just compile but
produces a physically sensible result.

<div class="sw-legend">
  <span class="sw-chip sw-pass">smoke passed</span>
  <span class="sw-chip sw-available">built / installed</span>
  <span class="sw-chip sw-in_progress">in progress</span>
  <span class="sw-chip sw-blocked">blocked</span>
  <span class="sw-chip sw-listed">recipe only</span>
</div>

<div class="sw-controls">
  <input type="search" id="sw-search" placeholder="Filter by name, category, description…" autocomplete="off">
  <select id="sw-system"><option value="">All systems</option></select>
  <select id="sw-category"><option value="">All categories</option></select>
  <select id="sw-state">
    <option value="">Any status</option>
    <option value="pass">Smoke passed</option>
    <option value="available">Built / installed</option>
    <option value="in_progress">In progress</option>
    <option value="blocked">Blocked</option>
  </select>
</div>

<div class="sw-tabs">
  <button class="sw-tab" data-view="matrix" aria-selected="true">Support matrix</button>
  <button class="sw-tab" data-view="smoke">Smoke tests</button>
  <button class="sw-tab" data-view="catalog">Software catalog</button>
</div>

<div id="sw-dashboard" data-src="software.json">
  <div id="sw-view-matrix" class="sw-view"></div>
  <div id="sw-view-smoke" class="sw-view" hidden></div>
  <div id="sw-view-catalog" class="sw-view" hidden></div>
  <p id="sw-empty" class="sw-empty" hidden>No software matches the current filters.</p>
  <noscript>This dashboard needs JavaScript. Raw data: <a href="software.json">software.json</a>.</noscript>
</div>

## Supported systems

| System | Facility | Description | Recipes |
|---|---|---|---|
| **Aurora** | ALCF | 10,624-node Intel Data Center GPU Max Series exascale supercomputer at Argonne National… | 35 |
| **Cerebras** | ALCF | 4 CS-3 wafer-scale engines + 4 worker nodes + 4 activation servers; AI testbed (Kuberne… | 1 |
| **Crux** | ALCF | 256-node AMD EPYC CPU-only cluster at Argonne National Laboratory | 24 |
| **Polaris** | ALCF | 560-node A100 GPU cluster at Argonne National Laboratory | 49 |
| **Sirius** | ALCF | ALCF staging cluster | 16 |
| **Sophia** | ALCF | 24-node DGX A100 GPU cluster at Argonne National Laboratory | 11 |
| **Sunspot** | ALCF | 128-node Intel Data Center GPU Max Series testbed for Aurora at Argonne National Labora… | 20 |
| **Tara** | ALCF | ALCF Tara North — GH200 (Grace-Hopper) inference cluster; cabinet-isolated, max 112-nod… | 28 |
| **Perlmutter** | NERSC | GPU/CPU hybrid supercomputer at NERSC (NVIDIA A100 GPUs + AMD Milan CPUs) | 41 |
| **Frontier** | OLCF | 9408-node AMD MI250X exascale GPU system at Oak Ridge National Laboratory | 31 |
| **Odo** | OLCF | 30-node AMD MI250X training system at Oak Ridge National Laboratory (Frontier architect… | 13 |

<style>
.sw-legend { margin: 0.5rem 0 1rem; display: flex; flex-wrap: wrap; gap: .4rem; }
.sw-chip { font-size: .72rem; padding: .12rem .5rem; border-radius: 1rem; white-space: nowrap; color: #1b1b1f; }
.sw-pass       { background: #7bd88f; }
.sw-available  { background: #bfe3ff; }
.sw-in_progress{ background: #ffe08a; }
.sw-blocked    { background: #ff9a9a; }
.sw-listed     { background: #e0e0e6; }
[data-md-color-scheme="slate"] .sw-chip { color: #0b0b0d; }
.sw-controls { display: flex; flex-wrap: wrap; gap: .5rem; margin: .5rem 0; }
.sw-controls input[type=search] { flex: 1 1 16rem; min-width: 12rem; padding: .4rem .6rem;
  border: 1px solid var(--md-default-fg-color--lightest); border-radius: .3rem;
  background: var(--md-default-bg-color); color: var(--md-default-fg-color); }
.sw-controls select { padding: .4rem .5rem; border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: .3rem; background: var(--md-default-bg-color); color: var(--md-default-fg-color); }
.sw-tabs { display: flex; gap: .3rem; margin: .4rem 0 .2rem; }
.sw-tab { padding: .35rem .8rem; border: 1px solid var(--md-default-fg-color--lightest);
  border-bottom: none; border-radius: .3rem .3rem 0 0; background: transparent;
  color: var(--md-default-fg-color--light); cursor: pointer; font-size: .82rem; }
.sw-tab[aria-selected="true"] { background: var(--md-code-bg-color);
  color: var(--md-default-fg-color); font-weight: 600; }
.sw-view { overflow-x: auto; }
table.sw-table { border-collapse: collapse; font-size: .78rem; width: 100%; }
table.sw-table th, table.sw-table td { border: 1px solid var(--md-default-fg-color--lightest);
  padding: .28rem .45rem; text-align: left; vertical-align: top; }
table.sw-table thead th { position: sticky; top: 0; background: var(--md-default-bg-color);
  z-index: 1; cursor: pointer; white-space: nowrap; }
table.sw-matrix td.sw-cell { text-align: center; width: 2.1rem; font-weight: 700; padding: .28rem; }
td.sw-cell.sw-pass       { background: #7bd88f; }
td.sw-cell.sw-available  { background: #bfe3ff; }
td.sw-cell.sw-in_progress{ background: #ffe08a; }
td.sw-cell.sw-blocked    { background: #ff9a9a; }
td.sw-cell.sw-listed     { background: #e0e0e6; }
td.sw-cell { color: #1b1b1f; }
.sw-app-cat { display: block; font-size: .68rem; color: var(--md-default-fg-color--light); }
.sw-tag { font-size: .68rem; padding: .05rem .4rem; border-radius: 1rem;
  background: var(--md-code-bg-color); white-space: nowrap; }
.sw-empty { color: var(--md-default-fg-color--light); font-style: italic; margin: 1rem 0; }
.sw-count { color: var(--md-default-fg-color--light); font-size: .78rem; margin: .3rem 0; }

</style>
