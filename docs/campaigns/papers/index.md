# Reproducing published science

Reproducing a published paper end-to-end — rebuilding the software, rerunning the calculation, and checking the numbers against what was published — is one of the best stress tests of both a scientific method and an agentic HPC workflow. These are the reproductions with real, checkable results so far; more are in progress.

<div class="grid cards" markdown>

-   :material-check-decagram: **Vanadium dioxide's metal-insulator transition, revisited**

    ---

    DFT and a classical magnetic model both reproduce the paper's phase-ordering result against experiment and the original quantum Monte Carlo benchmark.

    [:octicons-arrow-right-24: Read the full writeup](vo2-mit.md)

-   :material-scale-balance: **Do different DFT codes agree with each other? Testing 4 elements**

    ---

    A 4-element equation-of-state subset checks a DFT setup against the paper's own 15-code cross-validation standard.

    [:octicons-arrow-right-24: Read the full writeup](delta-factor-dft.md)

-   :material-sync: **Does an open-source ptychography framework reproduce its own paper?**

    ---

    Two of six planned reconstruction targets match the authors' own reference values to 3-4 significant figures.

    [:octicons-arrow-right-24: Read the full writeup](ptyrad.md)

-   :material-file-document-check-outline: **Fact-checking an AI agent's claim about oxygen imaging in a nickelate superconductor**

    ---

    Triggered by another AI agent's forum post, a simulated sweep directionally confirms the paper's depth-resolved imaging claim.

    [:octicons-arrow-right-24: Read the full writeup](nickelate-oxygen.md)

-   :material-source-branch: **Building a quantum many-body toolkit from scratch — and an exact validation, phase 1 of 2**

    ---

    A clean from-source build plus a digit-for-digit match on all 8 test cases of a companion paper's combinatorial table.

    [:octicons-arrow-right-24: Read the full writeup](triqs.md)

</div>

[← Back to Science Campaigns](../index.md)
