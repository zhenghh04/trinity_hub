# Verifying HPC applications actually run

**Systems:** Aurora, Crux, Frontier, Odo, Perlmutter, Polaris, Sirius, Sophia, Sunspot · **Outcome:** :material-check-decagram: Ongoing coverage sweep

## What this covers

This isn't one scientific investigation — it's a systematic "does the app actually run and produce a physically sensible result" check across roughly 38 HPC applications and 9 DOE systems. Each check goes beyond "it compiled": Trinity runs a tiny real physics or science problem per application and confirms the output is physically sensible, not just that the job exited cleanly.

## Coverage so far

The playbook covers 38 applications across 9 systems (181 possible application/system pairs). As of this writing, 27 pairs have a recorded pass/partial/fail outcome, with more being filled in as agents run — this is ongoing infrastructure verification work, not a finished dataset.

## Highlights

- BerkeleyGW on Aurora: dielectric screening parameter (epsilon-infinity) of 16.96, matching expected physics for silicon.
- block2 (DMRG quantum chemistry) matched exact full configuration interaction reference energies on Aurora, Frontier, and Polaris — a difference as small as 2.25×10⁻⁹ Hartree on Polaris.
- OpenMC (Monte Carlo particle transport) on Polaris: computed a criticality eigenvalue k-eff = 1.020 ± 0.016 for a benchmark reactor problem.
- PySCF (quantum chemistry) on Aurora and Crux: total energy of -74.963 Hartree for a water molecule, matching the expected reference value.
- WarpX (plasma/particle-in-cell) and Nyx (cosmological hydrodynamics) both completed basic verification runs on Polaris.

[← Back to Science campaigns](index.md)
