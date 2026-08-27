# RL130 target — extend the quotient-descent frontier beyond `L=40`

Start from the frozen RL129 primitive ordinary frontier `L>=41`.

1. Reuse the proved quotient-rotation lemma and universal transition-root bound
   `Q <= 2^(Z-1)(3^L-2^L)`.
2. For each new `L`, use the smallest positive `Z` only; prove/retain monotonicity in `Z` rather than scanning an unbounded tail.
3. Begin with `L=41`, whose exact quotient ceiling is `727,618,641`, and extend through the largest contiguous block that can be certified reliably in-session.
4. Extend the exact odd-start descent certificate only as far as required by the largest new quotient ceiling; use induction/checkpointing and exact integer arithmetic.
5. Study the spikes caused by unusually small positive `D=2^(L+Z)-3^L`, including continued-fraction/Diophantine structure, to seek a scalable ceiling law or a coupling to an inherited global closure route.
6. A quotient that reaches `1` gives only the trivial periodic parity word and cannot support a primitive nontrivial candidate.  Preserve this primitivity step explicitly.
7. Preserve all inherited ownership, scaling, physical-state, Raw/Farey, correction/demotion, verification-economy, sustained-attack, and finite-certificate rules.

Do not claim Gate A/B or global Collatz closure unless their independent obligations are actually discharged.
