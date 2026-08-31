#!/usr/bin/env python3
"""Bounded independent audit checks for the RL195 owned-local component.

Small word lemma: every odd seed class for lengths0..3, exponents1..4.
Actual graph: every final depth3 path also has a positive local witness
with parameter t=0 mod3. This adds no global or physical-realization claim.
"""

import importlib.util
from itertools import product
from pathlib import Path


SOURCE = Path(__file__).resolve().parents[1] / "verification" / "verify_rl195_owned_local_realizability.py"
spec = importlib.util.spec_from_file_location("rl195_owned_review_target", SOURCE)
target = importlib.util.module_from_spec(spec)
spec.loader.exec_module(target)


def valuation(n):
    answer = 0
    assert n > 0
    while n % 2 == 0:
        answer += 1
        n //= 2
    return answer


def brute_word_classes():
    word_count = residue_count = 0
    for depth in range(4):
        for word in product(range(1, 5), repeat=depth):
            expected, modulus, total, _ = target.word_residue(word)
            assert modulus == 2 ** (sum(word) + 1)
            assert total == sum(word)
            good_seeds = []
            for seed in range(1, modulus, 2):
                residue_count += 1
                x = seed
                compatible = True
                for exponent in word:
                    n = 3 * x + 1
                    if valuation(n) != exponent:
                        compatible = False
                        break
                    x = n // (2**exponent)
                    assert x > 0 and x % 2 == 1
                if compatible:
                    good_seeds.append(seed)
            assert good_seeds == [expected]
            word_count += 1
    assert word_count == 85
    assert residue_count == 27_931
    return word_count, residue_count


def verify_alternative_odd_class():
    # Build every full path without merging its history; the target's
    # transition rule has separately been audited against inherited scope.
    paths = [(root, ()) for root in target.INITIAL]
    cache = {}
    counts = []
    for depth, c in enumerate((2, 1, 2)):
        successor_paths = []
        for root, records in paths:
            state = records[-1][0] if records else root
            key = depth, state
            if key not in cache:
                cache[key] = tuple(target.transitions(state, c))
            for edge in cache[key]:
                successor_paths.append((root, records + (edge,)))
        paths = successor_paths
        counts.append(len(paths))
    assert counts == [540, 4517, 34_039]

    roots = set()
    patterns = set()
    for root, records in paths:
        aa = tuple(edge[1] for edge in records)
        bb = tuple(edge[2] for edge in records)
        residue, modulus, _, _ = target.seed_class(root, aa, bb)
        # Independent CRT construction for an allowed initial class
        # deliberately excluded by the original helper's extra mod3 check.
        t = residue + modulus * ((-residue * pow(modulus, -1, 3)) % 3)
        stride = 3 * modulus
        threshold = target.C0 + 1
        if t < threshold:
            t += ((threshold - t + stride - 1) // stride) * stride
        assert t >= threshold and t % modulus == residue and t % 3 == 0
        h, hp, C = root
        assert C == 3**37
        g = h - hp
        if g > 0:
            x, z = 2**g * t - C, t
        else:
            x, z = t, 2 ** (-g) * t + C
        assert x > 0 and z > 0 and x % 2 == z % 2 == 1
        assert x % 3 == z % 3 == 0
        sign_pattern = [(h > hp) - (h < hp)]
        for c, (successor, a, b) in zip((2, 1, 2), records):
            assert valuation(3 * x + 1) == a
            assert valuation(3 * z + 1) == b
            x, z = (3 * x + 1) // (2**a), (3 * z + 1) // (2**b)
            h, hp = h + c - a, hp + c - b
            assert (h, hp) == successor[:2]
            assert h >= 0 and hp >= 0
            assert x > 0 and z > 0 and x % 2 == z % 2 == 1
            assert x % 3 != 0 and z % 3 != 0
            actual_C = 2 ** max(h - hp, 0) * z - 2 ** max(hp - h, 0) * x
            assert actual_C == successor[2]
            sign_pattern.append((h > hp) - (h < hp))
        roots.add(root)
        patterns.add(tuple(sign_pattern))
    assert roots == set(target.INITIAL) and len(roots) == 42
    assert len(patterns) == 44
    return len(paths), len(roots), len(patterns)


if __name__ == "__main__":
    words, residues = brute_word_classes()
    paths, roots, patterns = verify_alternative_odd_class()
    print(f"PASS: brute_word_lemma_words={words}; exact_odd_residues={residues}")
    print(f"PASS: alternative_initial_class=t=0(mod3); full_depth3_paths={paths}")
    print(f"all_roots={roots}; four_source_sign_patterns={patterns}")
    print("scope=uncoupled_positive_odd_local_trajectories_only; NOT_PROMOTED")
