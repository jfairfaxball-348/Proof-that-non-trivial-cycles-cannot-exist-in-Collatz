# RL306 report — weighted-wall hard pivot, affine ballot sections, and shell-owner Gate-A reduction

Date: 2026-09-12
Base commit: `37cacb020ccb314dcc0ebe3885d4fbd9564eadd1`

## Classification

`SCALAR_WALL_HARD_PIVOT_AND_AFFINE_SHELL_OWNER_REDUCTION_PROVED`

Gate A remains OPEN. Gate B remains OPEN/frozen. `Bcal(P)<=1` remains OPEN. `Bcal(8)<=3` remains OPEN. The historical checkpoint-8 excess-one conjecture remains OPEN and is still stronger than required.

RL306 did not close Gate A. It did, however, execute the RL305/RL306 falsifiable strategy exactly: the normalized wall system produced useful finite-debt structure, the fixed-96 P/Q continuation then met the authoritative hard-pivot criterion, and the mandated fixed-seed ancestry/static-danger pivot produced a substantially simpler exact target.

## 1. Weighted wall subsystem: finite debt and acyclic direct mergers

Assume only the minimal checkpoint-8 ceiling `Bcal(8)<=3`. RL303's exact checkpoint-8 wall entries imply

`X_L(D), X_R(D) <= 6`.

With normalized wall debt

`y=max(0,X-3)`, 

one has `0<=y<=3`. For any exact same-endpoint normalized branch of weight `w`, owner debt `y_o` implies

`y_source <= clamp(y_o+w,0,3)`.

Thus the unresolved wall excess is quantized to four levels `0,1,2,3`; arbitrarily large raw positive branch weights cannot create more than three unresolved normalized Bellman-debt units once the checkpoint-8 cap is assumed.

The promoted RL305 weights give exact layer thresholds recorded in `RL306_SCRATCH_FREEZE.md`.

The five direct wall-merger families are also well-founded under

`r(L_D)=2D+1`, `r(RW_D)=2D`.

The adjacent `L_D -> RW_D` edge drops rank one, and each `D -> D-2` merger drops rank at least three. Hence the direct-merger subsystem contains no directed cycle at all. Any recurrence obstruction must therefore live in complementary P-siblings/renewal, not in the direct mergers themselves.

## 2. Universal gateway and complete last-bit split inside four macro cylinders

For source `S=(d,K)` and owner `O=(d+1,K+3^d)`, whenever the physical steps exist,

`S --0--> Y = O --1--> Y`,

while the complementary choices satisfy

`endpoint(O --0) = P o endpoint(S --1)`.

This is an exact parity-split identity. Applied to RL303's four prefinal `D -> D-2` macro pairs, it proves the exact complementary leading-P siblings. Therefore each of those four prefinal macro cylinders has a complete final-bit partition: final `0` is the lower-wall merger and final `1` is the exact leading-P sibling.

This is local coverage of those four cylinders, not a complete wall-prefix transducer.

## 3. D0 partial scalar contraction

Under `Bcal(R3)<=3` and `Bcal(8)<=3`, the exact checkpoint-2 recurrence gives `Bcal(2)<=2`. The inherited F/S mergers then make the displayed odd F/S direct-merger cylinders safely below the normalized `X_F<=3` target, while the complementary odd branch shares a physical state with the wall family with a large quadratic historical margin. The `d=3` base is owned from checkpoint 8 at equal cost.

This is not a complete D0 proof because no complete F/A prefix partition was established.

## 4. Fixed-96 P/Q continuation meets the hard-pivot criterion

RL304's six-column P/Q cut has zero relative historical cost and leaves one of twelve fixed residual factors `F_m,G_m`, `m=1,...,6`.

RL306 proves the obstruction is structural rather than merely inconvenient:

- every one of the twelve residual types occurs at every sufficiently deep stack height;
- after six columns the unresolved left context still has depth at least `2n-4`, hence is unbounded;
- the six-column cut supplies no strict historical contraction;
- one residual, `G_2`, is the fixed-seed renewal factor itself;
- the threat of `G_2` cannot be summarized by a finite scalar residual label because varying the left context gives arbitrarily large Bellman threat.

A concrete family is

`S_N=(1,J=2^(N+1)+4)`.

Composing the `G_2` residual with `S_N` gives a legal future with

`Bcal(S_N o G_2) >= N-1`.

Therefore the arbitrary left context is load-bearing. Any complete continuation must retain an unbounded state parameter with no decreasing credit. This is exactly the RL306 hard-pivot condition.

Disposition: the RL304 fixed-96/twelve-factor P/Q route is frozen intact and remains reusable, but it loses automatic priority. No further unweighted P/Q commutation is recommended.

## 5. Checkpoint-8 first-return contraction

After checkpoint 8's forced departure, write `q=K/3^d`. At the start `q=2`. Before the first return to `d=1`, a `1` edge gives `q'<=(3/2)q` and a `0` edge gives `q'<=max(1,q)`; every pre-return edge pays positive area. If the first-return cost is `A` and `u_b=(J_b+1)/2`, then

`u_b <= 3(3/2)^A`.

If that first return is even, a violation of the literal scalar ceiling would require `J_b>=2^(A+4)`, incompatible with the corridor. Hence an even first return from 8 cannot violate `Bcal(8)<=3`.

If the first return is odd, and the loop-erased retained boundary word contains `r` retained ones and `z` retained zeros, a dangerous complementary exit forces

`r-z > log_(3/2)(4/3) A + log_(3/2)(16/9)`.

Together with the corridor and the exact fact that the first positive odd return costs at least two, this forces the odd boundary origin onto the principal representative of its retained parity cylinder. This statement is for the first checkpoint-return macro; it does not by itself prove the full recursive ceiling.

The first-failure transformed-shadow resonance also gains two bits of precision relative to the historical excess-one setup: the minimal `+3` failure forces the same centre modulo `2^(A'+d'+5)`.

## 6. Fixed-source divisibility shells

For any physical source `s`, define

`M_s(k)=min { added area to a positive even checkpoint E : 2^k divides E }`.

Then exactly

`Bcal(s)=sup_(k>=1) [k-M_s(k)]`.

Therefore

`Bcal(s)<=T  <=>  M_s(k)>=k-T for every k`.

This is merger-invariant by construction and removes recursive intermediate-checkpoint reset bookkeeping from the statement.

For checkpoint 8 the literal target is simply

`M_8(k)>=k-3` for all `k`.

Exact session closures certify this target through `k<=28`. The next unresolved shell is `k=29`, which would require `M_8(29)>=26`. These bounded closures are supporting certificates only; RL307 must not turn the programme into generic cap extension.

## 7. Arbitrary-source affine-ballot bijection

Use RL302's canonical cascade coordinate `K=J+2^d-1`. For a source `S=(d,K)` define

`g_S(u)=3^d(u+1)-K-1`.

Equivalently,

`g_(d,J)(u)=3^d u-(J-3^d+2^d)`.

Let `a_i` and `b_i` be the ordinary half-step Collatz trajectories of `u` and `g_S(u)`, with parity bits `x_i,y_i`, and define

`d_i=d + wt(y_<i)-wt(x_<i)`.

Whenever all `d_i>=1`,

`J_i=3^(d_i)a_i-b_i+3^(d_i)-2^(d_i)`

reproduces exactly the four canonical paired-column transitions. Conversely every finite canonical future from `S` arises this way. A length-N future is therefore encoded by one residue `u mod 2^N`; the second parity word is determined by the affine section.

Added area is

`H_N=sum_(i=0)^(N-1)(d_i-1)`.

Thus every fixed-source shell is exactly a minimum-area problem on one affine ballot tree.

## 8. Cascade anti-homomorphism and seven-source affine atlas

For cascade composition

`A o B=(a+b,3^b K_A+K_B)`, 

one has the exact identity

`g_(A o B)=g_B o g_A`.

The seven RL305 Gate-A sources therefore have the affine sections

- `R3=(3,J=20)`: `27u-1`;
- `8=(1,J=8)`: `3u-7`;
- `D0=(3,J=17)`: `27u+2`;
- `(4,39)`: `81u+26`;
- `(2,-17)`: `9u+22`;
- `(2,-84)`: `9u+89`;
- `(3,-28)`: `27u+47`.

The source thresholds remain `(3,3,3,3,1,2,3)`.

Checkpoint 8 is especially rigid: `g_8(u)=3u-7` has parity opposite to `u`, so any nonempty legal future from depth one is forced through the free `01` paired column, landing at `(d,J)=(2,15)`. Hence the nonempty checkpoint-8 shell problem equals the `(2,15)` shell problem.

## 9. Checkpoint-8 balanced Ferrers numerator

For a balanced source-8 future of length `N` and common one-weight `r`, with ordinary Collatz parity numerators `Q_x,Q_y`, the suffix lift cancels and

`2^N J_end = 7*3^r + 3Q_x - Q_y + 2^N`.

If matched one positions satisfy `b_j<=a_j` and `delta_j=a_j-b_j`, then the added Ferrers area is `A=sum delta_j` and

`2^N J_end = 7*3^r + 2^N + sum_j 3^(r-j)2^(b_j)(3*2^(delta_j)-1)`.

Thus `Bcal(8)<=3` is a concrete valuation problem on the source-8 affine ballot tree.

Large exact finite source-8 affine-tree tests through length 28 found maximum nonempty score `nu_2(J)-A=1`; this supports the stronger historical excess-one conjecture but does not prove it.

## 10. Per-cell and local-potential barriers survive

The checkpoint-8 source term does not restore per-Ferrers-cell valuation Lipschitz behavior. An explicit formal source-8 pair of area 15 changes its cleared numerator from `124511` to `131072=2^17` when a single displacement cell is restored.

Likewise a local scalar inequality can fail on a legal state carrying fictitiously low credit; the same state is safe on the actual source-8 cone because its minimum ancestry area is much larger. This confirms that ancestry credit is essential and that the shell/min-plus formulation is not optional bookkeeping.

## 11. Exact shell front-door synthesis

For `k>=2`, RL302's exact P-source recurrence descends shellwise to

`M_P(k)=2+min(M_R3(k),M_8(k),M_D0(k))`.

RL292's exact five-state front door similarly gives

`M_seed(k)=min(1+M_P(k), 3+M_(4,39)(k), 1+M_(2,-17)(k), 2+M_(2,-84)(k), 3+M_(3,-28)(k))`.

Substitution yields

`M_seed(k)=3+min(`
` M_R3(k), M_8(k), M_D0(k), M_(4,39)(k),`
` M_(2,-17)(k)-2, M_(2,-84)(k)-1, M_(3,-28)(k))`.

Hence a single checkpoint-8 shell-owner theorem

`M_8(k) <=` each of the other six shifted shell functions

would imply

`M_seed(k)=3+M_8(k)`.

Since the genuine fixed-seed-to-8 history costs exactly three, the reverse inequality `M_seed(k)<=3+M_8(k)` is automatic. Therefore Gate A would reduce exactly to the checkpoint-8 shell ceiling `M_8(k)>=k-3`.

This shell-owner theorem is strictly weaker than same-endpoint ownership, O1, O2, or universal P/8.

## 12. Common-right-shadow formulation

The fixed seed has

`g_seed(u)=3u+14`,

while checkpoint 8 has

`g_8(u)=3u-7`.

Therefore

`g_seed(u)=g_8(u+7)`.

A seed shell witness and a candidate checkpoint-8 owner can thus share the same right ordinary Collatz trajectory; only the left trajectory changes from `u` to `u+7`.

This is the cleanest successor target: prove or falsify an area-nonincreasing dangerous-region exchange between these two left trajectories against a common right shadow.

Exact finite data through the certified region found

`M_seed(k)=3+M_8(k)`

for every visible shell `k<=21`. This is finite evidence only.

## 13. Scope

Proved analytic/reduction results are listed in `RL306_PROOF_AND_SCOPE.md`.

Not proved:

- checkpoint-8 shell-owner theorem;
- `M_8(k)>=k-3` all depth;
- `Bcal(8)<=3`;
- `Bcal(P)<=1`;
- O1/O2/P8;
- Gate A;
- Gate B;
- global non-trivial-cycle exclusion.

The fixed-96 P/Q route is frozen at its hard-pivot obstruction. Physical/resonance remains frozen at selector `a=7354673373747273032`. Radius 6+ remains frozen. Lean formalisation is separate.
