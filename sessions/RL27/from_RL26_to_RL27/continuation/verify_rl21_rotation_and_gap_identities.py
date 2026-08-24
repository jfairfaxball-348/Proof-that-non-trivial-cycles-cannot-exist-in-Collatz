from itertools import product, combinations
from math import gcd


def Qword(v):
    L = sum(v)
    p = 0
    q = 0
    for i,b in enumerate(v):
        if b:
            q += (1 << i) * 3 ** (L-1-p)
            p += 1
    return q


def v2(n):
    n = abs(n)
    c = 0
    while n and n % 2 == 0:
        n //= 2
        c += 1
    return c

rot_checks = 0
for A in range(2, 10):
    for bits in product((0,1), repeat=A):
        L = sum(bits)
        if not L or (1 << A) <= 3 ** L:
            continue
        D = (1 << A) - 3 ** L
        Q = Qword(bits)
        for m in range(1, A):
            u = bits[:m]
            v = bits[m:]
            p = sum(u)
            U = Qword(u)
            Qr = Qword(v + u)
            assert (1 << m) * Qr - 3 ** p * Q == D * U
            assert (Q % D == 0) == (Qr % D == 0)
            rot_checks += 1

# Equal-weight first-disagreement valuation lemma.
gap_checks = 0
for a in range(2, 11):
    for ell in range(1, a):
        words = []
        for pos in combinations(range(a), ell):
            w = [0]*a
            for i in pos:
                w[i] = 1
            words.append((w, Qword(w)))
        for i in range(len(words)):
            u,U = words[i]
            for j in range(i+1, len(words)):
                v,V = words[j]
                r = next(k for k,(x,y) in enumerate(zip(u,v)) if x != y)
                assert v2(U-V) == r
                gap_checks += 1

print('RL21 rotation/gap identity verifier: PASS')
print('rotation identity checks =', rot_checks)
print('equal-weight first-difference v2 checks =', gap_checks)
