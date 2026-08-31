# RL195 independent red team — physical zero adjacency

Date: 2026-08-31. Research-stage review, **NOT PROMOTED**.
BASE_HEAD: `df980ce3df6fa3e8906a934692221917af25644a`.
Reviewer: independent owned-local-realizability worker.

## Verdict

**PASS. No mathematical or finite-coverage finding in the reviewed adjacency
candidate.** The analytic charging argument is valid at the actual constants
and gives the stated conditional bound

`J=#{i mod L:h_i=h_(i+1)=0} >= 9719139553`.

This is a physical chronological edge statistic conditional on the surviving
high branch. It is not a p-shifted height-zero pair, H21 ownership/clean-start
count, necessary terminal population, or a claim that a high-branch word
exists. No promotion or authority change was performed by this reviewer.

## Exact reviewed inputs

- `.rl-work/RL195/artifacts/MOMENT_TO_ZERO_ADJACENCY.md`, SHA256
  `eed5185d8313e9366e6d749cfa506392a6e9742501656da2e91fb389f8d14bac`.
- `.rl-work/RL195/artifacts/verify_moment_adjacency.py`, SHA256
  `b84e93f5e5f065321b7ae760a1e6833313ec5a139fe87b6ddc35b0ec2fd90bc1`.
- Current authoritative RL194 rank-moment/occupation proof, main report,
  proof ledger and correction ledger.

For the one specifically load-bearing universal height definition, I also
read the exact frozen RL181 Section1, its proof ledger and correction
ledger in
`sessions/RL182/RL181_Shallow_Pair_Gap_Corridor_and_Normalized_Width_Occupancy_2026-08-30/`.
This was a narrow live-dependency check, not a broad historical audit or
expensive certificate replay. The sibling RL195 window proof already
carries this same inherited definition explicitly for portable handover.

## Analytic checks

1. **Universal height law.** With `b_i=floor(Ai/L)` and
   `S_i=sum_(j<i)a_j`, the inherited `h_i=b_i-S_i` gives
   `h_(i+1)=h_i+c_i-a_i` at every phase. This one-step identity does not
   inherit the p-shift gap's exceptional carry formula. At a period boundary,
   both b and S increase by A, so the same law remains valid. Nonnegative
   heights and a_i>=1 force h_(i+1)=0 at any c_i=1 source with h_i=0.
   In particular h_0=0 and c_0=1 force the mandatory edge J_0=1.

2. **Complete mechanical partition.** The actual constants obey
   `0<R<B<2R<L`, and chronological rank advance is `r -> r+B (mod L)`.
   Low ranks `[0,R)` advance to `[B,L)`. First c=2 doublet ranks
   `[2R,L)` advance to their second ranks `[R,B)` by subtraction of R.
   Remaining c=2 singletons are `[B,2R)`. These intervals are disjoint in
   their stated roles and cover every rank; no sampled rank test is being
   substituted for coverage. In particular the second-doublet and singleton
   capacities are exactly `[R,2R)`.

3. **Weight ratio and canonical boundaries.** For first-doublet phase i,
   the only possible eta/theta coefficient change under i -> i+1 is at
   i=p-1; a canonical wrap would require i=L-1. Their ranks are respectively
   R+1 and R, strictly below2R, so neither belongs to the first-doublet
   interval. No phase-zero d-weight occurs there. The two d-weights have
   the same coefficient, and the ordinary c_i=2 recurrence gives
   `d_(r-R)=(4/3)d_r` exactly. The canonical/lift distinction is respected.

4. **Binary charging.** For s>0,t=4s/3, the inequality
   `s*x+t*y<=t+s*x*y` holds for all four choices x,y in{0,1}.
   Both present, or only the heavier one present, give equality; the other
   cases satisfy the inequality in the correct direction. The product is
   an actual zero-zero edge at the first-doublet source. Low positive ranks
   have zero indicator equal to their zero-zero edge indicator by item1.
   Singleton occupancy is bounded by its whole weight. Summing gives
   exactly the displayed inequality(6), without double-counting a source.

5. **Mandatory origin and strictness.** Charged source ranks are
   `[1,R)` and `[2R,L)`, which are disjoint and omit phase zero. Their actual
   edge count is therefore at most J-1. Every such d_r is strictly smaller
   than theta: its coefficient is eta or theta, and its canonical rho is
   strictly below1. The independently verified M>C forces at least one
   charged edge, so the strict inequality
   `M<=Z0<C+theta*(J-1)` is justified, not inferred from a possibly empty sum.

6. **Exact capacity.** Direct inverse-rank arithmetic gives
   `I(R-1)=z-1`, `I(2R-1)=z-2`, with canonical z-2,z-1,z. Their mechanical
   digits are2 and1, so
   `w_(R-1)=3rho_z/2`, `w_(2R-1)=9rho_z/8`.
   Consequently the full telescoped capacity is
   `C=3rho_z/8=3(1+theta)/16`. No endpoint rank or carry weight is omitted.

7. **Moment and exact rounding.** The incoming moment yields
   `Z0>=M=2F-3rho_z+1` by the integer-height inequality V<=1/2 off height
   zero. Substituting the capacity gives
   `(M-C)/theta=(2F-11/16)/theta-27/16`.
   The strict inequality is `J-1>(M-C)/theta`, not J greater than that
   quantity. Its certified position between9719139551 and9719139552
   forces J-1>=9719139552, hence J>=9719139553. The off-by-one accounting
   is correct.

## Supplied verifier and independent constant replay

The supplied verifier ran successfully:

`python3 .rl-work/RL195/artifacts/verify_moment_adjacency.py`

It returned PASS, including256 bounded toy height arrays,7 admissible arrays
and3 strict cases. These are correctly classified as algebraic regressions,
not actual high-branch phase coverage.

I wrote and ran the independent audit script

`python3 .rl-work/RL195/agent_owned_realizability/verify_adjacency_independent.py`

SHA256:
`8c5861885357da0ff24cc7ac0cf17f1ad14f62eedec7257dc757654436468e7d`.

It uses128 positive rational logarithm terms with explicit geometric tails,
and degree12 expm1 sums with a first-omitted-term geometric tail. This
differs from the candidate's96 logarithm terms and quadratic expm1 bounds.
All decisions use Fraction arithmetic; decimals below are outward display
enclosures only:

- `0.241061109894 < M < 0.241061109895`;
- `0.187500000001 < C < 0.187500000002`;
- `9719139551.442382121733 < (M-C)/theta < 9719139551.442382121734`.

The underlying exact threshold interval has width below10^-40.
The script separately proves positivity before dividing interval numerators
by theta, checks the boundary rank identities, and exhausts all four binary
charging assignments. It returns PASS.

## Scope preservation and outstanding review boundaries

The candidate uses all cyclic chronological phases analytically; there is
no incomplete giant phase scan. N0's earlier floor is not substituted into
the false positive estimate2N0-L. No canonical early signature is moved to
another origin. Inherited terminal rank filters, spacing>=1001, flow/
variation bounds and the H21 budget are retained.

This review covers only the adjacency theorem and named numeric/geometry
checks. It does not confer a PASS on unrelated sibling code or replace
their own reviews. The separately reported owned-local helper assertion
repair is outside this adjacency review and is being handled by the parent.
No parent proof or verifier was edited by this reviewer.
