# RL195 independent red team — window reconstruction and denominator

Date: 2026-08-31. Research-stage review, **NOT PROMOTED**.
BASE_HEAD: `df980ce3df6fa3e8906a934692221917af25644a`.
Reviewer: independent owned-local-realizability worker.

## Verdict

**PASS. No mathematical or finite-coverage finding.** For a complete,
globally admissible height word at the stated constants, the candidate
correctly proves unique positive rational reconstruction and equality of
the orbit's common reduced odd denominator with the odd part of every
normalized p-gap denominator. One exactly dyadic gap is therefore equivalent
to full positive odd integrality.

The exact branch moment K0=2^37 triggers that implication only after a
complete globally admissible word exists. Neither existence nor impossibility
of such a word is supplied. Numerical intervals, local trajectory witnesses,
necessary prefix states and mere one-step height-rise bounds do not meet
those hypotheses. The proof preserves that distinction explicitly.

## Reviewed versions

- `PHYSICAL_WINDOW_RECONSTRUCTION_AND_DENOMINATOR.md`, SHA256
  `8d37a75f7dffc097115c4af94cc0421a1bf2b834a38dc24a0ef6624f2b31eb2f`.
- `SCOPE_AND_DEPENDENCIES.md`, SHA256
  `cf956c45db5e93700b446074725d0752be1c048e48a732799277b6c51b719d37`.
- `verify_rl195_window_reconstruction.py`, SHA256
  `f7959a2a7ae9c4c6575f6619da3ef0c928566d42549ee593a52db0606e2c7858`.

These three sources are under `.rl-work/RL195/agent_window_physical/`.
I read the complete proof, verifier and dependency note. Current RL194
main/weight proof/ledgers were already read for the preceding adjacency
review. Only the named frozen RL175 and RL181 live provenance was checked:
their explicit height/transport/owned-gap definitions, proof ledgers and
correction ledgers. No broad history or expensive historical scan occurred.

## Analytic checks

1. **Global admissibility is the right hypothesis.** With
   `h_i=floor(Ai/L)-S_i`, the law `a_i=c_i+h_i-h_(i+1)>=1` holds at every
   phase, including switches, carry and period boundary. The one-step
   height equation has no special p-gap carry term. Conversely a complete
   admissible height word defines cumulative S with S0=0 and S_L=A, so q
   has the required lift and recurrence. The weaker rise<=1 condition would
   not suffice at c=1 and is not substituted.

2. **Lifts and carry.** From Bezout, the floor increment over p is u0 at
   every noncarry source and u0+1 exactly at rankL-1 (phase z). Thus
   `alpha*rho_(i+p)/rho_i` is1 or2 respectively, giving the ordinary and
   carry formulas for Delta with the same lifted T coordinate. Crossing
   the canonical endpoint scales q,rho,T,K by lambda; y and h remain
   periodic. All windows and arc equations in the proof retain that lift.

3. **Transport and uniqueness.** The one-step affine equation gives
   `3(T_(i+1)-T_i)=q_i`, hence the p- and L-arc identities. For a given
   complete admissible word, `Y_i/[3(lambda-1)q_i]` is positive and periodic.
   Since `Y_(i+1)-Y_i=(lambda-1)q_i`, it satisfies the exact affine
   recurrence. Any periodic solution has the same full-period telescope,
   so uniqueness follows. This constructs rational states before any
   integrality claim. The positive-window inversion follows algebraically
   and supplies no independent equation. The stated squeeze follows from
   positive partial-arc mass strictly between0 and the full-period mass.

4. **Least-state statement.** At actual constants, canonical rho_i<1
   for i>0 and nonnegative h imply q_i<1. Positive arc increments give
   T_i>T0=y0. Thus y_i=T_i/q_i>y0. This conditional observation is valid
   for the rational reconstruction and does not imply integrality.

5. **Numerators and common denominator.** Expanding the lifted mass gives
   `y_i=R_i/D` with exactly the displayed integer sum R_i and
   `D=2^A-3^L`. Every a_i>=1 makes all noninitial summands even and the
   initial summand odd, so each R_i is positive odd. D is positive, odd,
   and coprime to3. The numerator recurrence gives
   `gcd(D,R_(i+1))=gcd(D,R_i)` because2 and3 are units moduloD. Thus the
   reduced denominator really is the same D_red at every phase; no
   unproved integrality propagation is hidden here.

6. **Symbolic Bezout unit.** If g divides D and `d=3^p-2^u0`, then
   `2^(Ap)=2^(u0L) (mod g)`. Their exponent difference is exactly1, so
   `g | 2^(u0L)*(2-1)`. Since g is odd, g=1. This proves the full gcd,
   including possible prime powers, and requires no enormous-integer
   computation. The argument does not infer coprimality merely from
   numerical small examples.

7. **Exact gap denominator.** The p-arc equation gives
   `Delta_i=(d*y_i+P_i)/2^(u0+h_i)` directly. Inserting R_i/D leaves the
   numerator `dR_i+P_iD`; its gcd withD is exactly gcd(D,R_i) by item6.
   Cancelling powers of two cannot alter any odd factor. Hence the odd
   part of the reduced denominator of every Delta_i is exactly D_red.
   This calculation also covers the carry because its p-arc is lifted.

8. **Equivalence and exact moment.** D_red=1 is equivalent to D|R0,
   one dyadic gap, and all gaps dyadic. If D divides all positive odd R_i,
   the quotients R_i/D are positive odd integers; their recurrence then
   makes each a_i the exact two-adic valuation, not merely a lower bound.
   Since rho0=1, the exact moment imposes the dyadic gap Delta0=K0=2^37
   and therefore integrality. The algebra does not require h_p=0, but that
   and all other branch anchors remain separate physical requirements.

## Independent and supplied executions

The supplied command ran PASS:

`python3 .rl-work/RL195/agent_window_physical/verify_rl195_window_reconstruction.py`

Its complete finite regression domain and counts are correct:
256 raw arrays,7 globally admissible toy words,35 cyclic gap checks,
175 source/arc-length checks; none of those7 words is odd-integral.
The separate trivial cycle has y0=K0=1 and supplies the positive integral
direction without claiming an actual high-branch example.

I also wrote and ran:

`python3 .rl-work/RL195/agent_owned_realizability/verify_window_independent.py`

SHA256:
`87b25aaed52379a05ec3fdd4e21fd2cbf17bc54de4e665c061a7df635c3c0813`.

This independent replay solves each cyclic affine map's fixed point by
composing its slope and intercept, rather than beginning with the candidate's
window formula. It then checks reconstruction, lifted transport, numerator
recurrences, exact carry, gcd cancellation and gap denominators. It
independently identifies the exact7 admissible height arrays and reproduces
all35/175 checks. All7 have common odd denominator13. The all-zero word
again gives y0=319/13 and K0=48/13; the separate integral case gives1.
The independent script and its syntax check both PASS.

## Provenance and scope conclusions

The q*y telescope and physical arc/full-closure identities are already
explicit in RL175.1. Corrected K and the normalized p-gap/carry chain are
already RL181.1. The reviewed text correctly labels those as inherited
and does not revive the sparse resultant as an independent obstruction.
The denominator argument is proved directly here without asserting broad
historical priority.

The initial research wording about odd-integrality always remaining an
additional test was corrected before this reviewed candidate; the final
two-regime statement is mathematically right. No inherited classification
is demoted or reinterpreted by that clarification.

No actual high-branch phase space is enumerated or certified by the toys.
No complete actual height word satisfying the exact moment is produced.
No atom realization/exclusion, H21 incidence, spacing improvement, branch
closure or global Collatz conclusion follows. Parent source files and
authority were not modified by this reviewer.
