# RL299 — external Collatz-computation provenance note

Status: **conditional lead / computational evidence, not used for the unconditional promoted frontier**.

RL299 investigated whether public exhaustive Collatz computations could replace direct replay after U5.

The explored sources included Eric Roosendaal's 3x+1 class-record project and David Barina's exhaustive convergence project/released verifier. The useful structural observations were:

- a finite externally verified stopping/delay range can feed the RL299 weight lemma;
- the B-ancestry `16h+15 -> ... -> B0` can reduce the physical start size by roughly a factor of five;
- Barina's released convergence verifier uses the relevant accelerated/half-Collatz dynamics and stores work-unit checksums, but the historical checksum database needed for a new quantitative global bound is not bundled in this repository;
- convergence/descent by itself does not imply the quantitative stopping or `J=O-E` bound required here.

Scratch arithmetic also identified much later resonance records and conditional frontier extensions. These are deliberately not promoted as unconditional RL299 theorem state because their load-bearing external finite certificate was not independently imported and replayed as part of this closeout package.

RL300 may revisit this route only by freezing exact source provenance, scope, and a reproducible/load-bearing certificate. Web-page claims alone are not to be treated as an internal exact certificate.
