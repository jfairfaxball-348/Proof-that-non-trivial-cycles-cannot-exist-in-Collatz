# RL274 — Radius-5 bridge strategy, determinant–discrepancy invariant, and exact barrier

Date: 2026-09-07

## Classification

Primary:
`RADIUS5_INSUFFICIENT_FOR_IDENTIFIED_BRIDGE`

Companion findings:
- `GENERAL_LOCAL_PATTERN_IDENTIFIED`
- `BRIDGE_EXACT_BARRIER`
- `RADIUS5_BRIDGE_REDUCED_TO_EXACT_TARGET`

This is a strategy/analytic-reduction generation. It does **not** prove global non-trivial-cycle exclusion.

## 1. Fixed local theorem

Retain the completed Radius-5 theorem exactly as inherited:

> Under the audited positive-domain, primitive, full-`D` self-rotation hypotheses inherited from RL238/RL265, with `D=2^A-3^L>1` and full-`D` numerator divisibility, no nontrivial cyclic self-rotation has exact cyclic earth-mover distance `5`.

RL270 closes `|kappa|=1`, RL271–RL272 close `|kappa|=3`, and RL273 closes `|kappa|=5` across all nine Radius-5 topology families.

Nothing in RL274 reopens or strengthens that local theorem.

## 2. Weakest direct Radius-5 encounter statement

For a hypothetical admissible primitive full-`D` cycle parity word `W`, the logically minimal direct bridge to the fixed local theorem would be

`exists m, 1 <= m < A, dist_cyc(W, tau^m W) = 5`.

Equivalently, `5` lies in the cyclic self-rotation spectrum of `W`.

This statement is sufficient, but on the retained full-phase representation it is false.

## 3. Parity obstruction for the genuine full-phase word

The inherited full-phase construction has genuine cycle word

`W = u v`

with two half-words of common length `a` and common weight `ell`. Hence the genuine full word has

`A = 2a`,
`L = 2ell`.

For any cyclic self-rotation, let `g` be an optimal integer transport flow and let

`kappa = sum_i g_i = qA - mL`.

Since both `A` and `L` are even, `kappa` is even.

For every integer flow,

`sum_i |g_i| == sum_i g_i (mod 2)`.

Therefore every cyclic self-rotation distance of `W` is even:

`dist_cyc(W, tau^m W) == 0 (mod 2)`.

Thus

`5 notin Sigma(W)`

identically in this retained genuine full-phase representation.

This is the exact reason Radius 5 cannot directly bridge the present full-phase object.

The half-words `u,v` do not repair this: they are two physical half-words, not automatically a primitive full-`D` word and one of its self-rotations.

## 4. General determinant–counterflow normal form

For an optimal cyclic self-rotation flow `g`, orient so `kappa >= 0` and define

`beta(g) = sum_i max(-g_i,0)`.

Then

`sum_i max(g_i,0) = beta + kappa`

and

`R := dist_cyc = sum_i |g_i| = kappa + 2 beta`.

Also

`kappa = qA - mL`

for an integer normalization parameter `q`, hence

`gcd(A,L) | kappa`

and

`R == kappa (mod 2)`.

At Radius 5 this yields exactly the three counterflow sectors

`(|kappa|, beta) = (5,0), (3,1), (1,2)`.

For the inherited determinant-2 selected Gate-B rotation sector,

`R = 2 + 2 beta`

whenever that selected normalization is the cyclic median normalization.

This explains the even-radius ladder as a counterflow-level ladder rather than a sequence of unrelated topology shells.

## 5. Exact determinant–discrepancy identity

Let `x` be a cyclic binary word of length `A` and weight `L`. Fix a rotation length `m`, and for an integer `q` write

`g_i = q - W_i(m)`,

where `W_i(m)` is the number of ones in the cyclic length-`m` window starting at `i`.

Put

`kappa = Aq - mL`,
`z = A-L`,
`B = m-q`.

Then

`mz - AB = kappa`.

Choose integers `c,d` and define

`H = dz - cA`,
`n = dB - cm`.

One has the exact determinant relations

`Hm = nA + d kappa`,
`HB = nz + c kappa`.

Assume `0 < H < A/gcd(A,m)` so that the sampled starts

`s, s+m, ..., s+(H-1)m`

are distinct.

Let `Z_r(s)` be the number of zeros in the cyclic length-`r` window starting at `s`. Summing the `H` length-`m` windows gives the exact identity

`Z_(d kappa)(s) = c kappa + sum_(j=0)^(H-1) g_(s+jm)`.

If `kappa >= 0`, set `beta=sum max(-g_i,0)`. Since the sampled values are distinct,

`c kappa - beta <= Z_(d kappa)(s) <= c kappa + beta + kappa`.

Therefore

`|2 Z_(d kappa)(s) - kappa(2c+1)| <= kappa + 2 beta`.

When `g` is an optimal normalization, the right side is exactly the cyclic earth-mover radius `R`.

So transport radius is an exact discrepancy budget for rationally resonant zero-count windows.

### Historical recovery

RL253 is the special determinant-2 choice

`(c,d)=(7,19)`,

which gives

`Z_38(s) = 14 + sum P`

and eliminates the Branch-C `beta(P)=6` regime.

RL254 generalizes the same `38`-window mechanism and, in the halving branch, its exact `19`-window factorization, forcing very large auxiliary counterflow.

Thus the Radius-3/4/5 transport machinery and the RL253/RL254 window machinery share a common determinant–counterflow / discrepancy structure.

## 6. Direction of the global machinery

The important strategic point is directional.

The promoted full-phase / terminal-zero / window machinery tends to prove

`counterflow is large`.

It does not force the same genuine self-rotation into a small exact radius.

RL253 kills `beta(P)=6`.

RL254 then forces, on surviving Branch C,

`beta(P) >= 260`

uniformly, and at least `355` in its non-halving branch.

RL255 raises/constrains the surviving scales further but still does not create an eligible small-radius self-rotation.

Therefore proving Radius 6, Radius 8, and so on attacks bounded counterflow levels, while the global machinery is already pushing the relevant discrepancy budget away from those levels.

## 7. Fixed-local-pattern no-escalation barrier

Let

`alpha = z/A`.

In the determinant–discrepancy construction,

`r = d kappa`

is the residual-window length and

`c kappa = alpha r - kappa H/A`.

If `0 < H < A`, then

`c kappa > alpha r - kappa`.

Suppose a proposed discrepancy contradiction uses only a fixed owned local pattern that can guarantee at most `C` zeros in the residual window, where `C` is independent of the global scale.

To force that fixed guarantee above the determinant baseline one needs

`C > c kappa`.

Hence necessarily

`alpha r < C + kappa`,

so

`r < (C+kappa)/alpha`.

Thus any argument whose only owned zero-rich input is a fixed finite local pattern can exploit only bounded residual denominators. It cannot by itself create an unbounded multi-approximant contradiction as `A` grows.

For the inherited determinant-2 Branch-C setting, `alpha > 7/19`. The fixed terminal `0^28` together with the adjacent fixed prefix supplies an absolute zero guarantee of the same kind used in RL253. Taking the conservative fixed bound `C=29` gives

`r < 31/(7/19) = 589/7 < 85`.

So this fixed-pattern mechanism can only reach bounded residual lengths. The exact constants are not the strategic point; the boundedness is.

This does **not** rule out a scale-growing discrepancy theorem based on repeatedly owned structures. It rules out obtaining one merely by iterating a fixed finite terminal pattern.

## 8. What RL256–RL264 show about escalation

RL256–RL262 already pursued the selector/discrepancy escalation very strongly:
- the first selector was contracted and eliminated using exact terminal/canonical ownership;
- the second selector was eliminated;
- the third selector was eliminated by an exact full-phase certificate;
- the fourth selector was eliminated over its complete feasible odd terminal range.

Those are real finite eliminations.

However RL262 did not produce a uniform eventual density theorem.

RL263 then proved that the proposed selector-independent ordered-prefix congruence is automatic on genuine physical full-phase pairs: it is an exact physical-gap telescope rather than an independent global restriction.

RL264 proved every finite legal canonical prefix has infinitely many positive physical lifts along an affine ray, while the canonical state is invariant along that ray. It also proved terminal physical ownership collapses to the already-promoted full-phase quotient and that the natural physical self-rotation is far from Radius 4.

Hence:
- finite local physical magnitude cannot be the missing scale-growing obstruction;
- the tested selector-independent ordered-prefix condition is tautological on genuine physical lifts;
- the successful selector eliminations consumed genuinely owned canonical height/phase information.

## 9. Exact missing implication

The global bridge is now best stated as a scale-growing ownership problem.

A sufficient direct form would be an owned theorem forcing a contradiction such as

`beta(P) > z-k+4`

against the promoted zero-budget ceiling

`beta(P) <= z-k+4`.

Equivalent useful forms include:

1. **scale-growing owned discrepancy:** full-`D` / full-phase ownership forces counterflow/discrepancy to grow faster than the available zero budget;
2. **owned replication:** a fixed zero-rich canonical feature is forced to reproduce at a number of independent owned locations growing with the global scale;
3. **owned compression:** sufficiently large determinant-2 discrepancy forces another primitive full-`D` self-rotation with a bounded/small transport radius;
4. an equivalent direct full-phase contradiction.

No such theorem is currently promoted.

## 10. Radius 6 comparison

Investment A — prove Radius 6:
- extends local machinery by one bounded transport shell;
- does not address the parity obstruction for Radius 5;
- does not supply an encounter theorem;
- does not solve the scale-growth problem;
- is therefore low leverage unless a new independent theorem first forces an eligible exact Radius-6 rotation.

Investment B — bridge / scale-growing ownership:
- attacks the missing implication directly;
- explains the historical successful selector eliminations;
- is the higher-leverage research direction.

Therefore Radius 6 remains frozen.

## 11. Recommended successor and frozen-fallback discipline

RL264 froze:
- Gate A, including the uniform odd-`k` low-area problem;
- the fifth retained arithmetic selector.

That freeze remains binding until a future user instruction explicitly starts the prepared successor.

RL274 now supplies a mathematical reason to recommend that fallback rather than continuing the Radius ladder:

the only existing mechanism that has successfully converted discrepancy/scale pressure into actual eliminations is the owned canonical height/phase machinery used in the Gate-A/selector certificates.

The recommended successor is therefore a **scale-growing ownership / Gate-A fallback activation**, with the uniform target:

> eliminate the full-phase low-area regime `H_can < k` uniformly, or derive an equivalent scale-growing owned contradiction.

The fifth selector may be used only as a controlled finite test bed, not as an automatic endless selector scan.

Preparing that successor does not itself unfreeze Gate A. A future user kickoff explicitly starting RL275 is required.

## 12. Dependency diagram

The originally hoped-for direct route is blocked:

`hypothetical non-trivial cycle`
`        |`
`        v`
`genuine full-phase word W, A=2a, L=2ell`
`        |`
`        v`
`all self-rotation distances even`
`        |`
`        X`
`exact Radius-5 encounter`

The recommended research route is instead:

`hypothetical retained full-phase object`
`        |`
`        v`
`determinant / discrepancy escalation`
`        |`
`        v`
`scale-growing owned canonical theorem`
`        |`
`        +----> contradiction to full phase / zero budget`
`        |`
`        or`
`        v`
`owned compressed self-rotation`
`        |`
`        v`
`applicable local Radius theorem`
`        |`
`        v`
`contradiction`

The middle scale-growing ownership implication is the exact open barrier.

## 13. Scope

- Radius 5: locally closed.
- Direct Radius-5 full-phase bridge: impossible in the retained doubled word representation by parity.
- Radius 6+: frozen.
- Gate A: open and frozen pending future explicit activation.
- Gate B: open.
- Fifth selector: frozen pending future explicit activation.
- Global non-trivial-cycle exclusion: open.
- Collatz conjecture: open.

No global proof is claimed.
