# RL80 — Blue dyadic funnel, certified basin, no-go theorem, and auxiliary basin capture

Date: 2026-08-24

## 0. Executive outcome

RL80 executed the requested exploration of the infinite proved-blue dyadic funnel and the rigorously certified basin of `1`, starting from the checksum-clean RL79 state.

No Gate A, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.

The session produces both a decisive no-go theorem for the original pure dyadic-belt intuition and a genuinely new positive structure.

The principal negative result is:

> **Dyadic/backward saturation is cycle-intersection neutral.** If `C` is an exact periodic orbit of the shortcut Collatz map and `S` is any seed set, then
>
> `C ∩ {2^k s : s in S, k>=0} != empty`
>
> iff
>
> `C ∩ S != empty`.
>
> More generally, if `Pre*(S)={x:T^r(x) in S for some r>=0}`, then
>
> `C ∩ Pre*(S) != empty`
>
> iff
>
> `C ∩ S != empty`.

So the fact that every proved-blue integer generates an infinite ray of proved-blue even multiples does **not** create a new set-theoretic trap for a hypothetical finite cycle. If a cycle ever hits `2^k s`, its forced even halvings put `s` on the same cycle already.

For a certified finite interval `[1,X]`, the dyadic saturation is exactly

`{N : oddcore(N) <= X}`,

and any cycle whose minimum exceeds `X` automatically avoids it. Thus the dyadic closure of a finite verified range adds no cycle obstruction beyond the inherited minimum-state floor.

The positive result is stronger than mere numerical abundance:

> **Analytic blue LTE comb.** For odd `k` and
>
> `1 <= j <= v3(2^k+1)=1+v3(k)`, define
>
> `B(j,k)=2^j(2^k+1)/3^j - 1`.
>
> Then `B(j,k)` is a positive odd integer and follows `j` consecutive odd shortcut-Collatz steps to `2^k`, then reaches `1` by `k` halvings.

This gives arbitrarily deep analytic backward branches and yields a **logarithmically dense family of certified-blue dyadic rays**: the fractional parts of `log_2 B(j,k)` are dense on the log-circle as `j,k` vary legally. Equivalently, for every multiplicative tolerance `epsilon>0`, a finite collection of analytically certified blue dyadic rays can be chosen so that, above some threshold, every positive scale lies within a factor `1+epsilon` of one of those rays.

That is a rigorous version of a very strong “blue belt / blue mesh” intuition. But it still does not force exact equality with a cycle state. The obstruction is a quantifier/scale barrier: arbitrarily fine *relative* proximity does not become an integer intersection without an independent equality-level or absolute-spacing theorem.

RL80 also finds a direct RL-specific basin capture:

> **Terminal all-`11` auxiliary basin theorem.** RL64's exact terminal all-`11` equality forces the start value of that suffix to be exactly `J_0=B(j,k)`. Hence that full-phase auxiliary `J_0` is analytically certified blue. For `k>=3`, the RL50 height-one coordinate `n_0=(J_0-1)/2` is also analytically certified blue.

This is a real contact point between inherited full-phase ownership geometry and the ordinary Collatz basin. It does **not** yet close anything because `J` and `(J-1)/2` are auxiliary quotient coordinates, not identified with an original cycle state. RL50 already warned that height-one synchronized dynamics can re-embed shortcut Collatz inside the quotient system.

The strongest next question is therefore no longer “are there enough blue numbers?” It is:

# Can the exact RL48/RL64 full-phase reconstruction transfer this auxiliary basin capture to an actual owned cycle integer, or prove that no such transfer can exist?

That is selected as the RL81 target.

---

## 1. Incoming state and verification economy

The uploaded RL79 outer SHA-256 matched its sidecar exactly:

`2d66bd49d25b62792e537148944e102a90ee6b6b7a66030ef1de55c9b76fcfdd`.

Fresh unpack:

- internal `SHA256SUMS.txt`: **PASS**;
- `bash verification/run_fast_rl79_verifiers.sh`: **PASS**;
- RL79 common-barrier verifier: **PASS**.

Under the verification-economy rule, the frozen RL79 ledger was accepted without recursively rerunning historical expensive certificates.

The inherited global closure state remains:

- primitive/full-`D` radius-3 local obstruction: **closed**;
- Gate A even terminal `k`: **closed analytically**;
- Gate A terminal `k<=25`: **closed by exact finite-certificate corollary**;
- Gate A odd `27<=k<=165`: **open**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

---

## 2. Shortcut map, basin, and odd cores

Use the ordinary shortcut Collatz map

`T(n)=n/2` for even `n`,

`T(n)=(3n+1)/2` for odd `n`.

Let the semantic basin of `1` be

`B={n>0 : T^r(n)=1 for some r>=0}`.

A sound finite or analytic certificate set `S` always satisfies `S subset B`.

For `N>0`, write uniquely

`N=2^v m`, `m` odd,

and define `oddcore(N)=m`.

### Theorem A — exact odd-core basin equivalence

For every `N>0`,

`boxed: N in B iff oddcore(N) in B.`

### Proof

The first `v` shortcut steps from `N=2^v m` are forced halvings and land exactly at `m`. Thus `N` reaches `1` iff `m` does.

Classification: **analytic theorem**.

### Corollary A1 — exact dyadic saturation of a finite interval

For

`S_X={1,2,...,X}`

and

`Sat_2(S_X)={2^k n : 1<=n<=X, k>=0}`,

one has

`boxed: Sat_2(S_X)={N>0 : oddcore(N)<=X}.`

The apparent union of infinitely many scaled intervals is therefore not an interval at the integer level. It is exactly an odd-core cutoff.

Classification: **analytic theorem**.

---

## 3. Main no-go theorem — dyadic saturation is neutral for cycles

### Theorem B — dyadic cycle-intersection invariance

Let `C` be any finite periodic orbit of `T`, and let `S` be any set of positive integers. Then

`boxed: C ∩ Sat_2(S) != empty iff C ∩ S != empty.`

### Proof

The reverse implication is immediate because `S subset Sat_2(S)`.

For the forward implication, if `x=2^k s` lies on `C`, then the next `k` iterations are forced even halvings and give

`T^k(x)=s`.

Because `C` is a periodic orbit and hence forward invariant, `s` also lies on `C`.

Classification: **analytic no-go theorem**.

### Consequence B1 — finite verification plus dyadic rays gives no stronger cycle floor

If `[1,X]` is certified blue and a hypothetical cycle has minimum `R>X`, then every cycle state has odd core `>X`. Otherwise a cycle state `2^k m` with `m<=X` would force `m` itself onto the same cycle.

Thus dyadic saturation of the verified interval does not improve the statement `R>X`.

This directly addresses the original “every checked number has an infinite tower of checked-blue doubles” intuition: the tower is real, but for a cycle it folds back onto its base by deterministic halving.

---

## 4. Stronger no-go — arbitrary certified backward trees are also neutral as set traps

For any seed set `S`, define the exact backward closure

`Pre*(S)={x>0 : T^r(x) in S for some r>=0}`.

### Theorem C — backward-closure cycle-intersection invariance

For every periodic orbit `C`,

`boxed: C ∩ Pre*(S) != empty iff C ∩ S != empty.`

### Proof

Again `S subset Pre*(S)`. Conversely, if `x in C` and `T^r(x)=s in S`, forward invariance of the periodic orbit gives `s in C`.

Classification: **analytic no-go theorem**.

### Interpretation

Growing a larger legal certified backward tree remains useful as an **arithmetic recognition device**: if an independent RL theorem forces some actual cycle integer to equal one of the tree nodes, there is an immediate contradiction.

But the backward tree is not, by itself, a stronger set-theoretic trap than its seed. The missing information is an equality-level bridge from genuine RL ownership to a certified node.

This is the exact point where the blue route must acquire new mathematics.

---

## 5. Exact legal backward predecessors

For a known-blue integer `y`, the always-legal even predecessor is `2y`.

An odd predecessor `x` must satisfy

`(3x+1)/2=y`,

so

`boxed: x=(2y-1)/3.`

This is a positive odd integer iff

`boxed: y == 2 (mod 3).`

Classification: **elementary analytic theorem**.

The odd-predecessor rule is genuinely specific to the ordinary `+1` map. For RL79's generalized map

`T_s(n)=(3n+s)/2`

on odd inputs, the corresponding predecessor is

`(2y-s)/3`,

not `(2y-1)/3`.

So the useful part of the backward-basin route does pass the RL79 “must consume `s=1`” red-team.

---

## 6. New analytic infinite family — the LTE blue comb

Start from `2^k` and take `j` consecutive odd predecessors.

Let `Y_0=2^k` and

`Y_r=(2Y_(r-1)-1)/3`.

Solving the affine recurrence gives

`boxed: Y_j = 2^j(2^k+1)/3^j - 1.`

Therefore `Y_j` is an integer exactly when

`3^j | 2^k+1`.

For odd `k`, LTE gives

`boxed: v3(2^k+1)=1+v3(k).`

### Theorem D — LTE blue comb

For every odd `k` and every

`1<=j<=1+v3(k)`, define

`B(j,k)=2^j(2^k+1)/3^j - 1`.

Then:

1. `B(j,k)` is a positive odd integer;
2. its first `j` shortcut steps are odd steps;
3. `T^j(B(j,k))=2^k`;
4. therefore `T^(j+k)(B(j,k))=1`.

Classification: **new analytic basin theorem**.

### Arbitrarily deep analytic branches

For every `j>=1`, choosing any odd `k` divisible by `3^(j-1)` gives

`j<=1+v3(k)`.

Hence there are infinitely many certified-blue integers at every prescribed backward odd depth `j`.

This is substantially stronger than the bare dyadic rays from powers of two.

---

## 7. New analytic “blue mesh” theorem on logarithmic scale

Put

`alpha=log_2(2/3)=1-log_2 3`.

`alpha` is irrational: if `alpha=p/q` were rational, then unique factorization would force an impossible identity between powers of `2` and `3`.

For fixed `j`, take legal odd exponents `k -> infinity` with `3^(j-1)|k`. Then

`B(j,k)=2^(k+j)/3^j * (1+o(1))`,

so

`log_2 B(j,k)=k+j alpha+o(1)`.

Modulo integers, its logarithmic phase therefore approaches

`j alpha (mod 1)`.

The irrational rotation sequence `{j alpha mod1}` is dense on the circle.

### Theorem E — dense certified-blue log phases

The set

`{ frac(log_2 B(j,k)) : k odd, 1<=j<=1+v3(k) }`

is dense in `[0,1)`.

Classification: **new analytic basin theorem**.

### Corollary E1 — arbitrarily fine multiplicative blue meshes

For every `epsilon>0`, there exist finitely many analytically certified blue integers

`b_1,...,b_m`

and a threshold `Y_0` such that every `Y>=Y_0` lies within multiplicative factor `1+epsilon` of some dyadic multiple `2^r b_i`, which is also certified blue.

Equivalently, the analytic basin contains an epsilon-net on the log scale at all sufficiently large scales.

Classification: **analytic corollary**.

### Barrier E2 — proximity is not intersection

The quantifiers are

`for every epsilon >0, there exists Y_0(epsilon), such that ...`.

To force equality with an unknown integer `Y`, one would need an absolute error below `1`, corresponding to `epsilon` of order `1/Y`. Nothing in the theorem gives the self-consistent inequality

`Y >= Y_0(c/Y)`.

For the explicit LTE construction, the depth needed for a fine log-phase net drives legal `k` through divisibility by large powers of `3`, so the threshold grows extremely rapidly as `epsilon` shrinks.

Thus the blue mesh gives a rigorous belt-like structure but not an exact trap.

Classification: **method/quantifier barrier for this architecture**.

---

## 8. Multiplicative interval coverage from a certified finite range

Suppose `[1,X]` is certified and `N>=X`.

Choose the least power of two `p=2^k` such that

`pX>=N`.

Then `p<2N/X`. Put

`m=floor(N/p)`

and

`b=pm`.

Then `1<=m<=X`, so `b` is in the dyadic saturation of the certified interval, while

`b<=N`,

`N-b<p<2N/X`.

Hence

`boxed: b > N(1-2/X).`

Classification: **analytic proximity theorem**.

Using the inherited external verification floor symbolically as `X` can make this relative gap fantastically small. But Theorem B shows why even extreme multiplicative density is not a cycle intersection theorem.

---

## 9. Modular/residue coverage audit

### 9.1 Powers of `2`

Modulo `2^a`, every dyadic ray eventually becomes `0`. This records valuation but loses the odd-core identity. It does not create a new ownership discriminator.

### 9.2 Powers of `3`

For every `b>=1`,

`boxed: ord_(3^b)(2)=2*3^(b-1)=phi(3^b).`

A short LTE proof is available from

`v3(4^m-1)=1+v3(m)`.

Therefore the single certified-blue ray

`1,2,4,8,...`

already hits **every unit residue class modulo `3^b`**.

This is maximal modular coverage and still does not imply that an arbitrary integer in that residue class is blue.

Classification: **analytic modular theorem + method warning**.

### 9.3 Modulus `24`

Any certified interval with `X>=24` already contains a representative of every residue class modulo `24`. Thus residue coverage modulo `24` is completely saturated before dyadic enlargement and cannot by itself distinguish a hypothetical cycle integer.

### 9.4 Full denominator `D=2^A-3^L`

`D` is odd. For any certified base `b`, its dyadic ray modulo `D` is the finite orbit

`{2^k b mod D : k>=0}`.

If `g=gcd(b,D)`, its period divides, and for a unit orbit equals a divisor of,

`ord_(D/g)(2)`.

Hence the dyadic modular shadow is a finite union of multiplicative `2`-orbits/cosets. Congruence of a genuine cycle state to one of these residues is not equality with the certified integer.

If in some branch `D<=X` for a certified interval `[1,X]`, then every residue modulo `D` is already represented by a certified base integer; this makes modular coverage even more obviously non-discriminating without an accompanying size/equality theorem.

### Modular conclusion

No tested modulus supplies the missing exact intersection. The problem is not lack of residue coverage; often coverage is complete. The problem is promotion from a residue shadow to equality with a certified basin node.

---

## 10. Accelerated odd-map translation

For odd `n`, define the accelerated odd map

`U(n)=(3n+1)/2^(v2(3n+1))`.

The dyadic saturation disappears entirely in odd coordinates: basin membership is exactly odd-core membership.

The LTE comb gives a particularly clean accelerated chain. For `j>1`,

`U(B(j,k))=B(j-1,k)`,

because the next value is odd and `v2(3B(j,k)+1)=1`.

At depth one,

`3B(1,k)+1=2^(k+1)`,

so

`U(B(1,k))=1`.

Thus

`B(j,k) -> B(j-1,k) -> ... -> B(1,k) -> 1`

is an exact accelerated-odd certified chain.

Classification: **analytic theorem**.

This shows that the genuinely new basin information is in the odd predecessor tree, not in repeated even doubling.

---

## 11. Mandatory RL ownership/full-phase interaction

RL80 selectively consulted the exact inherited RL50, RL64, RL66 and RL72 interfaces from GitHub.

The key inherited facts are:

1. RL64 terminal all-`11` suffix theorem:
   - if the suffix length is `j>0` and terminal `J_j=2^k`, then
   - `J_0+1=2^j q`,
   - `3^j q=2^k+1`,
   - and `j<=1+v3(k)`.
2. RL50 height-one Collatz conjugacy:
   - at height one, `n=(J-1)/2`;
   - the deterministic odd-preserving synchronized continuation is shortcut Collatz on `n`.
3. RL50's warning:
   - unconstrained height-one synchronized dynamics can simply re-embed Collatz inside the quotient system, so auxiliary Collatz behavior is not automatically a theorem about the original cycle integer.

### Theorem F — terminal all-`11` auxiliary basin capture

Under the RL64 terminal all-`11` hypotheses,

`J_0 = 2^j(2^k+1)/3^j - 1 = B(j,k)`.

Therefore

`boxed: J_0 in B.`

More explicitly, the all-`11` synchronized recurrence on `J` is

`J_(r+1)=(3J_r+1)/2`,

so the exact RL suffix itself is a genuine sequence of ordinary odd Collatz steps

`J_0 -> J_1 -> ... -> J_j=2^k -> ... -> 1`.

Classification: **new analytic synthesis from RL64 + ordinary Collatz**.

### Theorem G — the RL50 coordinate is also blue

Assume `k>=3` and put

`n_0=(J_0-1)/2`.

Then

`boxed: n_0 in B.`

Proof sketch:

- for `j>=2`, `J_0==3 (mod4)`, so `n_0` is odd and one shortcut odd step maps it to `(J_1-1)/2`; repeat until depth one;
- at depth one,
  `J_*=B(1,k)=(2^(k+1)-1)/3`, so
  `n_*=(2^k-2)/3` is even;
- one halving gives `(2^(k-1)-1)/3`, whose next odd step is exactly `2^(k-2)`;
- powers of two then reach `1`.

Classification: **new analytic synthesis**.

### Important limitation

Neither `J_0` nor `n_0=(J_0-1)/2` has been identified as an original positive cycle state.

They are quotient/full-phase auxiliary coordinates. Therefore their basin membership is **not** a contradiction to the existence of a hypothetical RL cycle.

This is the strongest genuinely positive RL80 bridge, but it exposes a new sharply named missing lemma:

# Basin-transfer lemma: relate the basin-captured terminal auxiliary coordinate to an actual owned cycle integer in a basin-preserving way.

No such lemma is currently proved.

---

## 12. Why the all-`11` coincidence is real but limited

For a one-letter synchronized step, RL64's exact identity gives

- `x=1` (`11`): `J'=(3J+1)/2`;
- `x=0` (`00`): `J'=(J+1)/2`.

The `11` transition is literally the ordinary odd shortcut-Collatz branch on `J`.

The `00` transition is **not** the ordinary even branch on `J`; before the terminal first-even exit, `J` is odd.

Therefore an arbitrary mixed synchronized terminal word is not itself an ordinary Collatz trajectory on `J`. The all-`11` suffix is a special exact overlap between RL quotient dynamics and the real Collatz basin.

This explains both the strength and the narrowness of Theorem F.

---

## 13. RL50 conjugacy selector and terminal-exit barrier

At height one put `n=(J-1)/2` with `J` odd.

For a synchronized bit `x`:

- if `x=0`, then `n'=n/2`;
- if `x=1`, then `n'=(3n+1)/2`.

For `n'` to remain an integer, the synchronized bit must satisfy

`boxed: x == n (mod2),`

or equivalently

`boxed: J == 1+2x (mod4).`

Under this exact selector, the next `J'=2n'+1` remains odd.

Therefore any synchronized block whose defining event is the **first even `J` exit** must violate the integer Collatz selector at that exit edge.

For a terminal all-`11` suffix, the final input before `J=2^k` is in fact `1 mod4`, while `x=1` would require `3 mod4` for the `n`-coordinate conjugacy to continue through that edge.

This is why Theorem G's real Collatz trajectory on `n` diverges from the synchronized quotient continuation at the last edge and takes a different path to a power of two.

Classification: **new analytic method barrier / coordinate clarification**.

---

## 14. RL79 generalized-map red-team

The session distinguishes two layers.

### Pure dyadic layer

The statement

`n blue => 2^k n blue`

uses only the even halving branch. The same formal ray propagation exists for every generalized `T_s` because the even branch is unchanged.

Therefore pure dyadic saturation is exactly the kind of structure RL79 warned is too insensitive to the unit increment.

### Odd-predecessor / basin layer

The formula

`(2y-1)/3`

uses the absolute `+1` and changes to `(2y-s)/3` under `T_s`.

A tiny exact negative control is

- ordinary Collatz: `5 -> 8 -> 4 -> 2 -> 1`;
- generalized `T_5`: `5 -> 10 -> 5`.

Thus the analytic LTE comb and the RL64 all-`11` basin capture are genuinely ordinary-Collatz (`s=1`) facts.

Classification: **exact analytic discrimination**.

---

## 15. Exact finite verification added in RL80

`verification/verify_rl80_blue_basin.py` audits, without serving as proof of the infinite theorems:

- `131,072` odd-core/dyadic-saturation equivalence checks;
- `227` LTE blue-comb instances;
- `226` RL50 auxiliary-blue instances;
- primitive-root order checks for `3^b`, `1<=b<=8`;
- `99,752` multiplicative-density bound instances;
- the exact `s=1` versus `s=5` negative control.

Fresh output:

`RL80 blue-basin verifier: PASS`.

Classification: **exact finite audit/falsification evidence**.

---

## 16. External certificates retained, not re-audited

The inherited RL50/RL72 ledger accepts Barina's peer-reviewed verification through `2^71` as a stable external computational floor.

RL80 does not re-audit that external computation and does not need its numerical value for the main analytic theorems. Whenever a finite verified interval is mentioned, the results are stated symbolically in `X`.

Classification: **externally inherited certificate, unchanged**.

---

## 17. Correction / demotion ledger additions

Retain all RL72–RL79 corrections and add:

1. **Pure dyadic-belt closure demoted.** Dyadic saturation is cycle-intersection neutral.
2. **Finite verified-range dyadic saturation demoted as a new cycle floor.** It is exactly an odd-core cutoff and gives no more than the cycle minimum bound.
3. **Backward-tree abundance demoted as a standalone trap.** `Pre*(S)` intersects a periodic orbit iff `S` already does; arithmetic recognition remains potentially useful.
4. **Modular blue coverage demoted without size/equality control.** Coverage can be total, especially modulo `3^b`, without implying basin membership of a candidate integer.
5. **Multiplicative/logarithmic proximity demoted as closure.** RL80 proves an arbitrarily fine analytic blue mesh, but relative proximity is not integer equality.
6. **New analytic basin family promoted.** The LTE comb `B(j,k)` gives arbitrarily deep, rigorously certified ordinary-Collatz backward branches.
7. **New RL-specific auxiliary basin capture promoted.** RL64 terminal all-`11` `J_0` and RL50 `n_0=(J_0-1)/2` are certified blue under the stated hypotheses.
8. **Auxiliary-coordinate warning strengthened.** Basin membership of quotient coordinates is not basin membership of an original cycle state.
9. **New missing lemma named.** A viable continuation of the blue route needs a basin-preserving transfer/equality theorem from full-phase auxiliary coordinates to a genuine cycle integer.

No prior closed radius-3 or Gate-A theorem is affected.

---

## 18. Exact proof state after RL80

### New proved analytic mathematics

- odd-core basin equivalence;
- exact dyadic saturation of `[1,X]`;
- dyadic cycle-intersection invariance;
- arbitrary backward-closure cycle-intersection invariance;
- legal odd-predecessor criterion;
- LTE blue-comb theorem;
- dense certified-blue logarithmic phases;
- arbitrarily fine multiplicative blue-mesh corollary;
- finite-interval multiplicative proximity bound;
- primitive-root/full-unit coverage modulo powers of `3`;
- accelerated-odd form of the blue comb;
- terminal all-`11` auxiliary `J` basin capture;
- RL50 auxiliary `n=(J-1)/2` basin capture for `k>=3`;
- exact height-one Collatz-selector / terminal-exit barrier.

### Exact finite certificate/audit added

- RL80 verifier counts listed in Section 15.

### Externally inherited certificate

- stable finite verification floor retained exactly as inherited; not re-audited.

### Computational evidence only

- no computational observation is promoted to an infinite theorem beyond the exact verifier's audit role.

### Conjectures/open obligations

- no basin-transfer lemma from auxiliary `J`/`n` to an original cycle state is known;
- no equality-level theorem forces a genuine RL state into the certified backward tree;
- mixed/all-`00` terminal synchronized tails are not analytically basin-captured by the all-`11` argument.

### Global closure state

Unchanged:

- radius-3 primitive/full-`D`: **closed local obstruction**;
- Gate A even `k`: **closed analytically**;
- Gate A `k<=25`: **closed by exact finite-certificate corollary**;
- Gate A odd `27<=k<=165`: **open**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

---

## 19. Route decision and RL81 selection

RL80 does not recommend spending another session merely generating more blue rays, residue coverage, density bounds, or finite backward-tree nodes. Those mechanisms are now structurally understood.

The most promising live continuation created by RL80 is the exact all-`11` auxiliary basin capture.

RL81 should therefore test:

# **Can full-phase ownership transfer the certified basin status of terminal all-`11` auxiliary coordinates to an actual cycle integer?**

The attack should be quick to kill if the exact RL48 reconstruction proves such a transfer impossible. If it dies, the blue route should be frozen as a barrier result and the programme should return to RL79's other non-homogeneous `s=1`/unit-lattice route rather than expanding basin numerics.
