# Building PyTorch from source for Intel GPUs — 23 iterations to a working build

**Build:** PyTorch source → Intel GPU (SYCL) build · **System:** Aurora · **Status:** :material-cpu-64-bit: Completed

## The ask

> "please build pytorch on Aurora from scratch using ClearML on Aurora login queue"

## What happened

The first approach, following the documented compiler configuration, hit a wall — a specific linking step silently produced an empty output file with no clear error, and no workaround was found after several attempts. Recognizing a dead end, Trinity switched to a different, newer version of the codebase that uses an entirely different build arrangement (a general-purpose compiler as the primary one, with the specialized GPU compiler invoked only for the GPU-specific code) — and pushed through further build-tool version conflicts along the way (a package installer silently pulling in an incompatible build-tool version had to be explicitly pinned).

## Results

- 23 build iterations resolved autonomously; final build took about 2 hours on the login node.
- Verified on a full compute node (6 Intel GPUs, over 800GB of combined GPU memory): correct results across three numeric precision modes on a matrix-multiply test, and all three distributed-training communication backends confirmed working.

[← Back to Engineering case studies](index.md)
