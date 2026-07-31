# Predicting Ti K-edge XANES spectra across three TiO2 polymorphs

**System:** Local (ML inference) · **Type:** ML spectral prediction · **Outcome:** :material-waveform: Success

## The ask

*(This campaign predates verbatim prompt logging — the request below is reconstructed from the campaign's recorded intent, not a direct quote.)*

> "Predict Ti K-edge XANES spectra for the three main TiO2 polymorphs (anatase, brookite, rutile) and benchmark them against experimental reference standards."

## What happened

Trinity pulled all three TiO2 polymorph structures from Materials Project and compared their predicted Ti K-edge XANES spectra — via a machine-learned spectral-prediction model — against experimental reference standards, using five different similarity metrics plus an energy-shift optimization. All three predictions were correctly matched to their corresponding experimental standard. One subtlety: brookite and anatase were nearly tied on one similarity metric, and a derivative-based metric was needed as an unexpected tiebreaker to correctly tell them apart — a genuinely useful methodological finding for future spectral-matching work.

## Results

- Anatase: best correlation 0.971 with its reference standard.
- Brookite: best correlation 0.944, correctly distinguished from anatase using a derivative-based tiebreaker metric.
- Rutile: best correlation 0.953.
- All three polymorphs correctly ranked and matched to their reference; all metrics exceeded the 0.9 similarity threshold set as the success criterion.

[← Back to Trinity runs](index.md)
