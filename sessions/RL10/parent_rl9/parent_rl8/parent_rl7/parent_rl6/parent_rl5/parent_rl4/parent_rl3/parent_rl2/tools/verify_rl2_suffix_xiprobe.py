#!/usr/bin/env python3
from itertools import product


def v3(n: int) -> int:
    m = 0
    while n % 3 == 0:
        n //= 3
        m += 1
    return m


def xi(y: int) -> int:
    m = v3(y + 1)
    return (2**m * (y + 1)) // (3**m)


def Q(word):
    n = len(word)
    E = 0
    out = 0
    for j, e in enumerate(word):
        out += 3 ** (n - 1 - j) * 2**E
        E += e
    return out


def phi(word):
    h = len(word)
    mod = 3**h
    s = 0
    out = 0
    for r in range(1, h + 1):
        s += word[-r]
        out = (out + 3 ** (r - 1) * pow(pow(2, s, mod), -1, mod)) % mod
    return out


def inverse_root(y, word):
    E = sum(word)
    num = 2**E * y - Q(word)
    den = 3 ** len(word)
    if num % den:
        return None
    return num // den


def backward_path(y, word):
    cur = y
    roots = [y]
    for d in reversed(word):
        num = 2**d * cur - 1
        if num % 3:
            return None
        cur = num // 3
        if cur <= 0 or cur % 2 == 0:
            return None
        roots.append(cur)
    return roots


def qmax_root_probe(d):
    # Largest integer q for which coefficient positivity is possible:
    # 2^(d-1+q) > 3^q.
    q = 0
    while 2 ** (d - 1 + q) > 3**q:
        q += 1
    return q - 1


# 1. Exact inverse-code equivalence on a declared finite domain.
code_checks = 0
legal_path_checks = 0
same_root_pair_checks = 0
for h in range(1, 5):
    for word in product(range(1, 7), repeat=h):
        ph = phi(word)
        mod = 3**h
        for y in range(1, 250, 2):
            if y % 3 == 0:
                continue
            x = inverse_root(y, word)
            congruent = (y - ph) % mod == 0
            integral = x is not None
            assert congruent == integral
            code_checks += 1
            path = backward_path(y, word)
            if x is not None and x > 0:
                assert path is not None
                assert path[-1] == x
                assert ph == y % mod
                legal_path_checks += 1

# Pair-collapse audit: all legal words into same endpoint have same Phi.
for h in range(1, 4):
    for y in range(1, 100, 2):
        if y % 3 == 0:
            continue
        vals = []
        for word in product(range(1, 7), repeat=h):
            path = backward_path(y, word)
            if path is not None:
                vals.append(phi(word))
        if vals:
            assert all(v == y % (3**h) for v in vals)
            same_root_pair_checks += len(vals) * (len(vals) - 1) // 2

# 2. Xi-safe infinite-lift selector modulo 9.
# Choose d mod 6 so 2^d*y == 4 (mod 9), making predecessor == 1 (mod 3).
selector = {}
for ymod in (1, 2, 4, 5, 7, 8):
    sols = [d for d in range(1, 7) if (pow(2, d, 9) * ymod) % 9 == 4]
    assert len(sols) == 1
    d = sols[0]
    selector[ymod] = d
    x = (2**d * ymod - 1) // 3
    assert (2**d * ymod - 1) % 3 == 0
    assert x % 3 == 1

lift_checks = 0
for start in range(1, 100, 2):
    if start % 3 == 0:
        continue
    R = max(1, start // 2)
    cur = start
    for _ in range(20):
        d0 = selector[cur % 9]
        d = d0
        while (2**d * cur - 1) // 3 < R:
            d += 6
        nxt = (2**d * cur - 1) // 3
        assert nxt >= R
        assert nxt % 3 == 1
        assert xi(nxt) == nxt + 1 >= R + 1
        cur = nxt
        lift_checks += 1

# 3. Xi-probe identity and root valuation ceiling.
probe_checks = 0
root_ceiling_violations_detected = 0
for y in range(1, 5000, 2):
    if y % 3 == 0:
        continue
    for d in range(1, 13):
        if (2**d * y - 1) % 3:
            continue
        x = (2**d * y - 1) // 3
        q = v3(2 ** (d - 1) * y + 1)
        assert v3(x + 1) == q - 1
        lhs = xi(x)
        rhs = (2**q * (2 ** (d - 1) * y + 1)) // (3**q)
        assert lhs == rhs
        probe_checks += 1

for R in range(1, 20000, 2):
    if R % 3 != 1:
        continue
    for d in range(2, 14, 2):
        q = v3(2 ** (d - 1) * R + 1)
        qm = qmax_root_probe(d)
        x = (2**d * R - 1) // 3
        # If q exceeds the analytic ceiling, xi(x) must fall below R+1.
        if q > qm:
            assert xi(x) < R + 1
            root_ceiling_violations_detected += 1

# 4. Height-defect recurrence and monotonicity audit.
def inv_step(x, d):
    num = 2**d * x - 1
    if num % 3:
        return None
    return num // 3

height_checks = 0
for R in range(3, 200, 2):
    for x in range(R, 500, 2):
        if x % 3 == 0:
            continue
        delta = x - R
        for d in range(1, 9):
            xp = inv_step(x, d)
            if xp is None or xp <= 0 or xp % 2 == 0:
                continue
            deltap = xp - R
            assert 3 * deltap == 2**d * delta + (2**d - 3) * R - 1
            if deltap >= 0:
                if d == 1:
                    assert deltap < delta
                else:
                    assert deltap > delta
            height_checks += 1


# 5. Exact initial exponent-1 run length for x == 3 (mod 4).
def accelerated_step(x):
    n = 3 * x + 1
    a = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    return n, a

neutral_run_checks = 0
for x in range(3, 20000, 4):
    s2 = v3(1)  # harmless initialization; overwritten below
    u = x + 1
    s2 = 0
    while u % 2 == 0:
        u //= 2
        s2 += 1
    assert s2 >= 2
    cur = x
    run = 0
    while True:
        nxt, a = accelerated_step(cur)
        if a != 1:
            break
        run += 1
        cur = nxt
    assert run == s2 - 1
    neutral_run_checks += 1

print('RL-2 suffix/xi-probe verifier: PASS')
print(f'inverse-code equivalence checks: {code_checks}')
print(f'positive legal-path checks: {legal_path_checks}')
print(f'same-root Phi pair-collapse checks: {same_root_pair_checks}')
print(f'xi-safe constructed lift steps: {lift_checks}')
print(f'xi-probe identity checks: {probe_checks}')
print(f'finite detected root-ceiling violations: {root_ceiling_violations_detected}')
print(f'height-defect recurrence checks: {height_checks}')
print(f'neutral-run exact-length checks: {neutral_run_checks}')
print('selector mod9 -> d mod6:', selector)
print('early root q ceilings:', {d: qmax_root_probe(d) for d in range(2, 14, 2)})
print('scope: exact identities + finite audits of analytic theorems; no nontrivial-cycle exclusion claim')
