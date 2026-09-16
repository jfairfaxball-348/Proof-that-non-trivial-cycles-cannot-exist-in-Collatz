#!/usr/bin/env python3
"""Independent edge-order and congruence checks for the RL336 handover."""
from itertools import product
from functools import lru_cache

E = 137_528_045_312
D = 80_448_749_305
UP = (1 << 76) + (1 << 36)

def residue_lift(gaps):
    r, modulus, constant, power2 = 0, 1, 0, 1
    for gap in gaps:
        constant = (1 << gap) * constant + modulus
        power2 <<= gap
        next_modulus = 3 * modulus
        options = [r + t * modulus for t in range(3)
                   if (power2 * (r + t * modulus) - constant) % next_modulus == 0]
        assert len(options) == 1
        r = options[0]
        modulus = next_modulus
    return r

def mechanical(length):
    cuts = sorted({0, E, *((-D * j) % E for j in range(length + 1))})
    out = set()
    for a, b in zip(cuts, cuts[1:]):
        for phase in (a, a + 1):
            if phase >= b:
                continue
            values = [(phase + D * j + E - 1) // E for j in range(length + 1)]
            out.add(tuple(1 + values[j] - values[j-1] for j in range(1, length + 1)))
    assert len(out) == length + 1
    return out

@lru_cache(None)
def profiles(p):
    return [part + (1,) for part in product(range(1, p+1), repeat=p-1)
            if all(part[j] <= part[j+1] + 1 for j in range(p-2)) and part[-1] <= 2]

for p, low, threshold, prefix_length, expected_prefixes, expected_minimum in (
    (5, 22, 56, 60, 4886, 1_244_028_314_838_852_758_759_941),
    (6, 30, 67, 58, 5778, 1_330_277_458_523_593_058_251_285),
):
    prefixes = set()
    for left in range(low, 38):
        for right in range(low, 38):
            if left + right < threshold:
                continue
            for base in mechanical(left + right + p - 1):
                for profile in profiles(p):
                    ext = (0,) + profile + (0,)
                    gaps = list(base)
                    for offset in range(p+1):
                        gaps[left-1+offset] += ext[offset+1] - ext[offset]
                    if min(gaps) > 0:
                        prefixes.add(tuple(gaps[:prefix_length]))
    assert len(prefixes) == expected_prefixes
    minimum = min(residue_lift(gaps) for gaps in prefixes)
    assert minimum == expected_minimum and minimum > UP

states = range(1, 38)
edges = []
for z in states:
    for nz in states:
        fallback = 5
        if z >= 22 and nz >= 22 and z + nz >= 56:
            fallback = 6
        if z >= 30 and nz >= 30 and z + nz >= 67:
            fallback = 7
        edges.append((z, nz, fallback))
        if z + nz <= 43:
            edges.append((z, nz, 1))
assert len(edges) == 2242
density = {z: max(0, 2*z-43) for z in states}
potential = {z: 0 for z in states}
for _ in states:
    changed = False
    for z, nz, k in reversed(edges):
        slack = density[nz] - density[z] - (2*nz - 43*k)
        assert slack >= 0
        value = potential[z] + 32*(k-2*(nz<=21)) - slack
        if value > potential[nz]:
            potential[nz] = value
            changed = True
    if not changed:
        break
else:
    raise AssertionError('positive cycle')
assert min(potential.values()) == 0 and max(potential.values()) == 43
assert all(potential[z] + 32*(k-2*(nz<=21))
           - (density[nz]-density[z]-(2*nz-43*k)) <= potential[nz]
           for z,nz,k in edges)

def escape(x):
    for steps in range(1001):
        if x < 1 << 71:
            return steps
        y = 3*x+1
        x = y // (y & -y)
    raise AssertionError('witness did not descend')

assert escape(63_442_609_230_978_977_492_819) == 229
assert escape(69_267_243_002_915_637_332_507) == 234
print('RL336_RED_TEAM_GREEN')
print('prefix_minima', 1_244_028_314_838_852_758_759_941,
      1_330_277_458_523_593_058_251_285,
      'graph', len(edges), 'potential_range', min(potential.values()), max(potential.values()))
print('zero_run_max_witnesses', 229, 234)
