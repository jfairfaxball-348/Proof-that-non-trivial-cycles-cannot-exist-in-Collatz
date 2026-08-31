#!/usr/bin/env python3
"""RL195 exact rational reconstruction / odd-denominator regressions.

This checks proofs on seven bounded toy height words and the
trivial one-cycle, not on any range of the actual high-branch phase space.
The actual large-number coprimality result has a symbolic Bezout proof.
"""

from fractions import Fraction as F
from itertools import product
from math import gcd


ACTUAL_A = 217_976_794_617
ACTUAL_L = 137_528_045_312
ACTUAL_P = 65_470_613_321
ACTUAL_U = 103_768_467_013
assert ACTUAL_A * ACTUAL_P - ACTUAL_U * ACTUAL_L == 1
assert 0 < ACTUAL_P < ACTUAL_L
assert ACTUAL_U >= 0


def odd_part(n):
    assert isinstance(n, int) and n > 0
    while n % 2 == 0:
        n //= 2
    return n


def verify_word(a_total, length, shift, bezout, heights):
    assert len(heights) == length and heights[0] == 0
    assert all(isinstance(h, int) and h >= 0 for h in heights)
    assert a_total * shift - bezout * length == 1
    assert 0 < shift <= length and bezout >= 0
    mechanical = [
        a_total * (i + 1) // length - a_total * i // length
        for i in range(length)
    ]
    acceleration = [
        mechanical[i] + heights[i] - heights[(i + 1) % length]
        for i in range(length)
    ]
    assert min(acceleration) >= 1
    assert sum(acceleration) == a_total

    D = 2**a_total - 3**length
    d = 3**shift - 2**bezout
    assert D > 0 and gcd(D, 6) == 1 and gcd(D, d) == 1
    lam = F(2**a_total, 3**length)
    alpha = F(3**shift, 2**bezout)
    beta = (alpha - 1) / (lam - 1)
    assert alpha > 1

    def local_sum(i, n):
        return sum(acceleration[(i + k) % length] for k in range(n))

    def numerator(i, n):
        return sum(
            3 ** (n - 1 - k) * 2 ** local_sum(i, k)
            for k in range(n)
        )

    canonical_rho = [
        F(2 ** (a_total * i // length), 3**i) for i in range(length)
    ]
    canonical_q = [
        canonical_rho[i] / 2 ** heights[i] for i in range(length)
    ]
    for i in range(length):
        assert canonical_q[i] == F(2 ** local_sum(0, i), 3**i)

    def q(i):
        turns, phase = divmod(i, length)
        return lam**turns * canonical_q[phase]

    def rho(i):
        turns, phase = divmod(i, length)
        return lam**turns * canonical_rho[phase]

    def mass(i, n):
        return sum((q(i + j) for j in range(n)), F(0))

    def reconstructed_y(i):
        return mass(i, length) / (3 * (lam - 1) * q(i))

    def T(i):
        return q(i) * reconstructed_y(i)

    def K(i):
        return (alpha * mass(i, shift) + beta * mass(i, length)) / 3

    D_red = D // gcd(D, numerator(0, length))
    integral_orbit = D_red == 1
    gap_tests = 0
    arc_tests = 0
    for i in range(length):
        yi = reconstructed_y(i)
        assert yi > 0 and yi == reconstructed_y(i + length)
        assert numerator(i, length) > 0 and numerator(i, length) % 2 == 1
        assert yi == F(numerator(i, length), D)
        assert yi.denominator == D_red
        assert 3 * yi + 1 == 2 ** acceleration[i] * reconstructed_y(i + 1)
        assert 2 ** acceleration[i] * numerator(i + 1, length) == (
            3 * numerator(i, length) + D
        )
        assert q(i + 1) == F(2 ** acceleration[i], 3) * q(i)
        assert 3 * (T(i + 1) - T(i)) == q(i)
        assert 3 * (lam - 1) * T(i) == mass(i, length)
        assert K(i) == alpha * T(i + shift) - T(i)
        assert K(i + length) == lam * K(i)

        delta = K(i) / rho(i)
        expected = (d * yi + numerator(i, shift)) / 2 ** (bezout + heights[i])
        assert delta == expected
        assert odd_part(delta.denominator) == D_red
        assert (odd_part(delta.denominator) == 1) == integral_orbit

        target = (i + shift) % length
        carry = 1 if i == length - shift else 0
        owned_delta = F(2**carry) * reconstructed_y(target) / 2 ** heights[target]
        owned_delta -= yi / 2 ** heights[i]
        assert delta == owned_delta

        if shift < length:
            assert 1 < T(i + shift) / T(i) < lam
            assert alpha - 1 < K(i) / T(i) < lam * alpha - 1

        if integral_orbit:
            assert yi.denominator == 1 and yi.numerator % 2 == 1
            value = 3 * yi.numerator + 1
            exact_valuation = 0
            while value % 2 == 0:
                exact_valuation += 1
                value //= 2
            assert exact_valuation == acceleration[i]
            assert value == reconstructed_y(i + 1)

        for n in range(1, length + 1):
            assert 3 * (T(i + n) - T(i)) == mass(i, n)
            assert 2 ** local_sum(i, n) * reconstructed_y(i + n) == (
                3**n * yi + numerator(i, n)
            )
            arc_tests += 1
        gap_tests += 1

    assert K(0) == (
        reconstructed_y(shift) / 2 ** heights[shift % length] - reconstructed_y(0)
        if shift < length
        else reconstructed_y(0)
    )
    assert odd_part(K(0).denominator) == D_red
    return reconstructed_y(0), K(0), gap_tests, arc_tests, integral_orbit


raw_arrays = 0
admissible_arrays = 0
total_gaps = 0
total_arcs = 0
integral_toys = 0
all_zero_output = None
for tail in product(range(4), repeat=4):
    raw_arrays += 1
    heights = (0,) + tail
    digits = [8 * (i + 1) // 5 - 8 * i // 5 for i in range(5)]
    exponents = [digits[i] + heights[i] - heights[(i + 1) % 5] for i in range(5)]
    if min(exponents) < 1:
        continue
    result = verify_word(8, 5, 2, 3, heights)
    admissible_arrays += 1
    total_gaps += result[2]
    total_arcs += result[3]
    integral_toys += int(result[4])
    if heights == (0, 0, 0, 0, 0):
        all_zero_output = result[:2]

assert raw_arrays == 256
assert admissible_arrays == 7
assert total_gaps == 35
assert total_arcs == 175
assert integral_toys == 0
assert all_zero_output == (F(319, 13), F(48, 13))

# The positive integral direction is also exercised, without representing
# the trivial one-cycle as a nontrivial actual-constant branch witness.
one_cycle = verify_word(2, 1, 1, 1, (0,))
assert one_cycle == (F(1), F(1), 1, 1, True)

print("PASS RL195 physical-window reconstruction / denominator checks")
print("actual_Bezout_identity=PASS; actual_giant_D_not_constructed")
print("toy_arrays=256; globally_admissible_toy_words=7")
print("toy_cyclic_gap_checks=35; toy_arc_checks=175; integral_toy_words=0")
print("all_zero_toy_y0=319/13; all_zero_toy_K0=48/13")
print("positive_integral_regression=trivial_one_cycle_only")
print("scope=analytic_reconstruction_and_denominator_equivalence_with_toy_regressions")
print("no actual-phase scan, atom realization, H21 count, or closure")
