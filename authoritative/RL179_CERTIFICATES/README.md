# RL179 certificate notes

`verify_v37_budget_and_sieve.py` checks the exact finite and arithmetic claims promoted by RL179.

It independently verifies:

- a rigorous rational lower bound `F2>1/3` for the high `g_p=2^37` branch;
- the complete 10-history RL178 necessary propagation through phase 29;
- the exact best/worst cumulative phase-24..29 flow values;
- the two-later-positive requirement for all ten histories and the three-later-positive requirement for four histories;
- the complete phase-30 images of the three positive phase-29 pair states;
- the ten zero-height indices with `c_(J+1)=1`;
- the exact local valuation alternatives `nu=1`, `nu=2`, `nu>=3`;
- the mod-8 class excluded for each sign and parity.

The certificate uses the RL178 pair-state transition law as promoted analytic input.  It does not assert that a surviving necessary state is physically realized.
