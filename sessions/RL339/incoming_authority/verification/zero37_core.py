#!/usr/bin/env python3
"""Portable exact zero-run-37 owned-candidate descent certificate."""
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

EXPECTED_COUNTS = [104265,106250,108207,111752,113636,115494,120647,122411,124151,127302,128977,130628,
                   135208,136777,138323,141124,142613,144080,146740,148153,149546,153411,154734,156038,
                   158402,159658,160896,164332,165508,166667,168769,169885,170985,172980,174040,175084,176115]
EXPECTED_MAXIMA = [196,162,229,213,169,164,141,199,162,147,165,179,182,154,192,154,173,159,
                   212,189,169,197,168,161,214,150,153,180,181,163,153,157,177,183,172,183,193]
assert len(EXPECTED_COUNTS) == len(EXPECTED_MAXIMA) == 37
assert sum(EXPECTED_COUNTS) == 5_343_788 and max(EXPECTED_MAXIMA) == 229

def verify(first, last):
    words = factors(36)
    assert len(words) == 37 and 0 <= first < last <= 37
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
    print('RL336_ZERO37_PART_GREEN', first, last, 'count', sum(x for x, _ in rows),
          'max_escape', max(y for _, y in rows))
