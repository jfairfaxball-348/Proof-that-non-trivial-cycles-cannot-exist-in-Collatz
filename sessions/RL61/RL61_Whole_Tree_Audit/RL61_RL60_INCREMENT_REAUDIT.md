# RL61 re-audit of the frozen RL60 increment

## Executive verdict

The RL60 internal K-threshold increment through `K=39` survives independent replay and can be promoted from “replay requested” to **re-audited exact finite certificate**.

The Barina path-record reduction also survives a fresh interface and boundary audit and can be classified as an **external computational certificate** giving `25 <= K <= 129` for the fixed safe-CF survivor.

Neither result is an analytic theorem, and neither closes Gate A globally.

## 1. Integrity and inherited verifier status

The outer RL60→RL61 archive, internal manifest, and unchanged inherited RL59→RL60 sidecar all verified.

The inherited `run_all_rl59_to_rl60_verifiers.sh` suite passed, including:

- normalized type-B obstruction;
- four-pump entry;
- final-tail rational forcing;
- strengthened bootstrap arithmetic;
- exact K25, K27, K29 terminal-ancestor searches and their boundary hits.

## 2. Audit of `residue_interval_cert.cpp`

### Core invariant

At recursion depth `j`, a node represents one residue class modulo `2^j` and an affine shortcut-Collatz state
\[
y(n)=\frac{A n+C}{2^j}.
\]
The parity split refines the residue class and updates the affine coefficients exactly.

The certifier performs three logically distinct operations:

1. **terminal target test:** detect whether the represented trajectory hits a permitted terminal predecessor;
2. **descent test:** when
   \[
   (2^j-A)n_{min}>C,
   \]
   every start in that node has already fallen below its initial value, so minimal-counterexample descent certifies no first counterexample in that class;
3. **exact fallback:** follow remaining singleton/small residue classes directly.

This is a valid exact finite-certificate strategy for the deployed bounded intervals.

### Important implementation caveat

The original RL60 source contains a fallback of the form

```text
if (mn == mx || j >= 36) exact(mn)
```

At `j>=36`, checking only `mn` is automatically exhaustive only when the submitted interval has width less than `2^36`, because then a residue class modulo `2^36` contains at most one submitted start.

All supplied RL60 replay chunks are roughly four billion wide, hence below `2^32` and therefore safely below `2^36`. The published deployment is sound.

However, the source should **not** be advertised as an arbitrary-width interval certifier without repairing this fallback.

## 3. Independent second implementation

RL61 wrote a second audit implementation, preserved as `audit_evidence/residue_interval_cert_audit3.cpp`, with two changes:

- terminal targets are precomputed;
- when a deep residue class can contain multiple starts, the fallback iterates all represented starts rather than checking only the first;
- singleton exact continuation starts from the already-computed affine state instead of replaying its first `j` steps.

On a cross-checked K39 chunk it exactly reproduced the original certifier's structural counts and peak:

- interval `[45,812,984,490, 49,812,984,489]`;
- `nodes = 94,206,395`;
- `drop = 8,187,909`;
- `leaf = 38,915,289`;
- `max j = 32`;
- `max steps = 454`;
- peak `41,170,824,451,011,417,002`.

This provides a meaningful implementation cross-check rather than a second invocation of the same binary.

## 4. Threshold replay results

### K31

Certified hit-free:
\[
[125{,}687{,}199,\;715{,}827{,}881].
\]
Boundary
\[
715{,}827{,}882
\]
hits the K31 terminal target. Therefore
\[
N(31)=715{,}827{,}882.
\]

### K33

Certified hit-free:
\[
[715{,}827{,}882,\;1{,}908{,}874{,}352].
\]
Boundary
\[
1{,}908{,}874{,}353
\]
hits the K33 target. Therefore
\[
N(33)=1{,}908{,}874{,}353.
\]

### K35

The interval from the K33 boundary to
\[
10{,}180{,}663{,}218
\]
was replayed in four bounded chunks, all hit-free. Boundary
\[
10{,}180{,}663{,}219
\]
hits K35. Thus
\[
N(35)=10{,}180{,}663{,}219.
\]

### K37

The full interval
\[
[10{,}180{,}663{,}219,\;45{,}812{,}984{,}489]
\]
was covered by nine bounded chunks, all hit-free. Boundary
\[
45{,}812{,}984{,}490
\]
hits K37. Thus
\[
N(37)=45{,}812{,}984{,}490.
\]

### K39

The frozen interval
\[
[45{,}812{,}984{,}490,\;122{,}167{,}958{,}640]
\]
was replayed in the twenty preserved bounded chunks. Every chunk certified hit-free.

The next start
\[
122{,}167{,}958{,}641
\]
hits the K39 terminal predecessor
\[
183{,}251{,}937{,}962
\]
immediately after one shortcut step. Hence
\[
\boxed{N(39)=122{,}167{,}958{,}641}.
\]

## 5. Audited threshold table

| K | `N(K)` | `J_min=2N+1` | derived `z` floor |
|---:|---:|---:|---:|
| 25 | 11,184,810 | 22,369,621 | 9,457,747 |
| 27 | 13,256,071 | 26,512,143 | 11,209,181 |
| 29 | 125,687,199 | 251,374,399 | 106,279,619 |
| 31 | 715,827,882 | 1,431,655,765 | 605,295,637 |
| 33 | 1,908,874,353 | 3,817,748,707 | 1,614,121,697 |
| 35 | 10,180,663,219 | 20,361,326,439 | 8,608,649,047 |
| 37 | 45,812,984,490 | 91,625,968,981 | 38,738,920,711 |
| 39 | 122,167,958,641 | 244,335,917,283 | **103,303,788,559** |

The z conversion uses the inherited terminal-mass inequality
\[
M_{final}>23/4,
\]
the per-zero `d=1` weight bound, and exact odd-`J` parity rounding. It is an analytic consequence of an exact finite threshold **within the fixed survivor hypotheses**.

## 6. Fresh external Barina audit

### Interface match

The path-record source defines the same shortcut map used by the synchronized terminal tail:
\[
T(n)=\begin{cases}
(3n+1)/2,&n\text{ odd},\\
n/2,&n\text{ even}.
\end{cases}
\]
It states that its table lists the path records for all starts below `2^71`. A peer-reviewed 2025 verification paper records convergence verification through `2^71`.

Audit source URLs:

- `https://pcbarina.fit.vut.cz/path-records.htm`
- `https://link.springer.com/article/10.1007/s11227-025-07337-0`

### Relevant record envelope

For the largest start bound arising near K129/K131, the controlling record is
\[
n_r=48{,}503{,}373{,}501{,}652{,}785{,}087
\]
with path peak
\[
P_r=296{,}696{,}710{,}908{,}147{,}364{,}747{,}230{,}298{,}439{,}288{,}489{,}642.
\]
The next path-record start is
\[
55{,}247{,}846{,}101{,}001{,}863{,}167,
\]
which remains above the audited start bound at K129 and K131.

### K129 boundary

The exact fixed-q coupling gives
\[
z_{129}=45{,}446{,}975{,}257{,}190{,}057{,}737.
\]
From the terminal mass bound, the largest admissible odd state is
\[
J_{max}=107{,}491{,}976{,}260{,}484{,}310{,}471,
\]
so
\[
n_{max}=53{,}745{,}988{,}130{,}242{,}155{,}235.
\]
The terminal target
\[
B_{129}=(2^{129}-2)/3
=226{,}854{,}911{,}280{,}625{,}642{,}308{,}916{,}404{,}954{,}512{,}140{,}970
\]
is below `P_r`, so K129 is not excluded by this envelope.

### K131 contradiction

Now
\[
z_{131}=45{,}446{,}975{,}257{,}190{,}057{,}735,
\]
with maximal admissible
\[
J_{max}=107{,}491{,}976{,}260{,}484{,}310{,}465,
\]
and
\[
n_{max}=53{,}745{,}988{,}130{,}242{,}155{,}232.
\]
The same record envelope still applies, while
\[
B_{131}=(2^{131}-2)/3
=907{,}419{,}645{,}122{,}502{,}569{,}235{,}665{,}619{,}818{,}048{,}563{,}882
\]
exceeds `P_r`. Therefore K131 is impossible.

For each larger odd K, `z=q+3-K` decreases, hence the allowable start bound does not increase, while `B_K` increases by a factor of four every two K-steps. The contradiction persists.

Thus the external certificate yields
\[
\boxed{25\le K\le129,\quad K\text{ odd}.}
\]

## 7. Exact z interval from the external certificate

The fixed survivor has
\[
q+3=45{,}446{,}975{,}257{,}190{,}057{,}866.
\]
Since `z=q+3-K`, odd `25<=K<=129` gives
\[
\boxed{
45{,}446{,}975{,}257{,}190{,}057{,}737
\le z\le
45{,}446{,}975{,}257{,}190{,}057{,}841.}
\]
There are 53 admissible odd K values, equivalently
\[
t=K-3\in\{22,24,\ldots,126\}.
\]

## 8. Classification and redundancy

The internal K39 floor and the external K<=129 reduction answer different provenance questions.

- **K39:** internal, independently replayed exact finite certificate; no external path-record table needed.
- **K<=129:** stronger for the fixed survivor, but external; depends on the stated completeness of the Barina path-record data below `2^71`.

For research using the external input, the K39 z floor is numerically superseded. It is nevertheless a valuable independent fallback and should remain preserved.

## 9. What RL60 did not prove

RL60 does **not** prove:

- the fixed safe-CF survivor impossible;
- Gate A uniformly;
- a global radius-3 bridge;
- RL closure;
- the Collatz conjecture.

The correct status is: a materially sharpened but still open restricted survivor, now with independently audited internal certificates and a valid external finite K window.
