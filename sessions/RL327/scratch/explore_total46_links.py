#!/usr/bin/env python3
"""Enumerate lifted total-46 singleton bridges with indexed link matching."""

from collections import defaultdict

namespace = {}
exec(open(".rl-work/RL327/explore_total47_links.py").read(), namespace)

M_LOWER = namespace["M_LOWER"]
STATE_UPPER = namespace["STATE_UPPER"]
HIGH_CARRY_THRESHOLD = namespace["HIGH_CARRY_THRESHOLD"]
delta_upper = namespace["delta_upper"]
mechanical_factors = namespace["mechanical_factors"]
forced_endpoint_and_states = namespace["forced_endpoint_and_states"]
reconstruct = namespace["reconstruct"]

new_rows = []
total = 46
modulus = 3**total
for left_zero in range(1, total):
    right_zero = total - left_zero
    for baseline in mechanical_factors(total):
        if baseline[left_zero] != 2:
            continue
        gaps = list(baseline)
        gaps[left_zero - 1] += 1
        gaps[left_zero] -= 1
        residue, _ = forced_endpoint_and_states(gaps)
        lift = max(0, (M_LOWER - residue + modulus - 1) // modulus)
        endpoint = residue + lift * modulus
        while endpoint < STATE_UPPER:
            states = reconstruct(endpoint, gaps)
            minimum = min(states)
            if delta_upper * minimum >= HIGH_CARRY_THRESHOLD:
                new_rows.append(
                    (
                        tuple(states[:left_zero]),
                        tuple(states[left_zero + 1 :]),
                        left_zero,
                        right_zero,
                        endpoint,
                        minimum,
                    )
                )
            endpoint += modulus

large_rows = new_rows + namespace["large_rows"]
left_index = defaultdict(list)
for index, row in enumerate(large_rows):
    left_index[(row[2], row[0][0])].append(index)

links = []
for first_index, first in enumerate(large_rows):
    for second_index in left_index[(first[3], first[1][0])]:
        links.append((first_index, second_index))

allowed_pair_links = {
    ((large_rows[i][2], large_rows[i][3]), (large_rows[j][2], large_rows[j][3]))
    for i, j in links
}

print("total46_high_candidates", len(new_rows))
print("total46_high_pairs", len({(row[2], row[3]) for row in new_rows}))
print("threshold46_edges", len(large_rows))
print("threshold46_exact_links", len(links))
print("threshold46_allowed_pair_links", len(allowed_pair_links))
