---
title: "Collatz R# Excursion-to-Proliferation — Cube-Root Fragmentation and Cumulative Packet Integral Handover"
date: 2026-08-18
authoritative_previous_handover: "Collatz_Rsharp_Spine_Bush_Packet_Amortization_Handover_2026-08-18.md"
status: "research handover; theorem/computation labels mandatory"
next_named_target: "Cumulative Packet Integral Lemma"
primary_goal: "Prove a uniform positive lower bound on time-integrated packet count for every no-leak pure r=1 corridor, then telescope strict packet drift into trapped inverse mass."
---

# 0. Executive state

This phase materially advances the spine–bush–packet programme but does **not** solve the Collatz conjecture and does **not** yet prove the arbitrary-length pure `r=1` corridor theorem.

The previous handover's local theorem-bearing verifiers were reproduced successfully. The neutral-ray quotient and exact common-digit affine packet state were frozen. The side-bush Green charge was sharpened from the inherited easy bound `<22.82` to `<20` using the actual certified contraction ratio.

The decisive new result is a **deterministic fractional scale-to-fragmentation lemma**. For corrected packet capacity

\[
\widehat E_r(P)=2^{-r}E(P),\qquad E(P)=\sum_{J\in P}2^J,
\]

define a cube-root packet moment. There are two certified forms:

1. **Broad form.** If
   \[
   M_9(t)=\sum_{x(P)\ge9}\widehat E(P)^{1/3},
   \]
   then every exact common-digit refinement satisfies
   \[
   \boxed{M_9(t+1)+H_t\ge M_9(t).}
   \]

2. **Strong high-packet form.** If
   \[
   M_{14}(t)=\sum_{x(P)\ge14}\widehat E(P)^{1/3},
   \]
   then
   \[
   \boxed{M_{14}(t+1)+H_t\ge \frac{109}{100}M_{14}(t).}
   \]

Here `H_t` is the packet mass permanently certified at that refinement. These statements are stronger than required by common-digit coupling: they hold packet-by-packet for **every** top phase and for either Beatty carry.

By Hölder,

\[
M^{}\le N^{2/3}E^{1/3},
\]

so

\[
\boxed{N\ge \frac{M^{3/2}}{E^{1/2}}.}
\]

This is the first clean deterministic bridge in the programme from exponential scale collapse to forced packet proliferation.

The frozen strict two-digit packet drift then splices directly:

\[
4H_2+V_{t+2}-V_t\ge N_{t+2}
\ge \frac{M_{t+2}^{3/2}}{\sqrt{E_{t+2}}}.
\]

For the strong cube-root moment,

\[
M_{t+2}\ge \left(\frac{109}{100}\right)^2M_t
-\frac{109}{100}H_2.
\]

Thus a two-digit scale valley cannot be free: it must be paid either directly through `H_2` or through a forced packet-count term that the strict `V` drift banks.

The remaining obstacle is **global**, not local: prove that these local payments integrate to a fixed positive fraction of corridor scale for the true entry ensemble.

A new empirical invariant points to the right scalar target. On six independently verified hostile no-leak corridors `q=24,26,...,34`, the cumulative packet count satisfies

\[
\frac{\sum_t N_t}{(3/2)^q}\approx0.0985\text{--}0.1018,
\]

with each time parity separately near `0.049`. This is computational evidence only, but it aligns almost perfectly with what the strict two-digit drift needs.

The next theorem should therefore target a **Cumulative Packet Integral Lemma** rather than another pointwise scale potential.

---

# 1. Frozen reproduction of inherited theorem-bearing code

The following inherited verifiers were run without changing their mathematics and passed:

- `packet_positive_drift_verifier.py`
  - strict two-digit packet drift
  - `4 H2 + sum V(Q) >= V(P) + #Q`
  - wide stress audit through packet top `x<=100`
- `collatz_scale_mixing_verifier.py`
  - corrected-height geometric kernel
  - exact bad-hit mixing split `1366:43:2752` in canonical ordering
  - finite 3-adic Perron values `m=1..9`
- `collatz_neutral_spine_verifier.py`
  - critical normalized local weights `1, 1/2, 1/4`
  - visible rational spine
  - inherited q=26 direct BFS specimen `20,275`, `eta=0.535288764039315...`
- `collatz_side_bush_spectral_gap.py`
  - certified contraction ratio `0.9888021178022558... < 0.99`
  - Green bound `<3400/149`

No inherited theorem-bearing verifier failed.

---

# 2. Neutral-ray quotient: newly frozen

New verifier:

`collatz_neutral_ray_quotient_verifier.py`

For

\[
P_2(t)=\frac{3t+1}{2},\qquad m=v_3(t+1),
\]

define

\[
\boxed{\xi(t)=\frac{2^m(t+1)}{3^m}.}
\]

The verifier freezes:

\[
v_3(P_2(t)+1)=m+1,
\]

and

\[
\boxed{\xi(P_2(t))=\xi(t).}
\]

Hence neutral phase-2 rays are classified by `xi`; the visible rational critical ray is the special case `xi=1/2`, not the only global neutral ray.

Finite-cylinder projection is also frozen. If `y` is known modulo `3^M` and has exact shadow depth `m<M`, the residual quotient label modulo `3^(M-m)` is preserved by legal neutral continuation. A fully sticky cylinder has exactly three next ternary lifts: one remains sticky one level deeper and two leave onto definite side labels.

**Status:** theorem-level algebra + executable exact audit.

---

# 3. Exact common-digit affine state: newly frozen

New verifier:

`collatz_common_digit_affine_verifier.py`

Each packet boundary is represented over one unresolved common 3-adic tail by

\[
y=a z+c.
\]

Resolving one digit writes

\[
z=d+3z',\qquad d\in\{0,1,2\},
\]

and the **same** `d` is applied to the entire packet ensemble.

For sibling index `i`,

\[
C=4^i(ad+c)+\frac{4^i-1}{3}.
\]

The two legal inverse branches update the affine boundary exactly:

phase 2:
\[
a'=2\,4^i a,\qquad c'=\frac{2C-1}{3},
\]

phase 1:
\[
a'=4\,4^i a,\qquad c'=\frac{4C-1}{3}.
\]

A large exact-integer audit passes.

This closes the implementation loophole in which descendants were accidentally allowed independent hostile ternary rotations.

**Status:** exact finite-cylinder state representation; suitable basis for complete-excursion work.

---

# 4. Side-bush charge sharpened

New verifier:

`collatz_side_bush_charge_verifier.py`

Using the actual exact-rational certified spectral ratio rather than rounding to `0.99`, and the exact first-emission `G` bound, the total normalized future ordinary side-bush cloud from one critical emission is bounded by

\[
\boxed{K_0<19.969<20.}
\]

Therefore an `m`-level critical episode emits at most

\[
\boxed{20m}
\]

normalized ordinary side-bush charge by subadditivity.

This improves the inherited easy constant `<22.82`.

**Status:** theorem-level consequence of the frozen exact-rational `G` certificate.

---

# 5. Independent reconstruction of the actual corridor entry ensemble

New engine:

`collatz_corridor_affine_engine.py`

New verifier:

`collatz_initial_frontier_reconstruction_verifier.py`

Starting only from

\[
n=2^{q+1}k-1,\qquad Y=2\,3^qk-1,
\]

an arbitrary-precision symbolic inverse BFS reconstructs the compulsory `q`-level corridor entry frontier. Before depth `q`, legality is `k`-independent because the affine coefficient retains enough powers of 3. At depth `q`, each frontier object is assigned its doubling channel, then converted into an exact common-digit packet ensemble.

The reconstruction independently reproduces **every row** of frozen `initstats.csv` for

\[
q=6,8,\ldots,44,
\]

including:

- certified core mass;
- frontier size;
- maximum channel;
- full channel histogram.

This means subsequent experiments no longer depend on the missing exploratory engine from the previous session.

**Status:** exact computational reconstruction; independently cross-checked against frozen statistics.

---

# 6. New literal hostile-corridor reproductions

New verifier:

`collatz_hostile_corridor_reproduction_verifier.py`

The common-digit affine engine found concrete terminal no-leak paths, and every final `k` was then checked by a **literal inverse BFS** under the shortened inverse rule.

| q | concrete k | exact trapped nodes | eta = nodes/(Y/n) |
|---:|---:|---:|---:|
| 24 | 21,110,133,131 | 9,434 | 0.560409713927523 |
| 26 | 67,938,179,757,581 | 20,092 | 0.530457304418146 |
| 28 | 29,331,473,504,814,788 | 43,746 | 0.513313983212251 |
| 30 | 279,078,973,701,192,084,041 | 95,609 | 0.498610022716389 |
| 32 | 592,755,155,208,612,185,970,728 | 212,214 | 0.491873858275712 |
| 34 | 4,560,926,434,595,330,056,987,588,682 | 473,775 | 0.488055636091818 |

Important consequences:

- The previously preliminary q=26 value near `0.53046` is now independently promoted to a concrete exact BFS witness: **20,092 nodes**.
- q=30 independently reconfirms that a universal `1/2` trapped-mass constant is false: `eta<1/2`.
- These are hostile examples, not lower-bound theorems.

The beam search is heuristic. Only the final listed witnesses and literal BFS counts are exact.

---

# 7. Negative result: a static bank still does not close the theorem

The strict packet potential does telescope locally. If `C` is cumulative packet harvest and `V` the frozen packet potential, then on admissible two-digit blocks

\[
4\Delta C+V_{t+2}-V_t\ge N_{t+2}.
\]

Hence `4C+V` is nondecreasing on the relevant two-step skeleton.

However, normalized static combinations

\[
\widehat E+\alpha(4C+V)
\]

still exhibit q-dependent minima on the new hostile paths. For example the normalized starting `4C+V` bank on the q=34 hostile path is only about `0.0970`.

Therefore the global theorem cannot be reduced to a fixed-coefficient static Lyapunov function of this form.

**Status:** computational falsification of a proof strategy, not a theorem about all possible potentials.

---

# 8. New theorem: fractional fragmentation bridge

Two new verifiers:

- `collatz_fractional_fragmentation_verifier.py`
- `collatz_cube_root_fragmentation_verifier.py`

The cube-root version is the cleaner theorem for subsequent work.

## 8.1 Capacity and corrected capacity

For

\[
P_{x,b}=(x,x-2,\ldots,b),
\]

let

\[
E(P)=\frac{2^{x+2}-2^b}{3}.
\]

If `r` Beatty `1` carries have accumulated, set

\[
\widehat E_r(P)=2^{-r}E(P).
\]

## 8.2 Broad cube-root moment

Define

\[
M_9=\sum_{x(P)\ge9}\widehat E(P)^{1/3}.
\]

Then every exact refinement obeys

\[
\boxed{M_9(t+1)+H_t\ge M_9(t).}
\]

The finite bridge strip `9<=x<=13` is interval-certified by exact integer cube-power comparisons. High packets are covered by the stronger theorem below. Children dropping below the cutoff can be discarded because their cube-root capacity is bounded by their already-created packet mass.

## 8.3 Strong cube-root growth/cash theorem

Define

\[
M_{14}=\sum_{x(P)\ge14}\widehat E(P)^{1/3}.
\]

Then

\[
\boxed{M_{14}(t+1)+H_t\ge\frac{109}{100}M_{14}(t).}
\]

This is proved by a coarse analytic branch selection that works for every phase.

For a high parent,

\[
E(P)\le\frac43 2^x.
\]

Every selected child has at least two channels, hence

\[
E(Q)\ge\frac54 2^{x_Q}.
\]

After the carry cancels in corrected coordinates, selected top shifts are:

- hostile phase 0: `-3,-4,-9,-10`;
- phase 1: `-1,-2`;
- neutral phase 2: `0,-5`.

Exact rational radical bounds give coarse ratios

\[
1.09536,\qquad 1.37898,\qquad 1.28118,
\]

respectively, all above `109/100`.

For every packet `x<14`,

\[
E(P)^{1/3}\le F(P),
\]

verified exactly by the integer inequality

\[
E(P)\le F(P)^3.
\]

Thus low fractional credit is cashed one-for-one into packet harvest.

## 8.4 Hölder scale-to-fragmentation consequence

For the surviving high packets,

\[
M=\sum e_P^{1/3}
\le N^{2/3}\left(\sum e_P\right)^{1/3}.
\]

Therefore

\[
\boxed{N\ge\frac{M^{3/2}}{E^{1/2}}.}
\]

This is a deterministic entropy/fragmentation inequality exactly of the type sought in Task E of the previous handover.

**Status:** theorem-level packet inequality with exact-rational / exact-integer executable certificate.

---

# 9. Task-F splice: cube-root fragmentation into strict packet drift

The frozen two-digit packet theorem gives, after summing over the ensemble,

\[
\boxed{4H_2+V_{t+2}-V_t\ge N_{t+2}.}
\]

Using the broad Hölder bridge,

\[
\boxed{
4H_2+V_{t+2}-V_t
\ge
\frac{M_{t+2}^{3/2}}{\sqrt{E_{t+2}}}.
}
\]

Using the strong high-packet cube-root inequality twice,

\[
M_{t+2}+H_{t+1}+\frac{109}{100}H_t
\ge
\left(\frac{109}{100}\right)^2M_t.
\]

Hence the simpler bound

\[
\boxed{
M_{t+2}
\ge
\left(\frac{109}{100}\right)^2M_t
-rac{109}{100}H_2.
}
\]

Combining,

\[
\boxed{
4H_2+\Delta V
\ge
\frac{
\left[
(109/100)^2M_t-(109/100)H_2
\right]_+^{3/2}
}{\sqrt{E_{t+2}}}.
}
\]

This is the cleanest formal local spine/fragmentation-to-packet-credit splice obtained so far.

It does **not** yet imply a uniform corridor constant by itself because the fractional moment is sublinear in a single concentrated exponential packet. Common-digit mixing / critical-excursion structure is still needed at the global integration step.

**Status:** theorem-level algebraic consequence of the two frozen local lemmas, modulo the same global packet-accounting distinctness convention inherited from the packet framework.

---

# 10. New global diagnostic: cumulative packet integral

New script:

`collatz_hostile_cumulative_packet_diagnostic.py`

For each frozen hostile terminal path, define `N_t` as the number of live packets after refinement `t`.

The exact affine replay gives:

| q | total `sum N_t / (3/2)^q` | parity 0 | parity 1 |
|---:|---:|---:|---:|
| 24 | 0.101817071196923 | 0.051858986671478 | 0.049958084525445 |
| 26 | 0.099797362666763 | 0.050637921056839 | 0.049159441609924 |
| 28 | 0.099562683389474 | 0.050280035158974 | 0.049282648230500 |
| 30 | 0.098570511556051 | 0.049564263363246 | 0.049006248192805 |
| 32 | 0.098546753900819 | 0.049459961462229 | 0.049086792438590 |
| 34 | 0.098651570872952 | 0.049371626765812 | 0.049279944107140 |

The near constancy is striking.

It is also exactly the quantity required by strict packet drift. If one can prove for every no-leak corridor

\[
\boxed{
\sum_t N_t\ge c_N\left(\frac32\right)^q
}
\]

for **any** universal `c_N>0`, then one parity has at least half that count. Applying the strict two-digit drift on that parity and telescoping to packet extinction gives, schematically,

\[
4H_{\rm packet}+V_{\rm final}
\ge
V_{\rm start}+\sum_{t\in\text{one parity}}N_t.
\]

At complete packet extinction `V_final=0`, so the packet harvest is at least a fixed positive multiple of corridor scale, up to the finite entry/endpoint bookkeeping.

Thus a cumulative packet integral theorem would essentially close the missing pure-corridor amortization step, subject to the final node-distinctness audit.

**Status:** the six numerical ratios are exact for the listed paths, but the uniform lower bound is **CONJECTURAL / OPEN**.

---

# 11. Revised gate status

## Gate 1 — inherited local verifiers

**CLOSED.**

## Gate 2 — neutral-ray quotient

**CLOSED.** New exact verifier added.

## Gate 3 — finite-cylinder critical-excursion representation

**SUBSTANTIALLY CLOSED, but stopping-time theorem not fully packaged.** The common-digit affine state and neutral quotient are exact. A formal publication-style excursion stopping-time definition should still be written.

## Gate 4 — bush charge lemma

**CLOSED with improved constant `<20` per critical level.**

## Gate 5 — scale-to-fragmentation

**LOCAL DETERMINISTIC BRIDGE CLOSED.** Cube-root moment + Hölder now gives an exact scale-to-packet-count inequality. The remaining issue is global integration across the true critical excursion.

## Gate 6 — splice strict packet drift

**LOCAL SPLICE CLOSED.** Exact nonlinear two-digit inequality obtained. Global telescope to a corridor-scale constant remains open.

## Gate 7 — uniform critical-excursion dichotomy

**OPEN.** It is now sharpened to the cumulative packet integral target below.

## Gate 8 — arbitrary pure `r=1` corridor theorem

**OPEN.** No theorem-level universal `c0>0` yet.

## Gate 9 — mixed excursion integration

**DO NOT START YET.**

---

# 12. Next named theorem: Cumulative Packet Integral Lemma

The next session should attack the following statement directly.

### Target CPIL

There exist explicit constants `q0` and `c_N>0` such that for every pure `r=1` corridor of length `q>=q0` beginning at the global lower barrier, and every exact common ternary continuation that does not leak below the barrier, the corresponding packet process satisfies

\[
\boxed{
\sum_{t\ge0}N_t
\ge
c_N\left(\frac32\right)^q.
}
\]

It is acceptable to prove a weaker parity-specific / blocked version directly, e.g.

\[
\sum_jN_{2j+\varepsilon}
\ge
c_N'\left(\frac32\right)^q
\]

for one `epsilon in {0,1}` selected after the finite entry step.

Do **not** target the observed constant `~0.049`; any explicit positive constant, even fantastically small, is enough.

### Why CPIL is now the right theorem

1. The strict packet drift pays one unit per successor packet on each two-digit block.
2. Terminal packet extinction removes residual `V` credit.
3. Cube-root fragmentation gives an exact lower bound on packet count whenever exponential capacity is dispersed.
4. The only way to avoid such dispersion for long is the neutral critical structure already isolated by the `xi` quotient.
5. Ordinary side bushes have a strict spectral gap and bounded Green charge.

Therefore the remaining proof should classify a complete excursion into:

- **fragmented epochs**, where Hölder + cube-root moment directly forces `N_t`;
- **concentrated epochs**, which must shadow a neutral phase-2 ray;
- **neutral epochs**, whose repeated side emissions and eventual exit must be charged into future fragmented epochs / packet integral;
- **low-packet epochs**, already cashed into `H`.

The key is to prove these charges are disjoint or bounded-overlap and that an arbitrarily long neutral shadow cannot suppress the **integrated** packet count.

---

# 13. Suggested next execution programme

1. **Formalize CPIL accounting skeleton.** Define exact time parity, `H_t`, `N_t`, `E_t`, `M_9`, `M_14`, `V_t`, and the complete extinction time. Write the strict telescope with endpoint terms explicitly.
2. **Prove packet-accounting distinctness.** Show every `F(Q)` unit charged in `H` corresponds to a genuinely new inverse node, or establish a bounded-overlap correction. This was still listed as unresolved in the previous handover.
3. **Concentration versus fragmentation lemma.** Use `N >= M^(3/2)/sqrt(E)` to define a quantitative concentrated state. Show that if `N` is too small to pay CPIL, a fixed fraction of `E` is carried by very few high packets.
4. **Concentrated state -> neutral shadow.** Use the deterministic bad-hit mixing `2752:1366:43` and corrected-top monotonicity to show a persistently concentrated high-scale carrier must repeatedly choose phase-2 top continuation and hence enter a high-depth `xi`-ray cylinder.
5. **Neutral shadow -> side-emission integral.** Use the exact `1/21` immediate side-emission structure and the `<20` bush Green charge to relate neutral duration to a controlled family of side excursions.
6. **Side excursions -> packet integral.** Apply the broad cube-root moment to those side packets. The desired estimate is not a lower bound on their instantaneous `E`, but on their cumulative `N_t` before they are cashed into `H` or rejoin the fragmented class.
7. **Close CPIL with horrible constants.** Optimize nothing. Use large safety factors and finite low kernels.
8. **Telescope strict drift.** Convert CPIL into an explicit trapped packet-harvest fraction.
9. **Add entry core + first-refinement bookkeeping and prove pure-corridor theorem.**
10. **Only then return to mixed `r` words.**

---

# 14. Files added in this phase

- `collatz_neutral_ray_quotient_verifier.py`
- `collatz_side_bush_charge_verifier.py`
- `collatz_common_digit_affine_verifier.py`
- `collatz_affine_shared_digit_probe.py`
- `collatz_corridor_affine_engine.py`
- `collatz_initial_frontier_reconstruction_verifier.py`
- `collatz_hostile_corridor_reproduction_verifier.py`
- `collatz_fractional_fragmentation_verifier.py`
- `collatz_cube_root_fragmentation_verifier.py`
- `collatz_hostile_cumulative_packet_diagnostic.py`
- this handover document

---

# 15. Claims discipline

### Theorem-level / exact certificate

- inherited strict packet drift;
- inherited corrected-height geometric kernel;
- inherited side-bush spectral gap;
- neutral-ray invariant and finite-cylinder quotient;
- exact common-digit affine packet refinement;
- side-bush charge `<20` per critical emission/level in the stated normalized sense;
- cube-root broad noncontraction/cash inequality;
- strong `1.09` high-packet cube-root growth/cash inequality;
- Hölder packet-fragmentation inequality;
- algebraic local splice into strict two-digit `V` drift;
- exact reconstruction of frozen entry histograms.

### Exact computational witnesses, not universal theorems

- hostile corridor node counts for q=24..34;
- q=30 `eta<1/2` witness;
- cumulative packet integral ratios near `0.099` total and `0.049` per parity;
- static potential valley diagnostics.

### Open / conjectural

- a universal positive lower bound for cumulative packet integral;
- a complete spine–bush–packet excursion dichotomy with uniform positive corridor-scale constant;
- arbitrary-length pure `r=1` corridor theorem;
- mixed-word proliferation theorem;
- any contradiction to a hypothetical least Collatz counterexample;
- the Collatz conjecture itself.

---

# 16. One-paragraph continuation prompt

Continue from `Collatz_Rsharp_CubeRoot_Fragmentation_CumulativePacket_Handover_2026-08-18.md`. Reproduce the theorem-bearing verifiers first. Treat the new cube-root fragmentation lemma as frozen: `M_9(t+1)+H_t >= M_9(t)`, `M_14(t+1)+H_t >= 1.09 M_14(t)`, and `N >= M^(3/2)/sqrt(E)`. Treat the strict two-digit packet drift as frozen. The next target is the **Cumulative Packet Integral Lemma**: prove any universal `c_N>0` such that every no-leak pure `r=1` corridor entry ensemble has `sum_t N_t >= c_N (3/2)^q` (or an equivalent parity-blocked statement). Use the neutral-ray `xi` quotient to classify concentrated epochs, the exact common-digit affine state to preserve coupling, the `1/21` side-emission geometry and `<20` bush charge for neutral episodes, and the cube-root moment/Hölder bridge for fragmented epochs. Do not claim a universal constant from the observed `~0.049` parity ratios; those remain diagnostics. Close node distinctness before promoting packet harvest to trapped inverse-node mass. Only after CPIL and the pure-corridor theorem are rigorous should the programme return to mixed `r` words.
