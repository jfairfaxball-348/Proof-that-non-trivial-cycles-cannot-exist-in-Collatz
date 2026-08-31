# H21 signed successor corridor: exact boundary lift exclusion

Frozen RL201 component. RL201 frozen proof component, 2026-08-31.

Scope: the inherited sole high branch `(37,0,23,-1)`. A rank or lift
surviving the conditions below is only arithmetically necessary; no
physical terminal, population, charging release, branch/Gate closure,
non-trivial-cycle exclusion, or Collatz conclusion is asserted.

## 1. Interface and canonical seam

Retain the incoming constants

`A=217976794617`, `L=137528045312`, `B=A-L=80448749305`,
`R=L-B=57079296007`, `p=65470613321`, `pB=1 mod L`,
`T=7*3^35=350220815692997949`,
`Klo=128081997553`, `Khi=146795909391`.

Write `a=25583192106`, `b=41775866136` for the endpoints of the RL200
core `D_K=[a,b]`, retaining all 12 inherited isolated deletions. Let
`i=pr mod L`, `0<=i<L`, `Ai=nL+r`, and `rho(r)=2^n/3^i`.
The inherited terminal potential is `K(r)=rho(r)T/2^21`.

RL199 supplies, for terminal sign `sigma` and valuation `1<=nu<=21`,

`Ksucc(r,sigma,nu)=K(r)+sigma rho(r)(2^nu-1)/(3*2^21)`

or, equivalently,

`Ksucc(r,sigma,nu)=rho(r)[3T+sigma(2^nu-1)]/(3*2^21)`.

The canonical chronological wrap `i=L-1 -> 0` has source rank

`r=(L-1)B mod L=L-B=R=57079296007`.

It lies strictly above `D_K`. Consequently no successor tested here
crosses the canonical phase seam, and no period-twist renormalization
is omitted. This argument does not assert that the potential is
untwisted across a seam outside the stated domain. At the exceptional
rank `a`, the canonical source phase is exactly `80277474042`.

## 2. Reverse-rank ordering and the full-range consumer

The incoming proof gives `delta=A ln2-L ln3`, `0<delta<2^-40`, and
`ln2>L delta`. For `r<s`,

`ln rho(r)-ln rho(s)=((i_r-i_s)delta+(s-r)ln2)/L`

`> (ln2-L delta)/L >0`.

Hence `rho` is strictly decreasing in rank. The coefficient
`3T+sigma(2^nu-1)` is positive for both signs and every `nu=1,...,21`.
Thus `Ksucc` is also strictly decreasing in rank at fixed sign and
valuation. At fixed rank its positive-sign value increases with `nu`,
and its negative-sign value decreases with `nu`.

Exact rational logarithm enclosures prove these four strict comparisons:

1. `Ksucc(a,+,20)<Khi`;
2. `Ksucc(a,+,21)>Khi`;
3. `Ksucc(a+1,+,21)<Khi`;
4. `Ksucc(b,-,21)>Klo`.

The first-rank terminal wall gap and the relevant increments have the
following rigorous open rational bounds (the displayed decimals are
exact rational endpoints):

| Quantity | Exact enclosing interval |
| --- | --- |
| `Khi-K(a)` | `(0.166545, 0.166546)` |
| `rho(a)(2^20-1)/(3*2^21)` | `(0.146504, 0.146505)` |
| `rho(a)(2^21-1)/(3*2^21)` | `(0.293008, 0.293009)` |
| `Khi-K(a+1)` | `(0.975521, 0.975522)` |
| `K(b)-Klo` | `(7209472271.745576, 7209472271.745577)` |
| `rho(b)(2^21-1)/(3*2^21)` | `(0.270045, 0.270046)` |

In particular the positive `nu=20` successor at `a` stays at least
`0.020040` below the upper wall, while the positive `nu=21` successor
exceeds it by more than `0.126462`. At every rank at least `a+1`,
even the largest positive successor stays more than `0.682512` below
the upper wall. Every negative successor stays more than
`7209472271.475530` above the lower wall.

By reverse-rank ordering and valuation monotonicity these finite
comparisons cover every integer rank in `[a,b]`, both signs, and all
21 allowed valuations. Positive increments cannot violate the lower
wall; negative increments cannot violate the upper wall because the
terminal potential already lies strictly inside the corridor.

**Complete classification:** the sole additional excluded tuple is

`(r,sigma,nu)=(25583192106,+,21)`.

Every other tuple in `D_K x {+,-} x {1,...,21}` passes this specific
terminal-plus-successor corridor consumer. This includes the full
interval before inherited deletions, so retaining those deletions
introduces no coverage gap. The upper endpoint `b` is an inherited
deletion used only to give a conservative extreme bound.

## 3. Exact residue implication

RL199 says positive terminal sign means even `eta`, with

`nu=v2(3^34(eta+21)-1)`.

Since `3^(-34) mod 2^22=1893305`, exact valuation `nu=21` requires

`eta+21=1893305+2^21=3990457 mod 2^22`,

or `eta=3990436 mod 4194304`.

Combining with the two even classes modulo 9 gives precisely

- class `eta=0 mod18`: `eta=37544868 mod37748736`;
- class `eta=8 mod18`: `eta=20767652 mod37748736`.

These two additional lift residues are forbidden **only at terminal
rank `25583192106`**. They are distinct from the inherited all-rank
Hensel exclusions for `nu>=22`, namely `18670500` and `1893284` in
the two even classes modulo `37748736`; each new residue differs from
its old counterpart by half that modulus.

Equivalently, at this single rank an even `eta` must have `nu<=20`.
The negative-sign classes still allow every `nu=1,...,21`.

## 4. Precise limitation

For any class `c in {0,8,9,17}` and valuation `nu>=1`, put
`m=2^(nu+1)`, and choose the unique odd residue

`s=3^(-34)+2^nu mod m`.

Multiplication by odd `3^34` fixes `2^nu mod m`, so this gives exact
valuation `nu`. Set `eta=s-21 mod m` for the two even classes, or
`eta=s mod m` for the two odd classes, and combine with `eta=c mod9`
by CRT. This yields exactly one residue modulo `9m`, with arbitrarily
large positive representatives and the required class modulo 18.

Consequently, even at rank `a`, each of the four classes retains
representatives with `nu<=20`. At every larger surviving necessary
rank, all four classes retain every valuation `1,...,21`.

This consumer therefore removes **no whole rank, no whole class
modulo 18, and no whole terminal sign**. The incoming necessary-rank
count `16192674019` remains unchanged. The result is a genuine
rank-coupled lift exclusion at one boundary rank, together with a
proof that this two-potential corridor alone cannot accomplish the
requested global state or sign selection.

The missing datum is still an absolute endpoint constraint or a
sharper rank-resolved successor constraint beyond the inherited full
period corridor. Nothing here proves that any CRT representative is
compatible with the global cycle, p-chain, fixed-K0 moment, or coupled
prehistory.

## 5. Certificate and explicit inherited support repair

`verify_rl201_successor_corridor.py` uses integer and exact
`Fraction` arithmetic, with signed atanh-tail bounds for every log.
It checks every valuation explicitly at the extreme ranks, the
monotonicity hypotheses, canonical seam, wall-gap enclosures, CRT
translation, 12 inherited deletions, and representatives of all four
classes and all 21 valuations. The analytic monotonicity argument
covers the whole rank interval; no finite scan is represented as
covering unscanned ranks.

The inherited RL200 helper returned `[partial,partial+tail]` even
when `x<1`, although the generic two-sided interval in that case
must be `[partial-tail,partial]`. This support-contract defect is
explicitly repaired in the new verifier. All used RL200 assertions
remain sound: only the lower-wall comparison uses a negative log,
and it subtracts the old **upper** endpoint, which was conservative.
Every inherited log assertion has also been independently rerun
with corrected sign-aware intervals. No inherited theorem,
certificate conclusion, or rank range is demoted, and frozen
history is not changed.

Classification: the complete successor-corridor classification and
the two rank-specific lift exclusions are proved analytic
mathematics supported by an exact finite boundary/CRT certificate.
The no-whole-class result is a scoped method limitation, not a
barrier to all global consumers.
