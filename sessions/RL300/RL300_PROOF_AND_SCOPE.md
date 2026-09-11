# RL300 — proof ledger, external dependency, and scope

Date: 2026-09-11

## Final classification

`EXTERNAL_DELAY_RECORD_CERTIFICATE_PLUS_EXACT_RESONANCE_FRONTIER_TO_A206745572560704146_WITH_DIRECT_START_BOUNDARY`

## Promoted inherited facts

From RL299:

1. New relaxed quotient-envelope records occur only at one-sided best approximants / upper continued-fraction convergents and intermediate convergents.
2. `Nhat(Delta)=floor((79/9)/(exp(Delta)-1))+2` is decreasing in positive `Delta`.
3. Physical starts are `A0=27h+22`, `B0=81h+80` for `N=19+24h`.
4. If a physical trajectory reaches 1 with imbalance `J=O-E`, then `2W(m)<=m+J+1`, so `2rho-m>=J+2` excludes weight `rho`.
5. The selector/full-phase excess is `2ell-a+26`.
6. Selector floor: `ell>=ceil(147a/233)`.
7. B-family ancestry: `16h+15 -> 24h+23 -> 36h+35 -> 54h+53 -> 81h+80`.

## New exact internal results

1. The common exact-rational continued-fraction prefix for `log_2(3)` is extended through coefficient `20` at index 33.
2. Exactly 51 upper resonance records are certified from
   `(630138897,397573379)` through
   `(206745572560704147,130441933147714940)`.
3. The final direct-start-safe controlling record is
   `(196864044717151823,124207383220472977)`.
4. Its exact relaxed ceiling is
   `1250146787826445598`.
5. Its exact largest B physical start is
   `4219245408914253845`.
6. The boundary record has exact relaxed ceiling
   `4894841535700125438` and B maximum
   `16520090182987923332`.
7. Local ordinary-Collatz replay gives
   `D(3571472436310255273)=2334` and
   `D(4761963248413673697)=2337`.
8. Ordinary delay bounds half-Collatz stopping time, which bounds `J`.
9. The selector floor gives a uniform excess vastly above `2336` throughout the new interval.

## Promoted external finite certificate

Source-backed assertion:

`forall positive n < 4761963248413673697, ordinary Collatz delay D(n) <= 2334`.

Why this is the exact external dependency:

- OEIS A006877 defines its entries as new record setters for number of steps to 1 and says both 3x+1 and halving steps are counted.
- its b-file, sourced from Eric Roosendaal's delay records, contains the consecutive entries
  `3571472436310255273`,
  `4761963248413673697`;
- Roosendaal defines a confirmed delay record by comparison against all smaller starts;
- the RL300 portable verifier independently computes delays 2334 and 2337 for those two record values.

The exhaustive confirmation that no smaller/intermediate start beats the record is **external computational provenance**, not re-executed internally.

## Resulting frontier

Using that external finite certificate,

`every retained selector through a=206745572560704146 is eliminated`.

The internally self-contained RL299 frontier `a=630138896` remains distinguishable from this externally certified extension.

## Direct-start method boundary

At

`(206745572560704147,130441933147714940)`

the relaxed direct-start B envelope rises above the frozen external threshold.

This proves only that this **particular direct-start consumer** no longer fits wholly inside the one frozen delay-record interval. It does not show that the physical route fails.

## Corrections / demotions

None.

No RL299 theorem is demoted.

## Explicit non-claims

- no independent exhaustive verification of every start below `4761963248413673697`;
- no use of later external delay records in the promoted frontier;
- no global bound on `J`;
- no global stopping theorem;
- no Gate A closure;
- no Gate B closure;
- no global non-trivial-cycle exclusion;
- no identification of selector resonance coordinate `H` with canonical `H_can`.

## Open obligation

The first unresolved selector record for the promoted external-certificate route is

`(206745572560704147,130441933147714940)`.

RL301 should test inherited B-ancestry/coupled physical compression against the finite delay certificate before importing a larger external ladder; if only another finite scaling frontier results, compare directly with the parked RL297 Bellman/P route.
