# RL299 — resonance-record compression and physical certificate report

Date: 2026-09-11
Base authority: `428d1d1b0c0d0444e6e920345692db8e40a34995`

## Classification

Primary:

`RESONANCE_RECORD_REDUCTION_PLUS_EXACT_PHYSICAL_FRONTIER_TO_A630138896_WITH_J_IMBALANCE_BARRIER`

Promoted components:

- **Proved analytic mathematics:** one-sided resonance-record reduction via continued fractions / intermediate convergents; monotone relaxed quotient envelope as a function of the positive logarithmic gap.
- **Exact finite certificate:** complete physical half-Collatz stopping envelopes needed for the record blocks through `a=630138896`.
- **Proved analytic mathematics:** sharpened stopping-to-weight lemma using half-step imbalance `J=O-E` rather than total stopping time.
- **Proved analytic mathematics / method barrier:** four-odd-step `B` ancestry and its optimality on `h == 0 (mod 3)`.
- **Computational evidence / conditional lead:** later external-certificate bridges beyond the unconditional frontier. These are frozen for RL300 but are not used to promote a larger unconditional frontier.

Gate A remains open. Gate B remains open. RL297 P-bottleneck work remains parked weak-green background. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed. The Lean project is separate.

## 1. Incoming state and replay

RL299 inherited the RL298 selector/physical quotient reduction:

- `N == 19 (mod 24)`;
- physical starts `A0=(9N+5)/8`, `B0=(27N+127)/8`;
- internal common weight `rho=ell-3`;
- longest inherited odd-terminal internal horizon `mmax=a-32`;
- RL298 exact physical frontier through `a=301994` with relaxed quotient ceiling `136073747` and stopping bound `588`.

The RL298 arithmetic checkpoint was independently replayed at session start and matched the frozen counts/frontier. The stopping-time ceiling/off-by-one argument was also rederived.

## 2. Global resonance-record reduction

Let

`Delta(a,ell)=a*ln(2)-ell*ln(3)>0`

for the canonical upper pair with `3^ell < 2^a`.

Normalizing the RL65/RL298 quotient equation gives the relaxed envelope

`Nhat(Delta)=floor((79/9)/(exp(Delta)-1))+2`.

The omitted terminal/rank-defect contributions are nonnegative in the direction which only lowers the actual phase quotient. Hence every admissible physical quotient satisfies `N <= Nhat(Delta)`.

`Nhat` is strictly decreasing in `Delta`. Therefore a worse quotient envelope can occur only at a new one-sided best approximation to `log_2(3)`. By the standard best-approximation theorem, the relevant record pairs occur among the upper convergents/intermediate convergents. Within each certified interval the elementary implication `a<a_next` and `a/ell>log_2(3)` bounds `ell` below the next record denominator, so the standard denominator form applies.

The closeout verifier uses exact rational atanh bounds

`ln 2 = 2 atanh(1/3)`, `ln 3 = 2 atanh(1/2)`

with rigorous geometric tails. It certifies the common continued-fraction prefix

`[1;1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3]`

and the following upper record sequence needed here:

- `U0=(301994,190537)`;
- `U1=(17087915,10781274)`;
- `U2=(102225496,64497107)`;
- `U3=(187363077,118212940)`;
- `U4=(272500658,171928773)`;
- `U5=(630138897,397573379)`.

This is the principal structural gain of RL299: selector-envelope control has been reduced from bulk selector enumeration to a sparse resonance-record sequence.

## 3. Exact relaxed quotient ceilings

Exact rational exponential enclosures in the portable verifier certify:

- `Nhat(U0)=136073747`;
- `Nhat(U1)=719078408`;
- `Nhat(U2)=1004967012`;
- `Nhat(U3)=1668206573`;
- `Nhat(U4)=4905934722`;
- `Nhat(U5)=82931674943`.

The U5 value is recorded as the first direct-replay scaling barrier; it is not needed for the promoted frontier through `U5-1`.

## 4. Physical certificates

The physical map is

`F(x)=x/2` for even `x`, `(3x+1)/2` for odd `x`.

The relevant full envelopes were exhaustively replayed as `N=19+24h`.

### U1/U2 envelope

Through `N=1004967012` there are `41,873,625` admissible quotients, hence `83,747,250` physical starts. The exact maximum stopping-to-1 time is `589`.

Extremal witness:

- `h=7,966,015`, `N=191184379`;
- `A0=215082427`, stopping time `180`;
- `B0=645247295`, stopping time `589`.

Independent 8-thread and 4-thread replays agreed.

### U3 envelope

Through `N=1668206573` there are `69,508,607` admissible quotients, hence `139,017,214` starts. The exact maximum is `612`.

Witness:

- `h=41,913,579`, `N=1005925915`;
- `A0=1131666655`, stopping time `165`;
- `B0=3394999979`, stopping time `612`.

Independent full replays agreed.

### U4 envelope

Through `N=4905934722` there are exactly `204,413,946` admissible quotients, hence `408,827,892` starts.

The gap-free shard partition was:

- `[0,50,000,000)`: max `612`, `h=41,913,579`, side B;
- `[50,000,000,100,000,000)`: max `613`, `h=83,827,159`, side B;
- `[100,000,000,150,000,000)`: max `631`, `h=124,048,315`, side A;
- `[150,000,000,200,000,000)`: max `676`, `h=190,785,579`, side A;
- `[200,000,000,204,413,946)`: max `600`, `h=203,706,651`, side A.

Therefore the exact global maximum is

`boxed: smax=676`.

Extremal witness:

- `h=190,785,579`, `N=4578853915`;
- `A0=5151210655`, stopping time `676`, peak `483308017730`;
- `B0=15453631979`, stopping time `145`, peak `222783572960`.

The portable C verifier in this package reproduces any shard or witness. The full replay is intentionally not part of the fast suite because it evaluates more than 408 million trajectories.

## 5. Certified selector frontier

The selector floor `ell >= ceil(147a/233)` gives a simple increasing lower bound on

`E=2*(ell-3)-(a-32)=2ell-a+26`.

Combining the resonance-record quotient envelopes with the physical certificates gives:

| selector interval | controlling record | quotient ceiling | physical bound | uniform `E` floor |
|---|---:|---:|---:|---:|
| `301995..17087914` | U0 | `136073747` | `588` | `79091` |
| `17087915..102225495` | U1 | `719078408` | `589` | `4473687` |
| `102225496..187363076` | U2 | `1004967012` | `589` | `26762926` |
| `187363077..272500657` | U3 | `1668206573` | `612` | `49052163` |
| `272500658..630138896` | U4 | `4905934722` | `676` | `71341400` |

Every row has `E >= s+2`; therefore the required internal common one-count cannot occur.

Combining with inherited RL298 gives the unconditional result

`boxed: every retained selector through a=630138896 is eliminated.`

This is not Gate-A closure: `U5=(630138897,397573379)` is the next unresolved record selector under the internally self-contained route.

## 6. Sharpened physical lemma

Suppose a half-Collatz trajectory reaches `1` after `O` odd and `E` even half-steps. Put

`J=O-E`.

At a later horizon `m`, after arrival at `1` the exact `1<->2` tail contributes at most half the remaining positions. Hence, if `W(m)` is total odd count through horizon `m`,

`2W(m) <= m + J + 1`.

Therefore

`boxed: 2rho-m >= J+2 => W(m)<rho.`

The RL298 stopping-time lemma follows from the crude inequality `J<=O+E=s`, but the new form identifies the true physical quantity that needs control.

This is important for RL300 because the available selector margins at future record spikes are enormous even when a stopping-time certificate is unavailable.

## 7. Exact B-ancestry identity and barrier

Write `N=19+24h`. Then

`A0=27h+22`, `B0=81h+80`.

There is an exact four-odd-step ancestry:

`16h+15 -> 24h+23 -> 36h+35 -> 54h+53 -> 81h+80=B0`.

Thus the B trajectory is a suffix of the trajectory from `Y=16h+15`, with four initial odd half-steps removed.

However, if `h == 0 (mod 3)`, then `Y` is divisible by 3. A positive state `x` has an odd half-Collatz predecessor iff `x == 2 (mod 3)`; when `x` is divisible by 3, only the even predecessor `2x` exists, and it remains divisible by 3. Therefore every earlier positive ancestor is `2^r Y`.

So on this infinite residue class `Y=16h+15` is the smallest positive ancestor of `B0`. The coefficient 16 is not improvable uniformly by deeper reverse-ancestry search.

Classification: **proved analytic method barrier**.

## 8. External-certificate bridge: frozen but not promoted as an unconditional frontier

RL299 also developed a large conditional continuation using public Collatz verification projects. Exact internal arithmetic identified later resonance records and showed how a finite external stopping/delay certificate could eliminate enormous intervals via either direct physical starts or the B-ancestry identity.

Because the load-bearing historical databases/checksums are not part of this repository package and were not independently reproduced during closeout, RL299 does **not** promote those later frontier claims as internal exact certificates. They are preserved in `RL299_EXTERNAL_PROVENANCE_NOTE.md` as provenance-dependent computational leads.

In particular, do not quote `a≈7.35e18` as the unconditional RL299 frontier. The unconditional promoted frontier is exactly `a=630138896`.

## 9. Open obligation

The first internally unresolved record is

`U5=(630138897,397573379)`

with exact selector coordinates

`(q,r,z,H,n)=(85137581,53715833,232565518,7772563,1050145)`.

Its relaxed envelope is `Nhat=82931674943`, which would require `3,455,486,456` admissible quotients / `6,910,972,912` physical starts under blind direct replay.

RL300 should not solve this by arbitrary volume. The intended next theorem is a physical compression controlling `J=O-E` (or a stronger coupled A/B invariant) along record spikes. A rigorously imported external finite certificate is allowed only with explicit provenance and exact scope.
