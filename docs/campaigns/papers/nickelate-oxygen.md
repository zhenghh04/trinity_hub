# Fact-checking an AI agent's claim about oxygen imaging in a nickelate superconductor

**Reproducing:** *Direct imaging of residual oxygen disorder in an infinite-layer nickelate superlattice via multislice ptychography* (Yang et al., Nature Communications 16, 11076, 2025). DOI: 10.1038/s41467-025-67124-6
**System:** Polaris · **Status:** :material-file-document-check-outline: Completed for this scope

## The goal

This reproduction started unusually: another AI research agent had posted an analysis of this paper on a public claim-verification forum, extending its finding with an additional numeric claim not actually stated in the paper itself. This project independently tested — via simulation — whether the paper's core method (and the other agent's extension of it) holds up.

## What happened

A 5-point simulated sweep of apical-oxygen occupancy was run, comparing a standard projected imaging approach against the paper's more sophisticated depth-resolved (multislice) ptychography method. The result directionally confirms the paper's central claim — that a simple projected image is nearly blind to this specific oxygen disorder while the depth-resolved method tracks it — but the report is explicit that this used a coarser, whole-image metric than the paper's own site-by-site method, so it can confirm the qualitative trend but not the paper's specific numeric detection threshold, and does not attempt to verify the other AI agent's extended numeric claim.

## Results

- Standard projected imaging: essentially flat response to oxygen occupancy across the full range tested (varying by only about 1%) — confirming it is nearly blind to this effect, as the paper states.
- Depth-resolved (multislice) ptychography: a clear, monotonic signal change across the same range — confirming the paper's method does detect what a projected image misses.
- Explicitly scoped as a directional confirmation, not a replication of the paper's precise detection-threshold number.

[← Back to Paper reproductions](index.md)
