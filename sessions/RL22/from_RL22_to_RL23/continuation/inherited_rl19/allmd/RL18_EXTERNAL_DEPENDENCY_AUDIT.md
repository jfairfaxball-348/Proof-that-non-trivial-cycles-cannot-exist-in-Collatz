# RL18 external dependency audit

Date checked: 2026-08-20.

## 1. Jacobian Conjecture: NOT USED

No file in the RL17 repair bundle uses the **Jacobian Conjecture**.  The phrase in `RL17_REPAIR_AND_STRATEGY_WORKPLAN.md` is:

> “use Jacobi/order arguments where possible”

This refers to the **Jacobi symbol** and associated quadratic-reciprocity/order arguments, not to the Jacobian Conjecture about polynomial maps.

The distinction matters because the mathematical status of the Jacobian Conjecture changed recently.  A 2026 counterexample in dimension 3 has been formally verified, and constructions now refute the conjecture in dimensions greater than two; the two-dimensional case remains open.  None of that enters the present Collatz/RL arguments.

**Dependency status:** NONE.

## 2. Jacobi symbol / quadratic reciprocity: classical proved mathematics

The inherited RL12 verifier contains finite exclusions labelled “excluded by Jacobi”.  These are uses of the ordinary Jacobi symbol and quadratic reciprocity/order facts.  They are classical theorems, not conjectural inputs.

**Dependency status:** SAFE / standard theorem.

## 3. Laurent–Mignotte–Nesterenko two-logarithm theorem: USED

The active deep external input is the Laurent–Mignotte–Nesterenko (LMN) lower bound for a nonzero linear form in two logarithms.

The inherited RL11/RL12/RL13/RL15/RL16 chain uses the rational specialization

`log |Lambda| >= -22 M^2 log H(a1) log H(a2)`,

with

`M=max(log(|b1|/log H(a2)+|b2|/log H(a1))+0.06, 21)`

for the appropriate nonzero rational two-log form.  This exact constant-22 specialization is stated in standard linear-forms-in-logarithms notes and attributed to Laurent, Mignotte and Nesterenko (1995).

Bibliographic source:

M. Laurent, M. Mignotte, Yu. Nesterenko, *Formes linéaires en deux logarithmes et déterminants d'interpolation*, Journal of Number Theory 55 (1995), 285–321.

RL18 uses this theorem in:

- restored RL12 finite reduction;
- restored RL13 near-density finite reduction;
- coefficient-3 P2 boundary `j=2` cutoff;
- omitted cubic three-orbit cutoff.

It is **not** used in the elementary `j=1` coefficient-3 boundary proof, the global orbit-sum identity, or the cubic Eisenstein-norm reduction.

**Dependency status:** PROVED EXTERNAL THEOREM; explicitly retained as an external dependency.

## 4. Continued fractions / Legendre theorem

Legendre's theorem on sufficiently good rational approximations and ordinary continued-fraction convergents are used after exponential defect bounds reduce the problem to rational approximation of `log 3/log 2`.

**Dependency status:** SAFE / classical theorem.

## 5. Resultants, irreducibility, Parseval/AM–GM

The repaired denominator estimates use standard integer resultants, Eisenstein irreducibility of `X^ell-2`, Parseval identities over roots of unity, and AM–GM.

**Dependency status:** SAFE / classical algebra and analysis.

## 6. BCZ note

An inherited RL12 script contains a stale comment mentioning “BCZ and LMN external theorems”.  No BCZ theorem is needed in the active RL18 reconstruction of the RL12/RL13 tails or the two newly closed branches.  RL18 therefore does **not** list BCZ as an active proof dependency.  If a future session revives an older argument that cites BCZ, it must identify the exact paper and theorem before use.

## Rule for future sessions

Every named non-elementary result must be entered into this dependency ledger with:

1. exact theorem statement/specialization used;
2. bibliographic source;
3. proof leaves depending on it;
4. whether it is proved, conjectural, conditional, or merely computational.

No conjecture may be used as if it were a theorem, even if older notes casually name it alongside proved tools.
