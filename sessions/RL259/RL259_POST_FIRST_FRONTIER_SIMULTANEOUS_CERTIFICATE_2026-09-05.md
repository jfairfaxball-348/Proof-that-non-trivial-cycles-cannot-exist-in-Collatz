# RL259 post-first-frontier simultaneous certificate

Date: 2026-09-05
Status: VERIFIED
Classification: `FRONTIER_CONTRACTION_WITH_TARGETED_GATE_A_CERTIFICATE`

## Result

After removing the RL258-certified first halving selector, the next exact
arithmetic selector surviving the promoted resonance, determinant,
beta/capacity, zero-budget, parity, and halving constraints is uniquely

`(a,ell,z,q,r,H_sel,n)=(1119,706,413,802,506,14,10)`.

There is no retained selector with `1100<a<1119`.

The exact identities are

- `1119*506 - 802*706 = 2`;
- `B=q-r=296`;
- `H_sel=19*413-7*1119=14`;
- `n=19*296-7*802=10`;
- with `K=7,t=5`, `7*802=5*1119+19` and `7*296=5*413+7`.

The Branch-C capacity inequality allows `beta(P)=360` but not `361`, hence
`beta(P)<=360` at this selector.

## Exact seven-layer geometry and terminal range

The seven 33-site physical blocks are

- `[129,161]`;
- `[297,329]`;
- `[446,478]`;
- `[614,646]`;
- `[763,795]`;
- `[931,963]`;
- `[1080,1112]`.

Their complement gaps have lengths

`135,116,135,116,135,116,135`,

with total complement size `888` and baseline isolated-root capacity `297`.

The exact 19-window lower sums are

- `R(28)=262`;
- `R(30)=283`;
- `R(32)=300`.

After the corresponding terminal-zero exclusions, the complement capacities
are respectively

- `293` for `tau=28` (`k=31`);
- `292` for `tau=30` (`k=33`);
- `292` for `tau=32` (`k=35`).

At `k=35`, the required complement negative-root count is
`R(32)-2=298>292`; monotonicity therefore excludes every `k>=35`.
The exact terminal exponent range at this selector is consequently

`k in {31,33}`.

## k=31 contraction

For `k=31`, the base complement requirement is `R(28)-2=260`, and the
capacity `293` gives `E_31<=33`.

The exact legal canonical right 9-bit prefix family has 199 members and
minimum `E_right=11`; equality occurs only for

- `110110111`;
- `110111010`.

Enumerating those 199 right prefixes against all ten left flank bits gives
10,183 budget-feasible pairs.  Applying the exact tail/right/left zero-root
exclusions and complement capacity test leaves exactly

**8,976 flank pairs**.

The unowned middle length is **1068**.  This is the finite simultaneous
unresolved family handed to RL260.

## k=33 targeted Gate-A certificate

For `k=33`, the base complement requirement is `R(30)-2=281` and capacity
`292`, so `E_33<=11`.  Since the right flank already costs at least 11,
`E_33=11`; the right word is one of the two equality words above and the
left eight unknown bits are forced to `11111111`.

Exact inversion of that left suffix from the corrected internal terminal
state `(d,J)=(1,2^33)` produces 16 suffix chains.

Under Gate-A danger `H_can<=32`, the exact prefix/suffix areas plus the
unavoidable bridge lower bound leave only one low-area case:

- right word `110111010`;
- prefix state `(d,J,H_pref)=(2,-42,4)`;
- suffix predecessor `(d,J,H_suf)=(5,27148435231,19)`;
- bridge lower bound `7`;
- total fixed lower bound `30`;
- remaining middle-area budget `9`;
- suffix y-word `10101001`.

The exact low-area middle state-set automaton from `(2,-42)` with budget 9
first repeats its full state set from depth 143 at depth 154, with period 11.
Across the complete preperiod and cycle its maximum reachable quotient is
`J=212` (1,462 states at the repeat return), whereas the required terminal
predecessor quotient is `J=27148435231`.

Therefore the required predecessor can never be reached under
`H_can<=32`, and hence

**`k=33 => H_can>=33`**

at the selector `(1119,706,413,802,506,14,10)`.

Thus `k=33` is Gate-A safe and is removed from the branch simultaneously
unresolved by Gate A and Gate B.

## Promoted frontier state

At the second selector, the simultaneous unresolved branch is reduced to
`k=31` only, represented by the exact 8,976-pair flank family with middle
length 1068.

This is a targeted result.  Gate A remains open uniformly.  Gate B remains
open.  Radius 4 is not invoked by RL259.  Radius 5 remains inactive.
