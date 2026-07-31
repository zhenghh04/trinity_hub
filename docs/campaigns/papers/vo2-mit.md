# Vanadium dioxide's metal-insulator transition, revisited

**Reproducing:** *Computation of the Correlated Metal-Insulator Transition in Vanadium Dioxide from First Principles* (H. Zheng & L. K. Wagner, Physical Review Letters 114, 176401, 2015). DOI: 10.1103/PhysRevLett.114.176401
**System:** Local/HPC (DFT + Monte Carlo) · **Status:** :material-check-decagram: Completed

## The goal

Check whether the paper's central finding — that the metallic (rutile) and insulating (monoclinic) phases of VO2 are correctly energetically ordered once electron correlation is properly captured — holds up when cross-validated with a cheaper method against the paper's own high-accuracy quantum Monte Carlo benchmark.

## What happened

This reproduction re-derives the paper's central result using density functional theory cross-checked against the original quantum Monte Carlo numbers, and separately models the material's magnetic behavior with a classical statistical-mechanics model, comparing directly against two independent experimental datasets from the 1960s-70s literature. A full three-way convergence study (checking sensitivity to pseudopotential choice, simulation cell size, and Monte Carlo time step) bounds the residual uncertainty. One honest caveat: the exact analysis script used to generate these results was never committed to version control and no longer exists — the results and figures themselves are preserved and complete, but the calculation cannot currently be re-run from scratch without rewriting that script.

## Results

- Rutile-vs-monoclinic magnetic energy ordering: -10.6 ± 5.9 meV per formula unit, correctly reproducing the paper's qualitative finding.
- Ferromagnetic-vs-antiferromagnetic energy difference in the rutile phase: +24.2 ± 5.8 meV per formula unit.
- A classical Monte Carlo model of the magnetic susceptibility closely tracks two independent experimental datasets from 1967 and 1975 across the transition temperature range.
- Full convergence/error-budget analysis (pseudopotential, cell size, timestep) bounds the residual uncertainty at roughly ±6 meV per formula unit.

[← Back to Paper reproductions](index.md)
