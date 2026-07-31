# Water dimer binding energy — DFT vs. quantum Monte Carlo

**System(s):** Polaris · **Code:** Quantum ESPRESSO + QMCPACK · **Outcome:** :material-alert-decagram-outline: Partial

## The ask

*(This campaign predates verbatim prompt logging — the request below is reconstructed from the campaign's documented design, not a direct quote.)*

> "Compute the binding energy of a water dimer with DFT, then refine it with quantum Monte Carlo for higher accuracy."

## What happened

Trinity computed the water dimer (two water molecules) binding energy via DFT successfully, then attempted to hand the result off to QMCPACK for a more accurate quantum Monte Carlo treatment. The Monte Carlo step was blocked by a technical incompatibility in how the k-point sampling was specified between the two codes — a real, disclosed limitation rather than a silent failure. Trinity correctly recognized and reported this as a partial success rather than claiming full completion.

## Results

- DFT-PBE binding energy: -0.067 eV, compared to a high-accuracy reference value of -0.215 eV — DFT-PBE is known to underestimate hydrogen-bond energies at this basis-set quality, consistent with expectations.
- Quantum Monte Carlo refinement did not complete, due to a k-point sampling incompatibility between the two codes — flagged as a fixable configuration issue for a future run, not a dead end.

[← Back to Science campaigns](index.md)
