#!/usr/bin/env python3
"""Exact prefix obstructions plus the q=32 all-length potential."""
from itertools import product
from functools import lru_cache

A = 217_976_794_617
ELL = 137_528_045_312
D = A - ELL
UP = (1 << 76) + (1 << 36)

def mechanical_words(length):
    cuts = sorted({0, ELL, *((-D * j) % ELL for j in range(length + 1))})
    words = set()
    for lo, hi in zip(cuts, cuts[1:]):
        for phase in (lo, lo + 1):
            if phase >= hi:
                continue
            ceilings = [(phase + D * j + ELL - 1) // ELL for j in range(length + 1)]
            words.add(tuple(1 + ceilings[j] - ceilings[j - 1] for j in range(1, length + 1)))
    assert len(words) == length + 1
    return words

@lru_cache(None)
def profiles(p):
    result = []
    for first in product(range(1, p + 1), repeat=p - 1):
        profile = first + (1,)
        if all(profile[j] <= profile[j + 1] + 1 for j in range(p - 1)):
            result.append(profile)
    return result

assert len(profiles(5)) == 42 and len(profiles(6)) == 132

def prefix_residue(gaps):
    constant = 0
    power2 = 1
    power3 = 1
    for gap in gaps:
        constant = (1 << gap) * constant + power3
        power2 <<= gap
        power3 *= 3
    return constant * pow(power2, -1, power3) % power3

def verify_family(p, low, threshold, prefix_length, expected_pairs, expected_prefixes, expected_minimum):
    prefixes = set()
    pair_count = 0
    template_count = 0
    for left in range(low, 38):
        for right in range(low, 38):
            if left + right < threshold:
                continue
            pair_count += 1
            for base in mechanical_words(left + right + p - 1):
                for profile in profiles(p):
                    extended = (0,) + profile + (0,)
                    gaps = list(base)
                    for offset in range(p + 1):
                        gaps[left - 1 + offset] += extended[offset + 1] - extended[offset]
                    if min(gaps) > 0:
                        template_count += 1
                        prefixes.add(tuple(gaps[:prefix_length]))
    assert pair_count == expected_pairs
    assert len(prefixes) == expected_prefixes
    minimum = min(prefix_residue(gaps) for gaps in prefixes)
    assert minimum == expected_minimum and minimum > UP
    assert 3 ** prefix_length > UP
    print('family', p, 'pairs', pair_count, 'templates', template_count,
          'prefix_length', prefix_length, 'distinct_prefixes', len(prefixes),
          'minimum_residue', minimum)

verify_family(5, 22, 56, 60, 178, 4886, 1_244_028_314_838_852_758_759_941)
verify_family(6, 30, 67, 58, 36, 5778, 1_330_277_458_523_593_058_251_285)

def density(z):
    return max(0, 2 * z - 43)

edges = []
for z in range(1, 38):
    for nz in range(1, 38):
        if z + nz <= 43:
            edges.append((z, nz, 1))
        fallback = 5
        if z >= 22 and nz >= 22 and z + nz >= 56:
            fallback = 6
        if z >= 30 and nz >= 30 and z + nz >= 67:
            fallback = 7
        edges.append((z, nz, fallback))
assert len(edges) == 2242
potential = {z: 0 for z in range(1, 38)}
for _ in range(37):
    changed = False
    for z, nz, k in edges:
        slack = density(nz) - density(z) - (2 * nz - 43 * k)
        assert slack >= 0
        weight = 32 * (k - 2 * (nz <= 21)) - slack
        if potential[z] + weight > potential[nz]:
            potential[nz] = potential[z] + weight
            changed = True
    if not changed:
        break
else:
    raise AssertionError('positive q=32 cycle')
assert min(potential.values()) == 0 and max(potential.values()) == 43
assert all(potential[z] + 32 * (k - 2 * (nz <= 21))
           - (density(nz) - density(z) - (2 * nz - 43 * k)) <= potential[nz]
           for z, nz, k in edges)
print('RL336_Q32_PREFIX_GREEN', 'edges', len(edges), 'potential_range',
      min(potential.values()), max(potential.values()))
