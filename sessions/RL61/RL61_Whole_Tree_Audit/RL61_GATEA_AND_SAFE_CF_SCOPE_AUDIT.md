# RL61 Gate-A and safe-CF scope audit

## Audit conclusion

Gate A is **globally open** in the retained one-excursion/full-phase architecture.

The RL50–RL60 safe continued-fraction campaign is a **restricted stress subtree** of Gate A. Eliminating its sole surviving convergent would close that subtree only. It would not prove the uniform Gate-A inequality for denominator/approximation regimes outside the safe reduction.

## 1. Exact Gate-A target

The retained one-excursion terminal geometry has
\[
q=z+t,
\]
with
\[
t\ge2\quad\text{even},
\]
and terminal excess
\[
H=e-z+1.
\]
RL46 identifies the missing inequality as
\[
\boxed{H\ge t+3}.
\]
Equivalently,
\[
e\ge q+2.
\]
This is a **uniform theorem target**: it must hold for every retained one-excursion/full-phase geometry if it is to close Gate A by this route.

## 2. What the q-specific work proves—and does not prove

RL46/RL47 constructed exact finite certificates for particular terminal ranges and `q`-slices. These are useful exact exclusions, but they do not quantify over arbitrary retained `q`.

Therefore:

- “many q values are excluded” does not imply Gate A;
- a single fixed continued-fraction convergent is not an exhaustive parametrization of Gate A;
- finite terminal-ancestor thresholds for that convergent are local certificates.

## 3. RL48 separable rank-relaxation barrier

RL47's cap/room programme relaxed the terminal problem into separable rank/displacement constraints. RL48 proves that, under the retained near-resonance hypotheses, this particular relaxation cannot rule out every strict Gate-A violation once
\[
z=q-t\ge42.
\]

This must be read correctly:

- it is **not a counterexample** to `H>=t+3`;
- it is **not evidence that Gate A is false**;
- it proves that the selected separable relaxation has thrown away information needed in the large-`z` regime.

Any successful uniform argument must restore coupling—phase, ownership, zero positions, terminal power, excursion structure, or another invariant not present in the relaxation.

## 4. RL50 height-one Collatz-conjugacy warning

The synchronized height-one subsystem has a particularly important exact interpretation. Under
\[
n=(J-1)/2,
\]
the local synchronized evolution is the shortcut Collatz map
\[
n\mapsto\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

This is a **methodological boundary**. An attempted Gate-A proof that discards the full-phase constraints and asks for an unrestricted theorem about all such height-one trajectories risks becoming the original Collatz problem in disguise.

The safe target is therefore not “solve arbitrary synchronized height-one dynamics.” It is “exploit the extra constraints that a genuine RL/full-phase object imposes on that dynamics.”

## 5. Safe continued-fraction gate

RL50 combines the full-phase approximation with a stable external verification floor at `2^71` and Legendre's continued-fraction criterion. The resulting safe denominator gate is
\[
\boxed{\ell\le92{,}524{,}042{,}457{,}747{,}860{,}050}.
\]
Within this gate, the relevant approximation must be a convergent. The audit recovers one surviving above-`log_2 3` convergent:
\[
 a=123{,}139{,}092{,}617{,}126{,}647{,}266,
\]
\[
 \ell=77{,}692{,}117{,}359{,}936{,}589{,}403,
\]
\[
 q=a-\ell=45{,}446{,}975{,}257{,}190{,}057{,}863.
\]
This object is the **sole safe-CF survivor**, not the sole Gate-A or RL survivor.

## 6. What lies outside safe-CF

At minimum the following remain outside the safe-CF classification:

1. retained denominator/approximation regimes above the Legendre-safe bound;
2. any retained full-phase geometry for which the phase squeeze is insufficient to trigger the same continued-fraction classification;
3. potential coupled configurations that survive the separable rank relaxation but may still be excluded by stronger phase/ownership information.

No RL50–RL60 theorem proves that these regimes are empty.

## 7. The fixed safe-CF survivor after RL59/RL60

For the surviving convergent, the frozen exact coupling is
\[
R=z-27,
\]
\[
K=q-z+3,
\]
\[
K+z=q+3=45{,}446{,}975{,}257{,}190{,}057{,}866.
\]
`K` is odd.

Inherited RL59/RL60 consequences include:

- `Z_x > 143/12`;
- defect energy `E < 5/3`;
- each zero has weight `<17/30`;
- terminal synchronized states `J_end=2^K`, `Q_end=2^K+1`;
- positive terminal potential;
- the repeatable `J=3 <-> 5` pump is neutralized;
- a deterministic final positive height-one tail;
- terminal mass `M_final>23/4`;
- exact terminal-hit alternatives for odd admissible `K`.

These are strong structural facts, but none is currently the missing universal contradiction.

## 8. Internal terminal-ancestor thresholds

RL61 independently re-audited the exact finite thresholds through K39. The strongest internal one gives
\[
N(39)=122{,}167{,}958{,}641,
\]
and, after the RL59 mass-to-`J` conversion,
\[
\boxed{z\ge103{,}303{,}788{,}559}.
\]

This is an exact finite result for the fixed survivor. It does not change the scope of Gate A.

## 9. External path-record restriction

The Barina path-record interface was freshly checked against the exact shortcut map used in the terminal tail. The table is stated complete below `2^71`; the peer-reviewed verification literature supplies the stable range.

For the fixed survivor the terminal-mass bound implies a bounded start `n=(J-1)/2`. Comparing that start bound against the relevant path-record envelope gives:

- `K=129`: no contradiction; the target lies below the applicable record peak;
- `K=131`: contradiction; the target lies above the same record peak;
- for larger odd K, the allowed start bound decreases while the terminal target grows, so the contradiction persists.

Thus the external certificate yields
\[
\boxed{25\le K\le129,\qquad K\text{ odd}.}
\]
Hence
\[
\boxed{t=K-3\in\{22,24,\ldots,126\}.}
\]
Using `K+z=q+3`,
\[
\boxed{
45{,}446{,}975{,}257{,}190{,}057{,}737
\le z\le
45{,}446{,}975{,}257{,}190{,}057{,}841.}
\]

This is an **external computational certificate**. It is not promoted to an analytic theorem of the project.

## 10. Exact K129/K131 comparison

For `K=129`,
\[
z=45{,}446{,}975{,}257{,}190{,}057{,}737.
\]
The terminal-mass bound yields the maximal admissible odd
\[
J=107{,}491{,}976{,}260{,}484{,}310{,}471,
\]
so
\[
n_{max}=53{,}745{,}988{,}130{,}242{,}155{,}235.
\]
The applicable path-record start is
\[
48{,}503{,}373{,}501{,}652{,}785{,}087
\]
with peak
\[
296{,}696{,}710{,}908{,}147{,}364{,}747{,}230{,}298{,}439{,}288{,}489{,}642.
\]
The odd-K terminal target is
\[
B_K=(2^K-2)/3.
\]
At K129,
\[
B_{129}=226{,}854{,}911{,}280{,}625{,}642{,}308{,}916{,}404{,}954{,}512{,}140{,}970,
\]
which is below the record peak, so the record envelope does not exclude K129.

For `K=131`,
\[
n_{max}=53{,}745{,}988{,}130{,}242{,}155{,}232,
\]
still below the next path-record start, so the same record peak controls. But
\[
B_{131}=907{,}419{,}645{,}122{,}502{,}569{,}235{,}665{,}619{,}818{,}048{,}563{,}882,
\]
which is above that peak. Therefore K131 is impossible, and all larger odd K are impossible by monotonicity of the two bounds.

## 11. Does eliminating the safe-CF survivor close Gate A?

**No.**

It closes precisely the current Legendre-safe continued-fraction subtree. Uniform Gate A still requires a theorem covering the retained regimes outside that classification.

This distinction is the most important whole-tree correction produced by the audit.

## 12. Smallest useful Gate-A theorem now

The clean global target remains:

> **Uniform coupled terminal-area lemma.** Every retained one-excursion/full-phase RL object satisfies `H>=t+3`.

A realistic proof must use information absent from the RL48 separable relaxation and must preserve enough full-phase structure not to degenerate into arbitrary shortcut-Collatz dynamics.

Promising ingredients already available in the project include defect energy `E`, height-one telescoping, zero-position telescoping, terminal power, backward grammar, and full-denominator/ownership constraints.
