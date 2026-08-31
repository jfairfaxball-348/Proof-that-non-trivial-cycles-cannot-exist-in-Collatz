#!/usr/bin/env python3
"""RL194 exact checks; no physical realization claim.

Actual-constant calculations use Fraction enclosures only.  Toy checks
exhaust 256 bounded height arrays and certify only their algebraic identities.
The general proofs are in proofs/RL194_WEIGHT_ORDER_AND_ZERO_HEIGHT_OCCUPATION.md.
"""

from fractions import Fraction as F
from itertools import product


A = 217_976_794_617
L = 137_528_045_312
p = 65_470_613_321
u0 = 103_768_467_013
K0 = 2**37


def ln_bounds_integer(n, terms=80):
    t = F(n - 1, n + 1)
    term = t
    total = F(0)
    for k in range(terms):
        total += term / (2 * k + 1)
        term *= t * t
    lower = 2 * total
    upper = lower + 2 * term / ((2 * terms + 1) * (1 - t * t))
    return lower, upper


def expm1_bounds(x_lower, x_upper):
    assert 0 < x_lower < x_upper < 1
    lower = x_lower + x_lower * x_lower / 2
    upper = x_upper + x_upper * x_upper / (2 * (1 - x_upper / 3))
    return lower, upper


assert A * p - u0 * L == 1
assert 0 < p < L
assert p < 2**39
assert (L - p) * (A - L) % L == L - 1

ln2_lo, ln2_hi = ln_bounds_integer(2)
ln3_lo, ln3_hi = ln_bounds_integer(3)
assert ln2_lo > F(1, 2)
delta_lo = A * ln2_lo - L * ln3_hi
delta_hi = A * ln2_hi - L * ln3_lo
assert 0 < delta_lo < delta_hi < F(1, 2**40)

# x=ln(alpha) and y=ln(lambda*alpha).  Form y directly with
# positive delta coefficient, so all interval endpoints are justified.
x_lo = (ln2_lo - p * delta_hi) / L
x_hi = (ln2_hi - p * delta_lo) / L
y_lo = (ln2_lo + (L - p) * delta_lo) / L
y_hi = (ln2_hi + (L - p) * delta_hi) / L
assert 0 < x_lo < x_hi < y_lo < y_hi < 1

lambda_minus_one_lo, lambda_minus_one_hi = expm1_bounds(delta_lo, delta_hi)
eta_lo, eta_hi = expm1_bounds(x_lo, x_hi)
theta_lo, theta_hi = expm1_bounds(y_lo, y_hi)
assert 0 < eta_hi < theta_lo

alpha_lo, alpha_hi = 1 + eta_lo, 1 + eta_hi
beta_lo = eta_lo / lambda_minus_one_hi
beta_hi = eta_hi / lambda_minus_one_lo
assert 0 < beta_lo < beta_hi

# Q bounds use 0<P<Q in 3K0=beta*Q+alpha*P.
Q_lower = 3 * K0 / (beta_hi + alpha_hi)
Q_upper = 3 * K0 / beta_lo
assert F(67_236_063_233) < Q_lower < Q_upper < F(80_336_439_250)

# F is the physical full-period flow, not an arbitrary relaxed total.
flow_lo = 3 * K0 * lambda_minus_one_lo
flow_hi = 3 * K0 * lambda_minus_one_hi
assert 0 < flow_lo < flow_hi < F(1, 2)

# M=2F-3rho_z+1=2F-1/2-3theta/2 must be positive
# before applying a strict per-zero-rank weight bound.
M_lower = 2 * flow_lo - F(1, 2) - 3 * theta_hi / 2
assert M_lower > 0
count_threshold_lower = (2 * flow_lo - F(1, 2)) / theta_hi - F(3, 2)
assert F(43_742_681_437) < count_threshold_lower
assert count_threshold_lower < F(43_742_681_438)
certified_N0_floor = 43_742_681_439
assert certified_N0_floor == 43_742_681_437 + 2
assert 2 * certified_N0_floor - L < 0


def toy_checks():
    a, length, shift, bezout = 8, 5, 2, 3
    carry = length - shift
    lam = F(2**a, 3**length)
    alpha = F(3**shift, 2**bezout)
    eta = alpha - 1
    theta = lam * alpha - 1
    beta = eta / (lam - 1)
    assert a * shift - bezout * length == 1
    assert 1 < alpha < lam * alpha

    rho = [F(2 ** (a * i // length), 3**i) for i in range(length)]
    phase = [(shift * r) % length for r in range(length)]
    w = [rho[i] for i in phase]
    d = [w[r - 1] - w[r] for r in range(1, length)]
    assert phase[-1] == carry
    assert w[-1] == lam * alpha / 2
    assert all(0 < weight < theta for weight in d)
    for r in range(1, length):
        i = phase[r]
        expected = alpha if i >= shift else lam * alpha
        assert w[r - 1] / w[r] == expected

    arrays_checked = 0
    rank_boundaries_checked = 0
    for heights_tail in product(range(4), repeat=length - 1):
        heights = (0,) + heights_tail
        values = [F(1, 2**h) for h in heights]
        canonical_q = [rho[i] * values[i] for i in range(length)]

        def q(i):
            turns, index = divmod(i, length)
            return lam**turns * canonical_q[index]

        def C(i):
            return sum((q(j) for j in range(i, i + shift)), F(0))

        def Y(i):
            return sum((q(j) for j in range(i, i + length)), F(0))

        def K(i):
            return (alpha * C(i) + beta * Y(i)) / 3

        physical_flow = []
        for i in range(length):
            error = values[(i + shift) % length] - values[i]
            if i == carry:
                error += 1
            f = rho[i] * error
            physical_flow.append(f)
            assert f == alpha * q(i + shift) - q(i)
            assert f == 3 * (K(i + 1) - K(i))
            assert K(i + length) == lam * K(i)

        V = [values[i] for i in phase]
        for m in range(1, length):
            direct = sum((w[r] * (V[r + 1] - V[r]) for r in range(m)), F(0))
            sbp = -w[m - 1] * (1 - V[m]) - sum(
                (d[r - 1] * (1 - V[r]) for r in range(1, m)), F(0)
            )
            assert direct == sbp <= 0
            assert (direct == 0) == all(V[r] == 1 for r in range(1, m + 1))
            rank_boundaries_checked += 1

        total = sum(physical_flow, F(0))
        rank_moment = theta + sum((d[r - 1] * V[r] for r in range(1, length)), F(0))
        canonical_moment = theta + eta * sum(canonical_q[shift:], F(0))
        canonical_moment += theta * sum(canonical_q[1:shift], F(0))
        assert total == rank_moment == canonical_moment
        assert total == 3 * (lam - 1) * K(0)
        assert 3 * K(0) == alpha * C(0) + beta * Y(0)
        assert 3 * K(0) / (alpha + beta) < Y(0) < 3 * K(0) / beta

        for start in range(length):
            prefix_q = sum(canonical_q[:start], F(0))
            prefix_f = sum(physical_flow[:start], F(0))
            assert prefix_f == alpha * (C(start) - C(0)) + eta * prefix_q

        Z0 = sum((d[r - 1] for r in range(1, length) if V[r] == 1), F(0))
        zero_count = sum(h == 0 for h in heights)
        M = 2 * total - 3 * w[-1] + 1
        assert Z0 >= M
        if M > 0:
            assert zero_count > 1
            assert Z0 < theta * (zero_count - 1)
            assert zero_count - 1 > (2 * total - F(1, 2)) / theta - F(3, 2)

        arrays_checked += 1

    assert arrays_checked == 256
    assert rank_boundaries_checked == 1024

    # Both arrays obey the basic cyclic height-rise law, but are NOT
    # candidates for the actual constants, early signature or branch K0.
    # They prove only that rank-prefix sign must not be substituted for
    # chronological-prefix sign under the bare rank-order hypotheses.
    for heights, expected in (
        ((0, 1, 0, 0, 0), F(1, 3)),
        ((0, 0, 1, 0, 0), F(-1, 2)),
    ):
        assert all(heights[(i + 1) % length] <= heights[i] + 1 for i in range(length))
        values = [F(1, 2**h) for h in heights]
        flow_before_two = sum(
            (rho[i] * (values[(i + shift) % length] - values[i]) for i in range(2)), F(0)
        )
        assert flow_before_two == expected

    return arrays_checked, rank_boundaries_checked


toy_arrays, toy_boundaries = toy_checks()
print("PASS RL194 rank-weight / positive-window / occupation checks")
print("alpha>1; theta>eta>0; unique carry included exactly")
print("Q_lower=67236063233 (strict); Q_upper=80336439250 (strict)")
print("actual_zero_height_count_N0>=43742681439 (conditional on physical branch)")
print(f"toy_algebra_arrays={toy_arrays}; all_rank_boundaries={toy_boundaries}")
print("no actual-phase scan; no realization; no H21 clean-start/count or budget claim")
print("scope=conditional_analytic_identities_and_exact_constant_checks")
