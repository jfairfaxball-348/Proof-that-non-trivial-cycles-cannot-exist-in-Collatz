#!/usr/bin/env python3
"""RL201 verified support: exact full-range H21 one-step successor-corridor certificate.

Only integer and Fraction arithmetic is used. The finite boundary assertions,
strict rank monotonicity, and monotonicity in nu cover every rank in D_K and
both signs for every nu=1,...,21; no rank scan or floating-point claim is used.
"""

from fractions import Fraction as Q
from functools import lru_cache

A = 217_976_794_617
L = 137_528_045_312
B = A-L
R = 2*L-A
p = 65_470_613_321
T = 7*3**35
KLO, KHI = 128_081_997_553, 146_795_909_391
DLO, DHI = 25_583_192_106, 41_775_866_136
M = 9*2**22


@lru_cache(maxsize=None)
def ln_bounds(x, terms=110):
    """Exact signed-tail enclosure of ln(x), x positive rational.

    For z=(x-1)/(x+1), the omitted atanh tail has sign(z) and absolute
    value <=2*abs(z)**(2*N+1)/((2*N+1)*(1-z*z)).
    """
    x = Q(x)
    assert x > 0
    assert isinstance(terms, int) and terms > 0
    z = (x-1)/(x+1)
    z2 = z*z
    term = z
    partial = Q(0)
    for j in range(terms):
        partial += term/(2*j+1)
        term *= z2
    partial *= 2
    tail = 2*abs(term)/((2*terms+1)*(1-z2))
    return (partial, partial+tail) if z >= 0 else (partial-tail, partial)


def mul(c, bounds):
    lo, hi = bounds
    return (c*lo, c*hi) if c >= 0 else (c*hi, c*lo)


LN2 = ln_bounds(2)
LN3 = ln_bounds(3)
LN87 = ln_bounds(Q(8, 7))


@lru_cache(maxsize=None)
def log_k_over_u(r, u):
    """Enclose ln[(rho(r)*T/2**21)/u], u a positive rational."""
    i = p*r % L
    n = (A*i-r)//L
    assert 0 <= r < L and A*i == n*L+r
    ulog = ln_bounds(Q(u)/2**37)
    pieces = [mul(n-55, LN2), mul(35-i, LN3),
              (-LN87[1], -LN87[0]), (-ulog[1], -ulog[0])]
    return sum(x[0] for x in pieces), sum(x[1] for x in pieces)


def log_successor_over_u(r, sign, nu, u):
    assert sign in (-1, 1) and 1 <= nu <= 21
    # Ksucc/Kterminal = (3*T + sign*(2**nu-1))/(3*T).
    factor = Q(3*T + sign*(2**nu-1), 3*T)
    assert factor > 0
    return log_k_over_u(r, Q(u)/factor)


def assert_k_interval(r, lo, hi):
    assert lo < hi
    assert log_k_over_u(r, Q(lo))[0] > 0
    assert log_k_over_u(r, Q(hi))[1] < 0


def assert_increment_interval(r, nu, lo, hi):
    # d_nu(r) = Kterminal(r)*(2**nu-1)/(3*T).
    scale = Q(3*T, 2**nu-1)
    assert lo < hi
    assert log_k_over_u(r, Q(lo)*scale)[0] > 0
    assert log_k_over_u(r, Q(hi)*scale)[1] < 0


def v2(n):
    assert n > 0
    return (n & -n).bit_length()-1


def eta_residue_for_exact_nu(cls, nu):
    """Unique class-compatible eta mod 9*2**(nu+1) with exact valuation nu."""
    assert cls in (0, 8, 9, 17) and nu >= 1
    m = 2**(nu+1)
    # Multiplication by odd 3**34 leaves 2**nu unchanged modulo 2**(nu+1).
    s = (pow(3**34, -1, m)+2**nu) % m
    a = (s-(21 if cls % 2 == 0 else 0)) % m
    eta = a+m*((cls % 9-a)*pow(m, -1, 9) % 9)
    assert 0 <= eta < 9*m
    assert eta % 18 == cls
    return eta


def main():
    assert p*B % L == 1
    assert T == 350_220_815_692_997_949
    delta_lo = A*LN2[0]-L*LN3[1]
    delta_hi = A*LN2[1]-L*LN3[0]
    assert 0 < delta_lo < delta_hi < Q(1, 2**40)
    assert LN2[0] > L*delta_hi
    # Thus for r<s, log rho(r)-log rho(s) > (ln2-L*delta)/L >0.
    # Multiplication by any positive fixed successor coefficient preserves
    # strict reverse-rank ordering.

    # Canonical chronological wrap i=L-1 occurs at exactly r=R.
    seam_rank = ((L-1)*B) % L
    assert seam_rank == R == 57_079_296_007
    assert DHI < R
    assert (p*DLO) % L == 80_277_474_042
    # No one-step successor under test needs a wrap/twist normalization.

    # Corrected inherited logarithm support: negative-argument reciprocal
    # symmetry, all used RL200 assertions, and conservative used-sidedness.
    x = Q(KLO, 2**37)
    direct, inverse = ln_bounds(x), ln_bounds(1/x)
    assert direct == (-inverse[1], -inverse[0])
    assert log_k_over_u(DLO-1, KHI)[0] > 0
    assert log_k_over_u(DLO, KHI)[1] < 0
    corrected_lower = log_k_over_u(DHI, KLO)[0]
    original_used_lower = corrected_lower-(direct[1]-direct[0])
    assert 0 < original_used_lower < corrected_lower
    assert Q(KHI, 2**37) > 1

    # Rational wall-gap certificates, with each endpoint an exact decimal
    # rational. These certify the displayed micron-scale enclosures.
    assert_k_interval(DLO,
                      Q("146795909390.833454"), Q("146795909390.833455"))
    assert_k_interval(DLO+1,
                      Q("146795909390.024478"), Q("146795909390.024479"))
    assert_k_interval(DHI,
                      Q("135291469824.745576"), Q("135291469824.745577"))
    assert_increment_interval(DLO, 20, Q("0.146504"), Q("0.146505"))
    assert_increment_interval(DLO, 21, Q("0.293008"), Q("0.293009"))
    assert_increment_interval(DHI, 21, Q("0.270045"), Q("0.270046"))

    # Four exact boundary tests give complete coverage. Positive increments
    # cannot break KLO and negative increments cannot break KHI.
    assert log_successor_over_u(DLO, 1, 20, KHI)[1] < 0
    assert log_successor_over_u(DLO, 1, 21, KHI)[0] > 0
    assert log_successor_over_u(DLO+1, 1, 21, KHI)[1] < 0
    assert log_successor_over_u(DHI, -1, 21, KLO)[0] > 0

    for nu in range(1, 22):
        d = 2**nu-1
        assert 0 < d <= 2**21-1 < 3*T
        assert 0 < Q(3*T-d, 3*T) < 1 < Q(3*T+d, 3*T)
        # Check every nu explicitly at the only potentially restrictive
        # upper boundary. Monotonicity covers all intermediate ranks.
        if nu <= 20:
            assert log_successor_over_u(DLO, 1, nu, KHI)[1] < 0
        else:
            assert log_successor_over_u(DLO, 1, nu, KHI)[0] > 0
        assert log_successor_over_u(DLO+1, 1, nu, KHI)[1] < 0
        assert log_successor_over_u(DHI, -1, nu, KLO)[0] > 0

    retained_deletions = {
        26_058_127_773, 26_058_127_774, 28_746_802_249, 28_746_802_250,
        31_435_476_726, 34_124_151_202, 36_398_517_184, 36_398_517_185,
        36_812_825_678, 39_087_191_660, 39_087_191_661, 41_775_866_136,
    }
    assert len(retained_deletions) == 12
    assert DLO not in retained_deletions
    assert all(DLO <= r <= DHI for r in retained_deletions)
    assert DHI-DLO+1-len(retained_deletions) == 16_192_674_019

    # Translate the sole forbidden (rank,+,21) tuple into eta lifts.
    assert pow(3**34, -1, 2**22) == 1_893_305
    odd_parameter_residue = (1_893_305+2**21) % 2**22
    assert odd_parameter_residue == 3_990_457
    assert (odd_parameter_residue-21) % 2**22 == 3_990_436
    removed = {cls: eta_residue_for_exact_nu(cls, 21) for cls in (0, 8)}
    assert removed == {0: 37_544_868, 8: 20_767_652}
    old_hensel_even = {0: 18_670_500, 8: 1_893_284}
    assert all((removed[c]-old_hensel_even[c]) % M == M//2 for c in (0, 8))

    # CRT supplies every class and every valuation before this corridor
    # test; representatives with nu<=20 remain in each class at DLO.
    # Adding arbitrary positive multiples of 9*2**(nu+1) preserves them.
    for cls in (0, 8, 9, 17):
        for nu in range(1, 22):
            eta = eta_residue_for_exact_nu(cls, nu)
            if eta == 0:
                eta += 9*2**(nu+1)
            s = eta+21 if cls % 2 == 0 else eta
            assert v2(3**34*s-1) == nu
            assert eta % 18 == cls
            ylo, yhi = 2**34*eta-1, 2**34*(eta+21)-1
            a35 = 1 if cls % 9 == 0 else 2
            for y in (ylo, yhi):
                z_numerator = 2**a35*y-1
                assert z_numerator % 3 == 0
                z = z_numerator//3
                assert z > 0 and z % 2 == 1 and z % 3 != 0

    print("PASS RL201 exact H21 signed successor-corridor certificate")
    print("rank_range=[25583192106,41775866136]; signs=+,-; nu=1..21")
    print("canonical_chronological_wrap_rank=57079296007; outside_core=yes")
    print("only_excluded_tuple=(rank=25583192106,sign=+,nu=21)")
    print("new_eta_residue_exclusions_at_first_rank={0:37544868,8:20767652} mod 37748736")
    print("first_rank_upper_wall_gap=(0.166545,0.166546)")
    print("next_rank_upper_wall_gap=(0.975521,0.975522)")
    print("last_rank_lower_wall_gap=(7209472271.745576,7209472271.745577)")
    print("max_increment_at_first_rank=(0.293008,0.293009)")
    print("newly_removed_entire_ranks=0; eta_mod18_classes_removed=0")
    print("remaining_necessary_ranks=16192674019; no_physical_realization_claim=yes")
    print("log_helper_contract_repaired=yes; inherited_conclusion_demotion=none")


if __name__ == "__main__":
    main()
