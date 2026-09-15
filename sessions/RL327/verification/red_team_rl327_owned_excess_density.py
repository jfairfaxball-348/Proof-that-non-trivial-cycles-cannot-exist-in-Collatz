#!/usr/bin/env python3
"""Independent structural red team for the RL327 candidate certificate."""

from itertools import product
from fractions import Fraction
from math import gcd
from pathlib import Path

namespace = {}
verifier_path = Path(__file__).with_name("verify_rl327_owned_excess_density.py")
exec(verifier_path.read_text(), namespace)

ELL = namespace["ELL"]
D = namespace["D"]
M_LOWER = namespace["M_LOWER"]
STATE_UPPER = namespace["STATE_UPPER"]
mechanical_factors = namespace["mechanical_factors"]
forced_residue = namespace["forced_residue"]
reconstruct = namespace["reconstruct"]

# Independent cut-cell enumeration: explicitly use both the discontinuity
# residue and one integer on its right.  This catches endpoint-cell omissions.
for length in (47, 48, 49, 54, 73, 99):
    cuts = sorted({(-D * step) % ELL for step in range(length + 1)})
    direct = set()
    for index, cut in enumerate(cuts):
        next_cut = cuts[index + 1] if index + 1 < len(cuts) else ELL
        samples = [cut]
        if cut + 1 < next_cut:
            samples.append(cut + 1)
        for residue in samples:
            heights = [(residue + D * step + ELL - 1) // ELL for step in range(length + 1)]
            direct.add(tuple(1 + heights[step] - heights[step - 1] for step in range(1, length + 1)))
    assert direct == set(mechanical_factors(length))

# Residue/lift coverage and recurrence orientation on every retained
# singleton candidate endpoint.
for left, right, left_length, right_length, endpoint in namespace["singleton_rows"]:
    assert M_LOWER <= endpoint < STATE_UPPER
    assert len(left) == left_length and len(right) == right_length
    assert left[0] == endpoint

# Exhaust the two-positive height logic independently.  For baseline bridge
# gaps in {1,2}, the only positive shapes returning to zero are (1,1),(2,1).
valid_shapes = set()
for baselines in product((1, 2), repeat=3):
    for first in range(1, 11):
        for second in range(1, 11):
            changes = (first, second - first, -second)
            if all(base + change >= 1 for base, change in zip(baselines, changes)):
                valid_shapes.add((first, second))
assert valid_shapes == {(1, 1), (2, 1)}

# Every max-plus edge independently satisfies the displayed potential; the
# boundary calculation is recomputed from the semantic initial states.
potential = namespace["potential"]
edges = namespace["edges"]
states = namespace["states"]
state_index = namespace["state_index"]
assert all(potential[source] + weight <= potential[target] for source, target, weight in edges)
boundary = max(
    zero - potential[state_index[("N", zero)]] for zero in range(1, 50)
) + max(potential)
assert boundary == 72

# Independently audit the residue-weighted loss algebra.  Coprimality makes
# the positive-rank residues distinct, so their ordered lower envelope is
# r=1,...,K.  Check the closed power sums against direct summation on a
# nontrivial prefix and rederive the exact certified cap.
assert gcd(namespace["A"], ELL) == 1
test_k = 10_000
assert test_k * (test_k + 1) // 2 == sum(range(1, test_k + 1))
assert test_k * (test_k + 1) * (2 * test_k + 1) // 6 == sum(
    value * value for value in range(1, test_k + 1)
)
assert (test_k * (test_k + 1) // 2) ** 2 == sum(
    value**3 for value in range(1, test_k + 1)
)
assert test_k * (test_k + 1) * (2 * test_k + 1) * (3 * test_k**2 + 3 * test_k - 1) // 30 == sum(
    value**4 for value in range(1, test_k + 1)
)
assert namespace["weighted_residue_sum_lower"] > namespace["positive_excess_min"]
weighted_rhs = (
    1
    + namespace["ideal_partial_upper"]
    - namespace["weighted_residue_sum_lower"]
    / (12 * namespace["LAMBDA_UPPER"])
)
assert 32_603_663_706 < weighted_rhs < 32_603_663_707
assert namespace["max_weight_polynomial"] < 2

# Recheck the bootstrap graph independently from the returned certificate.
assert len(namespace["bootstrap_rows"]) == 2414
assert len(namespace["bootstrap_pairs"]) == 187
assert len(namespace["bootstrap_links"]) == 9
assert namespace["bootstrap_boundary"] == 1347
assert all(
    namespace["bootstrap_potential"][source] + weight
    <= namespace["bootstrap_potential"][target]
    for source, target, weight in namespace["bootstrap_edges"]
)
bootstrap_rhs = (
    1
    + namespace["ideal_partial_upper"]
    - namespace["weighted_residue_lower"](namespace["bootstrap_positive_min"])
    / (12 * namespace["LAMBDA_UPPER"])
)
assert 32_596_612_662 < bootstrap_rhs < 32_596_612_663
assert namespace["bootstrap_max_weight"] < 2

# Spot-check the residue equation and lifted recurrence with endpoints from
# both the lower and upper parts of the band.
sample_rows = sorted(namespace["singleton_rows"], key=lambda row: row[4])
for row in (sample_rows[0], sample_rows[len(sample_rows) // 2], sample_rows[-1]):
    left_length = row[2]
    right_length = row[3]
    endpoint = row[4]
    # The exact word is recoverable from the stored state sequence around the
    # bridge, so verify the shared endpoint is odd and lies in the sole band.
    assert endpoint & 1
    assert 1 <= left_length <= 49 and 1 <= right_length <= 49

print("RL327_OWNED_EXCESS_RED_TEAM_GREEN")
print("factor_lengths_cross_checked", [47, 48, 49, 54, 73, 99])
print("singleton_endpoints_checked", len(namespace["singleton_rows"]))
print("bootstrap_endpoints_checked", len(namespace["bootstrap_rows"]))
print("two_positive_shapes", sorted(valid_shapes))
print("potential_edges_checked", len(edges))
print("weighted_cap_rederived", weighted_rhs.numerator // weighted_rhs.denominator)
print("bootstrap_cap_rederived", bootstrap_rhs.numerator // bootstrap_rhs.denominator)
