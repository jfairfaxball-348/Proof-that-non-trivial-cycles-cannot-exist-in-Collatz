#!/usr/bin/env python3
from math import gcd

def v3(n):
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c

def T(n):
    return n//2 if n%2==0 else (3*n+1)//2

def collatz_to_one(n, cap=10000):
    for _ in range(cap):
        if n == 1:
            return True
        n = T(n)
    return False

blue_checks = 0
lift_checks = 0
midpoint_noeq_checks = 0
max_j = 0
allowed_cases = 0
for k in range(27, 166, 2):
    nu = 1 + v3(k)
    max_j = max(max_j, nu)
    for j in range(1, nu+1):
        assert (2**k + 1) % (3**j) == 0
        q = (2**k + 1)//(3**j)
        J0 = 2**j*q - 1
        n0 = (J0-1)//2

        # RL80 basin audit
        x = J0
        for r in range(j):
            assert x % 2 == 1
            x = T(x)
        assert x == 2**k
        assert collatz_to_one(J0)
        if k >= 3:
            assert collatz_to_one(n0)
        # forward auxiliary orbits remain below terminal scale
        y=n0
        maxn=y
        for _ in range(1000):
            if y==1:
                break
            y=T(y)
            maxn=max(maxn,y)
        assert maxn < 2**k
        # With stable N>=2^71 and j<=5, the physical all-11 entry states exceed 2^k.
        # Check sufficient exact inequalities for A_0+1 and B_0+1.
        assert 2**j * 2**(k-2) * 2**71 > 3**(j+1) * (2**k + 1)
        assert 2**j * 2**(k-2) * 2**71 > 3**j * (2**k + 1)
        blue_checks += 2

        # RL66 necessary phase selector for a full all-11 terminal suffix.
        mod = 3**(j+2)
        two_1_minus_k = pow(pow(2, k-1, mod), -1, mod)
        base = (2 - two_1_minus_k) % mod
        if j < nu:
            allowed = True
            Nres = base
        else:
            allowed = (q % 3) == (pow(2, j, 3) % 3)
            Nres = (base - (2**j)*(3**(j+1))) % mod
        if allowed:
            allowed_cases += 1
            # Check neither blue auxiliary can equal either full-phase midpoint N or N+4.
            for aux in (J0, n0):
                for off in (0,4):
                    candN = aux - off
                    if candN > 0 and candN % 8 == 3:
                        assert candN % mod != Nres
                    midpoint_noeq_checks += 1

        # Exact terminal-tail physical lift family.
        # Solve 3^(j+1) a == 2 mod 2^(k-2).
        M = 2**(k-2)
        a0 = (2 * pow(pow(3,j+1,M), -1, M)) % M
        if a0 == 0:
            a0 = M
        # choose an m so b,N positive and N==3 mod8; then audit 3 lifts in that class
        found = None
        for m in range(0, 64):
            a = a0 + m*M
            b = 3*a - q
            numN = 3**(j+1)*a - 2**k - 2
            if b > 0 and numN > 0 and numN % M == 0:
                N = numN//M
                if N % 8 == 3:
                    found = m
                    break
        assert found is not None
        for z in range(3):
            m = found + 8*z
            a = a0 + m*M
            b = 3*a - q
            assert a % 2 == 0 and b % 2 == 1
            A = 2**j*a - 1
            B = 2**j*b - 1
            J = 3*A - B + 1
            assert J == J0
            # synchronized 11^j
            for r in range(j):
                assert A%2==1 and B%2==1 and J%2==1
                A = T(A); B = T(B); J = (3*J+1)//2
                assert J == 3*A - B + 1
            assert J == 2**k
            # omitted terminal (1,0)
            assert A%2==1 and B%2==0
            A = T(A); B = T(B)
            # t=k-3 synchronized zero tail
            t = k-3
            for _ in range(t):
                assert A%2==0 and B%2==0
                A//=2; B//=2
            assert A == B + 4
            assert B % 8 == 3
            N = B
            expectedN = (3**(j+1)*a - 2**k - 2)//M
            assert N == expectedN
            lift_checks += 1

assert max_j == 5

print("RL81 auxiliary-transfer verifier: PASS")
print(f"RL80 blue auxiliary checks = {blue_checks}")
print(f"RL66-allowed all-11 cases = {allowed_cases}")
print(f"midpoint equality negative checks = {midpoint_noeq_checks}")
print(f"terminal-tail physical lift checks = {lift_checks}")
print(f"max all-11 depth on open k-range = {max_j}")
