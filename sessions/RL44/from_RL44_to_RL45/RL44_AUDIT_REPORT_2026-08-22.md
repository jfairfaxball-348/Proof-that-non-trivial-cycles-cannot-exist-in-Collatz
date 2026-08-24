# RL44 Audit/Review Report

Date: 2026-08-22

## Executive conclusion

The RL43 handover is reproducible and, after skeptical review, its retained theorem-level claims survive. The outer SHA-256 matches, the internal manifest verifies, the inherited RL42->RL43 zip checksum matches, and all four RL43 verifiers pass from a fresh extraction. The retained RL42 verifier suite also reruns cleanly.

No RL43 theorem is invalidated by this audit. The main corrections are interpretive rather than destructive:

1. the one-excursion `e<=40` phase computation can now be promoted from "audit pending" to an **exact reproducible finite certificate**, but not to an analytic theorem;
2. the `t=6` normalized geometry begins at `e=35`, not `e=37`;
3. the radius-3 bridge is genuine at the level of the common short binomial `3T^q-2`, but RL19 and RL43 do **not** yet have comparable resultant-size regimes, because RL19 works modulo the large cubic cofactor `C=X^2+XY+Y^2`, whereas RL43 must beat the much smaller factor `X-Y`.

RL remains open, and the surviving near-resonant order-2 / `g=2` balanced-return branch remains open.

## 1. Reproducibility and integrity

Verified:

- outer bundle SHA-256:
  `95a9133ad83943cdd3df2a8c2b4927c5741cbdeeea5b86b13291cef5675d8ddc`;
- every file listed in the RL43 `SHA256SUMS.txt` manifest;
- inherited `Collatz_Rsharp_RL42_to_RL43_Handover_2026-08-22.zip` checksum;
- `verification/run_all_rl43_verifiers.sh`:
  - rho=49 elimination: PASS;
  - defect-support/radius-3 bridge: PASS;
  - cutoff-free gap-9 automaton: PASS;
  - full-denominator phase bridge: PASS;
- retained RL41/RL42 verifier suite: PASS, including the inherited `rho>=49` frontier.

The heavy phase scan was rerun in split form. All four normalized geometry families reproduce the recorded exact residue counts and all required-residue hits are false through `e=40`.

## 2. Proof-state ledger after RL44 audit

| Claim | Audit status | Comments |
|---|---|---|
| `D_E/3^p < 2^(e+1)` and crossing gap `g<2^(e+1)` | **Analytically proved** | Direct from `z=h-p<=e+1` and the geometric-series bound. |
| synchronization cost `e>=floor(c log_2 3)` | **Analytically proved** | Immediate from the previous inequality and `3^c|g`. |
| defect support `support(U-V)<=4(E+N)` before collection | **Analytically proved** | Each local word has at most `z<=e+1` 1-runs in a canonical excursion; each run gives two monomials. |
| `rho!=49`, hence retained frontier `rho>=50` | **Analytic reduction + exact finite certificate** | The equality-case reduction is exhaustive in the retained branch; all endpoint survivors are eliminated by exact effective-mass comparisons. |
| gap-9 crossing theorem `e>=8` | **Analytic infinite-length reduction + exact finite certificate** | At fixed excess the quotient graph is finite after identifying the unique neutral `(d,T)=(1,-2)` `11` self-loop. No hidden weight/length cutoff remains. |
| one-excursion full-denominator phase relation `P(rho)=0 mod (X-Y)` | **Analytically proved** | The RL21 two-factor decomposition, Bezout phase conversion, run compression and exponent positivity check out. |
| `3 rho^(a-ell)=2 mod (X-Y)` | **Analytically proved** | Direct quotient of `rho^a=1/3` and `rho^ell=1/2`. |
| `0 != Res(3T^q-2,P)` and `X-Y` divides it | **Analytically proved** | Divisibility follows from the common residue root; nonvanishing follows from irreducibility and positivity at the positive real root. |
| `|Res(3T^q-2,2T^ell-1)|=2^a-3^ell` | **Analytically proved** | Coprime-binomial resultant identity with `gcd(q,ell)=1`. |
| one-excursion no phase solution for `26<=e<=40` | **Exact finite computational certificate** | Geometry exhaustion and residue DP were audited and rerun. This yields the computational frontier `e>=41`, and nothing stronger. |
| `e >= (a-ell)+2`, equivalently `rho_E>=a` | **Conjectural** | Survives finite red-team through `e<=40`, but no proof. |

## 3. Independent audit of `rho>=50`

The `rho=49` reduction is logically closed inside the retained branch.

The key points are:

- `rho=P+E=49` and each excursion weight satisfies `p<=P<=49`, so the bounded `p<=49` no-`e<=3` crossing certificate is sufficient; there is no hidden need for an unbounded crossing classification.
- The exact effective-mass lower bound gives `P_+>=43`.
- The mandatory crossing has `e>=4`, giving `P<=45` and leaving only `(P,E)=(45,4),(44,5),(43,6)`.
- The sign restrictions used by the three DPs follow from the same strict effective-mass inequality.
- In the `E=4` case the unique crossing must be positive-to-negative and all other excursions have `e=0`.
- In the `E=5,6` all-positive cases, after the unique crossing at most two excess units remain, so the exact local `e<=2` catalogue is sufficient.
- The synchronized-run step is a safe over-approximation, not an under-enumeration: allowing every odd-count `c=0,...,v2(raw)` can only add false candidates.
- All surviving near-resonant endpoints are eliminated by exact integer comparisons against the effective-mass lower bound.

Conclusion: **`rho>=50` is certified only in the inherited surviving near-resonant order-2 / `g=2` balanced-return branch. It must not be stated globally.**

## 4. Cutoff-free gap-9 theorem

The finite-state claim is sound.

The exact transition is

`T'=[3^y T + x 3^(d+y-1)-y]/2`,

with excess update `e'=e+d-x`.

Every transition has nonnegative excess cost. The only zero-cost internal transition is `11` at `d=1`; there

`phi(T)=(3T+2)/2`,

and

`phi^k(T)=3^k(T+2)/2^k-2`.

Hence a zero-cost run is finite unless `T=-2`, in which case it is the exact neutral self-loop. Height `d` itself costs at least `d(d-1)/2` excess. Therefore the graph below a fixed excess ceiling is finite after quotienting that one loop.

The first crossing from incoming gap 9 occurs at `e=8`, preterminal `T=7`, giving outgoing gap 4. Thus **the theorem `e>=8` is genuinely cutoff-free**.

## 5. Defect-support compression

The claimed `4(E+N)` support bound is valid as a pre-collection bound.

For one canonical excursion, `rho>=h-1` gives `z=h-p<=e+1`. In the positive orientation, one local word begins with zero and the other ends with zero, so each has at most `z` maximal 1-runs. Each run contributes exactly two signed `2^r3^s` monomials. Thus the local difference uses at most `4z<=4(e+1)` terms. Summing over excursions gives `4(E+N)`.

No sharper universal bound was proved in this audit. A factor-of-two improvement would require additional cancellation or a joint-run structural theorem; it is not automatic from the current argument.

## 6. Full-denominator phase bridge

The RL43 repair of the earlier proper-factor-only bridge is sound.

RL21 gives the exact coprime factor decomposition

`X-Y | U+V`,

`X+Y | U-V`.

In the live one-excursion `G=4` branch, `U-V=(X+Y)4` implies

`Q(uv)=(X+Y)(V+4Y)`,

hence full `D` divisibility is equivalent to

`X-Y | V+4Y`.

The Bezout phase unit `rho` satisfies

`rho^a=1/3`, `rho^ell=1/2 (mod X-Y)`,

and every run of `k` ones contributes

`3(rho^b-rho^c)`, with `c-b=kq`, `q=a-ell`, and `0<b<c`.

Therefore

`P(T)=4+3 sum(T^b-T^c)`

has at most `2e+3` terms and satisfies `P(rho)=0 mod (X-Y)`.

The shorter binomial

`f(T)=3T^q-2`

also vanishes at `rho`, and the resultant is nonzero.

This is a genuine bridge to the **same binomial anchor** as RL19. It is not yet a closure theorem.

## 7. Line-by-line RL19 comparison and the exact missing lemma

The relevant RL19 `k=1` extreme-sector proof has this structure:

1. derive `r=a-ell` and `3rho^r=2`;
2. use radius-3 interlacing geometry to write `u=r+x`, `v=r+y` with `n=x+y<=ell-r`;
3. convert the sparse zero to `g(T)=1+2T^x+4T^n`;
4. obtain a common modular root of `f(T)=3T^r-2` and `g(T)` modulo the cubic cofactor `C=X^2+XY+Y^2`;
5. prove the resultant is nonzero;
6. use `|alpha|=(2/3)^(1/r)<1` to get `|Res(f,g)|<3^n 7^r`;
7. use `n<=ell-r` to show the nonzero resultant is strictly smaller than `C`, contradicting `C|Res`.

RL43 reproduces steps 1, 4 and 5 in a new setting and replaces the radius-3 trinomial by the defect-controlled paired phase polynomial `P`.

The missing analogue of RL19 steps 6-7 is **not merely a support bound**. Two extra difficulties remain:

- the determinant exponents `b,c` can be much larger than `ell` even when support is small;
- the divisor is now `M=X-Y`, potentially far smaller than the radius-3 cubic cofactor `C~X^2`.

A precise sufficient replacement is the following.

### RL45 resultant-benchmark target

Let

`f(T)=3T^q-2`, `q=a-ell`,

`P(T)=4+3 sum_r(T^(b_r)-T^(c_r))`,

with the full admissible one-excursion constraints, and let

`R=Res(f,P)`.

Because `gcd(3,M)=1` and `M|R`, also `M` divides the 3-free part

`R_(3') := R / 3^v3(R)`.

The exact comparison polynomial `L(T)=2T^ell-1` satisfies

`|Res(f,L)|=M`.

Thus a theorem of the form

> `0 < |R_(3')| < |Res(f,L)| = X-Y`

would close the one-excursion phase branch immediately.

The pairing identity

`c_r-b_r=k_r q`

should be used essentially. Modulo `f`, each pair collapses to one residue class modulo `q`:

`3(T^b-T^(b+kq)) = [2^s(3^k-2^k)/3^(s+k-1)] T^r`

when `b=sq+r`, `0<=r<q`.

So the phase relation can be reduced to degree `<q` with positive rational coefficients. The unresolved quantity is the resulting coefficient/height growth. This is the sharpest formulation of the missing radius-3 transplant lemma found in the audit.

## 8. Audit of the one-excursion `e<=40` computation

The quotient-state geometry was reconstructed independently with exact integer near-resonance tests.

After quotienting the exact neutral `(d,T)=(1,-2)` `11` pump and imposing:

- the one-excursion endpoint geometry;
- near resonance;
- `gcd(a,ell)=1`;
- inherited `rho>=50`;
- exact effective-mass feasibility;

there are exactly four normalized families through `e=40`, all at `(a,ell,q)=(65,41,24)`:

- `(z,t,g_out)=(24,0,4)` for `e=26..40`;
- `(22,2,16)` for `e=30..40`;
- `(20,4,64)` for `e=34..40`;
- `(18,6,256)` for `e=35..40`.

The `t=6` onset at `e=35` is confirmed.

The residue DP was code-audited and rerun. Its initialization and updates match the exact global half-word numerator `V`; the terminal `10` contributes no beta term, and synchronized trailing zeros contribute nothing. All recorded residue counts reproduce and no residue equals

`-4*3^41 mod (2^65-3^41)`.

Therefore the correct status is:

> **Exact finite certificate: no admissible one-excursion solution with `e<=40`; hence computational frontier `e>=41`.**

This is not a proof for `e>=41` and is not evidence for an eventual finite cutoff theorem by itself.

## 9. Red-team of the `J_d/K` candidate

Define

`H=e-z+1`,

`J_d=T+3^d-2^d`,

`K=H+d(d+1)/2-1`.

The exact transition laws are:

- `00`:
  `J_d'=(J_d+3^d-2^d)/2`, `K'=K+d-1`;
- `11`:
  `J_d'=(3J_d+2^d-1)/2`, `K'=K+d-1`;
- `01`:
  `J_(d+1)'=(3J_d+3^(d+1)-2^d-1)/2`, `K'=K+2d`;
- `10`:
  `J_(d-1)'=J_d/2`, `K'=K-1`.

An independent state exploration retaining `H` found no violation of

`2^K | J_d  =>  J_d/2^K <=1`

through `e<=40` (1,311,072 reachable `(d,e,T,H)` states checked).

This remains evidence only.

A useful red-team result is that the tempting stronger invariant

`J_d <= 2^K`

is **false**. A reachable counterexample appears at

`(d,e,T,H,K,J)=(1,30,4858,12,12,4859)`.

So a proof cannot simply replace the divisibility-conditioned statement by an unconditional size bound.

### Strong simplification of the proof target

Any counterexample to the candidate at height `d>1` can be followed by `d-1` compatible `10` descents. Divisibility by `2^K` guarantees the needed parity at every descent; `J` is halved and `K` drops by one each time, so the normalized quotient `J/2^K` is preserved.

Therefore it is enough to prove the **terminal height-one statement**.

At `d=1`,

`J_1=T+1`, `K=H`,

so the needed theorem becomes

> `2^H | (T+1)  =>  (T+1)/2^H <=1`.

For the actual one-excursion terminal geometry, `T+1=2^(t+3)`, so this reduces exactly to

`H>=t+3`.

Because

`H=e-z+1=rho_E-h+1`,

this is equivalent to the particularly clean valuation inequality

> **`v2(D_E-9*3^p) <= rho_E`.**

Indeed `D_E-9*3^p=2^h g_out`, and `g_out=4*2^t` in the retained one-excursion branch.

Under the exact proper-factor identity `D_E=2^a+3^ell` with `p=ell-2`, the left side is exactly `a`. Therefore this local valuation theorem would immediately imply

> **`rho_E>=a`, equivalently `e>=q+2`.**

This terminal valuation formulation is a sharper RL45 proof target than the original all-state invariant.

## 10. External and inherited dependencies

The RL43 results audited here do not invoke an unresolved conjecture.

Relevant inherited facts include the RL21 balanced two-factor decomposition, the retained order-2 / `g=2` near-resonant branch framework, the RL42 prefix cap/effective-mass theorem, and the inherited `rho>=49` certificate.

The specific RL19 cubic-skew `k=1` argument used for comparison explicitly states that it uses **no LMN theorem and no finite cutoff**.

Elsewhere in the wider project, two external classes remain explicitly external and must stay labelled as such:

- the inherited computational minimum-state floor `R>=2^71` where it is used;
- older radius-3 leaves that explicitly depend on the published Laurent-Mignotte-Nesterenko two-logarithm theorem.

Neither should be silently imported into the new RL43 one-excursion phase theorem.

## 11. How close is the radius-3 bridge?

The correct assessment is:

- **structurally much closer:** arbitrary-radius one-excursion transport now produces the same short binomial `3T^q-2` as the closed RL19 `k=1` radius-3 sector, and the second full-denominator factor is no longer missing;
- **not yet quantitatively closed:** radius 3 had a tiny positive trinomial plus a strong degree bound and divisibility by a large cubic cofactor; RL43 has defect-controlled support but potentially large determinant exponents and divisibility only by `X-Y`;
- **one major theorem away in the one-excursion branch, not one calculation away:** either a uniform terminal valuation theorem or a new resultant uniqueness/height estimate is needed.

The bridge is therefore mathematically genuine, but "same binomial" should not be confused with "same proof already applies."

## 12. Ranked RL45 road map

### Priority 1 — terminal valuation / transport theorem

Attack

`v2(D_E-9*3^p) <= rho_E`

for every canonical positive gap-9 excursion, or at least for every physically terminating one-excursion return.

Equivalent automaton form at `d=1`:

`v2(T+1) <= H` whenever `T+1>0` is the required terminal power of two.

This is the highest-leverage target because the live branch then gives `v2(D_E-9*3^p)=a`, hence `rho_E>=a` immediately. Work terminal-first; a proof of the stronger all-state `J/K` statement is optional, not necessary.

### Priority 2 — radius-3 resultant benchmark theorem

Exploit `c-b=kq` to reduce the phase polynomial modulo `3T^q-2`, track the 3-free resultant rather than its raw high-degree size, and try to prove

`0<|Res(3T^q-2,P)|_(3') < X-Y`.

The exact comparator `2T^ell-1` should be built into the proof from the start, because its resultant is exactly `X-Y`.

### Priority 3 — multi-excursion full-denominator phase compression

Generalize the RL43 `X-Y` phase relation from one excursion to `N>1`, with support/height controlled by `E+N`. Determine whether synchronized blocks only introduce unit phase shifts and whether each excursion still contributes paired exponents separated by multiples of `q`.

This is necessary for full branch closure unless another theorem forces `N=1`.

### Do not prioritize

Do not merely extend the phase cutoff `e=40` to 41, 42, ... unless the computation is explicitly used to test the terminal valuation theorem, identify a minimal counterexample, or discover a new invariant.

## Final audit verdict

**Clean with calibrated interpretation.**

Definitely proved/certified after RL44:

- retained `rho>=50`;
- cutoff-free gap-9 `e>=8`;
- defect-support compression `<=4(E+N)`;
- one-excursion full-denominator phase bridge and nonzero short-binomial resultant;
- exact one-excursion computational exclusion through `e=40`.

Still conjectural:

- `e>=q+2` / `rho_E>=a`;
- the original `J_d/K` invariant;
- any uniform resultant-size/uniqueness theorem sufficient to beat `X-Y`;
- the multi-excursion full-denominator phase generalization.

Highest-leverage next theorem:

> **Gap-9 terminal valuation theorem:** `v2(D_E-9*3^p) <= rho_E`.

A proof would convert the current computational pattern into the desired cutoff-free transport bound in one step.
