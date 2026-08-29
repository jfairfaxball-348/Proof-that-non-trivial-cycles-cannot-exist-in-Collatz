#!/usr/bin/env python3
"""Exact finite audit for the RL167 full-affine propagation identities."""
from itertools import product
from math import gcd


def numerator(word, start):
    """Full affine numerator for the cyclic rotation beginning at start."""
    length = len(word)
    prefix = 0
    total = 0
    for t in range(length):
        total += 3 ** (length - 1 - t) * (1 << prefix)
        prefix += word[(start + t) % length]
    return total


rotation_cases = 0
closure_cases = 0
phase_cases = 0
for length in range(1, 7):
    for word in product(range(1, 5), repeat=length):
        A = sum(word)
        D = (1 << A) - 3 ** length
        if D <= 0:
            continue
        numerators = [numerator(word, j) for j in range(length)]
        for j, exponent in enumerate(word):
            assert (1 << exponent) * numerators[(j + 1) % length] == 3 * numerators[j] + D
        # D is odd, so the recurrence makes every rotated divisibility test
        # equivalent to the first one.
        assert all((n % D == 0) == (numerators[0] % D == 0) for n in numerators)
        rotation_cases += 1
        if numerators[0] % D == 0:
            states = [n // D for n in numerators]
            assert all(y > 0 and isinstance(y, int) for y in states)
            for j, exponent in enumerate(word):
                assert 3 * states[j] + 1 == (1 << exponent) * states[(j + 1) % length]
            closure_cases += 1

        # The defect/phase normalization is a separate exact modular check.
        # It is exercised only in the coprime, nonnegative-defect cases where
        # the exponents of R_h are nonnegative integers.
        if length == 1 or gcd(A, length) != 1:
            continue
        S = [0]
        for exponent in word:
            S.append(S[-1] + exponent)
        h = [A * j // length - S[j] for j in range(length)]
        if min(h) < 0:
            continue
        p = pow(A, -1, length)
        u = (A * p - 1) // length
        inv3 = pow(3, -1, D)
        rho = pow(2, u, D) * pow(inv3, p, D) % D
        assert pow(rho, length, D) == pow(2, -1, D)
        R = sum(pow(rho, A * j - length * S[j], D) for j in range(length)) % D
        expected = numerators[0] * pow(inv3, length - 1, D) % D
        assert R == expected
        H = max(h)
        P = sum((1 << (H - h[j])) * pow(rho, (A * j) % length, D) for j in range(length)) % D
        assert P == (1 << H) * R % D
        assert (numerators[0] % D == 0) == (R == 0) == (P == 0)
        phase_cases += 1

assert rotation_cases > 0 and closure_cases > 0 and phase_cases > 0
print('RL167 full-affine rank-one verifier: PASS')
print(f'positive-D words checked: {rotation_cases}')
print(f'closed positive words checked: {closure_cases}')
print(f'coprime nonnegative-defect phase cases checked: {phase_cases}')
