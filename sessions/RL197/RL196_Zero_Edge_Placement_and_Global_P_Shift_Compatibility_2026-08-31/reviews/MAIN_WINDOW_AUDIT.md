# RL195 main-worker independent window/denominator audit

Date: 2026-08-31. NOT AUTHORITATIVE; bounded review of the independent
window-physical component. Reviewer: main worker; author: window agent.
Result: PASS. A further independent agent review is also requested.

Read the complete proof, scope/dependency note and verifier. Ran
`python3 .rl-work/RL195/agent_window_physical/verify_rl195_window_reconstruction.py`:
PASS (256 arrays,7 admissible words,35 cyclic gaps,175 arcs, trivial integral
one-cycle). These are toy algebra checks, not actual phase coverage.

Verified analytically:

1. The full periodic height law defines positive integer exponents and
   q_(i+1)=2^a_i q_i/3 with lambda lift, including switch/carry/seam. The
   q*y telescope is inherited, not a new claimed obstruction.
2. Y_i/[3(lambda-1)q_i] is the unique positive rational periodic affine
   solution; its prefix numerators R_i are positive odd integers because
   every cumulative nonempty exponent sum is at least1.
3. D is coprime to6 and the exact recurrence of R_i preserves gcd(D,R_i).
4. A common divisor of D and d must divide 2^(u0 L)(2-1), by Ap-u0L=1;
   it is odd, proving gcd(D,d)=1 without constructing the giant integers.
5. The p-arc formula gives Delta_i=(d*y_i+P_i)/2^(u0+h_i), with lifted
   source/target indexing. Its odd denominator is exactly the common
   reduced orbit denominator. Thus dyadic Delta implies positive odd
   integrality for the complete word, and the recurrence gives exact
   acceleration valuations.
6. At phase0, K0=Delta0. An exact fixed-K0 moment cannot be weakened to
   a numerical inequality in this equivalence. No local graph path or
   height-only countermodel supplies that complete exact normalization.

No missing case or mathematical correction found. The least-state and
relative-state squeeze observations retain their stated hypotheses; they
are not promoted to rank, H21 or cycle exclusions. Historical telescope
and owned-chain provenance is explicitly preserved, with no novelty claim
about unconsulted history.
