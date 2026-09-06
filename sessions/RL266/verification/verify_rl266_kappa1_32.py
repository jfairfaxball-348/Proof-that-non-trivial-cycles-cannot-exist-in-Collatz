#!/usr/bin/env python3
from math import gcd, log, sqrt
from collections import Counter

def Q(bits):
    L = sum(bits)
    q = 0
    r = 0
    for i,b in enumerate(bits):
        if b:
            r += 1
            q += (1 << i) * (3 ** (L-r))
    return q

def rot(bits,m):
    m %= len(bits)
    return bits[m:] + bits[:m]

def flow(bits,m):
    y = rot(bits,m)
    c = 0
    vals = []
    for a,b in zip(bits,y):
        c += a-b
        vals.append(c)
    med = sorted(vals)[(len(vals)-1)//2]
    return [v-med for v in vals]

def primitive(bits):
    A = len(bits)
    for p in range(1,A):
        if A % p == 0 and bits == bits[:p] * (A//p):
            return False
    return True

def runs(g):
    if not any(g):
        return []
    if 0 in g:
        k = g.index(0)
        z = g[k:] + g[:k]
    else:
        z = g
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

def topology(g):
    rr = runs(g)
    if max(abs(v) for v in g) <= 1:
        ll = sorted((len(r) for r in rr), reverse=True)
        return "[" + ",".join(map(str,ll)) + "]"
    return "other"

def solve_x_from_g(A,m,g):
    d = [g[i]-g[i-1] for i in range(A)]
    vals = [None]*A
    vals[0] = 0
    i = 0
    for _ in range(A-1):
        j = (i+m) % A
        vals[j] = vals[i] - d[i]
        i = j
    if (i+m) % A != 0 or vals[i] - d[i] != vals[0]:
        return []
    out = []
    for c in range(-min(vals)-1, 2-max(vals)+1):
        x = [v+c for v in vals]
        if all(v in (0,1) for v in x):
            out.append(x)
    return out

def edge_delta(bits,g):
    L = sum(bits)
    R = 0
    s = 0
    for i,(b,gi) in enumerate(zip(bits,g)):
        R += b
        if gi == 1:
            s += (1 << i) * (3 ** (L-R))
        elif gi == -1:
            e = L-R-1
            assert e >= 0
            s -= (1 << i) * (3 ** e)
    return s

def component_data(bits,g):
    L = sum(bits)
    R = 0
    pos = []
    neg = []
    for i,(b,gi) in enumerate(zip(bits,g)):
        R += b
        if gi == 1:
            pos.append((i,L-R))
        elif gi == -1:
            neg.append((i,L-R-1))
    def compress(terms):
        a = min(i for i,j in terms)
        b = min(j for i,j in terms)
        C = sum((2 ** (i-a)) * (3 ** (j-b)) for i,j in terms)
        return C,a,b
    return compress(pos), compress(neg)

def canonical_candidates(A):
    out = []
    for m in range(1,A):
        if gcd(m,A) != 1:
            continue
        for z1 in range(1,A-5):
            z2 = A-5-z1
            if z2 < 1:
                continue
            g = [1,1,1] + [0]*z1 + [-1,-1] + [0]*z2
            for x in solve_x_from_g(A,m,g):
                if flow(x,m) != g:
                    continue
                L = sum(x)
                if not (0 < L < A):
                    continue
                assert (m*L+1) % A == 0
                q = (m*L+1)//A
                assert q*A-m*L == 1
                D = (1 << A) - 3**L
                if D <= 1:
                    continue
                assert topology(g) == "[3,2]"
                direct = Q(rot(x,m)) - Q(x)
                edge = edge_delta(x,g)
                assert direct == edge
                (C3,a,b),(C2,c,d) = component_data(x,g)
                assert C3 in (7,9,13,19)
                assert C2 in (3,5)
                assert a < c and b >= d
                u = c-a
                v = b-d
                assert 0 <= v <= u <= A
                assert 0 <= L-v <= A-u
                out.append((A,L,m,q,z1,D,direct,primitive(x),C3,C2,u,v))
    return out

small = []
for A in range(7,57):
    small.extend(canonical_candidates(A))
assert len(small) == 7040
assert sum(1 for r in small if r[6] % r[5] == 0) == 0
assert sum(1 for r in small if not r[7]) == 0
proper = sum(1 for r in small if gcd(abs(r[6]),r[5]) > 1 and r[6] % r[5] != 0)
assert proper == 434

for A,L,m,q,z1,D,direct,prim,C3,C2,u,v in small:
    if u <= A-u:
        us,vs = u,v
    else:
        us,vs = A-u,L-v
    assert 0 <= vs <= us <= A//2
    B = 24 * (3 ** (A//2))
    assert C3 <= 19 and C2 <= 5
    assert C3 * (3 ** vs) + C2 * (2 ** us) <= B

def nonbracket_margin(A):
    return (log(2)/(2*A)) * (2.0**A) - 24.0 * (3.0**(A//2))
assert nonbracket_margin(57) > 0
assert nonbracket_margin(58) > 0
for A in range(57,200):
    assert nonbracket_margin(A) > 0

rho = sqrt(3)/2
K = 22 * log(2) * log(3)
fixed_cut = (K * 21**2 + log(48)) / (-log(rho))
assert 51389 < fixed_cut < 51390
transition = __import__("math").exp(20.94) / (1/log(3) + 1/log(2))
assert 5.27e8 < transition < 5.29e8
def upper_M(A):
    return log(A*(1/log(3)+1/log(2))) + 0.06
def F_upper(A):
    M = upper_M(A)
    return log(48) + A*log(rho) + K*M*M
assert F_upper(transition) < 0
deriv = log(rho) + 2*K*upper_M(transition)/transition
assert deriv < 0

def cmp_alpha(n,d):
    x = 1 << n
    y = 3 ** d
    return (x>y) - (x<y)

def upper_brackets(cut):
    low = (1,1)
    up = (2,1)
    rows = []
    while low[0] + up[0] <= cut:
        med = (low[0]+up[0], low[1]+up[1])
        c = cmp_alpha(*med)
        assert c != 0
        if c > 0:
            up = med
            if up[0] >= 5:
                A,L = up
                m,q = low
                assert q*A-m*L == 1
                assert 0 < m < A and 0 < q < L
                rows.append((A,L,m,q))
        else:
            low = med
    return rows

br = upper_brackets(51389)
assert len(br) == 33
assert br[:5] == [
    (5,3,3,2),(8,5,3,2),(27,17,19,12),(46,29,19,12),(65,41,19,12)
]
assert br[-1] == (24727,15601,1054,665)

coarse = []
for A,L,m,q in br:
    D = (1 << A) - 3**L
    assert D > 0
    B = 24 * 3**(A//2)
    if D <= B:
        coarse.append((A,L,m,q))
assert coarse == [
    (5,3,3,2),(8,5,3,2),(27,17,19,12),(46,29,19,12)
]

cnt = Counter((r[0],r[1],r[2],r[3]) for r in small)
assert cnt[(5,3,3,2)] == 0
assert cnt[(8,5,3,2)] == 2
assert cnt[(27,17,19,12)] == 14
assert cnt[(46,29,19,12)] == 26
assert sum(cnt[k] for k in coarse) == 42

neg = list(map(int,"00011110111"))
A = len(neg); L = sum(neg)
assert (1<<A)-3**L == -139

print("PASS RL266 kappa=1 [3,2] closure")
print("finite_canonical_A_le_56=7040")
print("finite_full_D_hits=0")
print("finite_nonprimitive_candidates=0 (not used as a filter)")
print("finite_proper_factor_only_candidates=434")
print("component_coefficients_C3={7,9,13,19}_C2={3,5}")
print("nonbracketing_analytic_cutoff=A>=57")
print("LMN_conditional_cutoff=A<=51389")
print("exact_bracket_edges_to_cutoff=33")
print("coarse_bracket_survivors=4 A={5,8,27,46}")
print("coarse_survivor_structural_candidates=42")
print("coarse_survivor_full_D_hits=0")
print("negative_D_scope_sentinel=-139")
print("FAST_RL266_VERIFIER_PASS")
