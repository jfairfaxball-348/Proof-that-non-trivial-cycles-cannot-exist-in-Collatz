Every genuine fixed-seed trajectory has a first-positive state. By H1, that state lies inside the relaxed first-positive envelope with assigned height no larger than its true height. By positive invariance, the rest of the genuine trajectory is contained in the exhaustive relaxed positive closure. Therefore a genuine `J=2^27` endpoint at height <=26 would force `(1,2^27)` to occur in that relaxed closure.

It does not.

Hence, conditional only on the already-promoted RL288/RL281/RL279 inputs and the exhaustive finite closure above,

`k=27 => H_can >=27`.

Classification candidate:

`FIRST_POSITIVE_ANALYTIC_OVERAPPROX_H26_K27_GATE_A_CLOSURE_PROVED`.

Combined with the H24 k=25 closure and the inherited lower-exponent closures, the local RL292 residual contracts to

`k>=29`, k odd, `H_can<k`.

Repository authority remains unchanged until closeout/promotion.

### H4. Reproducible verifier

Local standalone verifier:

`/mnt/data/rl292_scratch/verify_rl292_first_positive_H26.py`

Frozen output:

`/mnt/data/rl292_scratch/RL292_FIRST_POSITIVE_H26_OUTPUT.txt`

Independent standalone rerun: PASS.

Frozen counts:

- relaxed first-positive seed states: 6,224;
- relaxed positive physical states: 11,380,217;
- `2^27` through H<=26: ABSENT;
- relaxed power minima exactly as listed in H2.

Peak standalone memory in the frozen rerun was approximately 2.16 GB; runtime/implementation performance is not part of the mathematical claim.

### H5. Strategic consequence

The finite k=27 contraction no longer depends on finishing the large `(2,-84)` negative renewal enumeration or on proving the conjectural checkpoint-8 Bellman non-expansion theorem.

Those remain relevant to the scalable infinite residual, but for the finite exponent k=27 the first-positive analytic envelope is enough.

The next principal research target should therefore return to a scalable proof of Bellman/danger-set contraction for odd k>=29 rather than simply increasing the cap again. The checkpoint-8 renewal/equality structure and the relaxed ballot danger-cylinder formulation remain the preferred live routes.

## RL292 continuation — checkpoint-8 transformed-shadow resonance normal form (NOT PROMOTED)

Status: local scratch only. No authoritative repository transition.

### Transformed shadow coordinate
For ordinary Collatz shadows `a,b`, set `u=2a+1`, `v=2b+1` and
`D=v-3^d u`. Using the paired-state identity gives

`D = -2J + 3^d - 2^(d+1) + 1 = -2K + 3^d - 1`,
where `K=J+2^d-1`.

On one canonical pair column `(x,y)` ending at depth `d'`,

`2 D' = 3^y D + 1 - 3^(d')`.

Equivalently, column by column:

- `00`: `D'=-K`;
- `11`: `D'=3^d-1-3K`;
- `01`: `D'=-(3K+1)`;
- `10`: `D'=3^(d-1)-K`.

At a balanced checkpoint `d=1`, `D=-2J`.

For a future from checkpoint `8`, after the forced first `01` column one is at
`(d,J,K,D,A)=(2,15,18,-28,0)`. The strong live candidate
`nu_2(J_end)<=A+1` is equivalent at balanced endpoints to the all-depth candidate
`nu_2(D)<=A+d+1` after departure.

### Exact first-failure resonance theorem
If the all-depth candidate first fails at a child with local area `A'` and depth `d'`, then

`nu_2(D') >= A'+d'+2`,

hence

`D_parent == 3^(-y)(3^d' - 1) (mod 2^(A'+d'+3))`.

Thus excessive valuation is possible only through one explicit depth-labelled 2-adic resonance ball.
In `K` coordinates the four resonance forms are exactly

- `00`: `K`;
- `11`: `3K-3^d+1`;
- `01`: `3K+1`;
- `10`: `K-3^(d-1)`.

At `d=1`, the `00` and `11` forms become `J+1` and `3J+1`. Writing
`n=(J-1)/2`, their exit valuations are exactly those of `n+1` and `3n+2`, i.e.
RL283's two boundary `Beta` templates rooted at `n=-1` and `n=-2/3`.
Therefore the all-depth resonance mechanism and the old boundary hazard are the same object at the wall.

Finite closure of the four raw affine forms is NOT claimed: along retained `d=1` boundary motion the old infinite shifted-template proliferation remains, so the boundary must be quotiented by `Beta` / parity-cylinder isometry rather than by a finite shift table.

### Exact low-cost checkpoint-8 kernel gap
Direct finite analytic enumeration of all first-return excursions from checkpoint `8` with height `<8` gives exactly two returns:

- word `001`, height `2`, return `J=5`;
- word `011`, height `2`, return `J=12`.

There are no first returns of heights `1,3,4,5,6,7`.
The positive zero-height boundary orbit from odd return `J=5` is `5 -> 3 -> 5`, with complementary even exits exactly `{8,2}`.
Hence every checkpoint-quotient macro from `8` of cost `<8` lands in `{2,8,12}`, with cost exactly `2`; every other macro-edge from `8` costs at least `8`.

Regression support:
- `verify_rl292_d_resonance.py` PASS;
- 6,185 exact D-recurrence/column identities checked;
- 30 off-boundary states exhaustively examined below return height 8;
- frozen output `RL292_D_RESONANCE_OUTPUT.txt`.

Classification candidate:
`CHECKPOINT8_TRANSFORMED_SHADOW_RESONANCE_NORMAL_FORM_AND_HEIGHT_GAP_PROVED`.

Gate A remains open. Local unpromoted finite residual remains odd `k>=29`, `H_can<k` after the RL292 k=25 and k=27 contractions.

## RL292 continuation — static boundary-hazard preimage tree (NOT PROMOTED)

Status: local scratch only. No authoritative repository transition.

### Static preimage-tree representation of Beta

At a positive odd `d=1` boundary state write `n=(J-1)/2`. The retained map is the ordinary half-step Collatz map

`C_0(n)=n/2`,
`C_1(n)=(3n+1)/2`,

with the actual retained bit determined by parity. The complementary even-exit hazard is

`h(n)=nu_2(E(n)) = max{nu_2(n+1), nu_2(n+2/3)}`

in the 2-adic valuation on rationals with odd denominator. Thus the two hazard roots are

`alpha_1=-1`,
`alpha_0=-2/3`.

For a binary word `w` of length `t`, weight `r`, and ordinary Collatz numerator `Q_w`, define the exact pullback root

`rho_(w,alpha) = (2^t alpha - Q_w)/3^r`.

Equivalently `C_w(rho_(w,alpha))=alpha`.

Because

`C_w(n)-alpha = 3^r (n-rho_(w,alpha))/2^t`,

one has

`nu_2(C_w(n)-alpha)=nu_2(n-rho_(w,alpha))-t`.

If `w` is not the actual first `t` parity bits of `n`, then `rho_(w,alpha)` lies in the parity cylinder `w` while `n` does not, so the boundary phase-vector isometry gives

`nu_2(n-rho_(w,alpha)) < t`.

Hence such a nonactual branch contributes negatively and cannot beat the actual branch, whose current exit hazard is at least one.

Therefore RL283's dynamic definition

`Beta(n)=sup_(t>=0) nu_2(E(C^t(n)))`

has the exact static form

`boxed: Beta(n)=sup_(t>=0, w in {0,1}^t, alpha in {-1,-2/3}) [nu_2(n-rho_(w,alpha))-t]`.

Equivalently the depth-`R` boundary danger set is the static union of 2-adic balls

`boxed: {Beta>=R} = union_(t,w,alpha) {nu_2(n-rho_(w,alpha)) >= R+t}`.

This removes any need to reason about the eventual ordinary-Collatz orbit when defining the boundary hazard: the entire future boundary danger is a fixed weighted binary tree of 2-adic centres.

### Strong finite-affine-template barrier

The static tree gives a clean analytic strengthening of the old finite-shift barrier.

Take the all-zero pullback ray of `alpha_1=-1`. Fix `L>=2` and put

`n_(R,q)=2^L(2^R q-1)`, with `q` positive odd.

The first `L` retained boundary bits are zero and

`C^L(n_(R,q))=2^R q-1`,

so

`Beta(n_(R,q)) >= R`.

At the initial boundary state `J=2n+1`, the four RL292 transformed-D / K wall forms have valuations exactly

- `nu_2(K)=1`,
- `nu_2(3K-2)=2`,
- `nu_2(3K+1)=0`,
- `nu_2(K-1)=0`,

independently of `R` and odd `q`.

