#!/usr/bin/env python3
"""Exact finite sanity checks for RL122 analytic identities.

This script is not the proof of RL122.1--RL122.5.  It independently checks
the local run identities, the fixed-content diameter formula on a finite
exhaustive word range, the physical packing theorem on every fully owned/legal
word in that range, and the exact L=4,5 algebra used in the corollary.
"""

from itertools import product
from math import gcd

def q_num(bits):
    # Q(w)=sum_{i:d_i=1} 2^i 3^(ones strictly after i)
    suffix_ones = 0
    q = 0
    for i in range(len(bits)-1, -1, -1):
        if bits[i]:
            q += (1 << i) * (3 ** suffix_ones)
            suffix_ones += 1
    return q

def rot(bits, s):
    s %= len(bits)
    return bits[s:] + bits[:s]

def shortcut(x):
    return (3*x+1)//2 if x & 1 else x//2

def run_counts(bits, bit):
    A = len(bits)
    out = {}
    k = 1
    while k <= A:
        c = 0
        for i in range(A):
            if all(bits[(i+j) % A] == bit for j in range(k)):
                c += 1
        if c == 0:
            break
        out[k] = c
        k += 1
    return out

def p_bound(bits):
    zc = run_counts(bits, 0)
    oc = run_counts(bits, 1)
    p0 = max((((m-1) * (2**k) + 1) for k,m in zc.items()), default=0)
    p1 = max((((m-1) * (3**k)) for k,m in oc.items()), default=0)
    return max(p0, p1)

def is_primitive(bits):
    A = len(bits)
    for d in range(1, A):
        if A % d == 0 and bits == bits[:d] * (A//d):
            return False
    return True

# Local even-run and odd-run identities.
local_checks = 0
for k in range(1, 8):
    for x in range(1, 5000):
        y = x
        ok = True
        for _ in range(k):
            if y & 1:
                ok = False
                break
            y //= 2
        if ok:
            assert x % (2**k) == 0
            local_checks += 1

        y = x
        ok = True
        for _ in range(k):
            if not (y & 1):
                ok = False
                break
            y = (3*y+1)//2
        if ok:
            assert (y + 1) % (3**k) == 0
            assert (2**k) * (y+1) == (3**k) * (x+1)
            local_checks += 1

# Exhaustive finite word sanity through A=12.
word_checks = 0
owned_legal_checks = 0
for A in range(2, 13):
    for tup in product((0,1), repeat=A):
        bits = list(tup)
        L = sum(bits)
        Z = A-L
        if L == 0 or Z == 0:
            continue
        D = 2**A - 3**L
        if D <= 0:
            continue
        qs = [q_num(rot(bits,s)) for s in range(A)]
        B = (2**Z - 1) * (3**L - 2**L)
        assert max(qs) - min(qs) <= B
        word_checks += 1

        if not is_primitive(bits):
            continue
        if any(q % D for q in qs):
            continue
        xs = [q//D for q in qs]
        if any(x <= 0 for x in xs):
            continue
        # Check that rooted states follow the cyclic shortcut word.
        legal = True
        for i,x in enumerate(xs):
            if (x & 1) != bits[i]:
                legal = False
                break
            if shortcut(x) != xs[(i+1) % A]:
                legal = False
                break
        if not legal:
            continue

        W = max(xs) - min(xs)
        P = p_bound(bits)
        assert W >= P
        assert D*P <= B
        owned_legal_checks += 1

# Exact algebra behind the infinite Z>=4 L=4,5 deductions.
# L=4: 9D-B = 79*2^Z-664 > 0 for Z>=4.
assert 79*(2**4) - 664 > 0
# L=5: 12D-B = 173*2^Z-2705 > 0 for Z>=4.
assert 173*(2**4) - 2705 > 0

# Generalized-increment discriminator identity on odd runs.
for s in range(-7, 8):
    if s == 0:
        continue
    for k in range(1, 6):
        for x in range(1, 1000):
            y = x
            ok = True
            for _ in range(k):
                if not (y & 1):
                    ok = False
                    break
                num = 3*y + s
                if num % 2:
                    ok = False
                    break
                y = num//2
            if ok:
                assert (2**k)*(y+s) == (3**k)*(x+s)

print("RL122 run-fibre verifier: PASS")
print("local_run_checks =", local_checks)
print("fixed_content_words =", word_checks)
print("fully_owned_legal_words =", owned_legal_checks)
print("scope = finite sanity only; RL122 theorems are analytic")
