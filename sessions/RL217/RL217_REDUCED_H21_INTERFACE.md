# RL217 reduced H21 interface

Date: 2026-09-01. Compact successor interface.

## Global constants and frontier

`A=217976794617`, `L=137528045312`, `p=65470613321`, `u=103768467013`, `z=72057431991`, `K0=2^37`, with `Ap-uL=1`.

Necessary terminal frontier remains **13,415,865,871**:
- above-p source: `7,091,831,284`;
- below-p source: `6,324,034,587`.

The e=16 terminal rank `34,124,151,203` remains live.

## e=16 prefix family

There are **45,045** live prefixes after the RL216 deletion. For each prefix:

`eta = eta_* + 3^17 k`,
`y_0 = y_0^* + 3*2^58 k`,

with the inherited exact finite two-sided `k` window (one of the adjacent 28,812/28,813 to 36,180/36,181 windows) and inherited terminal-Hensel exclusions.

At phase 16 define the lifted coordinate `x=eta`. Then

`y_16 = 2^34 x - 1 - 3^16*2^13`, `h_16=1`.

## New RL217 phase-51 selector

A candidate remains in the conservative RL217 family only if its `x` lies in one of the **3,132,617** disjoint universal phase-51 survivor cylinders

`x = r mod 2^m`, `13<=m<=25`,

certified by `verification/verify_rl217_prefix_wide_height_automaton.py`. Cylinder digest:

`abf94388354f55d34ae35370e3bcbcd2086da2f6053035840c0a9f68665e8d05`.

Equivalently, within a prefix this is the exact congruence selector

`k = (r-eta_*) * (3^17)^(-1) mod 2^m`.

After this finite-horizon selector:

- arithmetic candidates: **139,581,280**;
- state011: **90,749,885**;
- state111: **48,831,395**;
- mod18: `0:35,622,831`, `8:19,167,422`, `9:55,127,054`, `17:29,663,973`;
- all **469** reachable eta classes mod2187 remain represented;
- every live prefix has 2,995..3,235 candidates.

These are arithmetic candidates satisfying necessary conditions through phase 51, not physical populations.

## Open locks carried to RL218

- No new rank, branch, Gate A or Gate B closure.
- No physical H21 incidence/charge/ownership theorem.
- Quotient residue `(Q/D) modD` remains undetermined.
- RL209 signed-successor conclusions remain scoped.
- Terminal valuation alone, collapsed endpoint moment, saturated G56 and flat-K normalized-gap integrality remain inert/locked.
- Do not continue the height route by naive cylinder-depth expansion without a new compression idea.
- RL80/RL81 certified-blue no-go locks must be inherited in RL218: density/proximity/arbitrary backward saturation do not imply cycle interception; the old auxiliary-transfer route lacks a basin-preserving equality to a physical cycle state.
