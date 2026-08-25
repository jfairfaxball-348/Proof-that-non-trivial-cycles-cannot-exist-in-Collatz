# RL85 target — historical RL# versus RL♭: extremal ownership inversion, canonical feeder, and owned low/high arc bridge

Date: 2026-08-24

## Purpose

Before reverting from the RL♭ maximum-state route to the older RL75 hybrid route, perform one deliberate comparison between the historical RL# / first-number / entry-side architecture and the new RL♭ maximum-state architecture.

RL84 found enough new structure that this comparison is now a mathematical target rather than a retrospective review.

Do not conflate:

- historical RL# entry/feeder objects;
- current `R=min C` (`R#` in RL20/RL83);
- `M=RL♭=max C`.

The central new paired objects are:

1. the forced external feeder `F=2M` and owned maximum `M`;
2. the genuine minimum `R` and maximum `M` as endpoints of two canonical owned cycle arcs.

## Mandatory inherited RL84 interface

Use without re-deriving unless a verifier fails:

- minimum ownership: `R` odd and its preceding cycle state is `2R`;
- maximum ownership: `M` even, `M==2 mod3`, preceding cycle state `(2M-1)/3`, external even inverse `2M`;
- canonical feeder tower `2^kM` is external for every `k>=1`;
- `F=2M=3P+1` with `P=(2M-1)/3`;
- cylinder transfer preserves normalized height exactly;
- every nonzero backward prefix from `R` is surplus;
- under inherited `R>=2^71`, the first `114,208,327,603` backward prefixes from `M` are non-surplus;
- exact extremal arc formulas
  `log u=S_RM-log(M/R)`,
  `log v=S_MR+log(M/R)`;
- `v> M/R>3/2`;
- either `u<1` (canonical owned low arc) or
  `L>3R log(3/2)`;
- under `R>=2^71`, the latter gives
  `L>=2,872,132,254,754,669,047,880`;
- at the exact first Farey pair, feasible cylinder normalized height obeys
  `theta < 200,000,000,000/2^q`,
  `q=72,057,431,991`;
- conservative half-height consequence:
  if `m=2n` is the least even cylinder representative then
  `n<3^((q+1)/2)`;
- `O^qE^(p-q)` is excluded at the first Farey pair by cylinder height + ceiling.

## Required investigation 1 — historical RL# hypothesis audit

Recover only the load-bearing historical RL# / least-root / entry-side lemmas relevant to this comparison.  For each, record:

- is the object provably on-cycle, merely an entry/feeder, or auxiliary?;
- does the lemma survive multiplication by two?;
- does it require least-state minimality?;
- does it require full-`D` / primitive cyclic ownership?;
- does it use the ordinary `+1` non-homogeneously?;
- can it be applied to `F=2M`, `M`, `R`, or none of them?

Use the RL72 catalogue as the strategic index and recover older source files selectively.  Do not recursively re-audit historical bundles.

## Required investigation 2 — canonical feeder/max coupling

Test historical feeder-side statements on

`F=2M`.

Any candidate theorem must exploit more than the tautological dyadic relation.  In particular seek constraints involving

- exact entry time `1` into `M`;
- `F=3P+1` with the sibling cycle predecessor `P`;
- physical size `F=2M` relative to `R,M`;
- parity/valuation of `F`;
- a non-dyadic residue or ordinary-`+1` invariant;
- an old RL# endpoint condition that becomes owned because the landing state is the actual maximum.

If every old feeder theorem is invariant under the RL80 dyadic-neutrality no-go, freeze this subroute explicitly.

## Required investigation 3 — extremal low/high arc versus RL20 programmes

The maximum-to-minimum arc is canonically high (`v>3/2`).

In the complementary branch `u<1`, determine whether the minimum-to-maximum arc satisfies the exact hypotheses of any live RL20/RL72 global consumer, especially:

- balanced-return weighted difference;
- strict-excursion packing;
- hard-root / second-low compensation;
- arbitrary-rotation weighted populations;
- full-`D` proper-factor ownership.

Do not call the extremal arc a “plateau”, “excursion”, or “canonical block” until the exact historical definition is matched.

A successful result would turn the old question “can one locate an owned compensating low block?” into a theorem with endpoints `R,M`.

## Required investigation 4 — opposite prefix rotations

The minimum-rooted backward rotation has every prefix surplus.  The maximum-rooted backward rotation has an enormous initial non-surplus prefix under the inherited floor.

Interrogate this as a cyclic-word problem with ordinary `+1` correction retained:

- locate the two rotations in the same parity word;
- compare raw prefix sums `i log2-o_i log3`;
- compare corrected sums `Delta_i-S_i=log(x_i/anchor)`;
- test whether a cycle-lemma / Christoffel / rotation-order theorem can couple the two without erasing the physical state terms;
- combine with the full denominator only if ownership remains exact.

## Required investigation 5 — first-Farey small-cylinder consumer

RL84 compresses a feasible first-Farey cylinder to an exponentially tiny normalized-height interval.

Seek an independent lower bound or digit obstruction from:

- historical RL# entry-side cylinders;
- maximum top grammar;
- minimum/maximum arc ownership;
- full-cycle divisibility;
- primitive rotation;
- a monotone residue-height recurrence.

The target is a theorem of the form

`legal first-surplus word => cylinder height >= H(q)`

with `H(q) >= 200000000000/2^q`,

or a structured survivor family if such a lower bound is false.

Do not enumerate `~10^11` symbols.

## Required investigation 6 — branch H

If the `R->M` arc is not low, retain simultaneously:

- `d>=114,208,327,604` from RL83;
- reduced local denominator `>=72,057,431,991`;
- `L>=2,872,132,254,754,669,047,880` at the inherited floor;
- `v>3/2`.

Test whether RL19/RL20 state packing or distinct local/global slope separation can sharpen this into a contradiction.  If it only produces still larger length lower bounds, mark the branch as a method barrier rather than extending numerics.

## Red teams

Any claimed bridge must survive:

1. RL80: dyadic/backward saturation is cycle-intersection neutral;
2. RL81: auxiliary blue `J` does not automatically lift to a physical cycle integer;
3. RL20: naive CF address / final-return coupling decouples;
4. RL83: count-only first-surplus optimization is insufficient;
5. RL84: the full cylinder height, not only `mod162`, is load-bearing.

## Stop/pivot rule

After this comparison, pivot back to the RL75 hybrid owned-macro periodicity/packing route if the audit proves that:

- historical RL# constraints add no non-dyadic information to `F=2M`;
- the extremal low arc cannot be consumed by any live owned global theorem;
- the first-Farey small-cylinder condition lacks an independent lower-height consumer;
- or all remaining work reduces to generic residue ladders / length inflation.

If one of those couplings is genuinely promising, keep the comparative route and state the single narrow next obstruction.

## Close-out

Freeze separately:

- proved analytic mathematics;
- exact finite certificates;
- inherited external certificates/input;
- computational evidence;
- conjectures;
- barriers/dead routes;
- corrections/demotions;
- exact historical hypothesis matches and mismatches;
- verifier status.

Create the next numbered authoritative bundle and sidecar and verify its fresh unpack.
