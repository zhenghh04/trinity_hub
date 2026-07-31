# Does an open-source ptychography framework reproduce its own paper?

**Reproducing:** *PtyRAD: A High-Performance and Flexible Ptychographic Reconstruction Framework with Automatic Differentiation* (Lee et al., Microscopy and Microanalysis, 2025). DOI: 10.1093/mam/ozaf070
**System:** Polaris · **Status:** :material-sync: In progress

## The goal

Check whether the authors' own open-source release of this ptychographic image-reconstruction framework actually reproduces its own published results end-to-end on independent hardware — useful both as due-diligence before adopting the framework for future imaging work, and as a template for future software-paper reproductions.

## What happened

The framework's configuration format had changed since the paper's original snapshot, requiring a full config rewrite before anything would run. Two of six planned reconstruction targets have been rerun to completion so far, with the remaining four queued.

## Results

- First target: per-iteration reconstruction loss trajectory matches the authors' own reference run to 3-4 significant figures.
- Second target: final reconstruction loss after 200 iterations matches the authors' bundled benchmark value to about 4 significant figures (0.3702 vs. 0.37020397).
- An informal speed comparison suggested a substantial advantage from newer GPU hardware, though this wasn't an apples-to-apples benchmark against the authors' original setup.
- Four more targets (including a regularization ablation and a hyperparameter-tuning demo) are queued to complete the full reproduction.

[← Back to Paper reproductions](index.md)
