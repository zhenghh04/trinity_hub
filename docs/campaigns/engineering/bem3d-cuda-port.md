# BEM_3D: from a 40GB memory wall to a 2TB-equivalent problem via matrix-free GMRES

**Port:** Fortran 90 + OpenMP + LAPACK/ScaLAPACK (CPU) → CUDA / cuSolverDn + custom iterative solver (NVIDIA A100) · **System:** Sirius · **Status:** :material-cube-outline: Completed

## The ask

*(No verbatim request on record — paraphrased from the project's documented goal.)*

Port the 3D sibling of BEM_2D — solving electromagnetic scattering off an arbitrary 3D dielectric body — to a single A100 GPU, and push mesh resolution well beyond what the original 2010 PhD thesis achieved.

## What happened

The 3D problem's underlying math is actually simpler to port than the 2D case (no special-function porting needed), but it runs into a hard memory wall: the dense system matrix for a realistic mesh doesn't fit in a single GPU's memory (a matrix that size would need hundreds of gigabytes, then eventually terabytes, while an A100 has 40GB). The fix was writing an iterative solver (restarted GMRES) entirely from scratch, so the matrix never needs to be stored at all — only computed on the fly.

The first version of this "matrix-free" approach used a naive parallel-update pattern that collapsed under heavy contention at large problem sizes, making each solver step take about a second; a redesigned version (cooperative reduction, one GPU compute unit per matrix row) cut that same step time by 15x. A subtle bug in a numerical-stability routine (a sign convention mismatch) was caught because it made the solver's error metric grow instead of shrink — and was fixed by cross-checking against the standard reference convention.

## Results

- 502x speedup vs. a 32-thread CPU baseline at a representative problem size using the dense direct solver.
- The matrix-free iterative version reaches a problem size equivalent to a dense matrix of about 2 terabytes — completing in 6.5 minutes on a single 40GB GPU, roughly 4x the mesh resolution of the original 2010 PhD thesis, and simply impossible for any dense method to store, let alone solve.
- Validated against the exact analytic solution for a sphere (Mie scattering theory): matches to within 0.35% at the largest mesh tested, and within 0.25% at an even larger mesh in an extended run.
- Cross-validated the direct and iterative solvers against each other in the size range where both are feasible — they agree to 5-7 significant figures, confirming the from-scratch iterative solver is correct.

[← Back to Engineering case studies](index.md)
