# RL312 checkpoint — owned balanced Radius-2 exclusion and optimal-flow normalization repair

Date: 2026-09-13
Status: LIVE RL312 CHECKPOINT
Classification: EXACT ANALYTIC CONSUMER + SCOPE REPAIR

`PARENT_DIFFICULTY_DELTA = LATERAL`

This checkpoint does **not** close the RL311 balanced-return branch or the complementary `g<=h+1` branch. It does add one genuinely ownership-sensitive local consumer and repairs an overstrong scratch interpretation of the balanced transport determinant.

## 1. Incoming RL311 balanced return

Retain the authoritative RL311 notation

`A=ga`, `L=g ell`, `g=gcd(A,L)`, `gcd(a,ell)=1`,

`X=2^a`, `Y=3^ell`, `D=X^g-Y^g>1`.

For the proper equal-level pair `j<k`, put `m=k-j` and `s=ma`. The physical segment has exactly

`p=m ell`

odd entries, hence

`sL/A = p`.

Thus the selected self-rotation is a **balanced** shift.

## 2. Canonical balanced flow and the normalization repair

For a cyclic binary word `w` of length `A`, weight `L`, and a balanced shift `s`, define the cyclic `s`-window count

`W_i(s)=sum_(r=0)^(s-1) w_(i+r)`

and the canonical balanced transport flow

`f_i=p-W_i(s)`, where `p=sL/A`.

Then

`sum_i f_i=0`

and

`f_(i+1)-f_i = w_i-w_(i+s)`.

Every cyclic edge flow transporting `w` to its shift differs from `f` by an integer constant `c`, so the exact cyclic earth-mover radius is

`R_s=min_(c in Z) sum_i |f_i+c|`.

Therefore the earlier scratch phrase "the determinant is identically zero" was too strong if interpreted as a statement about the *optimal* flow at arbitrary radius. The canonical balanced normalization has zero sum, while an optimal normalization can have determinant

`A c`.

However, if `R_s<A`, then

`A |c| = |sum_i(f_i+c)| <= R_s < A`,

so `c=0`. Hence every low-radius balanced encounter (`R_s<A`) is necessarily in the zero-sum normalization.

This repair is binding for RL312.

## 3. Exact Radius-2 theorem

### Theorem

Let `w` be a primitive positive full-`D` Collatz cycle word with

`D=2^A-3^L>1`.

No proper balanced self-rotation of `w` has exact cyclic earth-mover radius `2`.

### Proof

Assume a proper balanced shift `s` has exact radius `2`.

Since `D>1` forces `A>=3`, the previous normalization argument gives `c=0`. Thus the canonical flow itself has

`sum_i |f_i|=2`, `sum_i f_i=0`.

Therefore there is exactly one index `u` with `f_u=1`, exactly one index `v` with `f_v=-1`, and all other values are zero.

Define the centered prefix discrepancy on the periodic lift by

`T_i=C_i-iL/A`,

where `C_i` is the number of ones before position `i`. Then

`T_(i+s)-T_i = W_i(s)-p = -f_i`,

so

`f_i=T_i-T_(i+s)`.

The map `i -> i+s (mod A)` is a permutation. The sum of `f` on each of its orbits telescopes to zero. Since the only nonzero values are `+1` and `-1`, the two defect positions `u,v` lie on the same shift orbit.

Orient that orbit from `u` to `v`. At `u`,

`T_(u+s)=T_u-1`.

Every intermediate shift-orbit position has flow zero, so `T` remains constant until `v`. Hence

`T_v=T_u-1`.

Let

`r=(v-u) mod A`, `1<=r<A`,

and let `n` be the number of ones in the cyclic interval from `u` to `v`. Then

`T_v-T_u = n-rL/A = -1`,

hence

`rL=A(n+1)`.                                           (R312.1)

Using `A=ga`, `L=g ell` and `gcd(a,ell)=1`, (R312.1) gives

`r=t a`, `n+1=t ell`

for an integer `t` with

`1<=t<g`.                                               (R312.2)

Now root the genuine cycle at the physical state `x=x_u`, and let `y=x_(u+s)` be the state at the balanced shift. Let

`q_i=2^i 3^(-C_i)`

be the usual prefix weights from this root.

Because `f_u=1`, the rotated prefix-count difference is

`C'_i-C_i = W_i(s)-W_u(s) = 1-f_i`.

Hence the rotated weights are

`q'_i=q_i 3^(f_i-1)`.

Apply the exact RL19 positive population identity to the two genuine rotations:

`sum_i q_i=(lambda-1)(4x+1)`,

`sum_i q'_i=(lambda-1)(4y+1)`.

Multiplying the second equality by `3` and subtracting the first gives

`sum_i q_i(3^(f_i)-1)
 = (lambda-1)(12y-4x+2)`.

Only the two defect positions contribute. After rotating indices so `u=0`, one has `q_u=1` and

`q_v=2^r/3^n`.

Therefore

`2-(2/3) 2^r/3^n
 = 2(lambda-1)(6y-2x+1)`.

Since `lambda-1=D/3^L`, multiplication by `3^L/2` yields

`3^L-2^r 3^(L-n-1)
 = D(6y-2x+1)`.

Using (R312.2),

`L-n-1=(g-t)ell>=1`,

so, because `gcd(D,3)=1`,

`D | 3^(n+1)-2^r
   = 3^(t ell)-2^(t a)
   = Y^t-X^t`.                                         (R312.3)

But `D=X^g-Y^g>0`, so `X>Y`, and `1<=t<g` gives

`0 < X^t-Y^t < X^g-Y^g=D`.

Thus the nonzero integer in (R312.3) cannot be divisible by `D`, contradiction.

QED.

## 4. Why this is not the RL20 coboundary again

RL20 proves that the **whole** canonical block polynomial and its raw proper-factor cancellation are an exact state coboundary, so those global cancellations are not independent restrictions.

The theorem above does something different:

1. a low-radius physical encounter first forces an independently sparse balanced flow;
2. full-`D` ownership of the two genuine rotations converts that sparse flow into the proper two-term divisor `X^t-Y^t`;
3. its exponent is strictly smaller than the global exponent `g`.

This is exactly the kind of independently controlled sparse subfactor/resultant that RL20 left viable. No proper-prefix denominator ownership is assumed.

## 5. Immediate low-shell consequence

For any balanced proper self-rotation with radius `<A`, the optimal flow has zero sum. Hence its radius is even.

Therefore, in a primitive positive full-`D` cycle:

- radius `0` is impossible for a proper rotation by primitivity;
- radius `2` is impossible by the theorem above;
- radius `4` is impossible by the already-audited RL238 Radius-4 local theorem when its hypotheses apply.

Thus an RL311 balanced return cannot be consumed by a hidden Radius-2 exception. In the ordinary large-`A` regime, any such return lying in the already-closed local range through `5` would have to be Radius 4 and is therefore excluded.

This does **not** prove that the RL311 return has bounded radius, and it does not activate Radius 6+.

## 6. Exact block-cut splice

For the RL311 shift `s=ma`, the canonical flow satisfies at every canonical block cut

`f_(ra)=E_r-E_(r+m)`

(indices cyclically interpreted).

So a future consumer that proves small total balanced flow automatically proves near-periodicity of the entire RL311 height profile. Conversely, the present theorem shows that the first nontrivial owned balanced shell is already beyond Radius 2.

## 7. RL274 degeneracy barrier

RL274's determinant/discrepancy residual-window identity is driven by the flow determinant `kappa`.

For the canonical balanced normalization here,

`kappa=sum_i f_i=0`.

Therefore the RL274 residual length `d kappa` collapses to zero. That identity cannot by itself consume the RL311 balanced pair. Any successful continuation must add control of flow support/counterflow or another ownership-sensitive invariant; another determinant-discrepancy lower bound is not enough.

## 8. Scope and checkpoint assessment

Promoted in this checkpoint:

- exact normalization repair for balanced cyclic transport;
- exact full-`D` exclusion of balanced Radius 2;
- exact identification of the zero-determinant degeneration of the RL274 consumer.

Not proved:

- an upper bound on the RL311 balanced-return radius;
- contradiction for all balanced returns;
- closure of `g<=h+1`;
- Gate A, Gate B, or global non-trivial-cycle exclusion.

This is classified `LATERAL`, not `EASIER`, because although the Radius-2 loophole is closed by a genuinely independent consumer, neither side of the RL311 global dichotomy is yet eliminated.
