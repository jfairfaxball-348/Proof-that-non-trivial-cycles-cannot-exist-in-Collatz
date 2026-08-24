from itertools import product
from math import gcd, comb
from fractions import Fraction


def Qword(w: str) -> int:
    L = w.count('1')
    r = 0
    Q = 0
    for i, b in enumerate(w):
        if b == '1':
            r += 1
            Q += (1 << i) * (3 ** (L - r))
    return Q


def rot(w: str, m: int) -> str:
    m %= len(w)
    return w[m:] + w[:m]


def primitive_word(w: str) -> bool:
    A = len(w)
    for d in range(1, A):
        if A % d == 0 and w == w[:d] * (A // d):
            return False
    return True


def vp(n: int, p: int) -> int:
    n = abs(n)
    assert n != 0
    c = 0
    while n % p == 0:
        c += 1
        n //= p
    return c


def lcp_cyclic(w: str, i: int, j: int) -> int:
    A = len(w)
    c = 0
    while c < A and w[(i+c) % A] == w[(j+c) % A]:
        c += 1
    return c


def moments(vals, r):
    return sum(x**r for x in vals)

# Counters
word_cycles = 0
rotation_poly_checks = 0
monodromy_checks = 0
moment_checks = 0
vandermonde_checks = 0
lcp_checks = 0

# Exhaustive small-word audit.
for A in range(2, 11):
    for bits in product('01', repeat=A):
        w = ''.join(bits)
        L = w.count('1')
        if L == 0 or not primitive_word(w):
            continue
        D = (1 << A) - 3**L
        if D <= 0:
            continue

        qs = [Qword(rot(w, m)) for m in range(A)]
        Q0 = qs[0]
        g = gcd(D, Q0)
        s = D // g
        ns = [q // g for q in qs]

        # Theorem A: canonical primitive generalized-increment cycle.
        assert all(q > 0 for q in qs)
        assert all(gcd(D, q) == g for q in qs)
        assert all(gcd(s, n) == 1 for n in ns)
        assert len(set(ns)) == A
        for m, b in enumerate(w):
            q, qn = qs[m], qs[(m+1) % A]
            n, nn = ns[m], ns[(m+1) % A]
            assert 2 * qn == (3*q + D if b == '1' else q)
            assert 2 * nn == (3*n + s if b == '1' else n)
            assert n % 2 == (1 if b == '1' else 0)
        word_cycles += 1

        # Theorem B: all polynomial rotation algebra mod D is rank-one.
        # Q_m == u_m Q_0 (mod D), u_m=3^{P_m}2^{-m}.
        P = 0
        us = []
        inv2 = pow(2, -1, D)
        for m in range(A):
            if m:
                P += int(w[m-1] == '1')
            u = (pow(3, P, D) * pow(inv2, m, D)) % D
            us.append(u)
            assert qs[m] % D == (u * Q0) % D
            rotation_poly_checks += 1
        for i in range(A):
            for j in range(A):
                assert (qs[i] * qs[j] - us[i]*us[j]*(Q0**2)) % D == 0
                rotation_poly_checks += 1
        if A >= 3:
            i, j, k = 0, A//2, A-1
            assert (qs[i]*qs[j]*qs[k] - us[i]*us[j]*us[k]*(Q0**3)) % D == 0
            rotation_poly_checks += 1

        # Theorem C: full-word affine monodromy degeneracy.
        # F_w(x)=(3^L x+Q)/2^A and 2^A(F_w(x)-x)=Q-Dx.
        for x0 in (-7, -1, 0, 1, 5, 23):
            x = Fraction(x0, 1)
            for b in w:
                x = (3*x + 1)/2 if b == '1' else x/2
            assert x == Fraction(3**L * x0 + Q0, 1 << A)
            assert (1 << A) * (x - x0) == Q0 - D*x0
            monodromy_checks += 1
        if Q0 % D == 0:
            R = Q0 // D
            for x0 in (-3, 0, 2, 11):
                # Numerator of F_w(x)-x is D(R-x).
                assert Q0 - D*x0 == D*(R-x0)
                monodromy_checks += 1

        # Generalized moment hierarchy; exact s-sensitive global identities.
        E = [n for n, b in zip(ns, w) if b == '0']
        O = [n for n, b in zip(ns, w) if b == '1']
        for r in (1, 2, 3):
            Er = moments(E, r)
            Or = moments(O, r)
            lhs = ((1 << r)-1)*Er + ((1 << r) - 3**r)*Or
            rhs = 0
            for j in range(r):
                from math import comb as C
                Oj = L if j == 0 else moments(O, j)
                rhs += C(r, j) * (3**j) * (s**(r-j)) * Oj
            assert lhs == rhs
            moment_checks += 1

        # Theorem D: full-state Vandermonde cross-parity product identity.
        C0 = 1
        C1 = 1
        for e in E:
            for o in O:
                assert e != o
                assert e - 3*o - s != 0
                C0 *= (e-o)
                C1 *= (e-3*o-s)
        assert (1 << comb(A, 2)) * abs(C0) == (3**comb(L, 2)) * abs(C1)
        assert sum(vp(e-3*o-s, 2) for e in E for o in O) == comb(A, 2)
        vandermonde_checks += 1

        # The attractive 2-adic corollary collapses to an all-word LCP identity:
        # sum_{prev-bit 0 vs 1} LCP(next rotations) = C(e,2)+C(L,2).
        zpos = [i for i,b in enumerate(w) if b == '0']
        opos = [i for i,b in enumerate(w) if b == '1']
        lsum = sum(lcp_cyclic(w, i+1, j+1) for i in zpos for j in opos)
        assert lsum == comb(len(zpos),2) + comb(len(opos),2)
        lcp_checks += 1

# Mandatory RL20 exact negative control.
fake = ('1101101101011011010110110110101101101011011011010110110101101101101011011010110110101101101101011011010110110110101101101011011011010110110101101101101011011010110110101101101101011010')
A = len(fake); L = fake.count('1')
assert (A, L) == (184, 116)
D = (1 << A) - 3**L
qs = [Qword(rot(fake, m)) for m in range(A)]
g = gcd(D, qs[0]); s = D // g
assert g == 1 and s == D
ns = qs
assert len(set(ns)) == A
assert all(gcd(s,n) == 1 for n in ns)
for m,b in enumerate(fake):
    n,nn=ns[m],ns[(m+1)%A]
    assert n%2 == (1 if b=='1' else 0)
    assert 2*nn == (3*n+s if b=='1' else n)
E=[n for n,b in zip(ns,fake) if b=='0']
O=[n for n,b in zip(ns,fake) if b=='1']
assert sum(E)-sum(O) == L*s
assert 3*sum(e*e for e in E)-5*sum(o*o for o in O) == 6*s*sum(O)+L*s*s
# Vandermonde audit by valuations and several modular projections (avoid huge exact product allocation).
assert sum(vp(e-3*o-s,2) for e in E for o in O) == comb(A,2)
for p in (5,7,11,13,17,19,23,29,31):
    C0=C1=1
    for e in E:
        for o in O:
            C0 = (C0*(e-o)) % p
            C1 = (C1*(e-3*o-s)) % p
    assert (pow(2,comb(A,2),p)*C0 - pow(3,comb(L,2),p)*C1) % p == 0

print('RL79 common-barrier/new-route verifier: PASS')
print('primitive generalized-increment cycles checked =', word_cycles)
print('rotation polynomial-collapse checks =', rotation_poly_checks)
print('monodromy checks =', monodromy_checks)
print('generalized moment checks =', moment_checks)
print('small-word Vandermonde checks =', vandermonde_checks)
print('all-word LCP-collapse checks =', lcp_checks)
print('RL20 fake generalized increment s = D =', s)
print('RL20 fake Vandermonde v2 total =', comb(A,2))
