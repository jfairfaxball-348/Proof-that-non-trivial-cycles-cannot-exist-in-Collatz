#!/usr/bin/env python3
"""RL195 exact mechanical-zero geometry checks.

No physical orbit or full-branch realization is certified. Actual-rank
cells certify only a height/count relaxation witness. Small height arrays
are complete algebraic regression tests on their stated bounded domain.
"""

from fractions import Fraction as F
from itertools import product
from math import gcd


A = 217_976_794_617
L = 137_528_045_312
B = A - L
R = L - B
p = 65_470_613_321
u0 = 103_768_467_013
z = L - p
INCOMING_N0_FLOOR = 43_742_681_439


def mechanical_bit(i, a=A, length=L):
    return a * (i + 1) // length - a * i // length


def actual_constants():
    assert (B, R, B - R) == (80_448_749_305, 57_079_296_007, 23_369_453_298)
    assert gcd(B, L) == 1
    assert A * p - u0 * L == 1
    assert B * p % L == 1
    assert 1 < R < B < 2 * R < L < 3 * R
    assert (B * (p - 1)) % L == R + 1
    assert (B * (L - 1)) % L == R
    assert mechanical_bit(p - 1) == mechanical_bit(L - 1) == 2
    assert p * (R - 1) % L == z - 1
    assert p * (2 * R - 1) % L == z - 2
    assert mechanical_bit(z - 2) == 2
    assert mechanical_bit(z - 1) == 1
    assert mechanical_bit(0) == 1
    assert mechanical_bit(1) == 2
    assert mechanical_bit(p) == 1
    assert z == 72_057_431_991


def cells_for_rank_boundaries(boundaries, offsets):
    """Every shifted indicator is constant on each returned integer cell."""
    cuts = {0, L}
    for boundary in boundaries:
        for offset in offsets:
            cuts.add((boundary - offset * B) % L)
    ordered = sorted(cuts)
    cells = list(zip(ordered[:-1], ordered[1:]))
    assert cells[0][0] == 0 and cells[-1][1] == L
    assert all(left < right for left, right in cells)
    assert sum(right - left for left, right in cells) == L
    return cells


def word_cells():
    cells = cells_for_rank_boundaries((0, R), (0, 1, 2))
    populations = {}
    for left, right in cells:
        def signature(rank):
            return tuple(1 if (rank + j * B) % L < R else 2 for j in range(3))

        word = signature(left)
        assert signature(right - 1) == word
        assert word[:2] != (1, 1)
        assert word[1:] != (1, 1)
        assert word != (2, 2, 2)
        populations[word] = populations.get(word, 0) + right - left
    assert sum(populations.values()) == L
    assert sum(count for word, count in populations.items() if word[0] == 1) == R
    assert sum(count for word, count in populations.items() if word[:2] == (2, 2)) == L - 2 * R
    return len(cells), populations


def actual_one_edge_countermodel():
    # Z={0} union [R+1,2R), specified in rank coordinates.
    def height(rank):
        return 0 if rank == 0 or R + 1 <= rank < 2 * R else 1

    cells = cells_for_rank_boundaries((0, 1, R, R + 1, 2 * R), (0, 1))
    zero_count = edge_count = exponent_sum = 0
    for left, right in cells:
        def signature(rank):
            h = height(rank)
            next_h = height((rank + B) % L)
            c = 1 if rank < R else 2
            a = h + c - next_h
            return h, next_h, c, a

        h, next_h, c, a = signature(left)
        assert signature(right - 1) == (h, next_h, c, a)
        assert 1 <= a <= h + c
        multiplicity = right - left
        zero_count += multiplicity * (h == 0)
        edge_count += multiplicity * (h == next_h == 0)
        exponent_sum += multiplicity * a
    assert height(0) == height(B) == 0
    assert height(R) == 1  # phase L-1 is not zero.
    assert zero_count == R > INCOMING_N0_FLOOR
    assert edge_count == 1
    assert exponent_sum == A
    return len(cells), zero_count, edge_count


def actual_zero_free_window_countermodel():
    # h=1 exactly on [2,p+2). Only its two boundary transitions differ
    # from a_i=c_i; their exponents change by -1 and +1.
    assert 0 < 1 < 2 < p + 1 < p + 2 < L
    assert mechanical_bit(1) == 2
    entrance_a = mechanical_bit(1) - 1
    exit_a = mechanical_bit(p + 1) + 1
    assert entrance_a >= 1 and exit_a >= 1
    assert (p + 2) - 2 == p
    assert L - p > INCOMING_N0_FLOOR
    assert (entrance_a - mechanical_bit(1)) + (exit_a - mechanical_bit(p + 1)) == 0
    return L - p


def toy_regression():
    a, length, shift, bezout = 8, 5, 2, 3
    b, rcut = a - length, 2 * length - a
    carry = length - shift
    lam = F(2**a, 3**length)
    alpha = F(3**shift, 2**bezout)
    eta, theta = alpha - 1, lam * alpha - 1
    assert a * shift - bezout * length == 1
    assert 0 < eta < theta
    phase = [(shift * rank) % length for rank in range(length)]
    rho = [F(2 ** (a * i // length), 3**i) for i in range(length)]
    weights = [rho[i] for i in phase]
    d = {rank: weights[rank - 1] - weights[rank] for rank in range(1, length)}
    bits = [mechanical_bit(i, a, length) for i in range(length)]
    assert bits == [1, 2, 1, 2, 2]
    assert all(0 < value < theta for value in d.values())
    for rank in range(1, length):
        i = phase[rank]
        assert d[rank] == (theta if i < shift else eta) * rho[i]
    for rank in range(1, rcut):
        assert d[rank + b] == F(2, 3) * d[rank]
    assert d[b] == F(2, 3) * theta
    for rank in range(2 * rcut, length):
        assert d[rank - rcut] == F(4, 3) * d[rank]
    capacity = sum((d[rank] for rank in range(rcut, 2 * rcut)), F(0))
    assert capacity == weights[rcut - 1] - weights[2 * rcut - 1]
    assert capacity == F(3, 16) * lam * alpha
    assert phase[rcut - 1] == carry - 1
    assert phase[2 * rcut - 1] == carry - 2

    # Full binary local-dual domain and thresholds on both sides of each
    # breakpoint. Exact rationals only.
    dual_cases = 0
    for rank in range(1, rcut):
        lo, hi = d[rank], d[rank + b]
        for t in (F(0), hi / 2, hi, (lo + hi) / 2, lo, 2 * lo):
            direct = max(F(0), hi - t, lo + hi - 2 * t)
            assert direct == max(F(0), F(5, 3) * lo - 2 * t)
            dual_cases += 1
    for rank in range(2 * rcut, length):
        small, large = d[rank], d[rank - rcut]
        for u, v in product((0, 1), repeat=2):
            assert small * u + large * v <= large + small * u * v

    tested_arrays = legal_arrays = 0
    for tail in product(range(4), repeat=length - 1):
        heights = (0,) + tail
        tested_arrays += 1
        exponents = [heights[i] + bits[i] - heights[(i + 1) % length] for i in range(length)]
        if min(exponents) < 1:
            continue
        legal_arrays += 1
        assert sum(exponents) == a
        assert heights[1] == 0 and exponents[0] == 1
        x = [int(h == 0) for h in heights]
        edges = [x[i] * x[(i + 1) % length] for i in range(length)]
        assert edges[0] == 1
        for rank in range(rcut):
            i, j = phase[rank], phase[rank + b]
            assert j == (i + 1) % length
            assert heights[j] <= heights[i]
            assert x[i] <= x[j]
            assert edges[i] == x[i]
        Z0 = sum((d[rank] * x[phase[rank]] for rank in range(1, length)), F(0))
        selected_sources = list(range(1, rcut)) + list(range(2 * rcut, length))
        extra = sum((d[rank] * edges[phase[rank]] for rank in selected_sources), F(0))
        J = sum(edges)
        assert Z0 <= capacity + extra <= capacity + theta * (J - 1)
        if J > 1:
            assert Z0 < capacity + theta * (J - 1)
        if Z0 > capacity:
            assert J > 1
            assert F(J - 1) > (Z0 - capacity) / theta
    assert tested_arrays == 256
    assert legal_arrays > 0

    # The sharp one-edge relaxed witness also works for this toy, but it
    # is not asserted to meet the physical fixed-K0 moment.
    toy_zero_ranks = {0} | set(range(rcut + 1, 2 * rcut))
    toy_h = [0 if (i * b) % length in toy_zero_ranks else 1 for i in range(length)]
    toy_x = [int(h == 0) for h in toy_h]
    assert sum(toy_x) == rcut
    assert sum(toy_x[i] * toy_x[(i + 1) % length] for i in range(length)) == 1
    assert sum((d[rank] * toy_x[phase[rank]] for rank in range(1, length)), F(0)) == capacity - d[rcut]
    return tested_arrays, legal_arrays, dual_cases


if __name__ == "__main__":
    actual_constants()
    word_cell_count, populations = word_cells()
    witness_cells, N0, J = actual_one_edge_countermodel()
    window_N0 = actual_zero_free_window_countermodel()
    tested, legal, dual_cases = toy_regression()
    print("actual_constants_and_boundary_exceptions=PASS")
    print(f"mechanical_word_rank_cells={word_cell_count}")
    print(f"mechanical_word_populations={sorted(populations.items())}")
    print(f"relaxed_witness_rank_cells={witness_cells}")
    print(f"relaxed_witness_N0={N0}; J={J}; sum_a={A}")
    print(f"relaxed_zero_free_p_window=[2,{p + 2}); N0={window_N0}")
    print(f"toy_height_arrays_tested={tested}; height_admissible={legal}; local_dual_cases={dual_cases}")
    print("matching_doublets_capacity_boundary_and_dual=PASS")
    print("classification=analytic_geometry_and_explicit_relaxation_barriers")
    print("physical_realization_or_H21_ownership=NOT_CLAIMED")
