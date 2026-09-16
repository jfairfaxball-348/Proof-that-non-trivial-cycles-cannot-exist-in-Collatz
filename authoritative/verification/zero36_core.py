#!/usr/bin/env python3
"""Portable exact zero-run-36 owned-candidate descent certificate, chunked."""
from functools import lru_cache

A = 217_976_794_617
E = 137_528_045_312
D = A - E
LOW = 1 << 71
UP = (1 << 76) + (1 << 36)
MIN_OWNED = 22_689_747_442_693_040_208_618

@lru_cache(None)
def factors(length):
    cuts = sorted({0, E, *((-D * j) % E for j in range(length + 1))})
    words = set()
    for a, b in zip(cuts, cuts[1:]):
        for r in (a, min(a + 1, b - 1)):
            prev = (r + E - 1) // E
            gaps = []
            for j in range(1, length + 1):
                nxt = (r + D * j + E - 1) // E
                gaps.append(1 + nxt - prev)
                prev = nxt
            words.add(tuple(gaps))
    assert len(words) == length + 1
    return tuple(sorted(words))

def start_residue(gaps):
    c = 0
    power3 = 1
    total = 0
    for g in gaps:
        c = (1 << g) * c + power3
        power3 *= 3
        total += g
    return c * pow(1 << total, -1, power3) % power3, power3

def owned_threshold(gaps):
    c = 0
    power3 = 1
    total = 0
    threshold = MIN_OWNED
    for g in gaps:
        c = (1 << g) * c + power3
        power3 *= 3
        total += g
        threshold = max(threshold, (MIN_OWNED * power3 + c + (1 << total) - 1) >> total)
    return threshold

def escape(start, memo):
    x = start
    path = []
    while x >= LOW and x not in memo:
        if len(path) >= 1000:
            raise AssertionError('unresolved candidate')
        path.append(x)
        y = 3 * x + 1
        x = y // (y & -y)
    steps = 0 if x < LOW else memo[x]
    for x in reversed(path):
        steps += 1
        memo[x] = steps
    return steps

EXPECTED_COUNTS = [312796,318750,324623,335257,340909,346483,361942,367233,372454,381907,386930,391885,
                   405626,410330,414970,423373,427838,432242,440219,444457,448638,460232,464201,468116,
                   475206,478973,482689,492996,496524,500003,506305,509655,512957,522118,525254,528347]
EXPECTED_MAXIMA = [208,192,229,213,202,197,198,199,182,215,234,229,192,193,194,170,183,216,
                   212,202,220,197,214,230,214,191,171,180,200,220,161,167,190,194,199,193]
assert len(EXPECTED_COUNTS) == len(EXPECTED_MAXIMA) == 36
assert sum(EXPECTED_COUNTS) == 15_512_438 and max(EXPECTED_MAXIMA) == 234

def verify(first, last):
    words = factors(35)
    assert len(words) == 36 and 0 <= first < last <= 36
    rows = []
    for index in range(first, last):
        gaps = words[index]
        residue, modulus = start_residue(gaps)
        threshold = owned_threshold(gaps)
        start = residue + max(0, (threshold - residue + modulus - 1) // modulus) * modulus
        if not (start & 1):
            start += modulus
        assert start >= threshold and (start - residue) % modulus == 0 and start & 1
        memo = {}
        count = 0
        maximum = 0
        for x in range(start, UP, 2 * modulus):
            count += 1
            maximum = max(maximum, escape(x, memo))
        assert (count, maximum) == (EXPECTED_COUNTS[index], EXPECTED_MAXIMA[index])
        rows.append((count, maximum))
        print('factor', index, 'count', count, 'max_escape', maximum, flush=True)
    print('RL336_ZERO36_PART_GREEN', first, last, 'count', sum(x for x, _ in rows),
          'max_escape', max(y for _, y in rows))
