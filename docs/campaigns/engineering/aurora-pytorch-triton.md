# Building a GPU compiler stack — and confirming a known Intel compiler bug still exists

**Build + diagnosis:** PyTorch + Triton compiler, Intel GPU backend · **System:** Aurora · **Status:** :material-bug-outline: Completed

## The ask

> "Let's try to get PyTorch with optimized triton kernels on the latest dev stack on Aurora."

Follow-up: "After you build this, let us fix this bug" (referring to a previously-tracked Intel compiler issue).

## What happened

Building on the prior PyTorch build, this added Triton (a GPU kernel compiler used by many ML frameworks) with its Intel-GPU code generation path enabled. Rather than attempt to patch a closed-source compiler bug from the outside (not possible), the more useful move was designing two small, targeted test kernels that isolate the exact pattern known to trigger the bug, to determine whether it still affects the newly built compiler stack.

Along the way, a subtlety in the compiler's own internals meant an initial quick command-line test wouldn't work — the compiler needs to read its own kernel's source from an actual file on disk, not an inline command — so the test had to be restructured accordingly.

## Results

- 8 of 9 GPU verification tests passed (device detection, distributed backends, compiled and eager-mode execution).
- Just-in-time compilation delivered a measured 1.31x speedup over standard eager-mode execution on a matrix-multiply benchmark.
- Confirmed the previously known compiler bug still reproduces in the freshly built stack, and — more usefully — narrowed down exactly which kernel patterns trigger it (a specific multi-dimensional GPU work-grid configuration) versus which don't (a different, simpler configuration passed cleanly), correctly diagnosing it as an issue in Intel's closed-source compiler rather than something fixable from the PyTorch or Triton side.

[← Back to Engineering case studies](index.md)
