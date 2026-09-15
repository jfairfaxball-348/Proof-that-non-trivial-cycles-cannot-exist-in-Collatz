#!/usr/bin/env python3
"""Exact RL327 owned-bridge certificate and excess-density consumer."""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache

A = 217_976_794_617
ELL = 137_528_045_312
D = A - ELL
LAMBDA_UPPER = 1 + Fraction(1, 1 << 40)
M_LOWER = 1 << 71
STATE_UPPER = (1 << 76) + (1 << 36)
HIGH_CARRY_THRESHOLD = 20_390_252_058
OLD_CARRY_CAP = 32_839_291_403
BASE_DENSITY_CAP = 32_603_663_706
BOOTSTRAP_THRESHOLD = 32_596_612_663
NEW_CARRY_CAP = BOOTSTRAP_THRESHOLD - 1


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


ln2_lower, ln2_upper = log_interval_atanh(Fraction(1, 3))
ln3_lower, ln3_upper = log_interval_atanh(Fraction(1, 2))
delta_lower = A * ln2_lower - ELL * ln3_upper
delta_upper = A * ln2_upper - ELL * ln3_lower
assert 0 < delta_lower < delta_upper
epsilon = Fraction(1, 1 << 40)
assert delta_upper < 2 * (epsilon / (2 + epsilon))


@lru_cache(maxsize=None)
def mechanical_factors(length):
    """All length-L rational-mechanical factors, gap-free."""
    cuts = sorted({0, ELL, *((-D * step) % ELL for step in range(length + 1))})
    factors = set()
    for left, right in zip(cuts, cuts[1:]):
        for residue in {left, min(left + 1, right - 1)}:
            previous = (residue + ELL - 1) // ELL
            gaps = []
            for step in range(1, length + 1):
                current = (residue + D * step + ELL - 1) // ELL
                gaps.append(1 + current - previous)
                previous = current
            factors.add(tuple(gaps))
    assert len(factors) == length + 1
    return tuple(sorted(factors))


def forced_residue(gaps):
    constant = 0
    for step, gap in enumerate(gaps, 1):
        constant = (1 << gap) * constant + 3 ** (step - 1)
    modulus = 3 ** len(gaps)
    residue = constant * pow(pow(2, sum(gaps), modulus), -1, modulus) % modulus
    return residue, modulus


def reconstruct(endpoint, gaps):
    states = [endpoint]
    state = endpoint
    for gap in gaps:
        numerator = (1 << gap) * state - 1
        assert numerator % 3 == 0
        state = numerator // 3
        assert state & 1
        states.append(state)
    return states


def band_realizations(gaps):
    residue, modulus = forced_residue(gaps)
    lift = max(0, (M_LOWER - residue + modulus - 1) // modulus)
    endpoint = residue + lift * modulus
    while endpoint < STATE_UPPER:
        if endpoint & 1:
            yield endpoint, reconstruct(endpoint, gaps)
        endpoint += modulus


def high_carry_owned(states):
    # If delta_upper*min(states)<threshold<=n<Delta*m, then min(states)<m,
    # contradicting least-state ownership.  Retain the complement only.
    return delta_upper * min(states) >= HIGH_CARRY_THRESHOLD


# Singleton q-positive runs.  A bridge 0,1,0 changes the two joining gaps by
# +1,-1.  Totals 46--98 are enumerated; the base theorem uses 47--98 and the
# bootstrap consumes the additional lifted total-46 layer.
singleton_all = []
for total in range(46, 99):
    factors = mechanical_factors(total)
    for left_zero in range(max(1, total - 49), min(49, total - 1) + 1):
        right_zero = total - left_zero
        for baseline in factors:
            if baseline[left_zero] != 2:
                continue
            gaps = list(baseline)
            gaps[left_zero - 1] += 1
            gaps[left_zero] -= 1
            for endpoint, states in band_realizations(gaps):
                singleton_all.append(
                    (
                        tuple(states[:left_zero]),
                        tuple(states[left_zero + 1 :]),
                        left_zero,
                        right_zero,
                        endpoint,
                        delta_upper * min(states),
                    )
                )

singleton_rows = [
    row[:5]
    for row in singleton_all
    if row[2] + row[3] >= 47 and row[5] >= HIGH_CARRY_THRESHOLD
]

singleton_counts = Counter(row[2] + row[3] for row in singleton_rows)
assert singleton_counts == {47: 1034, 48: 342, 49: 106, 50: 35, 51: 10, 52: 1}
singleton_pair_counts = {
    total: len({(row[2], row[3]) for row in singleton_rows if row[2] + row[3] == total})
    for total in singleton_counts
}
assert singleton_pair_counts == {47: 46, 48: 47, 49: 45, 50: 26, 51: 10, 52: 1}

# Exact ownership linkage: equality of the first shared plateau state is a
# necessary condition for consecutive singleton bridges.  Determinism then
# makes the entire shared plateau agree.  Indexing makes the coverage exact.
left_index = defaultdict(list)
for index, row in enumerate(singleton_rows):
    left_index[(row[2], row[0][0])].append(index)
singleton_links = []
for first_index, first in enumerate(singleton_rows):
    for second_index in left_index[(first[3], first[1][0])]:
        singleton_links.append((first_index, second_index))
assert len(singleton_links) == 5
allowed_pair_links = {
    (
        (singleton_rows[first][2], singleton_rows[first][3]),
        (singleton_rows[second][2], singleton_rows[second][3]),
    )
    for first, second in singleton_links
}
assert allowed_pair_links == {
    ((1, 46), (46, 1)),
    ((2, 45), (45, 2)),
    ((2, 45), (45, 3)),
    ((2, 45), (45, 4)),
}
large_pairs = sorted({(row[2], row[3]) for row in singleton_rows})
assert len(large_pairs) == 175

# Positive q-runs of length two.  Positivity and return to zero force the
# shapes 0,h,1,0 with h in {1,2}.  Complete enumeration shows that every
# high-carry survivor has adjacent zero-run total at most 51.
two_positive_all = []
for zero_total in range(46, 99):
    gap_length = zero_total + 1
    factors = mechanical_factors(gap_length)
    for left_zero in range(max(1, zero_total - 49), min(49, zero_total - 1) + 1):
        right_zero = zero_total - left_zero
        for baseline in factors:
            for first_height in (1, 2):
                gaps = list(baseline)
                changes = (first_height, 1 - first_height, -1)
                for offset, change in enumerate(changes):
                    gaps[left_zero - 1 + offset] += change
                if min(gaps[left_zero - 1 : left_zero + 2]) < 1:
                    continue
                for _, states in band_realizations(gaps):
                    two_positive_all.append((zero_total, delta_upper * min(states)))
two_positive_counts = Counter(
    total
    for total, cutoff in two_positive_all
    if total >= 47 and cutoff >= HIGH_CARRY_THRESHOLD
)
assert two_positive_counts == {
    47: 468,
    48: 163,
    49: 62,
    50: 20,
    51: 4,
}

# Finite max-plus certificate.  N(z) records a zero run reached after a short
# singleton or a >=2 positive run.  L(a,b) records the exact type of the last
# singleton bridge of total >=47.  The graph is a conservative superset:
# totals <=46 are all admitted, exact large pairs and pair links are admitted,
# two-positive runs may join any pair of total <=51, and >=3 positive runs may
# join any pair.  Edge weight z_next-24*p proves Z<=24K up to a boundary.
states = [("N", zero) for zero in range(1, 50)] + [("L", pair) for pair in large_pairs]
state_index = {state: index for index, state in enumerate(states)}
edges = []
for state in states:
    source = state_index[state]
    current_zero = state[1] if state[0] == "N" else state[1][1]
    for next_zero in range(1, 50):
        if current_zero + next_zero <= 46:
            edges.append((source, state_index[("N", next_zero)], next_zero - 24))
    for pair in large_pairs:
        if pair[0] == current_zero and (
            state[0] == "N" or (state[1], pair) in allowed_pair_links
        ):
            edges.append((source, state_index[("L", pair)], pair[1] - 24))
    for next_zero in range(1, 50):
        if current_zero + next_zero <= 51:
            edges.append((source, state_index[("N", next_zero)], next_zero - 48))
        edges.append((source, state_index[("N", next_zero)], next_zero - 72))

assert len(states) == 224
assert len(edges) == 21_805
potential = [0] * len(states)
for iteration in range(len(states) + 1):
    changed = False
    for source, target, weight in edges:
        if potential[source] + weight > potential[target]:
            potential[target] = potential[source] + weight
            changed = True
    if not changed:
        break
else:
    raise AssertionError("positive max-plus cycle: density claim fails")
assert iteration + 1 == 9
assert all(potential[source] + weight <= potential[target] for source, target, weight in edges)
assert min(potential) == 0 and max(potential) == 25
boundary = max(
    zero - potential[state_index[("N", zero)]] for zero in range(1, 50)
) + max(potential)
assert boundary == 72

# Summing edge inequalities and adding the initial zero run gives
# Z<=24K+72.  Since T+1=Z+K, K>=ceil((T-71)/25).
rho = 60
matched_depth = ELL - rho
positive_excess_min = (matched_depth - 71 + 24) // 25
assert positive_excess_min == 5_501_121_808

# Exact RL326 ideal-sum enclosure with the improved density loss.
x_lower = ln2_lower / ELL
full_sum_upper = 1 / (2 * (x_lower + x_lower * x_lower / 2)) - Fraction(1, 2)


def omitted_lower(last_r):
    return sum(
        (Fraction(1 << ((A * r) // ELL), 3**r) for r in range(1, last_r + 1)),
        Fraction(0),
    ) / LAMBDA_UPPER


ideal_partial_upper = (full_sum_upper - omitted_lower(rho - 1)) / 3

# Residue-weighted loss.  Since gcd(A,ELL)=1, t -> A*t mod ELL is injective
# on 1,...,T.  Writing r_t=A*t mod ELL gives
# c_t = 2^(r_t/ELL-1)*lambda^(-t/ELL)
#     > 2^(r_t/ELL-1)/Lambda.
# Therefore K positive ranks lose at least the K smallest distinct residue
# weights, not K copies of their global infimum.  A quartic exponential lower
# polynomial keeps the certificate rational and essentially exact here.
assert __import__("math").gcd(A, ELL) == 1
def weighted_residue_lower(count):
    sum_r = count * (count + 1) // 2
    sum_r2 = count * (count + 1) * (2 * count + 1) // 6
    sum_r3 = sum_r**2
    sum_r4 = count * (count + 1) * (2 * count + 1) * (3 * count**2 + 3 * count - 1) // 30
    return (
        Fraction(count, 1)
        + ln2_lower * sum_r / ELL
        + ln2_lower**2 * sum_r2 / (2 * ELL**2)
        + ln2_lower**3 * sum_r3 / (6 * ELL**3)
        + ln2_lower**4 * sum_r4 / (24 * ELL**4)
    )


K = positive_excess_min
weighted_residue_sum_lower = weighted_residue_lower(K)
uniform_density_loss_lower = Fraction(K, 1) / (12 * LAMBDA_UPPER)
density_loss_lower = weighted_residue_sum_lower / (12 * LAMBDA_UPPER)
assert density_loss_lower > uniform_density_loss_lower
carry_rhs_upper = 1 + ideal_partial_upper - density_loss_lower
assert BASE_DENSITY_CAP < carry_rhs_upper < BASE_DENSITY_CAP + 1

rho59_carry_upper = Fraction(5, 6) + LAMBDA_UPPER * (1 << ((D * 59) // ELL))
assert rho59_carry_upper < NEW_CARRY_CAP
# Increasing rho by one relaxes the integer density floor by at most one.
# The resulting restoration is at most the largest quartic residue increment
# used at rho=60, still below 1/(6 Lambda), while the new omitted ideal term
# removes more than 1/(6 Lambda).  Hence rho>=60 is monotone decreasing.
max_x = ln2_lower * K / ELL
max_weight_polynomial = 1 + max_x + max_x**2 / 2 + max_x**3 / 6 + max_x**4 / 24
assert max_weight_polynomial < 2
assert max_weight_polynomial / (12 * LAMBDA_UPPER) < Fraction(1, 6 * LAMBDA_UPPER)


def bridge_automaton_certificate(threshold, ratio_numerator, ratio_denominator):
    """Return exact filtered graph data and a telescoping potential boundary."""
    rows = [row[:5] for row in singleton_all if row[5] >= threshold]
    left_lookup = defaultdict(list)
    for index, row in enumerate(rows):
        left_lookup[(row[2], row[0][0])].append(index)
    links = []
    for first_index, first in enumerate(rows):
        for second_index in left_lookup[(first[3], first[1][0])]:
            links.append((first_index, second_index))
    pair_links = {
        ((rows[first][2], rows[first][3]), (rows[second][2], rows[second][3]))
        for first, second in links
    }
    pairs = sorted({(row[2], row[3]) for row in rows})
    p2_max = max([45] + [total for total, cutoff in two_positive_all if cutoff >= threshold])
    graph_states = [("N", zero) for zero in range(1, 50)] + [("L", pair) for pair in pairs]
    graph_index = {state: index for index, state in enumerate(graph_states)}
    graph_edges = []
    for state in graph_states:
        source = graph_index[state]
        current = state[1] if state[0] == "N" else state[1][1]
        for next_zero in range(1, 50):
            if current + next_zero <= 45:
                graph_edges.append(
                    (source, graph_index[("N", next_zero)], ratio_denominator * next_zero - ratio_numerator)
                )
        for pair in pairs:
            if pair[0] == current and (state[0] == "N" or (state[1], pair) in pair_links):
                graph_edges.append(
                    (source, graph_index[("L", pair)], ratio_denominator * pair[1] - ratio_numerator)
                )
        for next_zero in range(1, 50):
            if current + next_zero <= p2_max:
                graph_edges.append(
                    (source, graph_index[("N", next_zero)], ratio_denominator * next_zero - 2 * ratio_numerator)
                )
            graph_edges.append(
                (source, graph_index[("N", next_zero)], ratio_denominator * next_zero - 3 * ratio_numerator)
            )
    graph_potential = [0] * len(graph_states)
    for graph_iteration in range(len(graph_states) + 1):
        graph_changed = False
        for source, target, weight in graph_edges:
            if graph_potential[source] + weight > graph_potential[target]:
                graph_potential[target] = graph_potential[source] + weight
                graph_changed = True
        if not graph_changed:
            break
    else:
        raise AssertionError("positive cycle in bootstrap density graph")
    assert all(
        graph_potential[source] + weight <= graph_potential[target]
        for source, target, weight in graph_edges
    )
    graph_boundary = max(
        ratio_denominator * zero - graph_potential[graph_index[("N", zero)]]
        for zero in range(1, 50)
    ) + max(graph_potential)
    return rows, pairs, links, p2_max, graph_edges, graph_potential, graph_boundary


# Self-consistent high-carry bootstrap.  If n is at least the displayed
# threshold, the stronger minimality filter applies.  Its potential proves
# 19Z<=449K+1347, which drives the telescope strictly below that threshold.
(
    bootstrap_rows,
    bootstrap_pairs,
    bootstrap_links,
    bootstrap_p2_max,
    bootstrap_edges,
    bootstrap_potential,
    bootstrap_boundary,
) = bridge_automaton_certificate(BOOTSTRAP_THRESHOLD, 449, 19)
assert len(bootstrap_rows) == 2414
assert len(bootstrap_pairs) == 187
assert len(bootstrap_links) == 9
assert bootstrap_p2_max == 51
assert bootstrap_boundary == 1347
bootstrap_divisor = 449 + 19
bootstrap_positive_min = (
    19 * matched_depth + 19 - bootstrap_boundary + bootstrap_divisor - 1
) // bootstrap_divisor
assert bootstrap_positive_min == 5_583_403_544
bootstrap_weighted_sum_lower = weighted_residue_lower(bootstrap_positive_min)
bootstrap_loss_lower = bootstrap_weighted_sum_lower / (12 * LAMBDA_UPPER)
bootstrap_rhs_upper = 1 + ideal_partial_upper - bootstrap_loss_lower
assert NEW_CARRY_CAP < bootstrap_rhs_upper < BOOTSTRAP_THRESHOLD
bootstrap_max_x = ln2_lower * bootstrap_positive_min / ELL
bootstrap_max_weight = (
    1
    + bootstrap_max_x
    + bootstrap_max_x**2 / 2
    + bootstrap_max_x**3 / 6
    + bootstrap_max_x**4 / 24
)
assert bootstrap_max_weight < 2
assert bootstrap_max_weight / (12 * LAMBDA_UPPER) < Fraction(1, 6 * LAMBDA_UPPER)
assert OLD_CARRY_CAP - NEW_CARRY_CAP == 242_678_741

print("RL327_OWNED_EXCESS_DENSITY_VERIFIER_GREEN")
print("singleton_high_counts", dict(sorted(singleton_counts.items())))
print("singleton_exact_links", len(singleton_links))
print("two_positive_high_counts", dict(sorted(two_positive_counts.items())))
print("max_plus_states_edges", len(states), len(edges))
print("max_plus_boundary", boundary)
print("positive_excess_min_at_rho60", positive_excess_min)
print("weighted_residue_sum_lower_gt", float(weighted_residue_sum_lower))
print("weighted_gain_over_uniform_gt", float(density_loss_lower - uniform_density_loss_lower))
print("density_loss_lower_gt", float(density_loss_lower))
print("rho60_carry_rhs_upper_lt", float(carry_rhs_upper))
print("base_density_cap", BASE_DENSITY_CAP)
print("bootstrap_rows_pairs_links", len(bootstrap_rows), len(bootstrap_pairs), len(bootstrap_links))
print("bootstrap_boundary", bootstrap_boundary)
print("bootstrap_positive_min", bootstrap_positive_min)
print("bootstrap_rhs_upper_lt", float(bootstrap_rhs_upper))
print("new_carry_cap", NEW_CARRY_CAP)
print("carry_contraction", OLD_CARRY_CAP - NEW_CARRY_CAP)
