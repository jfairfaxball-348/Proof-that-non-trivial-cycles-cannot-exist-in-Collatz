#!/usr/bin/env python3
from fractions import Fraction


def v3(n: int) -> int:
    q = 0
    while n % 3 == 0:
        n //= 3
        q += 1
    return q


def qmax_root_probe(d: int) -> int:
    # Exact largest q with 2^(d-1+q) > 3^q.
    q = 0
    while 2 ** (d - 1 + q) > 3**q:
        q += 1
    return q - 1


def inv_step(y: int, d: int):
    n = 2**d * y - 1
    if n % 3:
        return None
    return n // 3


# 1. RL-3 k=0 forbidden-cylinder classification.
# A ceiling violation q_d >= Q_d+1 is exactly
# R == -2^(1-d) mod 3^(Q_d+1).
# Reduced mod 9, the bad class cycles with d mod 6.
mod9_expected = {2: 4, 4: 1, 0: 7}
cylinder_checks = 0
for d in range(2, 122, 2):
    Q = qmax_root_probe(d)
    mod = 3 ** (Q + 1)
    bad = (-pow(pow(2, d - 1, mod), -1, mod)) % mod
    assert bad % 9 == mod9_expected[d % 6]
    # Direct valuation audit on several representatives of the bad cylinder.
    for t in range(4):
        R = bad + t * mod
        if R <= 0:
            continue
        q = v3(2 ** (d - 1) * R + 1)
        assert q >= Q + 1
        cylinder_checks += 1

# 2. Analytic geometric-measure bounds used in the report.
# alpha = log 2 / log(3/2) > 5/3 is equivalent to 3^5 < 2^8.
assert 3**5 < 2**8
# For R == 1 mod 9 only d == 4 mod 6 can violate:
# Q_d >= 10j+5 -> relative cylinder measure <= 3^(-10j-4).
# For R == 7 mod 9 only d == 0 mod 6 can violate:
# Q_d >= 10j+8 -> relative cylinder measure <= 3^(-10j-7).
bad_mass_mod9_1 = Fraction(1, 3**4) / (1 - Fraction(1, 3**10))
bad_mass_mod9_7 = Fraction(1, 3**7) / (1 - Fraction(1, 3**10))
assert bad_mass_mod9_1 == Fraction(729, 59048)
assert bad_mass_mod9_7 == Fraction(27, 59048)
assert 1 - bad_mass_mod9_1 == Fraction(58319, 59048)
assert 1 - bad_mass_mod9_7 == Fraction(59021, 59048)

# 3. Explicit integer families covering all six inherited k=0 classes mod 144.
# M is restricted to multiples of 4, so 3^M == 0 mod 9 and 1 mod 16.
minus_families = [(25, 7), (13, 43), (1, 79)]       # R = A*3^M - 2
plus_families = [(22, 55), (10, 91), (14, 127)]     # R = A*3^M + 1
family_probe_checks = 0
family_members = 0
for M in range(4, 33, 4):
    for A, cls in minus_families:
        R = A * 3**M - 2
        assert R % 144 == cls
        assert R % 3 == 1 and R % 4 == 3
        family_members += 1
        for d in range(2, 302, 2):
            Q = qmax_root_probe(d)
            q = v3(2 ** (d - 1) * R + 1)
            assert q <= Q
            t = 1 + v3(d // 2)  # LTE: v3(2^d-1)
            if t < M:
                assert q == t
            elif t > M:
                assert q == M
            else:
                # Cancellation case: the analytic proof uses N < 3^d.
                N = 2 ** (d - 1) * R + 1
                assert d > 3 * M + 7
                assert N < 3**d
                assert Q >= d - 1
            family_probe_checks += 1

    for A, cls in plus_families:
        R = A * 3**M + 1
        assert R % 144 == cls
        assert R % 3 == 1 and R % 4 == 3
        family_members += 1
        for d in range(2, 302, 2):
            Q = qmax_root_probe(d)
            q = v3(2 ** (d - 1) * R + 1)
            assert q <= Q
            t = 1 + v3(d - 1)  # LTE: v3(2^(d-1)+1), d-1 odd
            if t < M:
                assert q == t
            elif t > M:
                assert q == M
            else:
                N = 2 ** (d - 1) * R + 1
                assert d > 3 * M + 7
                assert N < 3**d
                assert Q >= d - 1
            family_probe_checks += 1

# 4. k>0 exact relative predecessor amplification.
# Two legal predecessors of the same endpoint have exponents of the same parity.
# If the exponents differ by 2m, the larger predecessor is
# 4^m times the smaller plus (4^m-1)/3.
amplification_checks = 0
for y in range(1, 500, 2):
    if y % 3 == 0:
        continue
    legal = []
    for d in range(1, 11):
        x = inv_step(y, d)
        if x is not None and x > 0 and x % 2 == 1:
            legal.append((d, x))
    for i, (d, x) in enumerate(legal):
        for e, z in legal[i + 1:]:
            assert (e - d) % 2 == 0
            m = (e - d) // 2
            assert z == 4**m * x + (4**m - 1) // 3
            amplification_checks += 1

# 5. Relative-order recurrence / crossing criterion.
relative_checks = 0
for x in range(1, 180, 2):
    for z in range(1, 180, 2):
        for d in range(1, 7):
            xp = inv_step(x, d)
            if xp is None or xp <= 0 or xp % 2 == 0:
                continue
            for e in range(1, 7):
                zp = inv_step(z, e)
                if zp is None or zp <= 0 or zp % 2 == 0:
                    continue
                Delta = x - z
                Deltap = xp - zp
                assert 3 * Deltap == 2**d * Delta + (2**d - 2**e) * z
                assert (xp < zp) == (2**d * x < 2**e * z)
                if Delta >= 0 and d >= e:
                    assert Deltap >= 0
                if Delta <= 0 and d <= e:
                    assert Deltap <= 0
                relative_checks += 1

# 6. Height coordinate: d=1 contracts exactly, d>=2 strictly expands above R#.
height_ratio_checks = 0
for R in range(3, 120, 2):
    for x in range(R, 280, 2):
        if x % 3 == 0:
            continue
        # use rational numerator comparison for u=(x+1)/(R+1)
        for d in range(1, 8):
            xp = inv_step(x, d)
            if xp is None or xp < R or xp % 2 == 0:
                continue
            if d == 1:
                assert 3 * (xp + 1) == 2 * (x + 1)
            else:
                assert (xp + 1) > (x + 1)
            height_ratio_checks += 1

print('RL-3 root-xi / relative-height verifier: PASS')
print(f'forbidden-cylinder checks: {cylinder_checks}')
print('relative bad-mass bound in R mod9=1:', bad_mass_mod9_1, float(bad_mass_mod9_1))
print('relative bad-mass bound in R mod9=7:', bad_mass_mod9_7, float(bad_mass_mod9_7))
print(f'explicit family members audited: {family_members}')
print(f'explicit family xi-probe checks: {family_probe_checks}')
print(f'entry amplification checks: {amplification_checks}')
print(f'relative-order recurrence checks: {relative_checks}')
print(f'height-ratio checks: {height_ratio_checks}')
print('scope: analytic theorems are proved in the report; this script is a finite exact audit, not a nontrivial-cycle exclusion')
