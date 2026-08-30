# RL186 verification

Run:

```bash
bash verification/run_fast_rl186_verifiers.sh
```

The verifier uses exact Python integer/Fraction arithmetic. It checks the late first-defect numerator enumeration for offsets 28 through 39, the refined first-defect coverage table, the uniform `2^(24-H)` charging bound, the numerical `tau>=37` tail consumer, the amplified `>354` flow floor, and a rational enclosure `0<F2<1/2`.

The first-defect numerator identity and zero-block density argument are analytic statements recorded in the RL186 report; the verifier certifies their finite/numerical consumers.
