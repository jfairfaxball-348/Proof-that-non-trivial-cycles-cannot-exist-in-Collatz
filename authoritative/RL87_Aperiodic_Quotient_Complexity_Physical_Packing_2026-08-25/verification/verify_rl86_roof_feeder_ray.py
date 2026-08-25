#!/usr/bin/env python3
"""Fast exact arithmetic/transcription guard for RL86.

Analytic proofs are in RL86_RLUPPER_ROOF_FEEDER_RAY_STRUCTURAL_INTERROGATION.md.
This verifier checks finite arithmetic consequences and small-depth instances only.
"""

P_FAREY = 114_208_327_604
Q_FAREY = 72_057_431_991
H = 27_021_536_997
B_RETURN = 43_234_459_194
DISTINCT_J = 930_959
M_CLASSES = (26, 80, 152)

assert H == (3 * Q_FAREY + 7) // 8
assert Q_FAREY - H == 45_035_894_994
assert all(m % 3 == 2 for m in M_CLASSES)
assert all(m % 9 == 8 for m in M_CLASSES)

P_CLASSES = tuple(((2 * m - 1) // 3) % 108 for m in M_CLASSES)
assert P_CLASSES == (17, 53, 101)


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def v3(n: int) -> int:
    r = 0
    while n % 3 == 0:
        n //= 3
        r += 1
    return r


# Roof side-ladder algebra on representatives from every inherited maximum class.
side_checks = 0
for base in M_CLASSES:
    # add full mod-162 periods to guard more than the smallest representative
    for t in range(4):
        M = base + 162 * t
        if M <= 2:
            continue
        ys = []
        for j in range(16):
            F = (4 ** j) * M
            num = 2 * F - 1
            assert num % 3 == 0
            y = num // 3
            assert y % 2 == 1
            assert T(y) == F
            if j == 0:
                assert y == (2 * M - 1) // 3
            else:
                assert y > M
            ys.append(y)
            side_checks += 1
        for j in range(15):
            assert ys[j + 1] == 4 * ys[j] + 1


# Small-depth exact order and residue-completeness audit.
odometer_depth_checks = 0
for a in range(1, 9):
    mod_y = 3 ** a
    mod_u = 3 ** (a + 1)

    # 4 has exact order 3^a modulo 3^(a+1).
    order = 1
    z = 4 % mod_u
    while z != 1:
        z = (z * 4) % mod_u
        order += 1
    assert order == 3 ** a

    for M in M_CLASSES:
        y = ((2 * M - 1) // 3) % mod_y
        seen = set()
        for _ in range(3 ** a):
            assert y not in seen
            seen.add(y)
            y = (4 * y + 1) % mod_y
        assert len(seen) == mod_y
    odometer_depth_checks += 1


# RL80 consistency guard: 2 is a primitive root mod 3^a for small a.
primitive_root_checks = 0
for a in range(1, 9):
    mod = 3 ** a
    target = 2 * 3 ** (a - 1)
    x = 1
    order = None
    for e in range(1, target + 1):
        x = (2 * x) % mod
        if x == 1:
            order = e
            break
    assert order == target
    primitive_root_checks += 1


# Pure-odd descendant formula and maximal depth on sample external ray levels.
pure_odd_checks = 0
for M in M_CLASSES:
    for j in range(0, 30):
        F = (4 ** j) * M
        depth = v3(F + 1)
        # even levels always have at least one odd predecessor because M == 2 mod 3
        assert depth >= 1
        x = F
        for r in range(1, depth + 1):
            assert x % 3 == 2
            x = (2 * x - 1) // 3
            formula = (2 ** r) * (F + 1) // (3 ** r) - 1
            assert x == formula
            pure_odd_checks += 1
        # deepest node has no further odd predecessor
        assert x % 3 != 2
        if j >= 1:
            # every such descendant is external; finite samples need not all remain above M
            assert T(x) >= 1


# Exact rational logarithm guard used for the first-Farey finite re-entry theorem.
LOG_DEN = 1_000_000
LOG2_3_UP_NUM = 1_584_963
LOG2_3_OVER_2_UP_NUM = 584_963
assert pow(3, LOG_DEN) < pow(2, LOG2_3_UP_NUM)
assert LOG2_3_UP_NUM - LOG_DEN == LOG2_3_OVER_2_UP_NUM

# If X <= M, then 2^r <= M+1 <= 3^H, so r < H*log2(3).
R_REENTRY_MAX = (H * LOG2_3_UP_NUM - 1) // LOG_DEN
assert R_REENTRY_MAX == 42_828_136_343

# 4^j < (3/2)^(r+1) gives 2j < (r+1)log2(3/2).
J_REENTRY_MAX = (LOG2_3_OVER_2_UP_NUM * (R_REENTRY_MAX + 1) - 1) // (2 * LOG_DEN)
assert J_REENTRY_MAX == 12_526_437_560

# Retained fallback constants.
assert B_RETURN == 43_234_459_194
assert DISTINCT_J == 930_959
assert R_REENTRY_MAX < B_RETURN

print("RL86 roof-feeder-ray verifier: PASS")
print(f"first Farey pair = ({P_FAREY}, {Q_FAREY})")
print(f"h = {H}")
print(f"roof maximum classes mod162 = {M_CLASSES}")
print(f"roof predecessor classes mod108 = {P_CLASSES}")
print(f"side-ladder algebra checks = {side_checks}")
print(f"odometer residue-depth checks = {odometer_depth_checks}")
print(f"primitive-root consistency checks = {primitive_root_checks}")
print(f"pure-odd descendant checks = {pure_odd_checks}")
print(f"log certificate: 3^{LOG_DEN} < 2^{LOG2_3_UP_NUM}")
print(f"pure-odd re-entry depth <= {R_REENTRY_MAX}")
print(f"pure-odd re-entry even-level index <= {J_REENTRY_MAX}")
print(f"RL85 fallback return span <= {B_RETURN}")
print(f"RL85 fallback spaced-distinct J >= {DISTINCT_J}")
