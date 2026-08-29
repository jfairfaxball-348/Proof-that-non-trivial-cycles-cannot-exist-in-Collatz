# RL176 certificate notes

`verify_integer_p_gap_consumer.py` verifies the new exact integer
consequences used by RL176.

The script deliberately treats the following as inherited certified
premises from RL175 rather than re-running historical logarithm
certificates:

- `Delta > 1/1,116,000,000,000`;
- `3*2^71*Delta > 6,365,000,000`;
- `s > 5*Delta` for `s=p*log(3)-u*log(2)`;
- the preferred-branch half-barrier
  `F2 < 1/2-Delta/16`;
- `F2=3*(exp(Delta)-1)*g_p`.

The new verifier checks the exact arithmetic transformations from those
premises, the p-gap lattice endpoint, the `2^38` comparison, and the
externally-qualified lower lattice endpoint.

The analytic proof of the first-mismatch valuation identity is in the
main RL176 report and is not replaced by a numerical sample test.
