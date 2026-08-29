# RL177 certificate notes

`verify_early_mismatch_consumer.py` exactly checks the finite local automaton
and the arithmetic consequences promoted by RL177.

It treats the following as frozen analytic input rather than re-proving them
numerically:

- `1<=J<=36` and `v2(g_p)=S_J+min(a_J,a_{p+J})<=37`;
- nonnegative physical heights and mechanical digits from
  `b_j=floor(Aj/L)`;
- the corrected physical p-shift functional;
- the RL168 lifted-defect/value-order theorem;
- the RL175 half-barrier and mandatory mechanical carry structure.

The exact verifier checks:

- the mechanical prefix and all locally reachable common heights;
- every legal identified mismatch tuple under `v<=37`;
- the 15,872 tuple count;
- survival of both signs and all valuations `2..37`;
- `|d|<=21`;
- the exact 28 zero-height signed types and their `>1/3` first-flow bound;
- the global first-flow rational lower quantum `>3/10^7`;
- the `v=36` and `v=37` high-valuation local classifications.

The analytic compensation and three-support proofs remain in the main report;
the finite scan does not replace them.
