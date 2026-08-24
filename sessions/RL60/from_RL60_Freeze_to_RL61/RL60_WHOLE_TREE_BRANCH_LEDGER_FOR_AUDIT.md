# RL60 whole-tree branch ledger for audit

Date: 2026-08-23

## Purpose

This is a **provisional orientation map**, not a substitute for reconstructing the original proof tree. The RL61 audit should verify every arrow against the inherited files and correct any branch nomenclature that has drifted over RL18–RL60.

## Status legend

- **Closed/local:** proved or certified only for the named local sector.
- **Open/global:** required for the full RL program and not proved.
- **Dead route:** a specific proposed proof route was invalidated; the target itself may remain open.
- **Subtree survivor:** last survivor only inside a restricted reduction, not globally.
- **Audit-pending:** claim/interface requires fresh independent checking.

## Provisional map

```text
RL / retained full-phase program
|
+-- Gate A: uniform terminal-area / valuation inequality
|   status: OPEN globally
|   |
|   +-- earlier rank/separable relaxations
|   |   status: method barrier proved for large z; do not keep polishing it
|   |
|   +-- safe continued-fraction stress regime
|       |
|       +-- all but one safe-CF case eliminated/reduced
|       |
|       +-- sole safe-CF survivor
|           status: OPEN SUBTREE SURVIVOR
|           current terminal-tail reduction frozen at RL60
|           internal: z >= 103,303,788,559 from K39
|           external/audit-pending: 25 <= K <= 129
|
+-- Gate B / connection into radius-3 closure
    status: OPEN globally
    |
    +-- exact local radius-3 theorem / closure
    |   status: CLOSED/INHERITED LOCAL COMPONENT
    |
    +-- RL48 direct half-period four-swap -> radius-3 match
        status: DEAD ROUTE after RL49 correction
        reason: cyclic adjacent-transposition distance is even
```

## Critical interpretation

The current terminal-tail object is **not** the radius-3/order-3 extremal sector itself. It is a survivor inside the safe-CF Gate-A attack.

The phrase **sole safe-CF survivor** means exactly that: sole survivor of that restricted continued-fraction stress regime. It does **not** mean sole remaining branch of RL.

If this survivor is eliminated, the safe-CF subtree closes. That is important, but it does not by itself establish the uniform Gate-A theorem outside the safe regime and does not automatically supply a Gate-B bridge.

## Branches/roles the RL61 audit must reconstruct explicitly

### 1. Radius-3 local closure

Use the recovered RL18/RL19 bundles to identify precisely:

- what the radius-3 theorem states;
- its support/orientation/gcd/boundary/primitivity hypotheses;
- which portions are analytic and which are finite certificates;
- which external theorem dependencies it uses;
- whether later RL work changed any convention needed to apply it.

Do not merely write “radius 3 is closed.” State the exact theorem domain.

### 2. Global Gate B / bridge attempts

Track at least:

- RL20 global-bridge program;
- RL43–RL48 phase/same-root attempts;
- RL48 four-swap construction;
- RL49 correction showing the direct half-period radius-3 invocation fails;
- any later Gate-B ideas that remain viable after that correction.

The audit should distinguish **target still open** from **specific route dead**.

### 3. Gate A

Reconstruct the exact logical role of

`H >= t+3 = v2(T+1)`

and how it interacts with one-excursion/full-phase structure.

Separate:

- uniform Gate A;
- finite q-specific certificates;
- safe continued-fraction stress reductions;
- the RL47/RL48 separable-rank barrier;
- RL49/RL50 coupled height-one invariants;
- RL51–RL60 terminal-tail narrowing.

### 4. Safe-CF survivor

Identify the exact implication chain that produces the fixed convergent

`q=45,446,975,257,190,057,863`

and explain what is actually exhaustive below the rigorous Legendre cutoff and what is not exhaustive globally.

This is the branch most recent sessions have focused on.

### 5. Denominator regimes outside safe-CF

Do not assume the continued-fraction reduction covers every possible full-phase denominator. State exactly what the safe Legendre gate proves and what denominator/approximation regimes remain outside it.

This is essential to answering whether eliminating the current survivor closes Gate A or only one subtree.

### 6. Collatz-conjugate height-one subsystem

RL50 identifies the deterministic height-one synchronized continuation with the ordinary shortcut Collatz map on `n=(J-1)/2`.

The audit must mark any proposed argument that implicitly requires global settling of arbitrary shortcut trajectories as circular/unavailable unless it has been reduced to a finite certified interval or proved independently.

## Questions the audit must answer in plain language as well as formally

1. Exactly how many logically open top-level RL branches remain?
2. Which one contains the current safe-CF survivor?
3. If the survivor dies, what theorem/subtree closes immediately?
4. What remains after that?
5. Which branches have seen no serious work since RL49/RL50 because the project tunneled into the safe-CF survivor?
6. Is the current survivor still the highest-leverage target, or should effort move to global Gate A or a new Gate-B bridge?
7. Which inherited claims are analytic theorems, exact finite certificates, external computations, audit-pending computations, conjectures, or dead routes?

## Audit discipline

The RL61 session should not promote this provisional diagram merely because it matches recent prose. It should reconstruct the tree from source and issue a corrected authoritative branch ledger.
