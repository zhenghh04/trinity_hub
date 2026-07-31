# Trinity science campaigns

These are real campaigns run end-to-end through Trinity's chat interface — DFT, molecular dynamics, ML benchmarking, and infrastructure verification — each backed by a full execution trace and, for auditability, a plain-language scientist report.

<div class="grid cards" markdown>

-   :material-alert-decagram-outline: **N2 gas molecular dynamics — two models, one open-ended ask**

    ---

    One vague prompt, two real experiments: a clean ideal-gas sweep and a two-site model that overshot temperature.

    [:octicons-arrow-right-24: Read the full campaign](lammps-n2-gas.md)

-   :material-bug-outline: **Fixing OpenFold's GPU kernel**

    ---

    A silently CPU-only fused-attention kernel diagnosed, rebuilt for CUDA, and verified against a reference structure.

    [:octicons-arrow-right-24: Read the full campaign](openfold-cuda-rebuild.md)

-   :material-database-search: **MLPerf Storage vector-database benchmark: DAOS vs. Lustre**

    ---

    An overnight Aurora benchmark comparing storage backends and scaling query throughput across client nodes.

    [:octicons-arrow-right-24: Read the full campaign](mlperf-vectordb-aurora.md)

-   :material-check-decagram: **Closing out Polaris application verification**

    ---

    Three stubborn code failures — NWChem, QMCPACK, WRF — diagnosed and fixed to complete a full verification suite.

    [:octicons-arrow-right-24: Read the full campaign](polaris-cseries.md)

-   :material-server: **First job on Perlmutter**

    ---

    A cross-facility smoke test that surfaced two real infrastructure bugs before declaring the system verified.

    [:octicons-arrow-right-24: Read the full campaign](iri-smoketest-perlmutter.md)

-   :material-atom: **3C-SiC ground-state energy via Quantum ESPRESSO**

    ---

    A clean first-try DFT run that still flagged its own smearing choice and residual-pressure caveat.

    [:octicons-arrow-right-24: Read the full campaign](sic-dft.md)

-   :material-bug-outline: **Liquid argon MD — catching its own mistake**

    ---

    A "liquid argon" run that was actually supercritical fluid, caught and corrected by Trinity itself.

    [:octicons-arrow-right-24: Read the full campaign](lammps-argon.md)

-   :material-check-decagram: **Graphene band structure — a 3-round convergence study**

    ---

    Three rounds of DFT refinement resolving k-point convergence and confirming graphene's Dirac cone.

    [:octicons-arrow-right-24: Read the full campaign](dft-graphene.md)

-   :material-waveform: **Predicting Ti K-edge XANES spectra across three TiO2 polymorphs**

    ---

    ML-predicted spectra for anatase, brookite, and rutile, correctly matched against experimental standards.

    [:octicons-arrow-right-24: Read the full campaign](xanes-tio2.md)

</div>

[← Back to Science Campaigns](../index.md)
