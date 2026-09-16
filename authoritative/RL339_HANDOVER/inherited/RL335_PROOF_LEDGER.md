# RL335 proof ledger — all-length owned-return compression and q=28 contraction

Date: 2026-09-16
Status: FROZEN AND VERIFIED
Incoming BASE_HEAD: `a22d083d82bce4e09657c4e5a39bb941d7230a11`
Successor: RL336

## Scope retained

Work remains in the ordered genuine `g=2`, `Z0>0`, `K<0` late-row parent branch with `(a,ell)=(217976794617,137528045312)`. The inherited least-state floor `m>=2^71` remains externally conditional and every physical exclusion below that uses it only under that condition. Gate A, Gate B, the separate `g=1` branch, R1, and global positive non-trivial-cycle exclusion remain open.

Incoming carry cap: `n<=32546313237`. Inherited high-carry ownership threshold: `n>=20390252058`.

## RL335.1 — exact physical pruning through four positives

Using the exact mechanical-factor enumeration, full congruence reconstruction in `2^71<=P<2^76+2^36`, parity checks, and deterministic odd-Collatz continuation, RL335 verifies the following physical layers for adjacent zero runs `1<=z_left,z_right<=37`.

At the new self-consistent bootstrap `n>=32546289531`, the singleton layers are unchanged:

- total 44: 9,836 physical rows across 31 pair types; every source reaches below `2^71`; maximum escape 185 odd steps;
- totals 45..51: 4,764 physical rows across 141 pair types with total multiplicities `45:3236,46:1058,47:337,48:97,49:26,50:8,51:2`; every source reaches below `2^71`; maximum escape 184 odd steps.

At the inherited high-carry threshold `20390252058`:

- p=2: 11,682 realizations across 176 pair types, all escaping; maximum 151 odd steps;
- p=3: 7,030 realizations across 165 pair types, all escaping; maximum 133 odd steps;
- p=4: 79,820 exact admissible templates, 4,986 physical realizations across 141 pair types, all escaping; maximum 81 odd steps.

The p=4 multiplicity by adjacent zero total is `44:3347,45:1119,46:376,47:105,48:35,49:3,50:1`. Pair `(37,37)` has 213 admissible p=4 templates and zero physical realization.

Classification: exact gap-free finite certificate under the explicitly conditional least-state floor.

## RL335.2 — all-length support-uniform compression

After the exact-owned singleton/p2/p3/p4 physical supports are removed, every surviving anonymous positive return has length at least five. For any fixed adjacent-zero pair, extending such a run by one positive increases true density slack by 43 while a q-charge increases by q. Hence the charge changes by `q-43` per added positive.

Therefore, for every `q<43`, the worst surviving anonymous return is the p=5 baseline. This is the required all-length mechanism: no enumeration of p=5,p=6,... is used to certify arbitrary depth.

A conservative 37-state graph on `N(1),...,N(37)` contains:

- singleton edges `N(z)->N(z')` with k=1 when `z+z'<=43`;
- a fallback k=5 edge for every ordered pair, representing every remaining run of length at least five.

The graph has 2,242 edges. An exact integer potential has range 0..31 and proves the density inequality. Defining true edge slack from this potential, a second exact potential of range 0..28 proves

`28(K-2H)-S <= 28`,

or equivalently

`2H >= K - S/28 - 1`.

Here H counts visits to low target plateaux `N(1)..N(21)` and S is total true slack.

Classification: exact finite-state theorem plus analytic all-length monotonicity for every surviving positive-run length.

## RL335.3 — sharp q=29 residual

The q=29 analogue fails first at the fallback self-loop `N(37)->N(37)` with baseline p=5. Its exact slack is

`43*5 - 2*37 = 141`.

Thus its q=28 charge is `28*5-141=-1`, while its q=29 charge is `29*5-141=+4`.

Longer runs are easier because each extra positive changes q=29 charge by `29-43=-14`. Accordingly the unresolved obstruction is localized to the exact five-positive `N37->N37` family, not to an arbitrary-depth catalogue.

Classification: exact obstruction localization; not a closure theorem.

## RL335.4 — q=28 phase consumer and new cap

Combining the q=28 anchor with the inherited phase lower bound gives

`W_struct >= K + C*(K/2 - (57/56)S - 3/2)`,

with inherited exact rational `C=25120009946627/10^14`.

The exact consumer verifies:

- at rho=60: `K=6112357564`, endpoint slack 3, optimized `h=59101261`, RHS `32546289526.519188...`;
- finite rho 60..2894: maximum remains at rho=60;
- uniform bridge from rho=2895 to 21,999,999: endpoint RHS `32546289530.756397...`;
- ordinary inherited Q256 handoff at rho=22,000,000: RHS `32546008794.296284...`;
- rho<=59 companion branch is below the same bootstrap.

Hence the self-consistent carry cap is

`n <= 32546289530`.

This improves RL334 by 23,707.

Classification: exact rational consumer with finite-range, uniform-bridge, and ordinary-handoff checks.

## Corrections and non-results

Scratch-only arithmetic/count mistakes were corrected before promotion: p=4 template count `72091 -> 79820`, `(37,37)` template count `237 -> 213`, and self-loop slack `144 -> 141`. None entered authoritative state.

RL335 does not close R1. The remaining live mathematical target is to remove or surcharge the exact five-positive `N37->N37` family by at least four q=29 charge units through an affine/exact-state/support-uniform argument, not by restarting p-by-p enumeration.

`PARENT_DIFFICULTY_DELTA = EASIER`.
