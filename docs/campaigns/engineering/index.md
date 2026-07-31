# Engineering case studies

Porting and performance work — moving code across GPU vendors, fixing GPU kernels, building software from source — done end-to-end through Trinity's agentic workflow, with the debugging story and validated numbers, not just a final checkmark.

<div class="grid cards" markdown>

-   :material-rocket-launch-outline: **BEM_2D: 1,041x speedup porting a 2008 PhD code to CUDA**

    ---

    A 1970s special-function routine gets a from-scratch GPU rewrite, verified bit-identical to the CPU reference at every stage.

    [:octicons-arrow-right-24: Read the full case study](bem2d-cuda-port.md)

-   :material-cube-outline: **BEM_3D: from a 40GB memory wall to a 2TB-equivalent problem**

    ---

    A matrix-free GMRES solver, written from scratch, reaches mesh resolutions no dense method could ever store.

    [:octicons-arrow-right-24: Read the full case study](bem3d-cuda-port.md)

-   :material-chart-bell-curve: **GeoSeries: a 7,638x speedup from four stacked performance bugs**

    ---

    Systematic profiling — not guesswork — finds four independent bottlenecks piled on top of each other.

    [:octicons-arrow-right-24: Read the full case study](geoseries-pvc.md)

-   :material-chip: **Porting a multiphysics framework across GPU vendors — and a 209x kernel speedup**

    ---

    Two weeks, three obscure vendor bugs, and a bypass of the framework's own bottleneck loop.

    [:octicons-arrow-right-24: Read the full case study](moose-libceed.md)

-   :material-dna: **Porting an AlphaFold2 reimplementation to Intel GPUs**

    ---

    A fix to the obvious call site wasn't enough — the same CUDA kernel was hardcoded a second time, deeper in the model.

    [:octicons-arrow-right-24: Read the full case study](openfold-xpu.md)

-   :material-sync: **Adding GPU support to GROMACS on Frontier — a work in progress**

    ---

    Both preferred GPU backends turned out to be unavailable; the honest current result is a real production slowdown, not a win yet.

    [:octicons-arrow-right-24: Read the full case study](gromacs-frontier-port.md)

-   :material-sync: **Porting a spatiotemporal model from AMD to NVIDIA — in under an hour**

    ---

    No model code changed — just the scheduler and hardware-detection glue around it, fixed across 10 job submissions.

    [:octicons-arrow-right-24: Read the full case study](matey-port.md)

-   :material-dna: **Getting a lightweight protein-folding model running on Aurora**

    ---

    A modest deployment story: a silent CPU-only install trap, a network config fix, and a clean inference smoke test.

    [:octicons-arrow-right-24: Read the full case study](chai-lab-aurora.md)

-   :material-cpu-64-bit: **Building PyTorch from source for Intel GPUs**

    ---

    A dead-end build arrangement abandoned for a newer one, resolved autonomously across 23 iterations.

    [:octicons-arrow-right-24: Read the full case study](aurora-pytorch-build.md)

-   :material-bug-outline: **Building a GPU compiler stack — and confirming a known bug still exists**

    ---

    Targeted test kernels isolate exactly which patterns trigger a known closed-source compiler bug, and which don't.

    [:octicons-arrow-right-24: Read the full case study](aurora-pytorch-triton.md)

-   :material-server: **Building PyTorch where the usual submission paths didn't work**

    ---

    Both standard job-submission routes failed outright; a dependency trap silently mismatched GPU toolkit versions.

    [:octicons-arrow-right-24: Read the full case study](sophia-pytorch-build.md)

-   :material-orbit: **Building a cosmology code with no direct system access**

    ---

    Four build failures diagnosed and fixed purely by reading logs through a file-transfer API — no terminal access at all.

    [:octicons-arrow-right-24: Read the full case study](hacc-build.md)

-   :material-gas-cylinder: **Designing a physics experiment from a single sentence**

    ---

    Given only "show PV=NRT," Trinity designed the densities, the runs, and the analysis, and got the right physical trend.

    [:octicons-arrow-right-24: Read the full case study](lammps-pvnrt.md)

</div>

[← Back to Science Campaigns](../index.md)
