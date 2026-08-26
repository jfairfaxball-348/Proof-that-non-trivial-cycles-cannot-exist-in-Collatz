#!/usr/bin/env python3
"""Portable exact checks for the RL102 handover."""

from itertools import product
from math import gcd


def numerator(word):
    total, later = 0, sum(word)
    for i, bit in enumerate(word):
        if bit:
            later -= 1
            total += (1 << i) * 3**later
    return total


def prefix_suffix_checks():
    all_checks = owned_checks = 0
    for length in range(2, 13):
        for word in product((0, 1), repeat=length):
            weight = sum(word)
            if weight in (0, length):
                continue
            full_q = numerator(word)
            d = (1 << length) - 3**weight
            for cut in range(1, length):
                a, b = word[:cut], word[cut:]
                u, v = 1 << cut, 3**sum(a)
                assert full_q == 3**sum(b) * numerator(a) + u * numerator(b)
                assert u * numerator(b + a) - v * full_q == d * numerator(a)
                all_checks += 1
                if d > 0 and full_q % d == 0:
                    m = full_q // d
                    assert (v * m + numerator(a)) % u == 0
                    x = (v * m + numerator(a)) // u
                    assert (1 << len(b)) * m == 3**sum(b) * x + numerator(b)
                    owned_checks += 1
    return all_checks, owned_checks


def generalized_witness_check():
    p, q, big_g, raw_g = 65, 41, 3, 2
    a, ell = big_g * p, big_g * q
    raw_a, raw_ell = raw_g * p, raw_g * q
    backward, ones = [], 0
    for i in range(1, raw_a):
        need = 0
        while 3**need < 2**i:
            need += 1
        bit = int(need > ones)
        backward.append(bit); ones += bit
    backward.append(0)
    assert sum(backward) == raw_ell
    assert all(2**i <= 3**sum(backward[:i]) for i in range(1, raw_a))
    assert 2**raw_a > 3**raw_ell
    complement, ones = [], 0
    for i in range(1, p):
        allowed = 0
        while 3 ** (allowed + 1) <= 2**i:
            allowed += 1
        bit = int(allowed > ones)
        complement.append(bit); ones += bit
    complement.append(1)
    word = complement + list(reversed(backward))
    assert all(a % d or tuple(word) != tuple(word[:d]) * (a // d)
               for d in range(1, a))
    d = 2**a - 3**ell
    qword = numerator(word)
    increment = d // gcd(d, qword)
    states = [qword // gcd(d, qword)]
    for bit in word:
        x = states[-1]
        states.append(x // 2 if bit == 0 else (3 * x + increment) // 2)
    assert states[-1] == states[0] == max(states[:-1])
    assert 2 * states[a - p] < states[0]
    assert 16 * states[a - raw_a] > 15 * states[0]
    assert increment > 1
    return increment


all_checks, owned_checks = prefix_suffix_checks()
increment = generalized_witness_check()
print("RL102 prefix/suffix and excursion verifier: PASS")
print("word/split checks =", all_checks)
print("owned closure checks =", owned_checks)
print("generalized witness increment =", increment)
