# RL272 verification

Run:

`bash sessions/RL272/verification/run_fast_suite.sh`

The suite contains two independent implementations:

1. `verify_rl272_height2.py`
   - exact size scan through the inherited LMN cutoff;
   - complete canonical height-two reconstruction through the resulting `A<=27`;
   - exact two-term numerator identity and complementary identity checks;
   - complete full-`D` hit test.

2. `redteam_rl272_height2.py`
   - raw positive-domain word/shift replay through `A<=15`;
   - every optimal median, not one median convention;
   - exact source/target reversal and cyclic normalization;
   - independent numerator/formula/full-`D` checks;
   - negative-domain sentinel.

`FAST_SUITE_OUTPUT.txt` is the frozen successful output.
