# Adding GPU support to GROMACS on Frontier — a work in progress

**Port:** CPU-only GROMACS → GPU-accelerated (AMD MI250X) · **System:** Frontier · **Status:** :material-sync: In progress

## The ask

*(No verbatim request on record — paraphrased from the project's documented goal.)*

Build GPU-accelerated GROMACS on Frontier's AMD GPUs, building on the CPU-only baseline established in an earlier cross-facility GROMACS benchmarking campaign.

## What happened

This project set out to find the fastest working GPU backend for GROMACS on AMD's MI250X GPUs, and the honest finding so far is that the two backends you'd expect to work best are both blocked: GROMACS's official released versions have never actually shipped the AMD-native GPU backend some documentation implies exists, and the alternative cross-vendor backend needs a specific compiler variant that isn't available as a system module on Frontier.

The backend that does build and run is an older, deprecated GPU standard (OpenCL) — which required tracking down the exact build-configuration variable names, since a slightly-wrong name silently links against a non-functional placeholder library instead of failing loudly. That backend works, but doesn't yet properly distribute work across multiple GPUs on a node — every GPU-assigned task currently lands on the first GPU regardless of how many are requested.

## Results

- Working GPU-accelerated build achieved via the older OpenCL backend, after the two preferred backends were both found to be unavailable on this system.
- At small scale (single GPU, smaller system size), the GPU path is 2.29x faster than the CPU-only baseline — a genuine, clean win.
- At realistic production scale (99,000 atoms, multiple GPUs), the current GPU path is actually slower than the CPU-only baseline (52.8 ns/day vs. 61.6 ns/day), because the backend doesn't distribute work across GPUs properly yet — an honestly disclosed current limitation, not a finished result.
- Next step identified: a properly multi-GPU-aware backend is needed before this becomes a genuine production speedup; work continues.

[← Back to Engineering case studies](index.md)
