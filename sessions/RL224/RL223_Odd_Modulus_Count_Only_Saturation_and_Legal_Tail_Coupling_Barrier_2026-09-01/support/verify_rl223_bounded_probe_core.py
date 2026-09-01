#!/usr/bin/env python3
"""Gap-free verifier for the bounded RL223 unconstrained residue probe.

The verifier independently recomputes every modulus in the declared interval,
checks there are no omitted eligible q, validates every fixed-weight residue
witness, and checks the compressed authoritative-witness target construction.
It verifies only the explicitly declared unconstrained relaxation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Dict, List, Tuple


EXPECTED_A = 217_976_794_617
EXPECTED_L = 137_528_045_312
EXPECTED_N = EXPECTED_A - 24
EXPECTED_M = EXPECTED_L - 16
EXPECTED_WITNESS = {
    "Q16": 43_079_489,
    "eta": 3_722_043_165_201,
    "k": 28_821,
    "state": "011",
    "y0": 24_921_895_945_404_894_117_887,
    "y16": 63_944_214_675_001_842_327_551,
}


def numerator_mod(word: str, q: int) -> int:
    value = 0
    two_power = 1 % q
    for bit in word:
        assert bit in "01"
        if bit == "1":
            value = (3 * value + two_power) % q
        two_power = (2 * two_power) % q
    return value


def independent_first_slice(q: int, max_h: int) -> Tuple[int, int, Dict[int, str]] | None:
    """Independent forward DP over (length, exact weight, Q mod q)."""
    states: List[Dict[int, str]] = [{0: ""}]
    power_two = 1 % q
    for h in range(1, max_h + 1):
        advanced: List[Dict[int, str]] = [dict() for _ in range(h + 1)]
        for weight in range(h):
            for residue in sorted(states[weight]):
                word = states[weight][residue]
                advanced[weight].setdefault(residue, word + "0")
                new_residue = (3 * residue + power_two) % q
                advanced[weight + 1].setdefault(new_residue, word + "1")
        states = advanced
        power_two = (power_two * 2) % q
        for weight in range(h + 1):
            if set(states[weight]) == set(range(q)):
                return h, weight, states[weight]
    return None


def multiplicative_order(a: int, q: int) -> int:
    assert math.gcd(a, q) == 1
    value = 1
    for exponent in range(1, q + 1):
        value = (value * a) % q
        if value == 1:
            return exponent
    raise AssertionError("unit order not found within q")


def uniform_capacity_bound(capacity: int) -> int:
    q = (1 + math.isqrt(1 + 4 * capacity)) // 2
    while (q + 1) * q <= capacity:
        q += 1
    while q * (q - 1) > capacity:
        q -= 1
    return q


def verify(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["format"] == "rl223-unconstrained-fixed-weight-residue-probe-v1"
    assert data["promotion_status"] == "PROMOTED_BY_RL223_AT_UNCONSTRAINED_COUNT_ONLY_SCOPE"
    assert data["authoritative_parameters"] == {
        "A": EXPECTED_A,
        "L": EXPECTED_L,
        "M": EXPECTED_M,
        "N": EXPECTED_N,
        "zeros": EXPECTED_N - EXPECTED_M,
    }
    assert data["authoritative_witness"] == EXPECTED_WITNESS
    scope = data["scope"]
    assert "all binary words of total length N" in scope["represented"]
    assert "candidate-specific parity/2-adic legality from fixed y16" in scope["not_represented"]
    assert "H21 phase/state/incidence/charge constraints after phase 16" in scope["not_represented"]

    block_lemma = data["analytic_block_switch_lemma"]
    assert block_lemma["promotion_status"] == "PROMOTED_BY_RL223_AT_UNCONSTRAINED_COUNT_ONLY_SCOPE"
    assert block_lemma["scope"] == "unconstrained fixed-(N,M) binary words only"
    capacity = min(EXPECTED_M, EXPECTED_N - EXPECTED_M)
    uniform_q_bound = uniform_capacity_bound(capacity)
    assert block_lemma["capacity"] == capacity == 80_448_749_297
    assert block_lemma["uniform_q_upper_bound_inclusive"] == uniform_q_bound == 283_635
    assert block_lemma["uniform_bound_product"] == uniform_q_bound * (uniform_q_bound - 1)
    assert block_lemma["next_integer_product"] == (uniform_q_bound + 1) * uniform_q_bound
    assert uniform_q_bound * (uniform_q_bound - 1) <= capacity
    assert (uniform_q_bound + 1) * uniform_q_bound > capacity

    bounds = data["bounded_search"]
    q_min = bounds["q_min"]
    q_max = bounds["q_max"]
    max_h = bounds["max_prefix_length"]
    assert q_min == 5
    expected_qs = [q for q in range(q_min, q_max + 1) if q % 2 == 1 and math.gcd(q, 6) == 1]
    records = data["moduli"]
    assert [record["q"] for record in records] == expected_qs
    assert bounds["tested_modulus_count"] == len(expected_qs)

    saturated = 0
    unsaturated: List[int] = []
    largest_minimal_h = 0
    largest_prefix_weight = 0
    largest_prefix_zeros = 0
    for record in records:
        q = record["q"]
        assert math.gcd(q, 6) == 1 and q % 2 == 1
        ratio = 4 * pow(3, -1, q) % q
        order = multiplicative_order(ratio, q)
        block_count = q * order
        assert block_count <= q * (q - 1) <= capacity
        assert pow(ratio, order, q) == 1
        equal_increment = pow(3, block_count - 1, q)
        assert math.gcd(equal_increment, q) == 1
        assert {
            (switch_count * equal_increment) % q for switch_count in range(q)
        } == set(range(q))
        result = independent_first_slice(q, max_h)
        if result is None:
            assert record == {"q": q, "status": "NOT_SATURATED_WITHIN_BOUND"}
            unsaturated.append(q)
            continue

        saturated += 1
        h, weight, witnesses = result
        assert record["status"] == "SURJECTIVE_UNCONSTRAINED_FIXED_WEIGHT_PREFIX"
        assert record["minimal_prefix_length"] == h
        assert record["prefix_weight"] == weight
        assert record["reachable_count"] == q
        assert set(witnesses) == set(range(q))
        for residue in range(q):
            word = witnesses[residue]
            assert len(word) == h
            assert word.count("1") == weight
            assert numerator_mod(word, q) == residue
        canonical = "\n".join(f"{residue}:{witnesses[residue]}" for residue in range(q))
        assert record["witness_map_sha256"] == hashlib.sha256(canonical.encode("ascii")).hexdigest()

        largest_minimal_h = max(largest_minimal_h, h)
        largest_prefix_weight = max(largest_prefix_weight, weight)
        largest_prefix_zeros = max(largest_prefix_zeros, h - weight)
        remaining_ones = EXPECTED_M - weight
        remaining_zeros = (EXPECTED_N - EXPECTED_M) - (h - weight)
        assert remaining_ones >= 0 and remaining_zeros >= 0
        target = (
            pow(2, EXPECTED_N, q) * EXPECTED_WITNESS["y0"]
            - pow(3, EXPECTED_M, q) * EXPECTED_WITNESS["y16"]
        ) % q
        witness_record = record["authoritative_witness"]
        assert witness_record["target_tail_numerator_mod_q"] == target
        assert witness_record["target_endpoint_mod_q"] == EXPECTED_WITNESS["y0"] % q
        assert witness_record["intersection_nonempty"] is True

        construction = witness_record["construction"]
        prefix = construction["prefix_word"]
        prefix_residue = construction["prefix_residue"]
        assert prefix == witnesses[prefix_residue]
        assert numerator_mod(prefix, q) == prefix_residue
        assert construction["remaining_ones"] == remaining_ones
        assert construction["remaining_zeros"] == remaining_zeros
        suffix_q = (pow(3, remaining_ones, q) - pow(2, remaining_ones, q)) % q
        assert construction["suffix_numerator_mod_q"] == suffix_q
        achieved = (
            pow(3, remaining_ones, q) * prefix_residue
            + pow(2, h, q) * suffix_q
        ) % q
        assert achieved == target == construction["achieved_tail_numerator_mod_q"]
        endpoint = (
            pow(pow(2, EXPECTED_N, q), -1, q)
            * (pow(3, EXPECTED_M, q) * EXPECTED_WITNESS["y16"] + achieved)
        ) % q
        assert endpoint == EXPECTED_WITNESS["y0"] % q

    assert bounds["saturated_modulus_count"] == saturated
    assert bounds["unsaturated_moduli"] == unsaturated
    return {
        "status": "PASS",
        "verified_scope": "unconstrained fixed-(N,M) binary words only; no legal-H21 continuation claim",
        "q_min": q_min,
        "q_max": q_max,
        "eligible_moduli_checked_gap_free": len(expected_qs),
        "surjective_moduli": saturated,
        "unsaturated_within_bound": unsaturated,
        "largest_minimal_prefix_length": largest_minimal_h,
        "largest_selected_prefix_weight": largest_prefix_weight,
        "largest_selected_prefix_zero_count": largest_prefix_zeros,
        "authoritative_witness_target_intersections": saturated,
        "analytic_uniform_q_upper_bound_inclusive": uniform_q_bound,
        "analytic_uniform_scope": "unconstrained binary words; proof uses block switches and Euler's theorem",
        "outside_bounds": "NOT PROMOTED / NOT VERIFIED",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify(args.certificate)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(rendered, encoding="utf-8")
    print(
        "PASS",
        f"q={result['q_min']}..{result['q_max']}",
        f"eligible={result['eligible_moduli_checked_gap_free']}",
        f"surjective={result['surjective_moduli']}",
        f"max_minimal_h={result['largest_minimal_prefix_length']}",
        "scope=UNCONSTRAINED_BINARY_WORDS_ONLY",
    )


if __name__ == "__main__":
    main()
