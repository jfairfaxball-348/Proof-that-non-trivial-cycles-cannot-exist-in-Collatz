#!/usr/bin/env python3
"""Independent A<=18 direct-word red team for RL269 [1,1,1,1,1]."""
from collections import Counter
from math import gcd

def Q(bits):
    L = sum(bits)
    q = 0
    r = 0
    for i, b in enumerate(bits):
        if b:
            r += 1
            q += (1 << i) * (3 ** (L - r))
    return q

def rotate(bits, m):
    return bits[m:] + bits[:m]

def optimal_flow(bits, m):
    y = rotate(bits, m)
    pref = []
    s = 0
    for a, b in zip(bits, y):
        s += a - b
        pref.append(s)
    med = sorted(pref)[(len(pref) - 1) // 2]
    return [z - med for z in pref]

def components(g):
    zeros = [i for i, v in enumerate(g) if v == 0]
    if not zeros:
        z = g
    else:
        k = zeros[0]
        z = g[k:] + g[:k]
    out = []
    cur = []
    for v in z:
        if v == 0:
            if cur:
                out.append(cur)
                cur = []
        else:
            cur.append(v)
    if cur:
        out.append(cur)
    return out

def edge_formula_after_zero_cut(x, m):
    y = rotate(x, m)
    pref = []
    s = 0
    for a, b in zip(x, y):
        s += a - b
        pref.append(s)
    L = sum(x)
    R = 0
    E = 0
    for i, (b, g) in enumerate(zip(x, pref)):
        R += b
        if g == 1:
            E += (1 << i) * (3 ** (L - R))
        elif g == -1:
            E -= (1 << i) * (3 ** (L - R - 1))
        else:
            assert g == 0
    return E, pref

raw = kp = km = full = proper = det_mismatch = edge_mismatch = 0
byA = Counter()

for A in range(1, 19):
    for mask in range(1 << A):
        bits = [(mask >> i) & 1 for i in range(A)]
        L = sum(bits)
        D = (1 << A) - 3 ** L
        if D <= 1:
            continue
        q0 = Q(bits)
        for m in range(1, A):
            g = optimal_flow(bits, m)
            if sum(abs(v) for v in g) != 5:
                continue
            if max(abs(v) for v in g) > 1:
                continue
            rr = components(g)
            if sorted((len(r) for r in rr), reverse=True) != [1, 1, 1, 1, 1]:
                continue
            kappa = sum(g)
            if abs(kappa) != 1:
                continue

            raw += 1
            byA[A] += 1
            if kappa == 1:
                kp += 1
            else:
                km += 1

            if (m * L + kappa) % A:
                det_mismatch += 1
            else:
                q = (m * L + kappa) // A
                if q * A - m * L != kappa:
                    det_mismatch += 1

            direct = Q(rotate(bits, m)) - q0
            if direct % D == 0:
                full += 1
            elif gcd(abs(direct), D) > 1:
                proper += 1

            if kappa == 1:
                z = next(i for i, v in enumerate(g) if v == 0)
                x = rotate(bits, z + 1)
                E, pref = edge_formula_after_zero_cut(x, m)
                direct_cut = Q(rotate(x, m)) - Q(x)
                if pref != rotate(g, z + 1) or E != direct_cut:
                    edge_mismatch += 1

assert raw == 8996
assert kp == 4498 and km == 4498
assert full == 0
assert proper == 714
assert det_mismatch == 0
assert edge_mismatch == 0
assert byA == Counter({17:4828, 18:1368, 15:1200, 16:1088, 13:364, 14:56, 12:48, 11:44})

print("PASS RL269 independent A<=18 [1,1,1,1,1] red team")
print("abs_kappa1_[1,1,1,1,1]_A_le_18=8996")
print("kappa_plus=4498 kappa_minus=4498")
print("full_D_hits=0")
print("proper_factor_only=714")
print("determinant_mismatches=0")
print("zero_cut_edge_identity_mismatches=0")
print("RL269_REDTEAM_PASS")
