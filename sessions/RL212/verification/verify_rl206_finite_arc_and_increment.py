#!/usr/bin/env python3
"""Exact finite sanity checks for RL206, using only the Python standard library.

Scope: all binary words of lengths 1..10, with arc parameters t=0,1,2,17;
the subset with 0<L<A, D=2^A-3^L>0 and gcd(A,L)>1 for rational block algebra;
one separately specified RL20 length-184 fake, without rotation-distance scans.

Passing these finite checks is not the proof of any infinite lattice theorem,
residual-family theorem, global Gate, primitive-cycle exclusion, or Collatz claim.
The root's written analytic proof must supply all infinite quantifiers.

RL206-C1 correction tested here:
H[j+1]-H[j] = z**j * 3**(-E[j+1]) * Q(B[j]) / Y.
"""

from fractions import Fraction
from itertools import product
from math import gcd
import json


MAX_LENGTH = 10
T_VALUES = (0, 1, 2, 17)
FAKE_REMAINDER = 322171738410077807581692882247758374512983113782519312
FAKE_ENDPOINT_RESIDUE_WITNESS = 2361183241434822606907
F = Fraction


def raw_q(word):
    """Raw Q from the independent one-position/rank formula."""
    ones = [i for i, bit in enumerate(word) if bit]
    return sum((1 << i) * 3 ** (len(ones) - rank - 1)
               for rank, i in enumerate(ones))


def prefix_data(word):
    """Prefix weights and numerators from sequential affine composition."""
    weights = [0]
    numerators = [0]
    for j, bit in enumerate(word):
        weights.append(weights[-1] + bit)
        numerators.append(3 ** bit * numerators[-1] + bit * (1 << j))
    return weights, numerators


def pow3(exponent):
    return F(3 ** exponent) if exponent >= 0 else F(1, 3 ** (-exponent))


def rational_orbit(word, initial):
    states = [F(initial)]
    for bit in word:
        states.append((3 ** bit * states[-1] + bit) / 2)
    return states


def check_finite_arc(word, counters):
    m = len(word)
    modulus = 1 << m
    weights, numerators = prefix_data(word)
    total_q = raw_q(word)
    assert numerators[-1] == total_q
    a0 = (-total_q * pow(3 ** weights[-1], -1, modulus)) % modulus
    assert 0 <= a0 < modulus
    assert (3 ** weights[-1] * a0 + total_q) % modulus == 0

    intercepts = [F(3 ** weights[j] * a0 + numerators[j], 1 << j)
                  for j in range(m + 1)]
    slopes = [3 ** weights[j] * (1 << (m - j)) for j in range(m + 1)]
    prefix_weights = [F(1 << j, 3 ** weights[j]) for j in range(m + 1)]
    assert all(a.denominator == 1 and a >= 0 for a in intercepts)
    assert all(b > 0 for b in slopes)
    assert all(prefix_weights[j] * slopes[j] == modulus for j in range(m + 1))
    assert intercepts[0] == a0
    assert slopes[0] == modulus
    assert slopes[-1] == 3 ** weights[-1]

    for t in T_VALUES:
        initial = a0 + modulus * t
        states = rational_orbit(word, initial)
        assert len(states) == m + 1
        assert all(state.denominator == 1 for state in states)
        assert all(state >= 0 for state in states)
        if t >= 1:
            assert all(state > 0 for state in states)
            counters['strictly_positive_sampled_arcs'] += 1
        else:
            assert all(state > 0 for state in states) == bool(sum(word))
        for j, state in enumerate(states):
            assert state == intercepts[j] + slopes[j] * t
            assert (1 << j) * state - 3 ** weights[j] * initial == numerators[j]
            assert prefix_weights[j] * state == initial + F(numerators[j], 3 ** weights[j])
            counters['sampled_phase_checks'] += 1
            if j < m:
                assert state.numerator % 2 == word[j]
                assert 2 * states[j + 1] == 3 ** word[j] * state + word[j]
                counters['sampled_parity_step_checks'] += 1
        assert modulus * states[-1] == 3 ** weights[-1] * initial + total_q
        assert (initial - a0) // modulus == t
        counters['sampled_arcs'] += 1

    counters['words'] += 1
    counters['intercept_slope_coordinates'] += m + 1
    if not any(word):
        assert a0 == 0
        assert all(a == 0 for a in intercepts)
        counters['all_zero_words_with_nonpositive_t0'] += 1


def check_block_algebra(word, counters):
    A = len(word)
    L = sum(word)
    D = (1 << A) - 3 ** L
    g = gcd(A, L)
    assert 0 < L < A and D > 0 and g > 1
    a, ell = A // g, L // g
    X, Y = 1 << a, 3 ** ell
    z = F(X, Y)
    total_q = raw_q(word)
    root = F(total_q, D)
    states = rational_orbit(word, root)
    assert states[-1] == root
    weights, _ = prefix_data(word)
    E = [weights[j * a] - j * ell for j in range(g + 1)]
    assert E[0] == E[-1] == 0
    xs = [states[j * a] for j in range(g + 1)]
    ys = [pow3(-E[j]) * xs[j] for j in range(g + 1)]
    H = [z ** j * ys[j] for j in range(g + 1)]
    coefficients = []
    increments = []
    for j in range(g):
        block = word[j * a:(j + 1) * a]
        block_q = raw_q(block)
        coefficient = pow3(-E[j + 1]) * block_q
        coefficients.append(coefficient)
        assert X * xs[j + 1] == 3 ** sum(block) * xs[j] + block_q
        assert coefficient == X * ys[j + 1] - Y * ys[j]
        actual = H[j + 1] - H[j]
        corrected = z ** j * coefficient / Y
        assert actual == corrected
        assert actual >= 0
        assert (actual > 0) == bool(sum(block))
        increments.append(actual)
        # Diagnostic only: the omitted-factor expression is not asserted true.
        if actual != z ** j * block_q / Y:
            counters['unnormalized_expression_mismatches'] += 1
        if not any(block):
            counters['zero_numerator_blocks'] += 1
        counters['corrected_increment_checks'] += 1
    lam = z ** g
    assert H[0] == root
    assert H[-1] == lam * root
    assert sum(increments) == (lam - 1) * root
    block_polynomial = sum(z ** j * coefficients[j] for j in range(g))
    assert block_polynomial == Y * (lam - 1) * root
    assert Y ** (g - 1) * block_polynomial == total_q
    counters['words'] += 1
    counters['telescope_checks'] += 1
    return E, H, states


def check_targeted_repair_witness():
    word = (1, 1, 0, 0, 0, 0)
    counters = new_block_counters()
    E, H, _ = check_block_algebra(word, counters)
    assert E == [0, 1, 0]
    assert H[1] - H[0] == F(5, 9)
    assert F(raw_q(word[:3]), 3) == F(5, 3)
    assert H[2] - H[1] == 0
    return {'word': '110000', 'actual_and_corrected_first_increment': '5/9',
            'omitted_factor_expression': '5/3', 'second_block_increment': '0',
            'scope': 'rational fixed-orbit algebra; not an integer-cycle counterexample'}


def valuation(value, prime):
    assert value > 0
    count = 0
    while value % prime == 0:
        count += 1
        value //= prime
    return count


def check_rl20_fake():
    # Integer-only construction of ceil(m log_3 2); no floating logarithms.
    prefixes = [0]
    for m in range(1, 184):
        p = prefixes[-1]
        while 3 ** p <= 1 << m:
            p += 1
        prefixes.append(p)
    prefixes.append(116)
    word = tuple(prefixes[j + 1] - prefixes[j] for j in range(184))
    assert all(bit in (0, 1) for bit in word)
    assert len(word) == 184 and sum(word) == 116
    assert word[:4] == (1, 1, 0, 1) and word[-2:] == (1, 0)
    proper_periods = [p for p in range(1, 184) if 184 % p == 0]
    assert all(any(word[j] != word[j % p] for j in range(184))
               for p in proper_periods)
    for m in range(1, 184):
        assert 3 ** prefixes[m] > 1 << m
        suffix_weight = 116 - prefixes[184 - m]
        assert 1 << m > 3 ** suffix_weight
    D = (1 << 184) - 3 ** 116
    total_q = raw_q(word)
    assert D > 1
    assert total_q % D == FAKE_REMAINDER != 0
    rational_root = F(total_q, D)
    assert rational_root.denominator > 1

    witness = FAKE_ENDPOINT_RESIDUE_WITNESS
    assert witness >= 1 << 71
    assert witness % 16 == 11 and witness % 9 == 1
    assert valuation(witness + 1, 2) == 2
    assert valuation(9 * ((witness + 1) // 4) - 1, 2) == 1
    assert valuation(2 * witness + 1, 3) == 1

    block_counts = new_block_counters()
    E, H, states = check_block_algebra(word, block_counts)
    assert states[-1] == rational_root
    assert all(state.denominator > 1 for state in states)
    assert min(states[:-1]) == rational_root
    # The fake is outside the lambda<16/15 numerical close/strict branch.
    # An earlier unpromoted draft asserted the opposite; that test expectation
    # was wrong. Only the all-word algebra is consumed for the fake here.
    fake_lambda = F(1 << 184, 3 ** 116)
    assert F(16, 15) < fake_lambda < F(3)
    assert all(E[j] >= 1 for j in range(1, len(E) - 1))
    assert all(H[j] > H[0] for j in range(1, len(H)))
    return {
        'length': 184,
        'weight': 116,
        'primitive': True,
        'prefix_and_suffix_checks_each': 183,
        'Q_mod_D': FAKE_REMAINDER,
        'full_D_quotient_integral': False,
        'near_resonant_16_over_15_scope_satisfied': False,
        'exact_lambda_bounds': '16/15 < lambda < 3',
        'endpoint_residue_witness_is_cycle_state': False,
        'canonical_block_imbalances': E,
        'corrected_increment_checks': block_counts['corrected_increment_checks'],
        'rotation_distance_scan_performed': False,
        'inherited_all_rotation_minimum_distance': 4,
        'distance_classification': 'inherited exact certificate; accepted, not rerun',
    }


def new_block_counters():
    return {
        'words': 0,
        'corrected_increment_checks': 0,
        'telescope_checks': 0,
        'unnormalized_expression_mismatches': 0,
        'zero_numerator_blocks': 0,
    }


def main():
    arc = {
        'words': 0,
        'sampled_arcs': 0,
        'sampled_phase_checks': 0,
        'sampled_parity_step_checks': 0,
        'intercept_slope_coordinates': 0,
        'strictly_positive_sampled_arcs': 0,
        'all_zero_words_with_nonpositive_t0': 0,
    }
    blocks = new_block_counters()
    for m in range(1, MAX_LENGTH + 1):
        for word in product((0, 1), repeat=m):
            check_finite_arc(word, arc)
            L = sum(word)
            if 0 < L < m and (1 << m) - 3 ** L > 0 and gcd(m, L) > 1:
                check_block_algebra(word, blocks)
    assert arc['words'] == (1 << (MAX_LENGTH + 1)) - 2
    assert arc['sampled_arcs'] == len(T_VALUES) * arc['words']
    assert arc['all_zero_words_with_nonpositive_t0'] == MAX_LENGTH
    assert blocks['unnormalized_expression_mismatches'] > 0
    summary = {
        'status': 'PASS',
        'classification': 'exact finite sanity checks; written proofs supply infinite claims',
        'finite_arc_domain': {'all_binary_word_lengths': [1, MAX_LENGTH],
                              'sampled_integer_parameters': list(T_VALUES),
                              'positivity': 't>=1 guaranteed by checked nonnegative intercepts and positive slopes'},
        'finite_arc_checks': arc,
        'block_domain': 'same lengths, 0<L<A, D>0, gcd(A,L)>1; rational fixed orbits',
        'corrected_block_checks': blocks,
        'targeted_repair_witness': check_targeted_repair_witness(),
        'RL20_fake': check_rl20_fake(),
        'scope_locks': ['no infinite theorem inferred from finite loops',
                        'no radius-distance rescan',
                        'no Gate closure or cycle exclusion claim'],
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
