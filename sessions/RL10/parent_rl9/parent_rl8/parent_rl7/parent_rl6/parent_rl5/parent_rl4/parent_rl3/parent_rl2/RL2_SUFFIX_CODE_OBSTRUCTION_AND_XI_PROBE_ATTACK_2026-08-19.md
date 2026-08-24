# Collatz R# RL-2 — Suffix-Code Obstruction and Xi-Probe Attack

**Date:** 2026-08-19  
**Branch:** RL / hypothetical least red integer eventually entering a nontrivial cycle  
**Session target:** nested suffix/rotation/xi survivor automaton  
**Verdict:** the proposed `Phi_h` tower is classified exactly and is not itself a pruning mechanism. A replacement state variable — exact height defect above `R#` — is isolated, together with a new family of xi side-branch probes. RL remains open.

## 1. Reproduction

The inherited verifiers were rerun and all passed:

- RL algebra baseline: PASS;
- LREC verifier: PASS;
- prefix automaton: PASS.

The new verifier `tools/verify_rl2_suffix_xiprobe.py` also passes. Its scope is exact algebra plus finite audits of the new analytic statements; it does not certify absence of a nontrivial cycle.

## 2. RL-L11 — `Phi_h` is exactly an inverse-integrality code

Let `y` be a positive odd integer with `3∤y`. Let

`e=(e_0,...,e_{h-1})`, `E=sum e_i`,

and let `Q_h(e)` and `Phi_h(e)` be the inherited affine numerator and suffix signature. Define the formal inverse root

`X_h(y;e) = (2^E y - Q_h(e))/3^h`.

Then

`X_h(y;e) ∈ Z  <=>  y = Phi_h(e) (mod 3^h)`.

If this integer is positive, the nested reductions modulo `3^r` for `r<=h` reconstruct a legal positive odd accelerated inverse path of exact exponent word `e` ending at `y`.

**Status: PROVED ANALYTIC THEOREM.**

### Proof sketch

The inherited affine identity gives

`2^E y = 3^h X_h + Q_h(e)`.

Thus integrality is exactly the congruence `y = 2^{-E}Q_h(e) (mod 3^h)`, and inherited result (S) identifies this residue with `Phi_h(e)`. Reducing the same congruence modulo `3^r` leaves only the terminal `r` exponents, so the successive backward divisions by 3 are legal. Each reconstructed predecessor is odd because `(2^d y-1)/3` is odd whenever integral and `y` is odd.

## 3. RL-L12 — same-endpoint suffix matching collapses

If `e` and `f` are any two legal length-`h` accelerated inverse exponent words ending at the same odd state `y`, then

`Phi_h(e) = y = Phi_h(f) (mod 3^h)`.

Therefore inherited RL-L3 does **not** express an extra tail-versus-cycle coincidence. It expresses the fact that both histories are individually legal histories into the same endpoint.

Consequences:

1. the `h=1` terminal parity equality is the parity condition required for an odd predecessor of `c0`;
2. the `h=2` mod-6 terminal-pair invariant is the corresponding two-step inverse-integrality class;
3. these conditions alone do not make the two exponent histories close, equal, or collision-prone.

**Status: PROVED ANALYTIC THEOREM / STRUCTURAL REINTERPRETATION.**

## 4. RL-L13 — periodic unwrapping strengthens the equality but confirms the obstruction

Let the cycle exponent word be extended periodically backwards from the entry state `c0`. For every `h>=1`, the unwrapped cycle supplies a legal length-`h` inverse history into `c0`. Hence

`Phi_h(cycle-backward suffix of length h) = c0 (mod 3^h)`.

For `k>0`, the preperiod supplies such a history for every `h<=k`, so in fact

`Phi_h(preperiod suffix) = Phi_h(periodically unwrapped cycle suffix) = c0 (mod 3^h)`

for **every `h<=k`**, with no `h<=L` restriction required once the cycle is unwrapped.

This is formally stronger than RL-L3 but strategically weaker than hoped: the equality survives to arbitrary depth precisely because both sides are inverse histories into the same root.

**Status: PROVED ANALYTIC THEOREM.**

## 5. RL-G6 — a `Phi`-only nested survivor automaton cannot close RL

For every positive odd `y` with `3∤y` and every depth, legal inverse continuations exist. More strongly, let `R<=y` be any fixed floor. One can construct an infinite accelerated inverse path

`y=x_0 <- x_1 <- x_2 <- ...`

such that for every `n>=1`:

- `x_n>=R`;
- `x_n=1 mod3`;
- `xi(x_n)=x_n+1>=R+1`.

### Construction

For a current odd unit `x mod9`, choose `d mod6` so that

`2^d x = 4 (mod9)`.

There is a unique class modulo 6 because 2 generates the units modulo 9. Then

`x'=(2^d x-1)/3 = 1 (mod3)`.

Replacing `d` by `d+6t` preserves this residue and makes `x'` arbitrarily large, so choose `t` large enough that `x'>=R`. Since `x'=1 mod3`, `v3(x'+1)=0` and therefore `xi(x')=x'+1`.

The six residue selectors are:

`1->2, 2->1, 4->6, 5->3, 7->4, 8->5 (mod 9 -> d mod 6)`.

Thus **suffix residue + ordinary inverse legality + least-red floor + local xi barrier admits infinite towers analytically**. Any successful RL automaton must add a genuinely global closure/height/periodicity variable.

**Status: FAILED / REFUTED ROUTE for the stated local automaton.**

## 6. RL-L14 — strict-preperiod entry histories diverge immediately

Assume `k>0`. The immediate preperiod predecessor `r_{k-1}` of `c0` is not the cycle predecessor `c_{L-1}`, because otherwise the preperiod would have entered the deterministic cycle one odd step earlier.

But both predecessors are of the form

`(2^d c0-1)/3`.

Hence

`b_{k-1} != a_{L-1}`.

Inherited `h=1` suffix matching gives equal parity, so

`b_{k-1}-a_{L-1}` is a nonzero even integer.

This is the first genuinely **relative** tail-versus-cycle datum at entry: not the shared `Phi_1`, but the fact that the two legal inverse branches in that shared parity class are distinct.

**Status: PROVED ANALYTIC THEOREM.**

## 7. RL-L15 — exact height-defect recurrence

For `k>0`, walk backwards along the true preperiod from the cycle entry. Put

`x_h=r_{k-h}` for `0<=h<=k`, so `x_0=c0`, `x_k=R#`,

and define

`delta_h=x_h-R# >=0`.

If the next backward exponent is `d=b_{k-h-1}`, then

`x_{h+1}=(2^d x_h-1)/3`

and therefore exactly

`3 delta_{h+1} = 2^d delta_h + (2^d-3)R# - 1`.

For `R#>1`:

- if `d=1`, then `delta_{h+1}<delta_h` whenever the next state remains above the floor;
- if `d>=2`, then `delta_{h+1}>delta_h`.

So **exponent 1 is the unique backward contraction move toward the least-red floor**. All exponents `>=2` move the inverse branch farther from `R#`.

This turns the strict-preperiod problem into an exact controlled-height problem: starting from `c0-R#>0`, a legal branch must remain nonnegative and land exactly at zero after `k` steps, while the periodically unwrapped cycle branch never lands at zero.

**Status: PROVED ANALYTIC THEOREM.**

### Normalized form

With

`z_h=(x_h+1)/(R#+1)`,

the backward transition is

`z_{h+1} = (2^d/3) z_h - (2^d-2)/(3(R#+1))`.

For `d=1` this is exactly `z_{h+1}=(2/3)z_h`. This is the real-height coordinate naturally paired with xi, since xi is precisely maximal iteration of this `d=1` contraction along a legal 3-adic run.

## 8. RL-L16 — xi side-branch probe identity

Let `y` be any red odd state with `3∤y`. For any legal accelerated inverse exponent `d`, define

`p_d(y)=(2^d y-1)/3`

and

`q_d(y)=v3(2^(d-1)y+1)`.

Then exactly

`v3(p_d(y)+1)=q_d(y)-1`

and

`xi(p_d(y)) = 2^q_d (2^(d-1)y+1) / 3^q_d >= R#+1`.

Thus every red state carries an infinite family of side-branch xi probes, not just the coarse profile `v3(y+1)`.

For the special case `y=R#=1 mod3` (in particular the `k=0` branch), every legal `d` is even and leastness forces

`2^(d-1+q_d) > 3^q_d`.

Equivalently

`q_d <= floor((d-1) log(2) / log(3/2))`.

The first ceilings are

`d=2: q<=1; d=4: q<=5; d=6: q<=8; d=8: q<=11; d=10: q<=15; d=12: q<=18`.

The `d=2` case is exactly the inherited exclusion `R# != 4 mod9`. Higher `d` give a sparse infinite family of new 3-adic root exclusions.

**Status: PROVED ANALYTIC THEOREM.**

## 9. RL-L17 — exact initial neutral-run length

Write

`R#+1 = 2^s q`, with `q` odd. Since `R#=3 mod4`, `s>=2`.

Then the forward accelerated orbit of `R#` begins with **exactly `s-1` consecutive exponent-1 steps**. Along this run,

`r_j+1 = (3/2)^j (R#+1)`

and

`xi(r_j)=R#+1`.

At the next state the exponent is at least 2.

Thus the length of the initial xi-neutral spine is not merely bounded: it is exactly `v2(R#+1)-1`.

**Status: PROVED ANALYTIC THEOREM.**

## 10. What session 2 changed

The original primary target asked whether nested `Phi_h` matching might become injective enough to force a contradiction. It does not: `Phi_h` is the endpoint's inverse-integrality code and therefore collapses every legal same-endpoint history into the same residue.

The genuinely discriminating variables are now:

1. **relative branch identity at the entry** (`b_{k-1}!=a_{L-1}` for `k>0`);
2. **height defect above `R#`**, whose sign and exact recurrence distinguish the finite tail from the periodic inverse branch;
3. **side-branch xi probe valuations** `q_d(y)`, which test more of the 3-adic inverse basin than `v3(y+1)` alone;
4. **cycle rotation/minimum constraints**, which remain necessary to tie the relative branch back to periodicity.

## 11. Current endpoint

RL is **not solved**. Session 2 has nevertheless closed one strategic uncertainty: there is no reason to spend another session deepening the raw `Phi_h` suffix scan. The correct next object is a **relative height/rotation/xi-probe automaton**, split by `k=0` and `k>0`.

A successful next theorem should force one of:

- the strict-preperiod height defect can never hit zero without violating a cycle-rotation or xi-probe constraint;
- the `k=0` cycle root violates one of the side-branch valuation ceilings;
- or the remaining survivor class is reduced to a finite recurrent grammar with a proved lift theorem.
