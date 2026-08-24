# RL-5 Roadmap Update — 2026-08-19

## Rank 1 — attack the rotation numerators modulo the cycle denominator

RL-L39 now supplies the missing common-denominator object. For every cyclic compressed word,

`W_r = C_r / [6^M(2^A-3^L)]`

at every rotation `r`.

The next theorem must use the **content** of this divisibility rather than merely restating it. Insert the two root gates:

- departure from the least anchor: RL-L27/RL-L33 forced-low exit;
- final return: RL-L36 odd `t`, strict high return, realized root side probe, and exact discrete-log class modulo `2*3^(n-1)`.

RL-L41 now shows that for generic admissible words, `D|C_r` at one rotation is already necessary and sufficient for the entire periodic integer anchor orbit. Primary target: find a prime divisor `p | D`, `D=2^A-3^L`, for which the two root gates force `C_r != 0 (mod p)`, or derive a lift/descent relation that excludes `D|C_r` directly.

If compatible words persist, characterize the recurrent residue family explicitly rather than reverting to a root-only sieve.

## Rank 2 — solve the exact saturation-boundary exception to RL-L41

RL-L40 shows the numerator valuations are much less mysterious than expected:

- `v2(C_r)=M+n_r` is automatic for every valid word;
- `v3(C_r)=M` is automatic whenever no transition satisfies `v3(2^t-1)=n`.

Therefore all genuinely nontrivial 3-adic numerator cancellation is localized to the exact boundary

`v3(2^t-1)=n`,

or equivalently

`v3(t/2)=n-1`.

Primary target: derive the finite 3-adic cancellation automaton for these boundary exits and test whether a periodic word can carry the required cancellation at **every** affected rotation.

## Rank 3 — exploit the multiplicative-ceiling map

Every transition is

`W_(j+1)=ceil(a_j W_j)`, `a_j=3^(h_j)/2^(h_j+t_j)`.

For a fixed discrete word the periodic rational orbit is unique. Seek a denominator-descent or monotonicity theorem for compositions of these ceiling maps, especially when the root is the strict minimum and the first/last coefficients have opposite xi direction.

A useful intermediate result would bound the possible residue of `W_0` modulo a prime factor of `D` using only a short prefix/suffix of the word.

## Rank 4 — extend the exact finite compressed-word sieve only when it tests a theorem

The verifier currently checks 75,894 words in the diagnostic domain

`P<=3`, `n,t<=6`, cancellation depth<=2,

and finds only repetitions of the trivial `W=2` anchor.

Do not scale this blindly. Increase the domain only after deriving a residue, boundary-cancellation, or ceiling-composition invariant whose failure/survival the enumeration can diagnose.

## Rank 5 — k>0 extend the 2R# rigidity horizon

RL-L37 makes physical order equal the sign of `C_h=D_h-E_h` for all `h<=2R#` unless `C_h=0`.

Replace the uniform per-step correction bound by a cumulative reciprocal-height budget. If the total correction remains below one bit on successive chunks, repeated crossings reduce globally to an integer walk plus zero-level events.

## Guardrails

- Do not multiply local Haar costs as if exits were independent.
- Do not return to root-only xi sieving as a closure route.
- Do not mistake the automatic numerator valuations in RL-L40 for new global leverage.
- Hercher `m>=92` is an external structural guardrail, not an internally re-proved theorem.
- RL remains open.
