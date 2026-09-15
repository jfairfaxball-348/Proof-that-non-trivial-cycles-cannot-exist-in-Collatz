#!/usr/bin/env python3
"""Explore self-consistent high-carry filtering of owned bridge automata."""

from collections import defaultdict
from fractions import Fraction

namespace = {}
exec(open(".rl-work/RL327/verify_rl327_owned_excess_density.py").read(), namespace)

M_LOWER = namespace["M_LOWER"]
STATE_UPPER = namespace["STATE_UPPER"]
delta_upper = namespace["delta_upper"]
mechanical_factors = namespace["mechanical_factors"]
band_realizations = namespace["band_realizations"]

# Retain all odd physical candidates with their exact minimality cutoff.
singletons = []
for total in range(45, 99):
    for left_zero in range(max(1, total - 49), min(49, total - 1) + 1):
        right_zero = total - left_zero
        for baseline in mechanical_factors(total):
            if baseline[left_zero] != 2:
                continue
            gaps = list(baseline)
            gaps[left_zero - 1] += 1
            gaps[left_zero] -= 1
            for endpoint, states in band_realizations(gaps):
                singletons.append(
                    (
                        tuple(states[:left_zero]),
                        tuple(states[left_zero + 1 :]),
                        left_zero,
                        right_zero,
                        delta_upper * min(states),
                    )
                )

two_positive = []
for zero_total in range(45, 99):
    for left_zero in range(max(1, zero_total - 49), min(49, zero_total - 1) + 1):
        right_zero = zero_total - left_zero
        for baseline in mechanical_factors(zero_total + 1):
            for first_height in (1, 2):
                gaps = list(baseline)
                for offset, change in enumerate((first_height, 1 - first_height, -1)):
                    gaps[left_zero - 1 + offset] += change
                if min(gaps[left_zero - 1 : left_zero + 2]) < 1:
                    continue
                for _, states in band_realizations(gaps):
                    two_positive.append((zero_total, delta_upper * min(states)))


def filtered_graph_data(threshold):
    rows = [row for row in singletons if row[4] >= threshold]
    left_index = defaultdict(list)
    for index, row in enumerate(rows):
        left_index[(row[2], row[0][0])].append(index)
    pair_links = set()
    link_count = 0
    for first in rows:
        for second_index in left_index[(first[3], first[1][0])]:
            second = rows[second_index]
            pair_links.add(((first[2], first[3]), (second[2], second[3])))
            link_count += 1
    large_pairs = sorted({(row[2], row[3]) for row in rows})
    p2_max = max([44] + [total for total, cutoff in two_positive if cutoff >= threshold])
    return rows, pair_links, large_pairs, link_count, p2_max


def maximum_cycle_ratio(threshold):
    rows, pair_links, large_pairs, link_count, p2_max = filtered_graph_data(threshold)
    base = [("N", zero) for zero in range(1, 50)] + [("L", pair) for pair in large_pairs]
    index = {state: position for position, state in enumerate(base)}
    base_count = len(base)
    node_count = 4 * base_count
    incoming = [[] for _ in range(node_count)]
    for state in base:
        source = index[state]
        current = state[1] if state[0] == "N" else state[1][1]
        for next_zero in range(1, 50):
            if current + next_zero <= 44:
                incoming[index[("N", next_zero)]].append((source, next_zero))
        for pair in large_pairs:
            if pair[0] == current and (state[0] == "N" or (state[1], pair) in pair_links):
                incoming[index[("L", pair)]].append((source, pair[1]))
        incoming[base_count + source].append((source, 0))
        for next_zero in range(1, 50):
            if current + next_zero <= p2_max:
                incoming[index[("N", next_zero)]].append((base_count + source, next_zero))
        incoming[2 * base_count + source].append((source, 0))
        incoming[3 * base_count + source].append((2 * base_count + source, 0))
        for next_zero in range(1, 50):
            incoming[index[("N", next_zero)]].append((3 * base_count + source, next_zero))
    negative = -10**9
    dynamic = [[negative] * node_count for _ in range(node_count + 1)]
    dynamic[0] = [0] * node_count
    for length in range(1, node_count + 1):
        for target in range(node_count):
            if incoming[target]:
                dynamic[length][target] = max(dynamic[length - 1][source] + reward for source, reward in incoming[target])
    means = []
    for target in range(node_count):
        ratios = [Fraction(dynamic[node_count][target] - dynamic[length][target], node_count - length) for length in range(node_count) if dynamic[length][target] > negative]
        if ratios:
            means.append(min(ratios))
    return max(means), len(rows), len(large_pairs), link_count, p2_max


def exact_density_and_cap(threshold, ratio):
    rows, pair_links, large_pairs, _, p2_max = filtered_graph_data(threshold)
    numerator = ratio.numerator
    denominator = ratio.denominator
    states = [("N", zero) for zero in range(1, 50)] + [("L", pair) for pair in large_pairs]
    index = {state: position for position, state in enumerate(states)}
    edges = []
    for state in states:
        source = index[state]
        current = state[1] if state[0] == "N" else state[1][1]
        for next_zero in range(1, 50):
            if current + next_zero <= 44:
                edges.append((source, index[("N", next_zero)], denominator * next_zero - numerator))
        for pair in large_pairs:
            if pair[0] == current and (state[0] == "N" or (state[1], pair) in pair_links):
                edges.append((source, index[("L", pair)], denominator * pair[1] - numerator))
        for next_zero in range(1, 50):
            if current + next_zero <= p2_max:
                edges.append((source, index[("N", next_zero)], denominator * next_zero - 2 * numerator))
            edges.append((source, index[("N", next_zero)], denominator * next_zero - 3 * numerator))
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
        raise AssertionError("positive cycle at computed ratio")
    assert all(potential[s] + w <= potential[t] for s, t, w in edges)
    boundary = max(denominator * zero - potential[index[("N", zero)]] for zero in range(1, 50)) + max(potential)
    T = namespace["ELL"] - 60
    divisor = numerator + denominator
    K = (denominator * T + denominator - boundary + divisor - 1) // divisor
    L = namespace["ln2_lower"]
    E = namespace["ELL"]
    s1 = K * (K + 1) // 2
    s2 = K * (K + 1) * (2 * K + 1) // 6
    s3 = s1**2
    s4 = K * (K + 1) * (2 * K + 1) * (3 * K**2 + 3 * K - 1) // 30
    weighted = Fraction(K, 1) + L * s1 / E + L**2 * s2 / (2 * E**2) + L**3 * s3 / (6 * E**3) + L**4 * s4 / (24 * E**4)
    loss = weighted / (12 * namespace["LAMBDA_UPPER"])
    rhs = 1 + namespace["ideal_partial_upper"] - loss
    return boundary, K, rhs


threshold = 32_596_612_663
for bootstrap_round in range(6):
    ratio, row_count, pair_count, link_count, p2_max = maximum_cycle_ratio(threshold)
    print("bootstrap", bootstrap_round, threshold, "ratio", ratio, "singleton_rows", row_count, "pairs", pair_count, "links", link_count, "p2_max", p2_max)
    boundary, K, rhs = exact_density_and_cap(threshold, ratio)
    cap = rhs.numerator // rhs.denominator
    print("bootstrap_consequence", "boundary", boundary, "K", K, "rhs", float(rhs), "cap", cap, flush=True)
    if cap >= threshold - 1:
        break
    threshold = cap + 1
