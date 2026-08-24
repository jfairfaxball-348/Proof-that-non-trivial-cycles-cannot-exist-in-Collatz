# RL42 — elimination of the rho = 48 boundary

Date: 2026-08-22

## Status

**EXACT FINITE CERTIFICATE over a rigorously reduced boundary case.**

Together with `RL42_CROSSING_EXCESS_TRANSPORT_FLOOR.md`, this proves

> # **`rho >= 49`.**

Companion verifier:

`verify_rl42_rho48_elimination.py`.

RL remains open.

## 1. Rigidity at rho=48

The crossing-excess transport floor already proves `rho>=48`.  Assume equality.

For `G=4`, define the exact normalized proper-factor threshold

`H(z)=12(z+1)/z^2`.

It is decreasing for `z>1`.  At the edge `z^2=16/15`,

`H(z)=(45/4)(1+sqrt(16/15)) > 91/4`,

because `sqrt(16/15)>46/45`.

For every positive moved rank,

`1-2^-delta <= (delta+1)/4`.

Hence if `P_+<=43`, then at `rho=48`

`M_eff <= (rho+P_+)/4 <= 91/4`,

contradicting `M_eff>=H(z)>91/4`.  Therefore

`P_+>=44`.                                                   (R42B.1)

On the other hand, the mandatory sign-changing excursion has excess at least four throughout this range, so

`P <= rho-4 =44`.                                           (R42B.2)

Consequently

> `P=P_+=44`, `E:=rho-P=4`.                                (R42B.3)

Thus every excursion is positive, exactly one has excess four, and all other excursions have excess zero.

The analytic transport theorem `rho>(45/4)G` also forces `G=4`: the next allowed value `G=8` would require `rho>90`.  The inherited exact common-prefix theorem for `G=4` therefore gives first excursion gap

> `Delta_0=9`.                                              (R42B.4)

## 2. Exact local e=4 crossing classification

The verifier first streams all `e<=3`, `p<=48` positive excursions and finds no physical crossing, independently reconfirming the crossing-excess input.

It then streams every `e=4` positive excursion with `p<=44`:

- 2,243,398 canonical words;
- exactly 40 physical crossing types;
- one type for every `p=5,...,44`.

Every crossing type satisfies exactly

`h=p+3`,

`g_in=1`, `g_out=4`,

`D=3^p+4*2^h`.                                              (R42B.5)

Thus the unique `e=4` excursion in (R42B.3) can cross only as

> `1 -> -4`.                                                (R42B.6)

The excess-zero positive excursions have the inherited explicit local data

`D=3^p-2^p`, `h=p+1`.                                      (R42B.7)

## 3. Safe boundary dynamic program

Starting from the forced gap `9`, the verifier propagates every composition of total moved mass 44 using

- arbitrary positive `e=0` excursions;
- exactly one `e=4` crossing from the complete list (R42B.5);
- every synchronized-run choice in the inherited safe over-approximation.

The synchronized-run rule intentionally permits **at least** every physically possible continuation.  Therefore absence in this DP is a valid impossibility certificate.

After the final excursion it imposes the inherited `G=4` terminal condition

`Delta_last=-4*2^s`.

The DP contains

- 7,791 states;
- 130 endpoint records.

Among those endpoint records, **none** satisfies the near-resonant window

`1 < 2^a/3^ell`,

`(2^a/3^ell)^2 < 16/15`.

Therefore `rho=48` is impossible.

## 4. Conclusion

The crossing-excess transport theorem proves `rho>=48`; the exact boundary DP proves `rho!=48`.  Hence

> # **`rho >= 49`.**                                       (R42B.8)

This new chain is independently reproducible and does not depend on the lost RL41 billion-scale area-26/27 transient tables.

## 5. Retained verifier output

```text
RL42 rho=48 elimination verifier: PASS
e<=3 words checked through p<=48 = 309781 with zero crossings
e=4 words checked through p<=44 = 2243398
e=4 crossing types = 40 all gap 1 -> -4
rho=48 rigidity: P=P+=44,E=4,G=4
safe boundary-DP states/endpoints = 7791 130
near-resonant endpoints = 0
certified consequence: rho != 48; together with rho>=48, rho >= 49
```

## 6. Next target

At `rho=49`, the same arithmetic already reduces the possibilities sharply.  The mandatory crossing still costs at least four excess units, so `P<=45`; the refined efficiency threshold forces `P_+>=43`.  Thus only the three total `(P,E)` layers

`(45,4)`, `(44,5)`, `(43,6)`

can survive, with at most two units of negative moved mass.  This is the next finite boundary to attack, preferably by classifying only crossing-capable `e=4,5,6` skeleton families rather than streaming all `e=6` words at large `p`.
