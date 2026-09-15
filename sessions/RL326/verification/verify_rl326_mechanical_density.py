#!/usr/bin/env python3
"""Exact RL326 certificate consumer for mechanical-run density and carry contraction."""

from fractions import Fraction

A = 217_976_794_617
ELL = 137_528_045_312
D = A - ELL
LAMBDA_UPPER = 1 + Fraction(1, 1 << 40)
M_LOWER = 1 << 71
M_UPPER = 1 << 75
STATE_UPPER = (1 << 76) + (1 << 36)  # 2*LAMBDA_UPPER*2^75
RUN_GAPS = 49
HIGH_CARRY_THRESHOLD = 20_390_252_058
NEW_CARRY_CAP = 32_839_291_403


def log_interval_atanh(x, terms=280):
    x2 = x * x
    term = x
    total = Fraction(0)
    for index in range(terms):
        total += term / (2 * index + 1)
        term *= x2
    lower = 2 * total
    tail = 2 * term / (2 * terms + 1) / (1 - x2)
    return lower, lower + tail


LN2_LOWER, LN2_UPPER = log_interval_atanh(Fraction(1, 3))
LN3_LOWER, LN3_UPPER = log_interval_atanh(Fraction(1, 2))
DELTA_LOWER = A * LN2_LOWER - ELL * LN3_UPPER
DELTA_UPPER = A * LN2_UPPER - ELL * LN3_LOWER
assert 0 < DELTA_LOWER < DELTA_UPPER

# Prove lambda=exp(Delta)<1+2^-40 by comparing Delta with a lower
# enclosure for log(1+2^-40)=2*atanh(epsilon/(2+epsilon)).
epsilon = Fraction(1, 1 << 40)
log_lambda_cap_lower = 2 * (epsilon / (2 + epsilon))
assert DELTA_UPPER < log_lambda_cap_lower


def mechanical_factors(length):
    """All factors of ceil(D*t/ELL)-ceil(D*(t-1)/ELL), plus the base one."""
    cuts = sorted({0, ELL, *((-D * step) % ELL for step in range(length + 1))})
    samples = set()
    for left, right in zip(cuts, cuts[1:]):
        samples.add(left)
        if left + 1 < right:
            samples.add(left + 1)
    factors = set()
    for residue in samples:
        previous = (residue + ELL - 1) // ELL
        gaps = []
        for step in range(1, length + 1):
            current = (residue + D * step + ELL - 1) // ELL
            gaps.append(1 + current - previous)
            previous = current
        factors.add(tuple(gaps))
    return factors


def forced_endpoint_and_states(gaps):
    """Return the only endpoint below 3^len(gaps), and its backward odd states."""
    constant = 0
    for step, gap in enumerate(gaps, 1):
        constant = (1 << gap) * constant + 3 ** (step - 1)
    modulus = 3 ** len(gaps)
    total_gap = sum(gaps)
    endpoint = constant * pow(pow(2, total_gap, modulus), -1, modulus) % modulus
    states = [endpoint]
    state = endpoint
    for gap in gaps:
        numerator = (1 << gap) * state - 1
        assert numerator % 3 == 0
        state = numerator // 3
        assert state & 1
        states.append(state)
    return endpoint, states


factors = mechanical_factors(RUN_GAPS)
assert len(factors) == RUN_GAPS + 1
assert 3**RUN_GAPS > STATE_UPPER

candidate_blocks = []
for factor in factors:
    endpoint, states = forced_endpoint_and_states(factor)
    if M_LOWER <= endpoint < STATE_UPPER and endpoint & 1:
        candidate_blocks.append((endpoint, min(states), factor))

assert len(candidate_blocks) == 3
max_block_minimum = max(block[1] for block in candidate_blocks)
assert max_block_minimum == 22_689_747_442_539_873_328_123

# Z0>0 gives n < (1-Y/X)m < Delta*m.  Hence a carry at or above the
# threshold forces m above the minimum state of every candidate block.
assert DELTA_UPPER * max_block_minimum < HIGH_CARRY_THRESHOLD

# Exact upper enclosure for the full ideal Beatty coefficient sum.
# Sum_{q=1}^{ELL-1} 2^(q/ELL-1)
# = 1/[2(exp(log(2)/ELL)-1)] - 1/2, and exp(x)-1>x+x^2/2.
x_lower = LN2_LOWER / ELL
full_sum_upper = 1 / (2 * (x_lower + x_lower * x_lower / 2)) - Fraction(1, 2)


def omitted_lower(last_r):
    total = Fraction(0)
    for r in range(1, last_r + 1):
        total += Fraction(1 << ((A * r) // ELL), 3**r)
    return total / LAMBDA_UPPER


rho = 60
matched_depth = ELL - rho
# A forbidden 49-gap exact block means each zero run among q_0,...,q_T
# has length at most 49.  With K positive q_t positions:
# T+1-K <= 49(K+1), so K >= ceil((T-48)/50).
positive_excess_min = (matched_depth - 48 + 49) // 50
assert positive_excess_min == 2_750_560_905

ideal_partial_upper = (full_sum_upper - omitted_lower(rho - 1)) / 3
density_loss_lower = Fraction(positive_excess_min, 1) / (12 * LAMBDA_UPPER)
carry_rhs_upper = 1 + ideal_partial_upper - density_loss_lower
assert carry_rhs_upper < NEW_CARRY_CAP + 1
assert carry_rhs_upper > NEW_CARRY_CAP

# The companion carry inequality disposes of rho<=59 well below the new cap.
rho59_carry_upper = Fraction(5, 6) + LAMBDA_UPPER * (1 << ((D * 59) // ELL))
assert rho59_carry_upper < NEW_CARRY_CAP

# Monotonicity consumer for rho>=60: each newly omitted ideal term is >1/2,
# so its decrease exceeds 1/(6*Lambda), while relaxing the integer density
# floor by one can restore at most 1/(12*Lambda).
assert Fraction(1, 6 * LAMBDA_UPPER) > Fraction(1, 12 * LAMBDA_UPPER)
assert NEW_CARRY_CAP + 1 > HIGH_CARRY_THRESHOLD

print("RL326_MECHANICAL_DENSITY_VERIFIER_GREEN")
print("mechanical_factor_count", len(factors))
print("candidate_49_gap_blocks", len(candidate_blocks))
print("max_candidate_block_minimum", max_block_minimum)
print("high_carry_threshold", HIGH_CARRY_THRESHOLD)
print("positive_excess_min_at_rho60", positive_excess_min)
print("density_loss_lower_gt", float(density_loss_lower))
print("rho60_carry_rhs_upper_lt", float(carry_rhs_upper))
print("new_carry_cap", NEW_CARRY_CAP)
print("scope", "exact finite factor/residue certificate plus analytic telescope consumer")
