# RL306 scratch freeze

Date: 2026-09-12
Status: FROZEN SUPPORTING SCRATCH. The report/proof ledger controls theorem status.

This file preserves the live research frontier, including partial results, diagnostics, failed shortcuts, numerical certificates and formulas that were useful during RL306 but do not all have promoted theorem status.

## 1. Scalar-safe wall windows before clipped debt

Assume `Bcal(8)<=3`. RL303 gives exact entries

- `8 -> L_D` at `B_L(D)+3`;
- `8 -> RW_D` at `B_R(D)+3`.

Hence `X_L,X_R<=6`. Any normalized owner branch of weight `w<=-3` is immediately safe at target `X<=3`.

Using RL305 exact weights gives coarse safe windows:

- `L_D -> RW_(D-2)`, `w=k-D-4`: `k<=D+1`;
- `L_D -> L_(D-2)`, `w=k-2D-5`: `k<=2D+2`;
- `RW_D -> L_(D-2)`, `w=k-3D-2`: `k<=3D-1`;
- `RW_D -> RW_(D-2)`, `w=k-2D-8`: `k<=2D+5`;
- adjacent `L_D -> RW_D`, `w=D-k-1`: `k>=D+2`.

These are different prefix cylinders and do not form a complete cover.

## 2. Clipped four-level wall debt

Still under `Bcal(8)<=3`, define

`y=max(0,X-3)`.

Then `0<=y<=3`, and an exact normalized source-to-owner rewrite of weight `w` satisfies

`y_source <= clamp(y_owner+w,0,3)`.

For owner debt zero the exact layers are:

1. `L_D -> RW_(D-2)`, `w=k-D-4`:
   debt 0 for `k<=D+4`, 1 at `D+5`, 2 at `D+6`, 3 for `k>=D+7`.
2. `L_D -> L_(D-2)`, `w=k-2D-5`:
   debt 0 for `k<=2D+5`, 1 at `2D+6`, 2 at `2D+7`, 3 for `k>=2D+8`.
3. `RW_D -> L_(D-2)`, `w=k-3D-2`:
   debt 0 for `k<=3D+2`, 1 at `3D+3`, 2 at `3D+4`, 3 for `k>=3D+5`.
4. `RW_D -> RW_(D-2)`, `w=k-2D-8`:
   debt 0 for `k<=2D+8`, 1 at `2D+9`, 2 at `2D+10`, 3 for `k>=2D+11`.
5. adjacent `L_D -> RW_D`, `w=D-k-1`:
   debt 0 for `k>=D-1`, 1 at `D-2`, 2 at `D-3`, 3 for `k<=D-4`.

The direct merger graph has rank

`r(L_D)=2D+1`, `r(RW_D)=2D`.

Adjacent merger drops 1; every `D->D-2` merger drops at least 3. Thus recurrence cannot live inside the direct-merger subsystem.

## 3. Universal gateway theorem and four sibling formulas

For `S=(d,K)` and `O=(d+1,K+3^d)`, when physical:

`S0=O1`,

and

`O0 = P o S1`, `P=(2,6)`.

Applying this to the four RL303 prefinal wall pairs gives:

1. `endpoint(RW_(D-2) 0000 1^(k-2)00)=P o endpoint(L_D 10 1^k01)`, `k>=2`, cost difference `4-k`.
2. `endpoint(L_(D-2) 00000 1^(k-2)00)=P o endpoint(L_D 010 1^k01)`, `k>=2`, cost difference `6-k`.
3. `endpoint(L_(D-2) 00000 1^(k-1)00)=P o endpoint(RW_D 1100 1^k01)`, `k>=1`, cost difference `2-k`.
4. `endpoint(RW_(D-2) 000000 1^(k-2)00)=P o endpoint(RW_D 0100 1^k01)`, `k>=2`, cost difference `7-k`.

Together with inherited final-bit-0 mergers, these complete the last-bit partition inside those four macro cylinders.

Session regression before closeout checked 9,433 legal wall sibling instances. The compact closeout verifier checks the generic gateway over a broad finite range and reports 2,211 realized `S0/O1` instances.

## 4. D0 partial splice

Assume `Bcal(R3)<=3` and `Bcal(8)<=3`. Then the exact checkpoint-2 recurrence gives `Bcal(2)<=2`.

Checkpoint 2 reaches `S_d` at exact cost `d(d-1)/2`, hence

`Bcal(S_d)<=d(d-1)/2+2`.

For odd `d`, the direct F/S merger cylinder

`F_d 00 1^j01 = S_d 1^(j+2)00`

is far below normalized target. On the complementary odd branch `d=D+2`, the F route and wall route share a physical state, and the D0 history is more expensive by

`(D^2+7D+8)/2`.

The base `d=3` has an equal-cost checkpoint-8 splice into `F_3`.

No complete F/A prefix cover was proved.

## 5. Fixed-96 P/Q hard-pivot diagnosis

RL304's six-column cut has zero relative historical cost and leaves twelve residual factors `F_m,G_m`, `m=1,...,6`.

RL306 found:

- all twelve residual types occur at every sufficiently large Q-stack height;
- after six columns unresolved left-context depth is at least `2n-4` and grows without bound;
- average depth change across the complete six-bit word set is zero, so no hidden strict depth contraction exists;
- `G_2` is the fixed-seed renewal factor;
- the residual label alone cannot bound threat because left context matters.

Concrete context family:

`S_N=(1,J=2^(N+1)+4)`.

Composing the `G_2` residual produces a legal future with

`Bcal(S_N o G_2)>=N-1`.

This is the hard-pivot obstruction. Preserve RL304 identities, but do not resume unweighted P/Q automatically.

## 6. Checkpoint-8 first-return pivot

After the forced launch from 8, normalized `q=K/3^d` starts at 2. Before first return:

- on input 1: `q'<=(3/2)q`;
- on input 0: `q'<=max(1,q)`.

For first-return cost `A`, writing `u_b=(J_b+1)/2`:

`u_b<=3(3/2)^A`.

An even first return cannot violate the minimal `+3` scalar ceiling.

If the first return is odd and its loop-erased retained boundary word has `r` ones and `z` zeros, then a dangerous complementary exit forces

`r-z > lambda*A + log_(3/2)(16/9)`,

`lambda=log_(3/2)(4/3)`.

Since first positive odd return cost is at least 2, the corridor implies the dangerous odd boundary origin is the principal representative of its retained parity cylinder.

First-failure resonance precision for the minimal `+3` target is `2^(A'+d'+5)`, two bits stronger than the historical excess-one first-failure precision.

## 7. Fixed-source shell reduction

For source `s` define

`M_s(k)=min { added area to positive even checkpoint E : 2^k | E }`.

Exactly:

`Bcal(s)=sup_k(k-M_s(k))`.

Thus `Bcal(s)<=T` iff `M_s(k)>=k-T` for all k.

For checkpoint 8: `M_8(k)>=k-3`.

Exact session closures:

- cost <=21: 1,275,880 positive physical states; no score above 3;
- cost <=22: 2,644,825 positive states; no valuation-26 checkpoint, so `M_8(26)>=23`;
- cost <=23: 5,475,369 states; maximum checkpoint valuation 21, so `M_8(27)>=24`;
- cost <=24: 11,373,143 states; maximum checkpoint valuation still 21, so `M_8(28)>=25`.

Hence minimal checkpoint-8 shells are certified through `k<=28`. The next unresolved shell is `k=29`, requiring `M_8(29)>=26`. These are diagnostics/certificates, not the successor strategy.

## 8. Checkpoint-8 affine/Ferrers form

For source 8,

`g_8(u)=3u-7`.

For balanced future length `N`, common weight `r`, and ordinary Collatz parity numerators `Q_x,Q_y`:

`2^N J_end = 7*3^r + 3Q_x-Q_y+2^N`.

If matched one positions satisfy `b_j<=a_j`, `delta_j=a_j-b_j`, then area

`A=sum_j delta_j`,

and

`2^N J_end = 7*3^r + 2^N + sum_j 3^(r-j)2^(b_j)(3*2^(delta_j)-1)`.

Exact one-residue affine-tree enumeration:

- length 24: 3,753,344 legal prefix residues, 149,601 positive balanced endpoints, max nonempty score 1;
- length 28: 55,664,932 legal prefix residues, 1,901,078 positive balanced endpoints, max nonempty score 1.

Finite evidence only. Do not promote excess-one.

Per-cell Lipschitz remains false. At `N=12,r=8`, area 15, restoring one cell changes cleared numerator

`124511 -> 131072=2^17`.

## 9. Failed shortcuts and equality mechanism

- Local scalar induction is false with fictitious ancestry credit. Example: boundary `J=18` assigned too little credit can jump to a child with `M'=32`; actual source-8 ancestry reaches it only after enough paid area.
- High retained drift does not force a large principal representative; long high-drift words with small representatives exist.
- `nu_2(J_end)>=A => J_end=8` is false. A length-194 exact path reaches `2^21` at cost 21.
- The cost-21 equality mechanism passes through checkpoint `490962` at cost 20, then a cost-one macro. Its odd boundary origin is `n=184111`, retained word `111101`, principal six-bit representative 47, and static hazard reaches 21. It is an equality model, not a violation.

## 10. Arbitrary-source affine ballot bijection

In canonical K-coordinate `K=J+2^d-1`, define

`g_S(u)=3^d(u+1)-K-1`.

Ordinary half-step Collatz trajectories of `u` and `g_S(u)`, with parity bits `x_i,y_i`, produce depth

`d_i=d_0+wt(y_<i)-wt(x_<i)`.

When all `d_i>=1`,

`J_i=3^(d_i)a_i-b_i+3^(d_i)-2^(d_i)`

is exactly the canonical paired recurrence. Conversely every finite canonical future arises this way. A length-N future is encoded by one residue mod `2^N`.

For source 8, opposite initial parity forces the unique free `01` paired column to `(2,J=15)`.

## 11. Cascade sections and seven-source atlas

Cascade composition satisfies

`g_(A o B)=g_B o g_A`.

Seven RL305 source sections:

- R3 `(3,20)`: `27u-1`;
- 8 `(1,8)`: `3u-7`;
- D0 `(3,17)`: `27u+2`;
- `(4,39)`: `81u+26`;
- `(2,-17)`: `9u+22`;
- `(2,-84)`: `9u+89`;
- `(3,-28)`: `27u+47`.

Fixed seed `(1,-13)` has

`g_seed(u)=3u+14=g_8(u+7)`.

Thus seed vs 8 is a common-right-shadow exchange between left trajectories `u` and `u+7`.

## 12. Exact shell front-door identity

For `k>=2`:

`M_P(k)=2+min(M_R3(k),M_8(k),M_D0(k))`.

RL292 shell front door:

`M_seed(k)=min(1+M_P(k),3+M_439(k),1+M_-17(k),2+M_-84(k),3+M_-28(k))`.

Hence

`M_seed(k)=3+min(M_R3(k),M_8(k),M_D0(k),M_439(k),M_-17(k)-2,M_-84(k)-1,M_-28(k))`.

If checkpoint 8 is pointwise shell owner, then

`M_seed(k)=3+M_8(k)`

and Gate A reduces to `M_8(k)>=k-3`.

Finite shell diagnostics during RL306:

- `M_R3(k)=M_8(k)+3` through all visible shells `k<=21`;
- `M_D0(k)=M_8(k)+5` for visible `k=4..21`;
- fixed seed `M_seed(k)=3+M_8(k)` throughout visible `k<=21` under the exact historical-cost-24 closure.

These are evidence only.

Known ingress witnesses:

- `R3 --111--> 8`, cost 3;
- `D0 --011--> (2,15)`, cost 5, while `8 --0--> (2,15)`, cost 0;
- scratch searches also found short paths from the three negative front-door sources to 8, but these are not promoted as global shell-owner proofs.

For `(4,39)`, immediate scalar partition:

- prefix `1` reaches `(4,66)` at cost 3; R3 reaches the same state at cost 2;
- prefix `01` reaches `(3,26)` at cost 6; 8 reaches the same state at cost 2;
- prefix `00` reaches `(5,191)` at cost 6 and remains the old residual.

## 13. Live successor frontier

Do not continue generic P/Q or generic cost caps.

Primary exact target:

`M_seed(k)>=3+M_8(k)`

for all relevant shells, or only the dangerous region needed for Gate A.

Exploit

`g_seed(u)=g_8(u+7)`

and seek an area-nonincreasing exchange between the two left ordinary Collatz trajectories against their common right shadow.

If this closes, immediately attack only the residual checkpoint-8 shell theorem `M_8(k)>=k-3`.
