# Silicon's electronic band structure from first principles

**System(s):** Polaris · **Code:** Quantum ESPRESSO · **Outcome:** :material-atom: Success

## The ask

*(This campaign predates verbatim prompt logging — the request below is reconstructed from the campaign's documented design, not a direct quote.)*

> "Compute the electronic band structure and band gap of crystalline silicon using DFT."

## What happened

Trinity ran the full four-step Quantum ESPRESSO band-structure workflow (self-consistent field → non-self-consistent field → band calculation → post-processing) on a 2-atom silicon unit cell. Early attempts failed because the required pseudopotential library isn't bundled with the installed version of Quantum ESPRESSO on this system — it had to be found and staged first, a fact now captured for future runs.

## Results

- Computed an indirect band gap of 0.54 eV (DFT-PBE typically underestimates the experimental 1.17 eV band gap by roughly 50%, a well-known limitation of this method, not an error).
- Full 4-step workflow completed in about 24 seconds total on one GPU node — roughly 50x faster than the same calculation would take on CPU.
- Key infrastructure finding: this Quantum ESPRESSO installation ships no pseudopotential library by default; pseudopotentials must be pre-staged.

[← Back to Science campaigns](index.md)
