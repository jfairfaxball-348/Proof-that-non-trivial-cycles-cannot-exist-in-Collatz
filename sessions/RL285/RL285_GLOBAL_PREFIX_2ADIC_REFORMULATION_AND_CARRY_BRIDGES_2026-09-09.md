# RL285 — global-prefix 2-adic reformulation and carry bridges

Date: 2026-09-09

Primary classification:

`GLOBAL_PREFIX_2ADIC_REFORMULATION_AND_FIRST_CARRY_BRIDGES_PROVED`

Gate A is **not closed**. The exact inherited residual remains

`k>=25`, `k` odd, `H_can<k`.

The preferred sufficient theorem remains

`globally reachable positive even d=1 checkpoint (J,H) => nu_2(J)<=H`.

## 1. Correction to unpromoted scratch

An early scratch proposal

`nu_2(J) <= H-d+1`

for all positive depths is false. The genuine reachable state `(d,J,H)=(2,4,2)` violates it.

This proposal was never promoted. No inherited theorem is demoted.

## 2. Post-column area and normalized valuation candidate

Keep

`K = J + 2^d - 1`

and define

`A = H + d - 1`.

If `d_i` is the depth after column `i`, then exactly

`A_n = sum_{i=1}^n (d_i-1)`.

Thus `A` is the post-column depth area. For a paired prefix `(x,y)`, it is also the area between the two prefix one-count paths.

The natural all-depth candidate is

`nu_2(K-1) <= H+d-1`.

At `d=1`, `K-1=J` and this is exactly the RL285 Gate-A target.

This global statement is **CONJECTURAL**.

### Exact finite certificate through H<=22

The complete normalized-state closure from `(d,J,H)=(1,-13,0)` through accumulated height `H<=22` contains:

- `3,837,389` reachable raw states;
- `584,154` positive raw states;
- maximum positive depth `7`;
- zero positive violations of `nu_2(K-1)<=H+d-1`;
- exactly three equality states:
  - `(d,J,H)=(1,8,3)`;
  - `(2,6,2)`;
  - `(3,2,1)`.

This is promoted only as an **exact finite certificate over H<=22**, not as a global theorem.

## 3. Shifted-shadow representation

For a binary word `w`, let the RL283 shadow numerator be

`U_w = -7*3^r + Q_w`.

Define

`W_w = U_w + 2^{|w|}`.

Then exactly

`W_empty=-6`,

`W_{w0}=W_w+2^{|w|}`,

`W_{w1}=3W_w`.

For a canonical paired prefix of length `n` and current depth `d`, set

`Z = 2^n(K-1)`.

Then

`Z = 3^d W_x - W_y - 2^n`.

The candidate inequality is equivalently

`nu_2(Z) <= n + A = sum_{i=1}^n d_i`.

At `d=1`, this is exactly the cleared-numerator form of `nu_2(J)<=H`.

## 4. Prefix-dominance/rank area identity

Suppose the one positions of `x` are `a_1<...<a_p` and those of `y` are `b_1<...<b_q`, with `q=p+d-1` and prefix dominance `b_j<=a_j` for matched ranks.

Give each unmatched `y`-rank a virtual `x`-position `a_j^*=n` for `p<j<=q`.

Then exactly

`A = sum_{j=1}^q (a_j^* - b_j)`.

Thus the depth correction `d-1` is precisely the displacement carried by unmatched ranks.

The arbitrary-depth cleared numerator has the exact rank form

`Z = -14*3^q + ((3^d-1)/2)*2^n + sum_{j=1}^q 3^{q-j}(3*2^{a_j^*}-2^{b_j})`.

## 5. High divisibility reconstructs canonical prefix legality

Take a formal prefix-dominant paired word, without assuming parity legality. If

`2^{n+A+1} | Z`,

then in particular `2^n | Z`, so the formal endpoint `J` is integral.

Each column has the affine form

`J_{i+1}=(c_i J_i+q_i)/2`

with odd `c_i`. Backward integrality therefore reconstructs integral `J_i` at every earlier prefix, and that integrality is exactly the required parity legality for the prescribed column.

Hence dangerous high divisibility is not an easier algebraic relaxation:

`high final divisibility + prefix dominance => genuine canonical prefix`.

If additionally `Z>0`, then since `A>=d-1`, high divisibility implies `K-1>=2^{A+1}>=2^d`, hence `J>=2`. Therefore a positive high-divisibility formal pair reconstructs a genuine positive canonical violation.

Equivalently, Gate A is embedded in the pure word-sign statement

`2^{n+A+1} | (3^d W_x-W_y-2^n) => 3^d W_x-W_y-2^n <= 0`.

No proof of this global sign theorem is claimed.

## 6. Four first-entrance congruences and local barrier

Let `M=K-1` and `A=H+d-1`. A first entrance into the bad cylinder is forced into one of four exact parent congruences:

- `11`: `3M+1 == 0 (mod 2^{A+d+1})`;
- `00`: `M+3^d-2 == 0 (mod 2^{A+d+1})`;
- `10`: `M-2 == 0 (mod 2^{A+d})`;
- `01`: `3M+3^{d+1}+1 == 0 (mod 2^{A+d+2})`.

These do not close locally. Positive residue-admissible fake parents exist for every branch, e.g. `J=21,63,18` at `d=1,H=3` and `J=64` at `d=2,H=3`, mapping into a child with `K'-1=32`.

Thus the candidate remains genuinely global.

## 7. Two-shadow/zero-mass equivalence

Let `q_w=2^n/3^r` and let `S_w` be the inherited zero-rank mass. Then exactly

`C_w(-7)+1 = (S_w-6)/q_w`.

At an equal-weight `d=1` checkpoint this gives

`q(J+1)=3S-S_v-12`,

which is exactly the inherited `B` telescope in shifted-shadow coordinates.

Therefore final shadow signs are not independent global invariants; they are zero-mass threshold statements in disguise.

A relaxed scalar construction at `k=25,H=3` satisfies the endpoint/zero-mass/coupon equations and final shadow-sign condition while still having `H<k`. It is noncanonical and is recorded as a route barrier: endpoint scalar data alone does not close Gate A.

## 8. Ferrers-cell carry identity and first-carry rigidity

For an equal-weight `d=1` paired prefix with matched one positions `b_j<=a_j`, the shifted-shadow difference is

`W_x-W_y = sum_j 3^{r-j}(2^{a_j}-2^{b_j})`.

Equivalently it is the sum over the Ferrers/displacement cells; an adjacent rightward `10 -> 01` swap across position `p`, with `s` later ones, contributes exactly `2^p 3^s`.

Let

`b_* = min{b_j : a_j>b_j}`.

There is a unique contribution at the lowest power `2^{b_*}`, so

`nu_2(W_x-W_y)=b_*`.

Writing the full cleared checkpoint numerator as

`Z = B_y + 3(W_x-W_y)`,

endpoint divisibility forces

`nu_2(B_y)=b_*`.

Backward divisibility along the diagonal prefix then reconstructs a legal zero-height boundary trajectory up to `b_*`, and the first mismatch is necessarily the legal `01` ascent from an even `J` into the first off-boundary excursion.

Thus:

`FIRST_CARRY_RECONSTRUCTS_FIRST_EXCURSION_ENTRY_PROVED`.

Iterating this peeling does not yield a new scalar inequality; it reconstructs the existing boundary/excursion decomposition. This is recorded as a route limitation, consistent with RL283's per-cell valuation-Lipschitz barrier.

## 9. Terminal extension as signed area

For terminal `J=2^k`, append the RL283 forced tails

`X=x 1 0^k`,

`Y=y 0^k 1`.

The extension runs formally at depth `0` for `k` columns before returning to depth `1`. Its signed area contribution is exactly `-k`.

Hence the balanced extended path has total signed area

`H-k`.

Gate A is exactly the assertion that this signed area is nonnegative for the fixed-endpoint extended pair.

No inherited cyclic/selector extremality was found that would make this immediate; the signed-area reformulation is promoted as an exact bridge, not a closure theorem.

## 10. Proof-state summary

Promoted analytic results:

- `POST_COLUMN_AREA_IDENTITY_PROVED`;
- `POST_COLUMN_AREA_EQUALS_PREFIX_DOMINANCE_AREA_PROVED`;
- `SHIFTED_SHADOW_K_MINUS_ONE_REPRESENTATION_PROVED`;
- `ALL_DEPTH_HIGH_DIVISIBILITY_RECONSTRUCTS_CANONICAL_PREFIX_PROVED`;
- `POSITIVE_HIGH_DIVISIBILITY_SIGN_REFORMULATION_PROVED`;
- `FOUR_BRANCH_FIRST_ENTRANCE_CONGRUENCE_CLASSIFICATION_PROVED`;
- `SHADOW_ZERO_MASS_COORDINATE_EQUIVALENCE_PROVED`;
- `FERRERS_CELL_SHIFTED_SHADOW_IDENTITY_PROVED`;
- `FIRST_DISPLACEMENT_2ADIC_RIGIDITY_PROVED`;
- `FIRST_CARRY_RECONSTRUCTS_FIRST_EXCURSION_ENTRY_PROVED`;
- `TERMINAL_EXTENSION_SIGNED_AREA_REFORMULATION_PROVED`.

Promoted exact finite certificate:

- `POST_COLUMN_2ADIC_INVARIANT_H22_RAW_CERTIFICATE`.

Promoted barriers/route limitations:

- `FALSE_DEPTH_RESERVE_SCRATCH_CORRECTED`;
- `LOCAL_POST_COLUMN_VALUATION_INDUCTION_BARRIER`;
- `FINAL_SHADOW_SIGN_SCALAR_CLOSURE_BARRIER`;
- `ITERATED_CARRY_PEELING_RECONSTRUCTS_EXISTING_EXCURSION_STRUCTURE`.

Open/conjectural:

- global `nu_2(K-1)<=H+d-1`;
- the equivalent positive high-divisibility sign theorem;
- Gate A itself.

Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.
