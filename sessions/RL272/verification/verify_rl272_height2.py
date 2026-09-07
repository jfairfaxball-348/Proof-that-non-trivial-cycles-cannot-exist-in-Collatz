#!/usr/bin/env python3
from collections import Counter
from itertools import product
from math import gcd

LMN_CUTOFF = 51389

def rot(bits, m):
    A = len(bits)
    m %= A
    return bits[m:] + bits[:m]

def Q(bits):
    L = sum(bits)
    out = 0
    r = 0
    for i, b in enumerate(bits):
        if b:
            r += 1
            out += (1 << i) * (3 ** (L - r))
    return out

def height2_flow(A, u):
    g = [0] * A
    g[0], g[1], g[2], g[u] = 1, 2, 1, -1
    return g

def solve_binary(A, m, g):
    delta = [g[i] - g[i - 1] for i in range(A)]
    d = gcd(A, m)
    seen = [False] * A
    cycles = []
    for start in range(d):
        if seen[start]:
            continue
        cyc = []
        i = start
        while not seen[i]:
            seen[i] = True
            cyc.append(i)
            i = (i + m) % A
        cycles.append(cyc)

    rows = []
    for cyc in cycles:
        rel = {cyc[0]: 0}
        i = cyc[0]
        ok = True
        while True:
            j = (i + m) % A
            nxt = rel[i] - delta[i]
            if j == cyc[0]:
                if nxt != 0:
                    ok = False
                break
            rel[j] = nxt
            i = j
        if not ok:
            return []

        offsets = []
        for b in (0, 1):
            if all(v + b in (0, 1) for v in rel.values()):
                offsets.append(b)
        if not offsets:
            return []
        rows.append((cyc, rel, offsets))

    out = []
    for choices in product(*[row[2] for row in rows]):
        x = [0] * A
        for (cyc, rel, _), b in zip(rows, choices):
            for i in cyc:
                x[i] = rel[i] + b
        out.append(x)
    return out

def exact_size_pairs(maxA):
    # Exact monotone scan. For fixed A, D(A,L)=2^A-3^L decreases with L,
    # so once the bound fails while descending in L it fails for every smaller L.
    out = []
    p2 = 1
    Lmax = 0
    p3max = 1
    for A in range(1, maxA + 1):
        p2 *= 2
        while p3max * 3 < p2:
            p3max *= 3
            Lmax += 1
        B = 16 * (3 ** (A // 2))
        L = Lmax
        p3 = p3max
        while L >= 1:
            D = p2 - p3
            if D <= 1:
                L -= 1
                p3 //= 3
                continue
            if D > B:
                break
            out.append((A, L, D))
            L -= 1
            p3 //= 3
    return out

# Non-bracketing elementary cutoff.
# ln 2 > 2/3 makes the determinant-three lower bound D > 2^A/A.
# Checking A=45 and A=46 is enough, because on each parity class
# [2^(A+2)/(A+2)]/[2^A/A] divided by the 3^(floor(A/2)) growth is
# 4A/(3(A+2)) > 1 for A>6.
for A in (45, 46):
    assert (1 << A) > 16 * A * (3 ** (A // 2))

pairs = [row for row in exact_size_pairs(LMN_CUTOFF) if row[0] >= 6]
assert len(pairs) == 90
assert max(A for A, _, _ in pairs) == 27
pair_by_A = Counter(A for A, _, _ in pairs)

states = []
full_hits = []
proper_factor_only = 0
formula_bad = 0
det_bad = 0
gcd_m_A = Counter()
gcd_A_L = Counter()
by_A = Counter()

for A in range(6, 28):
    for u in range(4, A - 1):
        g = height2_flow(A, u)
        assert sum(abs(z) for z in g) == 5
        assert sum(g) == 3
        for m in range(1, A):
            for x in solve_binary(A, m, g):
                y = rot(x, m)
                # The chosen cut has zero median and must reconstruct the exact flow.
                c = 0
                prefix = []
                for a, b in zip(x, y):
                    c += a - b
                    prefix.append(c)
                assert prefix == g

                L = sum(x)
                D = (1 << A) - 3 ** L
                if D <= 1:
                    continue

                if (m * L + 3) % A:
                    det_bad += 1
                    continue
                q = (m * L + 3) // A
                assert 1 <= q <= L

                r = sum(x[:u + 1])  # R_u, with x_u=0.
                assert r >= 2
                assert L - r - 1 >= 0

                diff = Q(y) - Q(x)
                formula = 15 * (3 ** (L - 2)) - (1 << u) * (3 ** (L - r - 1))
                if diff != formula:
                    formula_bad += 1

                # Remove the invertible 3-power from the exact identity.
                v = r - 1
                sparse = 15 * (3 ** v) - (1 << u)
                assert diff == (3 ** (L - r - 1)) * sparse

                # Complementary representative from 2^A == 3^L mod D.
                comp = 15 * (1 << (A - u)) - 3 ** (L - v)
                assert ((1 << (A - u)) * sparse - (3 ** v) * comp) == -D
                assert (sparse % D == 0) == (comp % D == 0)

                # Arc exponent bounds behind D <= 16*3^floor(A/2).
                assert 1 <= v <= u
                assert 0 <= L - v <= A - u

                by_A[A] += 1
                gcd_m_A[gcd(m, A)] += 1
                gcd_A_L[gcd(A, L)] += 1
                states.append((A, L, m, q, u, v, D, diff))

                if diff % D == 0:
                    full_hits.append(states[-1])
                elif gcd(abs(diff), D) > 1:
                    proper_factor_only += 1

assert det_bad == 0
assert formula_bad == 0
assert len(states) == 149
assert by_A == Counter({6:1, 9:4, 12:6, 15:16, 18:10, 21:36, 24:28, 27:48})
assert gcd_m_A == Counter({3:149})
assert gcd_A_L == Counter({1:114, 3:35})
assert proper_factor_only == 5
assert full_hits == []

print("RL272 height-two 4+1 exact certificate: PASS")
print("analytic_nonbracketing_cutoff=A>=45")
print("inherited_LMN_bracketing_cutoff=A<=51389")
print("exact_size_pairs=%d maxA=%d byA=%s" % (
    len(pairs), max(A for A,_,_ in pairs), dict(sorted(pair_by_A.items()))
))
print("canonical_positive_D_states=%d byA=%s" % (len(states), dict(sorted(by_A.items()))))
print("gcd_m_A=%s gcd_A_L=%s" % (dict(sorted(gcd_m_A.items())), dict(sorted(gcd_A_L.items()))))
print("binomial_identity_mismatches=%d" % formula_bad)
print("proper_factor_only=%d full_D_hits=%d" % (proper_factor_only, len(full_hits)))
print("RL272_HEIGHT2_4PLUS1_PASS")
