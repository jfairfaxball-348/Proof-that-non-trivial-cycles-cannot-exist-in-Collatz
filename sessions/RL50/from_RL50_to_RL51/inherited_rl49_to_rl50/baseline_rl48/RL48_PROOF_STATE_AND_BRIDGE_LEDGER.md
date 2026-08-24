# RL48 Proof State and Bridge Ledger

Date: 2026-08-22

## Status legend

- **Analytic:** exact symbolic consequence of the live RL45/RL47 conventions and one-excursion identities.
- **Exact finite certificate:** exhaustive finite computation with stated pruning/relaxations.
- **Verified computation:** exact algebra/trajectory regression used to audit formulas, not by itself a uniform theorem.
- **Audit-pending:** derivation is proved in the current framework but cannot yet be connected to an inherited theorem until its exact statement is recovered.
- **Open:** not proved.

## 1. Gate A — terminal area inequality

Target:

`H >= t+3 = v2(T+1)`.

RL47 established `H=sum_j(a_j-b_j)` and an exact normalized rank-transport identity. RL48 proved a limitation theorem for the RL47 separable relaxation:

> Under the retained near-resonance hypotheses, the RL47 cap/room + total-displacement relaxation cannot exclude a strict violation whenever `z=q-t>=42`.

This is an **analytic theorem about the proof method**, not a counterexample to the desired inequality.

### Consequence

A uniform Gate-A proof cannot come from merely sharpening constants in the same separable rank envelope. It needs a coupling invariant controlling synchronized height-one motion. The deterministic height-one `00/11` quotient remains the natural source of such an invariant.

### Status

**OPEN.** Known exact finite and analytic partial exclusions from RL47 remain valid.

## 2. Canonical same-root selector

Put

`f(T)=3T^q-2`, `L(T)=2T^ell-1`, `M=2^a-3^ell`.

Because `q=a-ell` and the retained primitive setup has `gcd(q,ell)=1`, Bezout gives integers `r,s` with `rq+s ell=1`. The unit

`rho=(2/3)^r (1/2)^s (mod M)`

is the unique common root of `f` and `L` modulo `M`.

At this root the RL45 phase polynomial satisfies

`P(rho)=4+Q(v)/3^ell (mod M)`.

Therefore

`P(rho)=0 (mod M) <=> M | Q(v)+4*3^ell`.

### Status

**ANALYTIC.** This removes the different-root contamination concern for the live full-modulus formulation.

## 3. General full-word reconstruction

Composing RL45's full half-word convention with the RL47 local start/terminal convention gives

`u=110 x 1 0^t`,

`v=111 y 0^(t+1)`.

Both have length `a` and weight `ell`.

For internal rank polynomials `Qx,Qy`, direct bookkeeping gives

`Q(u)=15*3^(ell-3)+24Qx+2^(a-t-1)`,

`Q(v)=19*3^(ell-3)+8Qy`.

### Status

**ANALYTIC from the conventions present in the RL47->RL48 provenance bundle.**

## 4. Proper-factor identity reconstructed internally

RL47's terminal identity yields

`3Qx-Qy = 14*3^(ell-3)+2^(a-1)-2^(a-t-4)`.

Substitution into the full-word formulas gives

`boxed: Q(u)-Q(v)=4(2^a+3^ell)`.

Thus the old proper-factor identity no longer needs to be imported as a black box for this branch.

### Status

**ANALYTIC.**

## 5. Full denominator factorization

For equal-length/equal-weight concatenation,

`Q(uv)=3^ell Q(u)+2^a Q(v)`.

Using the proper-factor identity,

`boxed: Q(uv)=(2^a+3^ell)(Q(v)+4*3^ell)`.

The cycle denominator for `uv` is

`2^(2a)-3^(2ell)=(2^a+3^ell)(2^a-3^ell)`.

Therefore full cycle divisibility is equivalent exactly to

`2^a-3^ell | Q(v)+4*3^ell`,

which is the selected-root phase condition.

### Status

**ANALYTIC.**

## 6. Four-swap trajectory theorem

Assume the full phase condition and define

`N=(Q(v)+4*3^ell)/(2^a-3^ell)`.

Then `N>0` and the standard Collatz affine maps attached to the parity words satisfy

`boxed: F_u(N)=N+4`,

`boxed: F_v(N+4)=N`.

The congruence selecting a parity word modulo `2^a` ensures these are genuine integer half-trajectories, not merely rational affine identities.

Thus the full phase condition produces a positive nontrivial cycle word `uv` whose midpoint values differ by exactly `4`.

### Status

**ANALYTIC.**

## 7. Exact radius-3 entrance

The prefixes are `u=110...` and `v=111...`, hence

`N=3 (mod 8)`, `N+4=7 (mod 8)`.

After the first two common odd steps, the two actual trajectory values differ by exactly `9`; the next parity column is `(0,1)`. In the RL local coordinate this is exactly

`T=-14`.

More generally, for the two actual internal trajectories `A_i,B_i`,

`boxed: T_i=3^(d_i)A_i-B_i`.

At the terminal `T=2^(t+3)-1`; the omitted terminal `(1,0)` column creates separation `2^(t+2)`, and the following `t` synchronized zero steps divide it back to the physical separation `4`.

### Status

**ANALYTIC.**

## 8. Radius-3 bridge claim — exact current status

RL48 proves the input configuration that one would naturally expect the radius-3 theorem to exclude:

`N --110 x 1 0^t--> N+4`,

`N+4 --111 y 0^(t+1)--> N`,

with the canonical post-`11` gap-9, `(0,1)`, `T=-14` entrance.

However, the exact RL18/RL19 theorem text is absent from the current provenance archive.

### Therefore

- If the audited radius-3 theorem excludes exactly this canonical positive depth-three four-swap/gap-9 configuration, **Gate B closes immediately**.
- If it requires additional support, orientation, gcd, boundary, multiplicity, or sparse-uniqueness hypotheses, the only remaining Gate-B task is to prove those hypotheses for the displayed `u,v` configuration.

### Status

**AUDIT-PENDING. Do not promote to unconditional Gate-B closure until the exact theorem is matched line-by-line.**

## 9. Rank-defect bridge remains a fallback, not the first route

RL48 also derived, under a hypothetical low-area violation, a sparse rank-displacement defect

`D=sum_{delta_j>0} 3^(r-j)2^b_j(2^delta_j-1)`

with at most `t+2` active ranks and phase congruence

`12D+2^(a-t-2) = 237*3^(ell-3) (mod 2^a-3^ell)`.

This remains useful if the radius-3 theorem turns out to be narrower than the direct four-swap configuration. It should not be made the primary target before the theorem audit.

## 10. Closure discipline

Do not claim global RL closure unless all of the following are explicitly checked:

1. the exact RL18/RL19 radius-3 theorem has been recovered from source;
2. every theorem hypothesis matches the four-swap configuration or is separately proved;
3. the theorem really excludes the live full-phase branch rather than only a proper-factor countermodel;
4. the remaining logical role of Gate A is determined explicitly;
5. no finite q-specific certificate is promoted to a uniform theorem;
6. inherited dependencies are listed and verified.
