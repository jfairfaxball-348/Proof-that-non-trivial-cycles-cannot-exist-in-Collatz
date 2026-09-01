# RL206-C2 — repair of the RL203 below-p source/terminal indexing

Date: 2026-08-31. Classification: **explicit mathematical correction RL206-C2**; independent review and exact verification passed.
Ordinary research paused when this live inherited dependency was recovered for the
successor handover. Historical files remain immutable.

## 1. First invalid dependency

The RL203 dyadic-prefix proof at immutable commit
`51daff87f4661a7f206a60df62492bc3d2d19f57` (`authoritative/proofs/RL203_DYADIC_PREFIX_INFORMATION_BOUNDARY.md`,
section 4) sets the tau34 **source** phase to `a=p-e`, computes its rank `aB mod L`,
and compares it with `[25583192106,41775866136]`. That interval is a **terminal**
rank core, not a source-rank core. The displayed modular arithmetic is correct;
the phase-role identification is not.

The inherited exact distinction is explicit in:

- `sessions/RL202/RL201_H21_Absolute_Endpoint_Moment_and_Coupled_Prehistory_2026-08-31/proofs/RL201_ABSOLUTE_ENDPOINT_MOMENT.md`,
  section 1: source rank is in `[40886621976,57079296006]`;
- `sessions/RL203/RL202_H21_Root_Anchor_Speed_Cone_and_Height_Collision_2026-08-31/proofs/RL202_ABSOLUTE_ROOT_ANCHOR.md`,
  section 4: the H21 terminal is 34 chronological steps after its tau34 source,
  so terminal rank is `((a+34)B) mod L`;
- the corresponding RL202 verifier's zero-anchor collision formula uses that
  same `+34` shift.

The RL203 verifier checks the printed source ranks and their membership in the
terminal interval. It does not verify that the interval and phase have the same
role. Its historical passing result therefore does not establish the claimed
source separation `p-a>=39` or normalized root depth `>=63`.

## 2. Exact corrected interface

Retain the inherited constants

`A=217976794617`, `L=137528045312`, `B=80448749305`,
`p=65470613321`, `u=103768467013`, `Ap-uL=1`, `pB=1 mod L`.

Let `a<p` be the canonical tau34 source phase, `e=p-a`, and
`i=a+34` its terminal phase in the offsets considered here. Its necessary terminal
rank is

`r_i=((a+34)B) mod L = (1-(e-34)B) mod L`.

Its source rank is instead `j_a=(aB) mod L`. In the inherited core there is no
rank wrap on subtracting the 34-step terminal shift, and

`j_a=r_i+15303429870`.

Thus the translated source interval is exactly
`[40886621976,57079296006]`, as stated in RL201. All inherited exclusions must
likewise be transported using the phase-role distinction, not reapplied to the
unshifted source rank.

## 3. Corrected separation and normalized depth

The zero-height anchor argument remains valid: offsets `1<=e<=33` force one of
the positive source-tail heights (offsets 0 through 33) to coincide with `h_p=0`.

For the remaining first offsets the correct terminal ranks are:

| e | source rank | terminal rank | terminal in inherited core |
|---|---:|---:|---|
| 34 | 15303429871 | 1 | no |
| 35 | 72382725878 | 57079296008 | no |
| 36 | 129462021885 | 114158592015 | no |
| 37 | 49013272580 | 33709842710 | yes |
| 38 | 106092568587 | 90789138717 | no |
| 39 | 25643819282 | 10340389412 | no |

At `e=37`, terminal rank `33709842710` is not among the twelve old isolated
deletions or the four RL202 zero-height deletions. Its terminal phase is `p-3`,
outside both length-`2^24` root windows, so it passes the inherited exact necessary
rank predicate. This is a **necessary label**, not a physical H21 realization.

Consequently the valid below-p necessary-source separation from these inherited
inputs is

`p-a>=37`,

and this lower bound is attained at the level of the inherited necessary predicate.
An actual physical source at that label is neither asserted nor excluded here.

The Bezout calculation is unchanged:

`b_(p-e)=u-ceil((Ae-1)/L)`, `S_a=b_a-1`.

At `e=37`, `58L<37A-1<=59L`, so

`u-S_a=60`.

The ceiling is nondecreasing with e, hence every surviving below-p necessary source
has normalized root-prefix depth at least **60**, not the inherited asserted 63.
The root-normalization term begins at depth at least **97**, not 100.

## 4. Remaining valid frontier

The exact endpoint identity, shallow eta-parity equivalence, terminal Hensel
precision of 22 eta bits, and required normalized modulus `2^56` are unchanged.
For the corrected below-p sources the exact prefix representation is still

`E_a=3*2^(u+37)-2^u P_a-3^p sum_(j=a)^(p-1)q_j`.

At a physical source `S_a=b_a-1`. Since `P_a` is an odd 2-adic unit, its normalized
root-prefix term starts exactly at depth `u-S_a>=60>56`; the first root-normalization
term starts at `u+37-S_a>=97>56`. Both therefore still vanish modulo `2^56`.

Thus the **qualitative RL203 one-sided information boundary survives**. Its sharper
source-offset and depth constants are explicitly weakened to their corrected values.
No rank is deleted or restored: RL203 promoted zero rank deletions and the RL202
predicate/count is unchanged at **16,188,727,234**. No eta/state/sign is selected.
No `a>p` conclusion, physical occurrence, H21 charge, Gate or global closure follows.

This correction is mathematical, not a checksum or packaging repair. Carry the
first invalid dependency, the corrected phase-role formula, and the surviving
qualitative scope into the next canonical proof/correction ledgers.
