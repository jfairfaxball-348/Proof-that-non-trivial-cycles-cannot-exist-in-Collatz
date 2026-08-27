#!/usr/bin/env python3
"""RL123 verification and exact residual certificate.

Analytic theorems are proved in the RL123 report. This script independently
sanity-checks their finite combinatorics and supplies the explicitly classified
exact finite residual certificate used only for the low-L corollary.
"""
from itertools import combinations, product
from math import comb


def q_num_from_positions(pos, L):
    q = 0
    for j, p in enumerate(pos):
        q += (1 << p) * (3 ** (L - 1 - j))
    return q


def is_primitive_bits(bits):
    A = len(bits)
    for d in range(1, A):
        if A % d == 0 and bits == bits[:d] * (A // d):
            return False
    return True


def balanced_parts(n, t):
    q, r = divmod(n, t)
    return [q + 1] * r + [q] * (t - r)


def occupancy(parts, k):
    return sum(max(a - k + 1, 0) for a in parts)


def sharp_occupancy_floor(n, t, k):
    return max(n - t * (k - 1), 0)


def side_floor(n, t, base, zero_side=False):
    best = 0
    k = 1
    while True:
        c = sharp_occupancy_floor(n, t, k)
        if c <= 0:
            break
        v = (c - 1) * (base ** k) + (1 if zero_side else 0)
        best = max(best, v)
        k += 1
    return best


def H_floor(L, Z):
    return min(
        max(side_floor(Z, t, 2, True), side_floor(L, t, 3, False), 6 * (t - 1))
        for t in range(1, min(L, Z) + 1)
    )


def run_pairs(bits):
    A = len(bits)
    if all(b == bits[0] for b in bits):
        return []
    s = next(i for i in range(A) if bits[i] == 1 and bits[(i - 1) % A] == 0)
    out = []
    i = s
    while True:
        o = 0
        while bits[i % A] == 1:
            o += 1
            i += 1
        z = 0
        while bits[i % A] == 0:
            z += 1
            i += 1
        out.append((o, z))
        if i % A == s:
            break
    return out


def run_counts(bits, bit):
    A = len(bits)
    out = {}
    for k in range(1, A + 1):
        c = sum(all(bits[(i + j) % A] == bit for j in range(k)) for i in range(A))
        if c == 0:
            break
        out[k] = c
    return out


def p_plus_word(bits):
    zc = run_counts(bits, 0)
    oc = run_counts(bits, 1)
    p0 = max((((m - 1) * (2 ** k) + 1) for k, m in zc.items()), default=0)
    p1 = max(((m - 1) * (3 ** k) for k, m in oc.items()), default=0)
    crt = 0
    pairs = run_pairs(bits)
    if pairs:
        maxj = max(o for o, _ in pairs)
        maxk = max(z for _, z in pairs)
        for j in range(1, maxj + 1):
            for k in range(1, maxk + 1):
                c = sum(o >= j and z >= k for o, z in pairs)
                if c:
                    crt = max(crt, (c - 1) * (3 ** j) * (2 ** k))
    return max(p0, p1, crt)


def shortcut(x):
    return (3 * x + 1) // 2 if x & 1 else x // 2


def q_num(bits):
    return q_num_from_positions([i for i, b in enumerate(bits) if b], sum(bits))


def rot(bits, s):
    s %= len(bits)
    return bits[s:] + bits[:s]


def flow_distance(bits, s):
    A = len(bits)
    dif = [bits[i] - bits[(i + s) % A] for i in range(A)]
    pref = []
    u = 0
    for d in dif:
        u += d
        pref.append(u)
    med = sorted(pref)[A // 2]
    return sum(abs(v - med) for v in pref)


def window_distance(bits, s):
    A = len(bits)
    hs = [sum(bits[(i + r) % A] for r in range(1, s + 1)) for i in range(A)]
    med = sorted(hs)[A // 2]
    return sum(abs(h - med) for h in hs)


# 1) Exact run-occupancy floor: finite sanity and simultaneous balanced attainment.
occupancy_checks = 0
for n in range(1, 31):
    for t in range(1, n + 1):
        bal = balanced_parts(n, t)
        for k in range(1, n + 2):
            floor = sharp_occupancy_floor(n, t, k)
            assert occupancy(bal, k) == floor
            occupancy_checks += 1

# 2) Window-count transport identity and the exact s=2 formula.
window_checks = 0
for A in range(2, 11):
    for tup in product((0, 1), repeat=A):
        bits = list(tup)
        L = sum(bits)
        Z = A - L
        if L == 0 or Z == 0:
            continue
        pairs = run_pairs(bits)
        t = len(pairs)
        for s in range(1, A):
            assert flow_distance(bits, s) == window_distance(bits, s)
            window_checks += 1
        if A > 2:
            assert flow_distance(bits, 2) == min(2 * L, 2 * Z, A - 2 * t)

# 3) New CRT packing bound on every fully-owned legal primitive word through A=12.
owned_legal_checks = 0
for A in range(2, 13):
    for tup in product((0, 1), repeat=A):
        bits = list(tup)
        L = sum(bits)
        Z = A - L
        if L == 0 or Z == 0 or not is_primitive_bits(bits):
            continue
        D = (1 << A) - 3 ** L
        if D <= 0:
            continue
        qs = [q_num(rot(bits, s)) for s in range(A)]
        if any(q % D for q in qs):
            continue
        xs = [q // D for q in qs]
        if any(x <= 0 for x in xs):
            continue
        legal = True
        for i, x in enumerate(xs):
            if (x & 1) != bits[i] or shortcut(x) != xs[(i + 1) % A]:
                legal = False
                break
        if not legal:
            continue
        W = max(xs) - min(xs)
        assert W >= p_plus_word(bits)
        owned_legal_checks += 1

# 4) Analytic semi-infinite packing thresholds used in the low-L corollary.
# L=6: W>=18 for Z>=5.
assert (18 * 64 - (3**6 - 2**6)) > 0
assert 18 * ((1 << 11) - 3**6) > ((1 << 5) - 1) * (3**6 - 2**6)
# L=7: W>=18 for Z>=8.
assert (18 * 128 - (3**7 - 2**7)) > 0
assert 18 * ((1 << 15) - 3**7) > ((1 << 8) - 1) * (3**7 - 2**7)
# L=8: H(8,12)=25 and W>=25 thereafter.
assert H_floor(8, 12) == 25
assert (25 * 256 - (3**8 - 2**8)) > 0
assert 25 * ((1 << 20) - 3**8) > ((1 << 12) - 1) * (3**8 - 2**8)
# L=9: H(9,18)>=39 and W>=39 thereafter (Z>=20 from 2Z-1).
assert H_floor(9, 18) >= 39
assert H_floor(9, 19) >= 39
assert (39 * 512 - (3**9 - 2**9)) > 0
assert 39 * ((1 << 27) - 3**9) > ((1 << 18) - 1) * (3**9 - 2**9)

# 5) Exact residual fixed-content certificate after the analytic semi-infinite cuts.
residual_pairs = (
    [(6, 4)]
    + [(7, z) for z in range(5, 8)]
    + [(8, z) for z in range(5, 12)]
    + [(9, z) for z in range(6, 18)]
)
residual_words = 0
divisibility_hits = []
primitive_hits = []
for L, Z in residual_pairs:
    A = L + Z
    D = (1 << A) - 3 ** L
    assert D > 0
    pair_count = 0
    for pos in combinations(range(A), L):
        pair_count += 1
        q = q_num_from_positions(pos, L)
        if q % D == 0:
            bits = [0] * A
            for p in pos:
                bits[p] = 1
            hit = (L, Z, ''.join(map(str, bits)), q // D, is_primitive_bits(bits))
            divisibility_hits.append(hit)
            if hit[-1]:
                primitive_hits.append(hit)
    assert pair_count == comb(A, L)
    residual_words += pair_count

expected_hits = [
    (7, 7, '10101010101010', 1, False),
    (7, 7, '01010101010101', 2, False),
    (8, 8, '1010101010101010', 1, False),
    (8, 8, '0101010101010101', 2, False),
    (9, 9, '101010101010101010', 1, False),
    (9, 9, '010101010101010101', 2, False),
]
assert sorted(divisibility_hits) == sorted(expected_hits)
assert primitive_hits == []
assert residual_words == 8_606_677

print('RL123 packing-globalization verifier: PASS')
print('occupancy_floor_checks =', occupancy_checks)
print('window_transport_checks =', window_checks)
print('fully_owned_legal_words =', owned_legal_checks)
print('exact_residual_words =', residual_words)
print('divisibility_hits =', len(divisibility_hits))
print('primitive_divisibility_hits =', len(primitive_hits))
print('low_L_frontier = every hypothetical primitive nontrivial positive ordinary cycle has L >= 10')
print('scope: RL123.1--RL123.5 analytic; low-L residual exclusion is exact finite certificate')
