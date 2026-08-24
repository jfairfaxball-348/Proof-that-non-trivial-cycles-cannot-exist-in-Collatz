# RL23 — exact local saturation witness for the new packing constant

Date: 2026-08-21

## Status

**ANALYTIC PARAMETRIC LOCAL WITNESS.** This is not a full Collatz cycle and not an RL counterexample. It is an exact infinite family of integer trajectory segments satisfying the local least-state, parity, low/high, and nonzero-mod-3 conditions used by the RL21--RL23 packing argument.

Its purpose is to identify exactly what additional information is required for any further Track-A improvement.

## 1. Parametric family

For any integer `t>=0`, put

`R = 361+486t`,

and define five successive odd states

`x0 = 379+512t`,

`y0 = 569+768t`,

`x1 = 427+576t`,

`y1 = 641+864t`,

`z  = 481+648t`.

Then

`z=(4R-1)/3`,

so `z` is exactly the RL22 high threshold.

The induced odd-map valuations are exactly

`[1,2,1,2,2]`,

and the transitions are

`x0 -> y0 -> x1 -> y1 -> z -> R`.                         (R23S.1)

Moreover

`R < x0,x1 < z`,

while `y0,y1,z` are high. Thus `x0,x1` form a maximal two-low short-linked chain of RL22 type II, with no additional high state after the owned terminal `z` before the next low state `R`.

## 2. Exact equality in the RL23 core bound

For `F(s)=1+1/(3s)`, direct multiplication gives

`F(x0)F(y0)F(x1)F(y1)F(z)`
` = 256R/(256R-319)`.                                     (R23S.2)

This is exactly the type-II `k=2` core bound that defines the RL23 global factor

`G(R)=[256R/(256R-319)]^(1/5)`.

So the dominant local block inequality is not merely an artifact of a relaxed rational threshold: it is attained by an infinite family of exact integer Collatz trajectory segments.

## 3. Compatibility with the global mod-3 phase theorem

The displayed states are all nonzero modulo `3` whenever

`t != 1 (mod 3)`.

Hence infinitely many exact saturation segments survive the RL20 theorem that no actual phase state is divisible by `3`.

The terminal state is not an arbitrary return to the minimum. Since

`z=(4R-1)/3`,

we have

`3z+1=4R`.

Equivalently, `z` is exactly the physical odd predecessor produced by the RL20 exceptional weak final-return address `(n_close,t_close)=(1,1)`: from `2R+1=3q` one gets `z=2q-1=(4R-1)/3`. Thus the local packing extremizer lands on the same weak-close mechanism that survives the RL20 final-return audit.

There are even infinite subfamilies compatible with the inherited hard least-root residue package. If

`t == 3 or 11 (mod 24)`,

then

`R == 91 (mod 144)`,

`R == 11 (mod 16)`,

and all displayed states remain nonzero modulo `3`. These are precisely congruence-compatible with the unique hard-root class in which RL20 allows the exceptional `(n_close,t_close)=(1,1)` close.

Thus the local extremizer is not removed by the currently frozen hard-root/final-return congruence conditions.

## 4. Strategic consequence

The new coefficient

`319/1280`

is a genuine saturation point for the present **independent local block** method.

Any further global packing improvement must use information that couples this five-odd-state segment to material outside the segment. Candidate inputs include:

- restrictions on what can precede the returning least state `R`;
- restrictions on consecutive maximal-chain block types;
- the global valuation average `sum nu_i/L=A/L`;
- RL-specific root/final-return ownership not present in the generic least-state packing argument;
- a global residue or transport condition that excludes the parametric family despite its local compatibility.

Simply tightening the existing six core inequalities, the high/high pair estimate, or the nonzero-mod-3 phase condition cannot beat the RL23 constant uniformly.

Verifier: `verify_rl23_local_packing_saturation.py`.
