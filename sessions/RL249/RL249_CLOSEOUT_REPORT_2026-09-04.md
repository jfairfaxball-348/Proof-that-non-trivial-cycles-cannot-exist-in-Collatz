# RL249 closeout report

Date: 2026-09-04
Classification: **`R4_BRIDGE_REDUCED`**.

## Scope

RL249 continued only the audited Branch-C `beta(P)=6` target inherited from RL248. Gate A remains open. Gate B remains open. Radius 5 remains inactive. Radius 4 is not invoked in this session.

The incoming exact flow is

`P_i = r - W_i^u(q)`, with `ar-q ell=2`,

and exact derivative

`P_(i+1)-P_i = u_i-u_(i+q)`.

Branch C means every negative root is an isolated singleton valley, with cyclic gap at least three between negative roots.

## 1. Analytic beta=6 profile contraction — PROMOTED

Assume Branch C and `beta(P)=6`.

Every negative root is therefore exactly `-1`, so there are exactly six negative roots. Since `sum_i P_i=2`, total positive mass is exactly

`sum_i (P_i)_+ = 8`.

A positive component reaching height 3 would contain at least the 1-Lipschitz profile `1,2,3,2,1`, of positive mass 9. Hence

`boxed: P_i in {-1,0,1,2}`

for every root.

Consequences:

- total absolute mass `sum_i |P_i|=14`;
- positive support has at most 8 roots;
- total nonzero support has at most 14 roots.

## 2. Exact mismatch/variation contraction — PROMOTED

The q-shift Hamming defect is exactly the total variation:

`M_q := #{i : u_i != u_(i+q)} = sum_i |P_(i+1)-P_i|`.

By the cyclic triangle inequality,

`M_q <= 2 sum_i |P_i| = 28`.

Each of the six isolated `-1` roots forces one down-step and one up-step at its two boundaries, and these twelve boundary steps are distinct. Therefore

`boxed: 12 <= M_q <= 28`.

Because the cyclic derivative sums to zero, the number of `0->1` q-shift mismatches equals the number of `1->0` mismatches. Each orientation occurs between 6 and 14 times.

This is word/counterflow geometry only. It is not a Radius-4 distance theorem.

## 3. Mandatory q-shift agreement corridor — PROMOTED

RL248 freezes `z=a-ell>=46`, while the retained resonance gives `a/ell<8/5`. Therefore

`a > (8/3) z >= 368/3`,

so `a>=123`.

At most 14 roots have `P_i!=0`, hence at least `a-14>=109` roots have `P_i=0`. Their cyclic zero set has at most 14 runs, so one run has length at least

`ceil(109/14)=8`.

If `P_j=...=P_(j+7)=0`, then on the seven edges `i=j,...,j+6`,

`0=P_(i+1)-P_i=u_i-u_(i+q)`.

Thus

`boxed: u_j...u_(j+6)=u_(j+q)...u_(j+q+6)`.

The inherited `min(q,a-q)>=8` makes these two length-7 factors disjoint.

Important scope: this is synchronization of `u` with its q-shift. It is **not** automatically an RL64 synchronized `(u,v)` canonical block.

## 4. Zero-run q-propagation lemma — PROMOTED

Let an ordinary `u`-zero run have length `L>=10`:

`u_s...u_(s+L-1)=0^L`.

On every site of the run,

`P_(i+1)-P_i=-u_(i+q)<=0`.

No zero-run root can have `P_i=-1`: then `P_(i+1)<=-1`, creating adjacent negative roots and contradicting Branch C. Hence `P_i>=0` throughout the zero run and `P` is non-increasing there.

The entire cycle has only eight units of positive `P` mass, so by the ninth root of the run the value has reached zero. For every subsequent non-final zero-run site, a shifted `1` would create a negative value which, at the next zero site, forces an adjacent negative root. Therefore

`boxed: 0^L in u => a consecutive 0^(L-9) block in the q-shifted positions}`.

This lemma uses the current determinant-2 q only. No historical Gate-A q identity is used.

## 5. Refined near-resonant ratio — PROMOTED

The inherited scale window is

`1 < 2^a/3^ell`, `(2^a/3^ell)^2 < 16/15`.

Let `rho=log_2(3)`. Then

`0 < a-rho ell < (1/2)log_2(16/15)`.

From `z>=46` and `a/ell<8/5`, one has `ell>=77`.

If `a/ell>65/41`, integrality gives `41a-65ell>=1`, so

`a-rho ell >= ell(65/41-rho)+1/41`.

At `ell=77` this lower bound already exceeds `(1/2)log_2(16/15)`, contradiction. Hence

`boxed: log_2(3) < a/ell <= 65/41`.

Equivalently,

`boxed: 1-1/log_2(3) < (a-ell)/a <= 24/65`.

This sharpens the retained coarse corridor on the beta=6 Branch-C survivor.

## 6. Phase-magnitude route barrier — PROMOTED AS BARRIER

RL47 gives `Phi_start=-8` and terminal

`Phi_terminal=9 R (1+2^-k)`, `R=2^a/3^ell>1`.

Therefore the required total phase rise is strictly greater than 17.

RL248's valid beta=6 selected-positive aggregate lower bound is only

`DeltaPhi_selected_01 > 2/6561`.

Thus the current lower bound, used **only as a magnitude estimate**, cannot itself overshoot the terminal phase requirement or force compensating negative motion. Any successful phase attack must use exact support/order/ownership/residue information or prove a much stronger total-positive estimate.

This is a route barrier, not a proof that the phase route fails.

## 7. Corrections and demotions made during RL249

The following exploratory statements are **NOT PROMOTED** and must not be inherited as theorems:

1. **Historical/current q collision.** Earlier scratch identified the historical Gate-A identity `q=z+t` from RL47 with the current determinant-2 rotation parameter satisfying `ar-qell=2`. No authoritative theorem identifying these two q-parameters was located. All explicit zero-desert placements and zero-budget bounds depending on that identification are demoted.
2. In particular, scratch bounds such as `z>=48`, `z>=57`, `z>=58`, `m>=19`, `m>=28`, `m>=29`, and the special `k={31,33,35}` split are not promoted from those arguments.
3. The later proposed quadratic zero-desert amplification and formulas `z >= (k^2-21k+126)/2`, `m >= (k^2-23k+130)/2` are **NOT PROMOTED**. Their low-denominator separation/overlap induction was not independently audited to the repository standard before closeout.
4. The final exploratory claim that q-ordered zero-block covering forces `B in {13,14}` in the coprime case, `B=14` in the two-orbit case, and hence globally `P_i in {-1,0,1}`, is **DEMOTED / NOT PROMOTED**. Closeout red-team checking found that one stated coprime 12-block covering formula was not exact. The direction may remain worth revisiting, but no theorem is inherited.
5. A q-shift agreement block in `u` is not an RL64 synchronized `(u,v)` block unless a separate ownership theorem identifies them.
6. RL246's old uniform single-packet `>1/4374` statement remains demoted exactly as in RL248.

These demotions leave Sections 1–6 above unaffected.

## 8. Verification

Portable verifier `verification/verify_rl249_beta6_profile.py` checks:

- beta=6 mass bookkeeping;
- the 14-unit absolute-mass and 28-mismatch ceilings;
- the inherited `z>=46` / resonance consequences `a>=123`, at least 109 zero roots, and an 8-root `P=0` run;
- the 7-edge q-shift agreement consequence;
- exhaustive local zero-run propagation states for lengths through 64 under the exact promoted hypotheses;
- the strict arithmetic comparison proving `a/ell<=65/41` from `ell>=77` and the scale window;
- `2/6561 < 17` for the magnitude-only phase barrier.

Fresh clean reconstruction, internal SHA256 manifest verification, and the portable verifier all pass at closeout.

## 9. Remaining live obstruction / successor route

Beta=6 Branch C is not eliminated. The correct next target is no longer a generic magnitude estimate. RL250 should combine:

- exactly six singleton negative roots and only eight positive mass units;
- at most 28 total q-shift mismatch edges;
- the mandatory disjoint 7-column q-shift agreement corridor;
- the zero-run q-propagation lemma;
- the refined `a/ell<=65/41` corridor;
- RL248's exact selected `10` event-versus-rigid canonical arms and physical envelope amplification;
- exact RL47/RL64 full-phase/terminal ownership.

The aim is to classify the finite defect/event support tightly enough to force either canonical descent/height for Gate A, an exact full-phase contradiction, or a fully audited eligible Radius-4 self-rotation.

Gate A: open.
Gate B: open.
Radius 5: inactive.
Knowledge catalogues: stale/deferred.
