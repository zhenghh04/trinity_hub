# Autonomous science campaigns

A systematic study running real physics, chemistry, and engineering campaigns end-to-end across ALCF, NERSC, and OLCF systems — not to produce a single result, but to examine how well an autonomous agent handles failure, self-corrects, and knows when a result is trustworthy, not just whether a job finished. Across the full study, agents self-corrected roughly 49 of 65 recorded iteration failures with zero human intervention.

<div class="grid cards" markdown>

-   :material-snowflake-thermometer: **Finding argon's melting point via molecular dynamics**

    ---

    A 7-temperature LAMMPS sweep locates the solid-to-liquid transition within 4% of the literature value.

    [:octicons-arrow-right-24: Read the full campaign](c1-argon-melting.md)

-   :material-atom: **Silicon's electronic band structure from first principles**

    ---

    A four-step Quantum ESPRESSO DFT workflow computes silicon's band gap in 24 seconds on one GPU node.

    [:octicons-arrow-right-24: Read the full campaign](c2-silicon-bands.md)

-   :material-dna: **Trp-cage mini-protein thermal stability across three temperatures**

    ---

    Three GROMACS runs show a mini-protein's structure destabilizing steadily as temperature climbs.

    [:octicons-arrow-right-24: Read the full campaign](c3-gromacs-trp-cage.md)

-   :material-alert-decagram-outline: **Water dimer binding energy — DFT vs. quantum Monte Carlo**

    ---

    A clean DFT result, plus an honestly reported handoff failure when refining it with quantum Monte Carlo.

    [:octicons-arrow-right-24: Read the full campaign](c4-water-dimer.md)

-   :material-sync: **Turbulent pipe flow across two facilities: Polaris vs. Aurora**

    ---

    The same CFD simulation on NVIDIA and Intel GPUs, five build iterations apart, within 13% throughput of each other.

    [:octicons-arrow-right-24: Read the full campaign](c5-nekrs-turbulent-pipe.md)

-   :material-bug-outline: **Reproducing the same GPU bug on two different supercomputers**

    ---

    A cosmology code's GPU crash reproduced identically on Polaris and Perlmutter, confirming a real code defect.

    [:octicons-arrow-right-24: Read the full campaign](c6-hacc-gpu-bug.md)

-   :material-sync: **GROMACS water box: GPU (Polaris) vs. CPU-only (Frontier)**

    ---

    A cross-facility performance baseline that later fed a follow-on GPU-porting effort on Frontier.

    [:octicons-arrow-right-24: Read the full campaign](c7-gromacs-multi-facility.md)

-   :material-chart-bell-curve: **Opening silicon's band gap the right way: G0W0 many-body corrections**

    ---

    A many-body GW correction pushes silicon's DFT gap toward its true value, as theory predicts.

    [:octicons-arrow-right-24: Read the full campaign](c8-berkeleygw-g0w0.md)

-   :material-molecule: **Breaking a nitrogen molecule apart, three ways, across three supercomputers**

    ---

    DMRG matches exact full configuration interaction to nine decimal places, verified on three systems.

    [:octicons-arrow-right-24: Read the full campaign](c12-block2-n2.md)

-   :material-thermometer: **Copper's melting point via a heating-ramp simulation**

    ---

    A continuous heating ramp finds copper's melting discontinuity, showing the expected superheating artifact.

    [:octicons-arrow-right-24: Read the full campaign](t3-1-cu-melting.md)

-   :material-speedometer: **Pushing turbulent pipe flow to a higher Reynolds number**

    ---

    The same spectral-element method holds stable and performant at nearly 4x the turbulence intensity.

    [:octicons-arrow-right-24: Read the full campaign](t3-2-nekrs-high-re.md)

-   :material-cube-outline: **Running four molecular dynamics replicas at once**

    ---

    Four independent GROMACS replicas in one job, each on its own GPU, with negligible parallel overhead.

    [:octicons-arrow-right-24: Read the full campaign](t3-3-gromacs-ensemble.md)

-   :material-waveform: **Silicon carbide's vibrational spectrum from first principles**

    ---

    DFPT phonon frequencies land within 1% of experiment, with symmetry checks passing cleanly.

    [:octicons-arrow-right-24: Read the full campaign](t3-4-sic-phonons.md)

-   :material-check-decagram: **Verifying HPC applications actually run**

    ---

    A coverage sweep across ~38 applications and 9 systems, checking for a physically sensible result, not just a clean exit.

    [:octicons-arrow-right-24: Read the full campaign](smoke-tests.md)

</div>

[← Back to Science Campaigns](../index.md)
