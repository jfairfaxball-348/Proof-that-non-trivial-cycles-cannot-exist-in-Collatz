#!/usr/bin/env python3
"""Exact regression for the RL319 crossing residue and local barrier.

The finite loops are regression evidence only. The proofs and scope are in
RL319_CROSSING_RESIDUE_AND_SUFFIX_BRIDGE.md.
"""

from math import gcd


def step_h(value, h):
    if value % 2:
        return (3 * value + h) // 2, 1
    return value // 2, 0


phase_checks = 0
crossing_checks = 0

for h in range(5, 160, 2):
    if gcd(h, 6) != 1:
        continue
    for R in range(2, 40):
        for E in range(1, min(h * R, 35)):
            if gcd(h, E) != 1:
                continue
            physical = h * R
            shadow = physical - E
            if shadow <= 0:
                continue
            shadow_ones = 0
            delta = E
            power_two = 1
            for _phase in range(20):
                assert physical % h == 0
                assert gcd(shadow, h) == 1
                assert gcd(delta, h) == 1
                assert (power_two * delta - pow(3, shadow_ones, h) * E) % h == 0

                next_physical, physical_bit = step_h(physical, h)
                next_shadow, shadow_bit = step_h(shadow, h)
                next_delta = next_physical - next_shadow

                if delta > 0 and next_delta < 0:
                    assert physical_bit == 0
                    assert shadow_bit == 1
                    p = physical // h
                    q = -next_delta
                    assert p % 2 == 0
                    assert h * (2 * p + 1) == 3 * delta + 2 * q
                    assert gcd(q, h) == 1
                    assert ((3 * delta + 2 * q) // h) % 4 == 1
                    crossing_checks += 1

                physical = next_physical
                shadow = next_shadow
                delta = next_delta
                shadow_ones += shadow_bit
                power_two *= 2
                phase_checks += 1

# Exact local saturation: every admissible h has reverse crossings of the
# required divisibility/coprimality type.
family_checks = 0
for h in range(5, 1000, 2):
    if gcd(h, 6) != 1:
        continue
    for p in range(2, 42, 2):
        physical = h * p
        shadow = physical - 1
        next_physical, physical_bit = step_h(physical, h)
        next_shadow, shadow_bit = step_h(shadow, h)
        q = next_shadow - next_physical
        assert physical_bit == 0 and shadow_bit == 1
        assert q > 0
        assert q == (h * (2 * p + 1) - 3) // 2
        assert gcd(q, h) == 1
        assert h * (2 * p + 1) == 3 + 2 * q
        family_checks += 1

assert phase_checks > 0
assert crossing_checks > 0
assert family_checks > 0

print("RL319 crossing residue regression: PASS")
print(f"phase_checks={phase_checks}")
print(f"observed_crossing_checks={crossing_checks}")
print(f"all_h_local_saturation_checks={family_checks}")
print("scope=regression evidence; analytic proof is in the checkpoint note")
