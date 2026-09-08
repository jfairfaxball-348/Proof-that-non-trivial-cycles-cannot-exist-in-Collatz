# RL284 — labelled accelerated reversibility and local irreversibility barriers

Date: 2026-09-08

## Classification

Primary:

`LABELLED_ACCELERATED_REVERSIBILITY_AND_LOCAL_IRREVERSIBILITY_BARRIERS_PROVED`

Promoted analytic subordinate results:

- `ACCELERATED_ODD_LABELLED_BIJECTION_PROVED`
- `ADMISSIBLE_PREDECESSOR_RAY_PROVED`
- `LOCAL_PRIMALITY_BRANCH_INDIFFERENCE_PROVED`
- `MOD3_ORIENTATION_ACYCLICITY_BARRIER_PROVED`
- `VALUATION_ONLY_CYCLE_CHARGE_BARRIER_PROVED`

RL284 does **not** exclude non-trivial Collatz cycles and does **not** close Gate A.

The exploratory structural/irreversibility pivot has reached a decisive local barrier. The recommended successor is therefore the frozen Gate-A upstream programme.

Gate A remains open with exact residual

`k>=25`, `k` odd, `H_can<k`.

The preferred sufficient theorem remains

`d=1, J>0, J even, globally reachable at accumulated height H
 => nu_2(J)<=H`.

Gate B remains separate/open/frozen. The fifth selector remains unscanned. Radius 6+ remains frozen.

## 1. Accelerated odd map and dissipation label

For any odd integer `n`, define

`3n+1 = 2^a m`

where `a=nu_2(3n+1)>=1` and `m` is odd.

The accelerated odd Collatz step is `n -> m`, and `a` is the exact number of removed factors of `2`.

RL284 asked whether `a` can be interpreted as an intrinsically irreversible or dissipative event label.

The answer is structurally sharp: the unlabelled accelerated map is many-to-one, but the labelled map retains enough information to reconstruct the source exactly.

## 2. Labelled accelerated odd bijection

### Theorem

The map

`n |-> (m,a)`

defined by

`3n+1 = 2^a m`

is a bijection from odd integers `n` to labelled pairs `(m,a)` satisfying

- `m` odd;
- `3` does not divide `m`;
- `a>=1`;
- `m == (-1)^a (mod 3)`.

The inverse is

`P_a(m)=(2^a m-1)/3`.

### Proof

If `n` is odd then `3n+1` is a nonzero even integer, so `a>=1` and after dividing by its exact `2`-adic valuation the quotient `m` is odd.

Modulo `3`,

`2^a m = 3n+1 == 1`.

Since `2 == -1 (mod 3)`, this is equivalent to

`m == (-1)^a (mod 3)`,

and in particular `3` does not divide `m`.

Conversely suppose `(m,a)` satisfies the four displayed conditions. The congruence gives

`2^a m == 1 (mod 3)`,

so

`n=(2^a m-1)/3`

is an integer. Because `a>=1` and `m` is odd, `2^a m-1` is odd; division by the odd integer `3` preserves oddness, so `n` is odd. Finally

`3n+1=2^a m`.

Because `m` is odd, the exact `2`-adic valuation of the right side is `a`. Thus the accelerated step from `n` has precisely target `m` and label `a`, proving existence and uniqueness.

### Structural consequence

There is no information-theoretic irreversibility in the operation “odd growth followed by removal of `2^a`” once the exact removal count `a` is retained as the edge label. Any successful irreversibility argument must therefore discard or quotient labels in a mathematically justified way, or use genuinely global structure beyond the labelled local transition.

## 3. Exact admissible predecessor ray

For a fixed odd target `m` not divisible by `3`, the admissible exponents have one parity:

- if `m == 1 (mod 3)`, then `a` is even;
- if `m == -1 (mod 3)`, then `a` is odd.

Hence all admissible predecessors form a single infinite affine ray.

### Theorem

Whenever `a` is admissible for `m`,

`P_(a+2)(m)=4P_a(m)+1`.

### Proof

Directly,

`P_(a+2)(m)
 =(2^(a+2)m-1)/3
 =(4*2^a m-1)/3
 =4(2^a m-1)/3+1
 =4P_a(m)+1`.

Thus the local inverse tree at an odd target is not combinatorially irregular: it is one parity-selected affine ray.

## 4. Prime overlay: no local branch-selection leverage

The exact admissibility criterion for a predecessor branch is only

`m == (-1)^a (mod 3)`.

It does not refer to whether `m` is prime, composite, squarefree, or to any other factorisation property.

Therefore primality does not change:

- which valuation parities are admissible;
- existence of arbitrarily deep inverse branches;
- the exact predecessor recurrence `P_(a+2)=4P_a+1`;
- local reconstruction from `(m,a)`.

This is deliberately local. RL284 does **not** prove that prime factorisation can never enter a different global Collatz theorem. It proves only that primality supplies no deterministic leverage for the inverse-branch/dissipation mechanism examined in this pivot.

The prime overlay is therefore dropped as an independent local route.

## 5. Mod-3 orientation does not become acyclic

All four directed transitions between the nonzero residue classes `1` and `-1` modulo `3` occur on positive exact accelerated transitions:

- `1 -> 1`: `1 -> 1`, with `a=2`;
- `1 -> -1`: `7 -> 11`, with `a=1`;
- `-1 -> 1`: `5 -> 1`, with `a=4`;
- `-1 -> -1`: `11 -> 17`, with `a=1`.

Therefore this two-class residue event graph is the complete directed graph including both self-loops. No strict cyclic-order obstruction can arise from this quotient alone.

## 6. Valuation-only additive entropy is constrained by genuine cycles

Consider any proposed edge charge depending only on the removed valuation:

`edge charge = w(a)`.

If its sum is required to vanish around every genuine accelerated odd cycle, existing exact cycles already force several charges to zero.

The positive fixed cycle `1 -> 1` has valuation word `(2)`, hence `w(2)=0`.

The negative fixed cycle `-1 -> -1` has valuation word `(1)`, hence `w(1)=0`.

The exact negative seven-cycle

`-91 -> -17 -> -25 -> -37 -> -55 -> -41 -> -61 -> -91`

has valuation word

`(4,1,1,1,2,1,1)`.

Zero total charge gives

`5w(1)+w(2)+w(4)=0`.

Together with the two fixed cycles this yields `w(4)=0`.

Thus a valuation-only additive “dissipation entropy” cannot simply assign a strictly positive irreversible cost to every factor-removal event: exact closed dynamics already force at least `a=1,2,4` to be neutral.

This is a route barrier, not a theorem that every possible state-dependent cocycle is impossible.

## 7. Relation to inherited project structure

These conclusions are consistent with the inherited warnings that known neutral loops must be quotiented rather than treated as positive entropy production, aggregate scalar quantities can be dependent on existing telescopes, and local valuation behavior need not be monotone even while the global Gate-A theorem remains plausible.

RL284 therefore does not reinterpret earlier Gate-A work as failed. It identifies why a tempting alternative “dissipation/entropy” explanation does not bypass the established global-reachability difficulty.

## 8. Exact verification

Portable verifier:

`verification/verify_rl284_structural.py`

It checks:

- `3,996` forward labelled reconstruction cases over odd `n` in `[-3995,3995]`;
- `396` admissible converse pairs with odd `m` in `[-99,99]` and `1<=a<=12`;
- `396` affine predecessor-ray cases;
- the four exact mod-3 orientation transitions;
- the positive fixed cycle, negative fixed cycle, and negative seven-cycle valuation words.

The recorded verifier output is in `verification/RL284_FAST_VERIFIER_OUTPUT.txt`.

The proof-state/scope red team is `verification/RL284_RED_TEAM.md` and records PASS.

## 9. Strategic conclusion

RL284 was explicitly exploratory and was not authorized to displace the Gate-A programme without a theorem-sized advance, scalable reduction, or decisive barrier.

It has produced both an exact structural theorem and a decisive barrier:

1. the accelerated odd transition becomes exactly reversible when its full valuation label is retained;
2. the admissible inverse structure is an affine residue-controlled ray rather than an irreversible branching mechanism;
3. primality adds no local branch-selection information;
4. the simplest residue orientation and valuation-only additive entropy architectures are defeated by exact transitions/cycles.

No surviving scale-independent irreversibility quantity with a plausible closure route was obtained.

Accordingly the exploratory pivot ends and the successor returns to the frozen Gate-A theorem

`globally reachable positive even d=1 checkpoint (J,H) => nu_2(J)<=H`.

That programme remains mathematically open, not demoted.

No global non-trivial-cycle exclusion is claimed.
