#!/usr/bin/env python3
from math import gcd


def T(n):
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2


def Ts(n, s):
    return n // 2 if n % 2 == 0 else (3*n + s) // 2


def oddcore(n):
    while n % 2 == 0:
        n //= 2
    return n


def v3(n):
    c = 0
    while n % 3 == 0:
        c += 1
        n //= 3
    return c

# 1. Exact odd-core characterization for finite base intervals, audited on a box.
odd_core_checks = 0
for X in range(1, 65):
    for N in range(1, 2049):
        rhs = oddcore(N) <= X
        lhs = False
        p = 1
        while p <= N:
            if N % p == 0 and N // p <= X:
                lhs = True
                break
            p *= 2
        assert lhs == rhs
        odd_core_checks += 1

# 2. LTE comb: j consecutive odd predecessors of 2^k.
comb_checks = 0
terminal_aux_checks = 0
for k in range(1, 302, 2):
    assert v3(2**k + 1) == 1 + v3(k)
    vmax = v3(2**k + 1)
    for j in range(1, vmax + 1):
        num = 2**j * (2**k + 1)
        assert num % (3**j) == 0
        J = num // (3**j) - 1
        assert J > 0 and J % 2 == 1
        y = J
        for _ in range(j):
            assert y % 2 == 1
            y = T(y)
        assert y == 2**k
        for _ in range(k):
            y = T(y)
        assert y == 1
        comb_checks += 1

        # RL50 auxiliary n=(J-1)/2 is also blue for k>=3.
        if k >= 3:
            n = (J - 1) // 2
            assert n > 0
            z = n
            seen = 0
            while z != 1 and seen < k + j + 20:
                z = T(z)
                seen += 1
            assert z == 1
            terminal_aux_checks += 1

# 3. 2 is a primitive root modulo 3^b for small b (analytic proof is separate).
order_checks = 0
for b in range(1, 9):
    m = 3**b
    x = 1
    for e in range(1, 2*3**(b-1) + 1):
        x = (2*x) % m
        if x == 1:
            order = e
            break
    assert order == 2*3**(b-1)
    order_checks += 1

# 4. Symbolic multiplicative-density bound from a certified interval, finite audit.
# Choose the smallest power p=2^k with p*X >= N; b=p*floor(N/p).
# Then b is in 2^*[1,X], b<=N and X(N-b)<2N.
packing_checks = 0
for X in [8, 16, 32, 64, 128]:
    for N in range(X, 20000):
        p = 1
        while p*X < N:
            p *= 2
        m = N // p
        assert 1 <= m <= X
        b = p*m
        assert b <= N
        assert oddcore(b) <= X
        assert X*(N-b) < 2*N or N == b
        packing_checks += 1

# 5. Exact s=1 specificity: ordinary-blue 5 becomes a T_5 2-cycle.
assert T(5) == 8 and T(T(T(T(5)))) == 1
assert Ts(5, 5) == 10 and Ts(10, 5) == 5

print('RL80 blue-basin verifier: PASS')
print(f'odd-core saturation checks = {odd_core_checks}')
print(f'LTE blue-comb checks = {comb_checks}')
print(f'RL50 auxiliary-blue checks = {terminal_aux_checks}')
print(f'primitive-root spot checks = {order_checks}')
print(f'multiplicative-density checks = {packing_checks}')
print('ordinary s=1 / generalized s=5 negative control = PASS')
