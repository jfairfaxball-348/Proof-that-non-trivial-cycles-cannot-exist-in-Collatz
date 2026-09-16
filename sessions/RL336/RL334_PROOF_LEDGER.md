# RL334 proof ledger — zero-run elimination, refined owned returns, and q=22 contraction

Date: 2026-09-15
Status: FROZEN CANDIDATE FOR RL334 CLOSEOUT
Incoming authoritative HEAD: `31352b47ae6e27fbf019ea8270faf73f894510bc`

## Scope
Work remains in the ordered genuine `g=2`, `Z0>0`, `K<0` parent branch at `(a,ell)=(217976794617,137528045312)`. The inherited external least-state floor `m>=2^71` remains conditional. The fixed high-carry ownership threshold is `n>=20390252058`. Gate A, Gate B, R1, `g=1`, and global positive non-trivial-cycle exclusion remain open.

RL333 enters with cap `n<=32548554424`, density theorem `2Z<=43K+129`, phase constant `c=25120009946627/10^14`, and all-rho residue-consumer architecture.

## RL334.1 — state-dependent defect charging
Exact max-plus analysis of the inherited ownership graph showed that the old nine slack-4 equality edges are transient projection artefacts rather than the true asymptotic obstruction. On the inherited graph an integer potential of range `0..36` proves the intermediate theorem

`2H >= K - S/9 - 4`.

It is sharp on the inherited conservative graph at the two-edge projected cycle `L(43,8)->N43->L(43,8)`. This theorem is valid but superseded below.

Classification: **proved exact finite-state intermediate theorem, superseded by RL334.4**.

## RL334.2 — exact physical support refinement
RL334 reconstructed two-positive and three-positive ownership at the fixed high-carry floor rather than using blanket total-length projections. Pair-level cycles such as `N22<->N29`, `N26<->N23`, and the old `N49->N49` obstruction disappear when exact shared physical identity is retained. The frozen RL329 three-positive certificate was independently reconstructed in this process; in particular the old `N49->N49` three-positive realization does not exist.

Finite run-by-run enumeration remains a binding barrier: diagnosing individual p=4, p=5, ... returns only exposes new long-run projected cycles and is not promoted as an all-length method.

Classification: **exact finite ownership certificates plus confirmed route barrier**.

## RL334.3 — 38-zero physical exclusion theorem
Let a zero run mean consecutive ranks with `q_t=0` in the inherited mechanical-excess sequence. A run of 38 zero values contains 37 exact mechanical gaps. There are exactly 38 rational-mechanical factors of length 37.

Using the exact high-carry ownership condition `Delta_upper * min(states) >= 20390252058`, equivalently

`min(states) >= 22689747442693040208618`,

the complete state-band reconstruction yields exactly `1,825,797` ownership-compatible endpoint blocks. Deterministic ordinary odd-to-odd Collatz continuation of every such endpoint reaches an odd state below `2^71` in at most `213` odd steps. Such an endpoint cannot lie on a cycle whose least state is at least `2^71`.

Therefore, in the live fixed-high-carry regime,

`every zero q-run has length at most 37`.

Classification: **exact gap-free finite certificate plus deterministic physical least-state contradiction, in the inherited externally conditional scope**.

## RL334.4 — refined owned-return graph and q=22 anchor theorem
At the final bootstrap, retain only zero plateaux of length at most 37 and preserve exact owned identity for large singleton, total-44 singleton, and two-positive states. Exact source-aware p2/p3 successor tests are used before falling back conservatively to multiplicity at least four.

The final conservative graph has:

- 37 anonymous `N` states;
- 141 retained large-singleton `L` states;
- 31 retained total-44 singleton `T` states;
- 176 retained owned two-positive `P` states;
- 385 states total;
- 15,835 edges.

An integer density potential has range `0..31`. For each edge let

`sigma = Phi(t)-Phi(s)-(2z-43k) >= 0`,

and let `I_low(t)=1` for `N(1),...,N(21)` and zero otherwise. A second integer potential `Pi`, range `0..44`, proves on every edge

`22*(k-2 I_low(t)) - sigma <= Pi(t)-Pi(s)`.

Telescoping gives the exact global path theorem

`22(K-2H)-S <= 44`,

hence

`2H >= K - S/22 - 2`.

An independent reverse-order max-plus reconstruction obtains the same charge-potential range `0..44` and verifies every edge inequality.

Classification: **proved exact finite-state theorem backed by exact owned-support certificates and independent red team**.

## RL334.5 — strengthened phase envelope
The inherited all-length phase theorem gives phase contribution at least `c(H-S-1)`. RL334.4 implies

`H >= K/2 - S/44 - 1`,

so

`H-S-1 >= K/2 - (45/44)S - 2`.

Therefore

`W_struct >= K + c*(K/2 - (45/44)S - 2)`.

Classification: **proved support-uniform analytic corollary**.

## RL334.6 — all-rho carry contraction
At `rho=60`, exact intersection of the structural and residue-weighted consumers occurs at

`h=58,816,735`,

and gives

`n < 32546313237.019188...`,

hence `n<=32546313237`.

Exact rational evaluation covers `rho=60..2894`; the maximum right-hand side is at `rho=60` and the minimum structural gain in that range is at least `58,816,733`. A worst-endpoint-slack uniform gain of `58,808,670` gives a valid bridge from `rho=2895` through `21,999,999`; at the bridge start the upper bound is `32546313237.9308... < 32546313238`. At `rho=22,000,000`, an exact Q=`2^256` fixed-point lower bound for omitted Beatty mass gives ordinary-consumer upper bound `32546008794.296284... < 32546313238`; inherited ordinary-consumer monotonicity then applies. The inherited companion inequality handles `rho<=59`.

Thus the live branch satisfies

`1 <= n <= 32546313237`.

Classification: **proved all-rho contraction with exact rational/fixed-point certification**.

## RL334.7 — lower-bootstrap self-consistency
At bootstrap `H=32546313238`, the exact singleton reconstruction has `13,559` total-44 rows and `7,189` large rows. Relative to the old RL331 base counts, the pair deltas are +1 at `(4,40)`, `(5,39)`, and `(38,6)`; relative to RL333 only `(38,6)` is new. The large layer is unchanged from RL333.

The new `(38,6)` state contains a forbidden 38-zero plateau and is absent from the refined graph. Rebuilding the load-bearing graph at the new bootstrap reproduces the 385-state / 15,835-edge graph and the q=22 theorem.

Classification: **proved self-consistent lower-bootstrap reconstruction**.

## Sharp live frontier
The first failed next integer charge is q=23. Its simplest sharp projected cycle is

`N(29) -> L(29,22) -> N(29)`.

The entry is a singleton; the return is an owned return conservatively representing a run of at least four positives. The cycle has total positive defect 5 and total slack 113, so q=22 is safe while q=23 is positive. Direct finite diagnostics exclude compatible return lengths 3 through 11 from the sharp owned source, but another long-run obstruction appears afterward. These finite diagnostics are evidence only for the all-length nature of the remaining blocker and are not promoted as a closure theorem.

The smallest remaining R1 obligation is therefore an **all-length owned-return theorem for the >=4-positive tail**: exclude those returns, prove enough additional slack/charge, or obtain a genuine owned descent/contradiction without blind run-length enumeration.

## Final status
Authoritative RL334 cap: `1<=n<=32546313237`.
R1 remains OPEN. Gate A remains OPEN. Gate B remains OPEN. `g=1` remains separate. Global positive non-trivial-cycle exclusion remains OPEN.

`PARENT_DIFFICULTY_DELTA = EASIER`.
