# RL47 Research Session Kickoff

Continue the Collatz R-sharp / RL one-excursion research from the attached `Collatz_Rsharp_RL46_to_RL47_Handover_2026-08-22.zip` as a skeptical research mathematician.

## 0. Mandatory verification

First verify the bundle checksums and run:

```bash
sha256sum -c SHA256SUMS.txt
bash verification/run_rl46_structural_verifiers.sh
bash verification/run_rl46_q55_verifier.sh
```

Treat any failure as a stop-and-repair event. Do not extend the research until the failed certificate is understood.

Read, in order:

1. `README_START_HERE.md`
2. `RL46_REPAIR_AND_PREFIXCAP_PROGRESS.md`
3. `RL46_REPRODUCIBILITY_LEDGER.md`
4. inherited RL45 notes if a dependency needs reconstruction.

## 1. Re-audit the RL46 repair before using it

Independently reconstruct the neutral `11` self-loop at `d=1,T=-2` and the exact prefix-cap inequality. Verify line-by-line that:

- a virtual pump may start only when its first actual pump column is cap-legal;
- once legal, each additional neutral pump improves the cap ratio by `2/3` and stays legal;
- this repair explains why the earlier e=43..49 and e=52 candidates were spurious.

Also independently audit the analytic claims:

- `3` never divides an internal `T`;
- terminal `t` is even;
- the inherited final moved-rank cap excludes `t=0`, hence `t>=2`;
- `H=e-z+1=sum(d-1)` and `e>=q+2` is equivalent to `H>=t+3=v2(T+1)`.

Do not promote any of these if an inherited assumption is being used outside its proved scope.

## 2. Main attack: uniform terminal area/valuation lemma

The priority theorem remains

\[
H\ge t+3=v_2(T+1)
\]

for every genuine retained one-excursion terminal geometry.

Do **not** attack arbitrary height-one dynamics by proving global settling: RL45/RL46 found that the unrestricted height-one quotient is exactly conjugate to the ordinary Collatz map, so that route risks circularity.

Exploit instead the genuine prefix-cap / near-minimum structure. The exact fixed-pair layer DP shows that at actual column `n`:

- `p_alpha=n-z` is redundant;
- for fixed `(d,T,z)`, minimum `H` dominates;
- every strict counterexample lies in the triangular live region `H+z<q+3`;
- equality lies on `H+z=q+3`.

Find an additional analytic quotient or monotone invariant that controls the growth of exact `T` states. The q=79 run is the current stress point. Prefer a proof-level compression over simply increasing RAM or extending a cutoff.

Promising directions to test rigorously include:

- cap-slack variables that evolve monotonically and may bound admissible `T` residues;
- reverse/preterminal analysis, using the rigidity `T+1=2^{t+3}` with even `t>=2`;
- dominance relations stronger than exact equality of `T` but still preserving parity/integrality and future cap tests;
- induction on `q` or on the area budget `H`, using the boundary `H+z=q+3`.

Reject any proposed quotient unless you can prove it cannot merge a violating path with a nonviolating one.

## 3. Exact finite frontier

After the analytic work, try to settle `(a,ell,q)=(214,135,79)` exactly if a genuinely better state representation emerges. The bundled old q=79 log is **partial only** and must not be cited as a certificate.

The already certified fixed pairs are:

- `(46,29,17)`: no terminal geometry at all;
- `(65,41,24)`: unique structural terminal record, exact minimum excess `125`;
- `(149,94,55)`: no terminal state with `H<=t+3`.

Use these as regression cases for every new quotient/invariant.

## 4. Radius-3 bridge track — secondary

Only if the terminal-area attack stalls after a serious attempt, continue the RL45 same-root arithmetic direction. Do not revive the disproved universal bound

\[
|\operatorname{Res}(3T^q-2,P)|_{(3')}<X-Y.
\]

The better target is a gcd/subresultant/Bezout statement tying a common root of the phase polynomial to the short-binomial anchor and the full denominator. Any claim here must explicitly identify the missing quantitative lemma needed for closure.

## 5. Proof-state discipline

Keep separate ledgers for:

- analytic theorems;
- exact finite certificates;
- inherited dependencies;
- partial computations;
- conjectures / heuristic patterns.

The objective is not to accumulate numerics. The objective is to turn the prefix-cap geometry into a cutoff-free terminal valuation/area theorem, or to isolate a precise smaller lemma whose proof would do so.

Before ending the session, package all new source, verifier output, proof notes, checksums, and a next-session kickoff in one handover bundle.
