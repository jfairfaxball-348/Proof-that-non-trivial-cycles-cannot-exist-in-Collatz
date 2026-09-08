# RL284 closeout red-team note

Date: 2026-09-08

Result: **PASS**

This is a closeout proof-state/scope red team, not new research.

Checks:

1. **Gate scope.** RL284 does not claim Gate A. The authoritative residual remains `k>=25`, `k` odd, `H_can<k`.
2. **Fallback theorem.** `nu_2(J)<=H` for globally reachable positive even `d=1` checkpoints remains open and is restored as RL285's target.
3. **Labelled bijection scope.** The bijection is for odd integer sources and labelled accelerated odd transitions; it does not make the unlabelled accelerated map injective.
4. **Inverse formula.** The converse requires exactly `m` odd, `3∤m`, `a>=1`, and `m==(-1)^a (mod 3)`. Under those hypotheses `P_a(m)` is odd and has exact valuation label `a`.
5. **Negative inputs.** `nu_2` is applied to the absolute value for nonzero integers; the algebraic quotient retains sign. No zero case occurs because `3n+1!=0` for integer `n`.
6. **Predecessor ray.** `P_(a+2)=4P_a+1` is asserted only for admissible exponents; admissibility parity is preserved by `a -> a+2`.
7. **Primality scope.** The promoted result is local branch indifference only. It does not claim prime factorisation is globally irrelevant to every possible Collatz argument.
8. **Mod-3 barrier.** The four positive witnesses establish failure of a two-class acyclic orientation quotient only; they do not rule out richer state-dependent orderings.
9. **Valuation-charge barrier.** The cycle argument applies to additive charges depending only on `a`. It does not rule out state-dependent cocycles or quantities with extra labels.
10. **Seven-cycle ordering.** The exact cycle is `-91,-17,-25,-37,-55,-41,-61` with valuation word `(4,1,1,1,2,1,1)`. The verifier checks the ordered word directly.
11. **No entropy overclaim.** RL284 concludes that the tested local entropy/dissipation mechanisms do not provide an independent closure route; it does not prove that every conceivable scale-independent structural proof is impossible.
12. **Inherited RL283 barriers.** No RL283 theorem or barrier is corrected or demoted.
13. **No forbidden reopening.** Gate B, fifth selector, Radius 6+, raw larger-height enumeration, and unrelated historical branches are not reopened.
14. **Successor isolation.** RL285 is exactly one generation ahead and returns to the explicitly frozen Gate-A upstream theorem.
15. **Global claim.** No global exclusion of non-trivial Collatz cycles is claimed.

No mathematical correction or demotion of inherited authoritative mathematics is required.
