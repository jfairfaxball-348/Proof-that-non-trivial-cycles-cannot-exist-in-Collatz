# RL340 exact `(23,23,p=6)` q=0 escape certificate

Date: 2026-09-16
Status: PROMOTED EXACT FINITE CERTIFICATE under the inherited ordered `g=2`, `Z0>0`, `K<0` parent assumptions and external least-state-floor qualification `m>=2^71`.

Use `a=217976794617`, `ell=137528045312`, `D=a-ell`, and q=0 source band `2^71 <= P < 2^76+2^36`. For `(left,right,p)=(23,23,6)`, the complete word length is `L=51`.

The verifier reconstructs every rational-mechanical factor by phase cuts `(-D*j) mod ell`, retaining cut and immediate interior representatives and deduplicating, giving exactly `L+1=52` base factors. It enumerates the complete inherited p=6 profile grammar, applies the interface deformation, and rejects nonpositive gaps, giving exactly 684 admissible templates. For each template it solves the exact backward composition congruence modulo `3^L`, enumerates every odd residue lift in the q=0 band, and checks every backward numerator for integrality and odd parity.

The complete reconstruction yields exactly 10 candidate rows / 10 distinct sources:

| source | run-exit state | profile | escape depth |
|---:|---:|---|---:|
| 4849394078535927753485 | 4972226358524775028967 | `(2,2,2,1,1,1)` | 1 |
| 5104336667936172544451 | 5233626492726523538495 | `(1,3,3,2,1,1)` | 2 |
| 16626200920766294819051 | 17047332743335551412607 | `(4,3,3,2,2,1)` | 11 |
| 27252553616645642592365 | 27942844659616834978331 | `(3,2,2,1,1,1)` | 17 |
| 30947206230200270477065 | 31731080635740066734623 | `(1,2,2,2,1,1)` | 29 |
| 31638206750376685000279 | 32439583789852218973807 | `(2,2,1,2,1,1)` | 17 |
| 43087614946595355414935 | 44178998714847430760639 | `(3,3,3,2,2,1)` | 24 |
| 47922981921398150458445 | 49136842671408969053087 | `(3,2,3,2,1,1)` | 6 |
| 75005841997025759408449 | 76905695553113622372655 | `(1,1,1,2,1,1)` | 6 |
| 75515727175826248990381 | 77428495821517119391711 | `(2,1,2,2,1,1)` | 16 |

Forward escape uses `F(x)=(3x+1)/2^{v_2(3x+1)}`. Every source reaches below `2^71`; maximum escape depth is exactly 29 odd steps. Therefore none can occur on a cycle whose least odd state is at least `2^71`.

`verification/verify_rl340_fast.py` and `verification/red_team_rl340.py` independently reproduce 52 factors, 684 templates, 10 rows / 10 sources, and maximum escape 29. This certificate concerns exactly `(23,23,p=6)` and does not prove the broader `92/91` candidate inequality.
