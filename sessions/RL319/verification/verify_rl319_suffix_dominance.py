#!/usr/bin/env python3
"""Exact regression for RL319 rankwise suffix dominance.

Enumeration is evidence only; the analytic proof is in the checkpoint note.
"""

from itertools import combinations


def numerator_from_positions(positions):
    weight = len(positions)
    return sum(2**position * 3 ** (weight - 1 - rank)
               for rank, position in enumerate(positions))


checks = 0
strict_checks = 0
equality_checks = 0

for length in range(2, 12):
    for weight in range(1, length):
        words = list(combinations(range(length), weight))
        for physical in words:
            for shadow in words:
                if not all(p <= t for p, t in zip(physical, shadow)):
                    continue
                for cut in range(1, length + 1):
                    consumed_physical = sum(position < cut for position in physical)
                    consumed_shadow = sum(position < cut for position in shadow)
                    lead = consumed_physical - consumed_shadow
                    assert lead >= 0

                    alpha = tuple(position - cut for position in physical if position >= cut)
                    beta = tuple(position - cut for position in shadow if position >= cut)
                    assert len(beta) - len(alpha) == lead

                    for index, position in enumerate(alpha):
                        assert beta[lead + index] >= position

                    q_alpha = numerator_from_positions(alpha)
                    q_beta = numerator_from_positions(beta)
                    assert q_beta >= q_alpha
                    if q_beta == q_alpha:
                        assert lead == 0 and alpha == beta
                        equality_checks += 1
                    else:
                        strict_checks += 1
                    checks += 1

assert checks > 0 and strict_checks > 0 and equality_checks > 0
print("RL319 suffix dominance regression: PASS")
print(f"rankwise_suffix_checks={checks}")
print(f"strict_cases={strict_checks}")
print(f"equality_cases={equality_checks}")
print("scope=regression evidence; analytic proof is in the checkpoint note")
