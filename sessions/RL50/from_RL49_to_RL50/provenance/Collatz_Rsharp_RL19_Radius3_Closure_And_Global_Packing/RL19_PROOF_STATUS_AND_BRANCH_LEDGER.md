# RL19 proof-status and radius-3/global ledger

## Evidence labels

- **ANALYTIC** — proved in the written chain by elementary algebra/number theory.
- **EXTERNAL: LMN** — invokes the published Laurent–Mignotte–Nesterenko two-logarithm theorem.
- **EXACT FINITE CERTIFICATE** — finite exhaustive arithmetic/combinatorial check after an analytic finite reduction.
- **EXTERNAL COMPUTATIONAL INPUT** — inherited external computational bound, explicitly not an analytic theorem.
- **COMPUTATIONAL EVIDENCE** — exploratory/search evidence only; not part of a proof.
- **OPEN** — genuine missing theorem.

## Exact radius-3 state

The RL18 repaired ledger is retained for every previously closed branch. RL19 changes only the final one-orbit cubic leaf.

| Direction/gcd sector | support/canonical sector | RL19 status | Evidence |
|---|---|---|---|
| connected same-direction | `[3]` | CLOSED (RL10) | ANALYTIC |
| mixed direction | disconnected `[2,1]`, `[1,1,1]` | CLOSED (RL11) | ANALYTIC + EXTERNAL: LMN + EXACT FINITE CERTIFICATE |
| same direction, coprime, `j=0,P3` | strict `[1,1,1]` | CLOSED; RL18 provenance repair retained | ANALYTIC + EXTERNAL: LMN + EXACT FINITE CERTIFICATE |
| same direction, coprime, `j=0,P3` | coefficient-5 `[2,1]` boundary | CLOSED (RL16) | ANALYTIC + EXTERNAL: LMN + CF + EXACT FINITE CERTIFICATE |
| same direction, coprime, `j=1,P2` | strict `[1,1,1]` | CLOSED (RL14) | ANALYTIC |
| same direction, coprime, `j=1,P2` | coefficient-3 `[2,1]` boundary | CLOSED (RL18) | ANALYTIC |
| same direction, coprime, `j=1,P3` | strict `[1,1,1]` | CLOSED (RL15) | ANALYTIC + EXTERNAL: LMN + EXACT FINITE CERTIFICATE |
| same direction, coprime, `j=1,P3` | coefficient-5 `[2,1]` boundary | CLOSED (RL16) | ANALYTIC + EXTERNAL: LMN + CF + EXACT FINITE CERTIFICATE |
| same direction, coprime, `j=2,P2` | strict `[1,1,1]` | CLOSED (RL16) | ANALYTIC + EXTERNAL: LMN + EXACT FINITE CERTIFICATE |
| same direction, coprime, `j=2,P2` | coefficient-3 `[2,1]` boundary | CLOSED (RL18) | ANALYTIC + EXTERNAL: LMN + CF + EXACT FINITE CERTIFICATE |
| same direction, `gcd(A,L)=1,gcd(A,m)=3` | three-orbit sector | CLOSED; RL18 repair retained | ANALYTIC + EXTERNAL: LMN + EXACT FINITE CERTIFICATE |
| same direction, `gcd(A,L)=3,gcd(A,m)=3` | three-orbit cubic sector | CLOSED for primitive words (RL18) | ANALYTIC + EXTERNAL: LMN + CF + EXACT FINITE CERTIFICATE |
| same direction, `gcd(A,L)=3,gcd(A,m)=1` | one-orbit cubic sector | **CLOSED for primitive words (RL19)** | **ANALYTIC** on top of RL10 + RL17 reductions |

### RL19 final-leaf theorem

Under

`A=3a`, `L=3ell`, `gcd(a,ell)=1`, `gcd(3a,m)=1`, `ap-mell=1`,

and the genuine RL10 one-orbit radius-3 geometry, a full-`D` sparse zero

`1+3rho^u+9rho^(u+v)=0`, `u+v+w=3a`,

cannot occur for a primitive word.

The proof is in `RL19_CUBIC_SKEW_ANALYTIC_CLOSURE.md` and has four exhaustive pieces:

1. exact weak interlacing of the three jumps with their inverse-step translate;
2. one-gap-`a` boundary killed by the short-order obstruction `rho^h!=1 (mod C)` for `0<|h|<a`;
3. all remaining `max gap<2a` skew triples killed by an Eisenstein lift with norm/integer size `<C`;
4. the only extreme sectors (`k=1` and `k=3`) killed by nonzero resultants of absolute value `<C`.

Equal gaps force an `a`-periodic jump indicator, hence an `a`-periodic orbit-coordinate bit word and therefore nonprimitivity.

The old `a<=80` scan remains **COMPUTATIONAL EVIDENCE** and is not used in the closure.

### Radius-3 conclusion

**Subject to the inherited RL7--RL17 hypotheses and the explicitly retained external dependencies in the older branches, exact radius 3 is now CLOSED for primitive `D`-divisible self-rotations.**

This is not an RL contradiction.

---

## Global RL state

### Bounded-radius bridge status

The route

> proved least-root/final-return local grammar alone forces a distinguished rotation pair to radius `<=3`

is **not proved**. RL19 found an in-session length-184 local-grammar countermodel suggesting the implication is false under the local package, but the exact word/certificate was not frozen to disk before closeout.

Status: **COMPUTATIONAL/SESSION EVIDENCE AGAINST THE BRIDGE; FORMAL FALSIFICATION NOT YET FROZEN.**

The next session should reconstruct and preserve the smallest exact countermodel before citing the bridge as retired. In all cases, such a local model is not a counterexample to RL because it does not establish the global `D|Q` cycle condition.

### RL18 arbitrary-radius orbit identity

Retained **ANALYTIC**:

`D|Q` is equivalent modulo `D` to the RL18 shift-orbit polynomial vanishing.

### RL19 exact positive lift and weighted-difference identity

New **ANALYTIC** identities for an actual positive cycle word:

`Z=sum_i 2^i 3^(-P_i)=(lambda-1)(4R+1)`,

and for rotation `m`,

`sum_i q_i(3^(-G_i)-1)=4(lambda-1)(R_m-R)`.

Consequences:

- positivity/sign of the entire raw `Z` lift cannot itself be the global obstruction; its positive quotient is exactly known;
- a viable unbounded-radius route must use a proper factor/resultant, a weighted difference, or additional state/ownership structure.

### RL19 weighted populations and state packing

New **ANALYTIC** identities:

`sum_(d_i=1) q_i = 3R(lambda-1)`,

`sum_(d_i=0) q_i = (R+1)(lambda-1)`.

At the least state `R#`, distinct parity-separated phase states give

`3 D/2^A <= sum_(j=0)^(L-1) 1/(R#+2j)`,

hence

`D/2^A <= 1/(3R#)+(1/6)log(1+2(L-1)/R#)`.

So for any `epsilon>0`, either `D/2^A<epsilon` (near resonance) or

`L >= 1+(R#/2)(exp(6epsilon-2/R#)-1)`.

Conditional on the inherited **EXTERNAL COMPUTATIONAL INPUT** `R#>=2^71`, for example:

- `D/2^A>=1/16` forces `L>0.22749 R# >2^68.86`;
- otherwise `2^A/3^L<16/15`.

This is a genuine radius-independent necessary dichotomy, not a contradiction.


### RL19 odd-step product strengthening

New **ANALYTIC** identity for an actual positive cycle:

`lambda = prod_(d_i=1) (1+1/(3x_i))`.

At the least state `R#`, the distinct odd phase states satisfy `x_(j)>=R#+2j`, hence

`log lambda <= sum_(j=0)^(L-1) log(1+1/(3(R#+2j)))`

and therefore

`log lambda <= 1/(3R#)+(1/6)log(1+2(L-1)/R#)`.

Equivalently,

`L >= 1+(R#/2)(lambda^6 exp(-2/R#)-1)`.

This strictly strengthens the earlier `D/2^A` packing bound because `1-1/lambda < log lambda` for `lambda>1`. It still gives only a near-resonance/huge-length dichotomy, not an RL contradiction.

---

## Distances that must remain separate

### Distance to exact radius-3 closure

**Closed**, subject to the inherited audited case tree and its older explicit dependencies.

### Distance to an actual RL contradiction

**Still OPEN and substantial.** Closing radius 3 removes one local possibility but no theorem forces an RL object to encounter radius 3. The best new global result is the strengthened odd-step-product/least-state packing dichotomy above.

The next serious target is to combine the near-resonant branch with additional RL-specific structure, or derive a proper-factor/resultant obstruction from the arbitrary-radius weighted difference. Do not start a radius-4/5 cutoff ladder unless a theorem makes bounded radius globally relevant.
