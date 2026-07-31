# Building a quantum many-body toolkit from scratch — and an exact validation, phase 1 of 2

**Reproducing:** *TRIQS: A toolbox for research on interacting quantum systems* (Parcollet et al., Computer Physics Communications 196, 2015), plus a companion continuous-time quantum Monte Carlo paper (Seth et al., 2016). DOI: 10.1016/j.cpc.2015.04.023
**System:** Crux · **Status:** :material-source-branch: Phase 1 of 2 completed

## The goal

Build this widely-used quantum many-body physics toolkit from source, then reproduce one of its companion paper's fully deterministic, exactly-checkable results as a first validation step before attempting the harder Monte Carlo/DMFT figures that are the paper's real scientific content.

## What happened

The toolkit and its quantum-impurity-solver extension built successfully from source on the first attempt, with no workarounds needed — itself a small positive data point about the software's portability. A combinatorial table from the companion paper (counting how a Hilbert space splits into independent blocks under different symmetry choices, for several small quantum systems) was then recomputed and checked digit-for-digit against the published values.

## Results

- All 8 of 8 test cases matched the published values exactly (e.g., a 7-orbital system with full spherical symmetry splits into exactly 960 independent blocks, matching the paper precisely).
- Clean build from source with no compatibility issues — a good sign for future work with this toolkit.
- This validates the software and the easy, deterministic part of the companion paper; the harder Monte Carlo/DMFT figures that are the paper's actual physics content are still pending as phase 2.

[← Back to Paper reproductions](index.md)
