# RL178 certificate notes

`verify_second_transition_consumer.py` exactly checks the finite arithmetic consequences promoted in RL178.

It treats the following as frozen analytic input:

- the RL176/RL177 preferred `h_p=0` branch and corrected p-shift convention;
- `0<g_p<2^38`, the first-mismatch valuation identity, and the zero-height `v=37,J=23,d=+/-1` classification;
- nonnegative mechanical heights with `b_j=floor(Aj/L)`.

It then checks, from exact integer arithmetic:

- `g_p=2^37` in the high valuation case;
- the signed phase-24 pair relations;
- the `v2(3^25+1)=2` exclusion of `d=+1`;
- the `v2(3^25-1)=1` forced `(1,1)` continuation of `d=-1`;
- the exact necessary transition recursion through phase 30;
- the state counts `1,1,2,2,5,10,16`;
- no nonnegative defect before phase 29;
- no zero defect at phase 29;
- the three phase-29 positive height pairs and their exact flow quanta.

The certificate is a necessary-interface certificate.  It does not assert that surviving states extend to a physical cycle.
