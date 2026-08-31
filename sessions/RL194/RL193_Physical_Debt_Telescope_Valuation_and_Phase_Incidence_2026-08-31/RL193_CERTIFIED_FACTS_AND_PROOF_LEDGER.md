# RL193 Certified Facts and Proof Ledger

Date: 2026-08-31

All physical assertions below are conditional on a hypothetical physical
terminal on the sole high branch `(37,0,23,-1)`.  Necessary-state survival is
never physical realization.

## Newly proved analytic mathematics

1. The complement of a tau=37 zero prefix has length `L-37`, mechanical sum
   `A-k-21` for start gap `2^k`, and weighted numerator
   `D=(2^A-3^L)/2^21` on both atoms.
2. Its physical weights telescope term by term to
   `D=(3^(L-37)/rho_terminal)(K_(start+L)-K_terminal)`.
   The zero-prefix identity and monodromy reproduce the required debt.
3. The first complementary error has valuation -21; all later weighted
   terms have valuation at least -20.  The total valuation is therefore -21
   automatically.  The stronger endpoint congruences remain total identities.
4. Over a base period `sum epsilon_i=1`; outside the zero prefix the ordinary
   unweighted sum is `2^(-h_z)-1`.
5. The complement has signed flow between zero and 1/2, while its carry
   contributes strictly more than 1/2.  The ordinary weighted net is strictly
   negative.  Its magnitude exceeds `72912057143/733007751850` on the
   `2^38` atom and `91625968981/733007751850` on the `2^37` atom; carry
   height at least one improves each bound by 1/4.
6. The canonical K-prefix flow is strictly positive on the `2^38` atom and
   strictly negative on the `2^37` atom.  The possible equality rank Q is
   excluded by the known canonical early-defect window.

## Exact finite certificates and coverage

The portable RL193 verifier uses exact integer/Fraction arithmetic.  It checks
all of the following complete finite domains, not sampled ranges:

- carry-prefix distances 1..37 for E and 1..35 for D_H21: 9 and 5 deletions;
- canonical known-zero phases 0..23 and every terminal whose zero prefix
  meets a known nonzero source in 24..29: 15 and 9 additional deletions;
- disjoint unions: 24 E ranks and 14 D_H21 ranks in total;
- remaining necessary-rank cardinalities: 31,021,168,209 and 18,406,412,825;
- canonical terminal floors 71 and 67, with all boundary cases checked;
- carry buffers after terminal / before next start: 11/5 for `2^38`, 4/7 for
  `2^37`;
- exact logarithm enclosure, cancellation constants, atom endpoints and
  `v_2(3^L-1)=10` by modular exponentiation.

The inherited RL178 necessary transition automaton is included byte-for-byte
and replayed over every transition from phase 24 through phase 30.  Its
certificate proves `G_24,...,G_28<0` and `G_29!=0`; it does not realize any
surviving state.  Its incoming classification remains **inherited exact finite
certificate**, not a newly discovered RL193 theorem.

## Method barriers

The displayed total weighted-debt and total-valuation identities alone do
not exclude either full-period atom.  They are conditionally automatic.
This does not rule out every future aggregate-flow argument.  Unsigned
variation cannot be turned into excursion without an ordering theorem.

## Inherited facts preserved

RL191 spacing at least 1001, `N35<=7559400754`, ordinary absolute flow
`>480`, directional K variation `>80`, and the H21 binding charging budget
are unchanged.  RL192's two-atom phase lock and nonphysical relaxed-witness
barrier remain valid.  The main report carries the load-bearing definitions,
constants, phase convention, corridor, and provenance.

## Still open / not certified

Physical existence or exclusion of either atom; a sign/rho ordering or owned
prefix congruence obstruction; stronger spacing; H21 physical incidence or
count; a chronological excursion theorem; the sole high branch, Gate A,
Gate B, and non-trivial-cycle/global Collatz closure.  No partial scan is
promoted and no uncovered range is described as complete.
