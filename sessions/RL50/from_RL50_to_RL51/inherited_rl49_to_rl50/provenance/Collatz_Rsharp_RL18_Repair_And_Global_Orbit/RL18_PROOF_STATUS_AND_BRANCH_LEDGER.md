# RL18 proof-status and radius-3 branch ledger

## Evidence labels

- **ANALYTIC** — proved in the written chain by elementary algebra/number theory.
- **EXTERNAL: LMN** — invokes the published Laurent–Mignotte–Nesterenko theorem on two logarithms.
- **EXACT CERTIFICATE** — finite exhaustive arithmetic/combinatorial check after an analytic finite reduction.
- **COMPUTATIONAL EVIDENCE** — search only; not part of a proof.
- **OPEN** — a genuine missing theorem.

## Repaired inherited items

| Item | RL18 status | Evidence |
|---|---|---|
| RL7–RL10 local transposition structure | retained | ANALYTIC / inherited |
| RL11 mixed-direction closure | retained | ANALYTIC + EXTERNAL: LMN + EXACT CERTIFICATE |
| RL12 coprime three-orbit same-direction closure | **repaired** | ANALYTIC denominator theorem + EXTERNAL: LMN + inherited EXACT CERTIFICATE |
| RL13 `j=0,P3` strict interior | **repaired** | ANALYTIC near/far resultant bounds + EXTERNAL: LMN + inherited EXACT CERTIFICATE |
| RL14 `j=1,P2` strict interior | retained | ANALYTIC / inherited |
| RL15 `j=1,P3` strict interior | retained | ANALYTIC + EXTERNAL: LMN + EXACT CERTIFICATE |
| RL16 coefficient-5 P3 boundaries | retained after RL17 audit | ANALYTIC + EXTERNAL: LMN + CF + EXACT CERTIFICATE |
| RL16 `j=2,P2` strict interior | retained after RL17 audit | ANALYTIC + EXTERNAL: LMN + EXACT CERTIFICATE |
| coefficient-3 P2 boundary, `j=1` | **CLOSED in RL18** | ANALYTIC elementary resultant |
| coefficient-3 P2 boundary, `j=2` | **CLOSED in RL18** | ANALYTIC resultant barrier + EXTERNAL: LMN + CF + EXACT CERTIFICATE |
| `gcd(A,L)=3,gcd(A,m)=3` | **CLOSED for primitive words in RL18** | ANALYTIC P2 reduction + EXTERNAL: LMN + CF + EXACT CERTIFICATE; sole arithmetic zero is `(10)^3` |
| `gcd(A,L)=3,gcd(A,m)=1` | **OPEN** | full-`D` sparse reduction proved; infinite skew uniqueness missing |
| radius-3 exclusion => RL contradiction | **OPEN / absent** | needs a global bridge |

## Authoritative radius-3 branch ledger

| Direction/gcd sector | support/canonical sector | Status after RL18 |
|---|---|---|
| connected same-direction | `[3]` | CLOSED (RL10) |
| mixed direction | disconnected `[2,1]`, `[1,1,1]` | CLOSED (RL11) |
| same direction, coprime, `j=0,P3` | strict `[1,1,1]` | CLOSED; proof provenance repaired here |
| same direction, coprime, `j=0,P3` | coefficient-5 `[2,1]` boundary | CLOSED (RL16) |
| same direction, coprime, `j=1,P2` | strict `[1,1,1]` | CLOSED (RL14) |
| same direction, coprime, `j=1,P2` | coefficient-3 `[2,1]` boundary | **CLOSED (RL18, elementary)** |
| same direction, coprime, `j=1,P3` | strict `[1,1,1]` | CLOSED (RL15) |
| same direction, coprime, `j=1,P3` | coefficient-5 `[2,1]` boundary | CLOSED (RL16) |
| same direction, coprime, `j=2,P2` | strict `[1,1,1]` | CLOSED (RL16) |
| same direction, coprime, `j=2,P2` | coefficient-3 `[2,1]` boundary | **CLOSED (RL18)** |
| same direction, `gcd(A,L)=1,gcd(A,m)=3` | three-orbit sector | CLOSED; proof provenance repaired here |
| same direction, `gcd(A,L)=3,gcd(A,m)=1` | one-orbit cubic sector | **OPEN: full-`D` skew sparse uniqueness** |
| same direction, `gcd(A,L)=3,gcd(A,m)=3` | three-orbit cubic sector | **CLOSED for primitive words (RL18)** |

Subject to the inherited RL7–RL16 case-tree hypotheses audited in RL17, this leaves one exact-radius-3 arithmetic leaf.

## Remaining radius-3 theorem

Let

`A=3a`, `L=3ell`, `gcd(a,ell)=1`, `gcd(3a,m)=1`,

and let integers `p,m` satisfy

`a p - m ell = 1`.

Put

`D=2^(3a)-3^(3ell)`, `rho=2^m 3^(-p) (mod D)`.

For positive gaps `u+v+w=3a`, the inherited/full-`D` reduction gives

`1 + 3 rho^u + 9 rho^(u+v) = 0 (mod D)`.

**Open target:** under the genuine rotation-geometry hypotheses, prove this implies

`u=v=w=a`.

The equal-gap case then collapses to the known nonprimitive third-repeat exceptional pattern.  RL18 proves a new necessary Eisenstein-norm congruence for every skew zero; see `RL18_CUBIC_NORM_REDUCTION.md`.

## Distances that must not be conflated

### Distance to exact radius-3 closure
One explicit infinite theorem: the full-`D` cubic skew sparse uniqueness statement above.

### Distance to RL closure
Much larger and structurally different.  Even a complete radius-3 exclusion is not an RL contradiction unless the RL least-root/final-return grammar forces a radius-3 encounter, or the local arithmetic is promoted to an unbounded-radius obstruction.  RL18's global orbit-sum identity is a candidate framework for the latter, but no such bridge theorem is proved yet.
