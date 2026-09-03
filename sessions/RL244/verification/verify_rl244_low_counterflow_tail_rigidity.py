#!/usr/bin/env python3
"""
RL244 exact low-counterflow determinant-2 tail-rigidity verifier.

This verifier audits the finite cyclic interval geometry used in the RL244
analytic reduction beta(P) in {1,2,3}.  It uses exact Fraction arithmetic.

It does NOT treat P as a Radius-4 theorem input and it does NOT prove Gate A.
The inherited H<=24 certificate is used separately in the proof ledger only
to discharge the small-k side of a hypothetical simultaneous survivor.
"""
from fractions import Fraction
from itertools import combinations


def val(f, x):
    return f[0] + f[1] * x


def add(f, g):
    return (f[0] + g[0], f[1] + g[1])


def sub(f, g):
    return (f[0] - g[0], f[1] - g[1])


def sum_aff(fs):
    a = Fraction(0)
    b = Fraction(0)
    for f in fs:
        a += f[0]
        b += f[1]
    return (a, b)


def equality_roots(f, g, lo, hi):
    h = sub(f, g)
    if h[1] == 0:
        return []
    x = -h[0] / h[1]
    return [x] if lo < x < hi else []


def modular_position_cells(n, step, lo, hi):
    """Affine positions k*step mod 1, with all modular-order breakpoints."""
    bps = {lo, hi}
    a, b = step
    for k in range(1, n):
        raw = (k * a, k * b)
        vlo = val(raw, lo)
        vhi = val(raw, hi)
        mn, mx = min(vlo, vhi), max(vlo, vhi)
        m0 = mn.numerator // mn.denominator - 2
        m1 = mx.numerator // mx.denominator + 3
        for m in range(m0, m1 + 1):
            if raw[1]:
                x = (Fraction(m) - raw[0]) / raw[1]
                if lo < x < hi:
                    bps.add(x)

    bps = sorted(bps)
    cells = []
    for L, R in zip(bps, bps[1:]):
        if L == R:
            continue
        mid = (L + R) / 2
        pos = []
        for k in range(n):
            raw = (k * a, k * b)
            y = val(raw, mid)
            fl = y.numerator // y.denominator
            pos.append((raw[0] - fl, raw[1]))
        pos.sort(key=lambda f: val(f, mid))
        cells.append((L, R, pos))
    return cells


def cyclic_gaps(pos):
    gaps = []
    for i in range(len(pos) - 1):
        gaps.append(sub(pos[i + 1], pos[i]))
    gaps.append((Fraction(1) + pos[0][0] - pos[-1][0],
                 pos[0][1] - pos[-1][1]))
    return gaps


def cover_breakpoints(n, c, step, lo, hi):
    bps = {lo, hi}
    for L, R, pos in modular_position_cells(n, step, lo, hi):
        bps.update((L, R))
        gaps = cyclic_gaps(pos)
        for i, j in combinations(range(len(gaps)), 2):
            bps.update(equality_roots(gaps[i], gaps[j], L, R))
    return bps


def cover_affine_at(n, c, step, x):
    """
    A-part of the minimum cardinality of <=c cyclic integer intervals covering
    n marked positions on a circle of length A:
        A*(1-sum(c largest normalized gap distances)) + c_eff.
    """
    a, b = step
    pos = []
    for k in range(n):
        raw = (k * a, k * b)
        y = val(raw, x)
        fl = y.numerator // y.denominator
        pos.append((raw[0] - fl, raw[1]))
    pos.sort(key=lambda f: val(f, x))
    gaps = cyclic_gaps(pos)
    order = sorted(range(len(gaps)), key=lambda i: val(gaps[i], x),
                   reverse=True)
    ceff = min(c, n)
    top = [gaps[i] for i in order[:ceff]]
    return sub((Fraction(1), Fraction(0)), sum_aff(top)), ceff


def verify_one_orbit(n, c, step, lo, hi, target):
    """Check continuous A-part of cover >= target throughout an open interval."""
    checked = 0
    worst = None
    for L, R, pos in modular_position_cells(n, step, lo, hi):
        gaps = cyclic_gaps(pos)
        local = {L, R}
        for i, j in combinations(range(len(gaps)), 2):
            local.update(equality_roots(gaps[i], gaps[j], L, R))
        local = sorted(local)
        for l, r in zip(local, local[1:]):
            if l == r:
                continue
            mid = (l + r) / 2
            order = sorted(range(len(gaps)),
                           key=lambda i: val(gaps[i], mid), reverse=True)
            top = [gaps[i] for i in order[:min(c, n)]]
            cover = sub((Fraction(1), Fraction(0)), sum_aff(top))
            diff = sub(cover, target)
            vl, vr = val(diff, l), val(diff, r)
            assert min(vl, vr) >= 0, (n, c, step, l, r, cover, target)
            w = min(vl, vr)
            if worst is None or w < worst:
                worst = w
            checked += 1
    return checked, worst


def verify_two_orbits(n, C, lo, hi, expected_aff, expected_const):
    """
    n consecutive ordinary tail zeroes split into ceil(n/2), floor(n/2)
    reduced parity-orbit points.  Verify every allocation c1+c2=C of the
    available zero blocks against a claimed lower bound
        A*expected_aff(delta/A) + expected_const.
    """
    n1, n2 = (n + 1) // 2, n // 2
    step = (Fraction(0), Fraction(-1))
    allocations = [(c1, C - c1) for c1 in range(1, C)]

    bps = {lo, hi}
    for c1, c2 in allocations:
        bps |= cover_breakpoints(n1, c1, step, lo, hi)
        bps |= cover_breakpoints(n2, c2, step, lo, hi)
    bps = sorted(bps)

    formulas = set()
    checks = 0
    for L, R in zip(bps, bps[1:]):
        if L == R:
            continue
        mid = (L + R) / 2
        for c1, c2 in allocations:
            f1, e1 = cover_affine_at(n1, c1, step, mid)
            f2, e2 = cover_affine_at(n2, c2, step, mid)
            f = add(f1, f2)
            const = e1 + e2
            formulas.add((f, const, c1, c2))
            diff = sub(f, expected_aff)
            vl, vr = val(diff, L), val(diff, R)
            assert min(vl, vr) >= 0, (n, C, c1, c2, L, R, f)
            if min(vl, vr) == 0:
                assert const >= expected_const, (n, C, c1, c2, const)
            checks += 1
    return checks, formulas


# gcd(a,q)=1: x=z/a in (7/19,3/8), and q^{-1}/a is x/2 or (1+x)/2.
lo1, hi1 = Fraction(7, 19), Fraction(3, 8)
target_z = (Fraction(0), Fraction(1))
gcd1_cases = ((11, 4), (13, 6), (16, 8))
gcd1_checks = 0
for n, c in gcd1_cases:
    for step in ((Fraction(0), Fraction(1, 2)),
                 (Fraction(1, 2), Fraction(1, 2))):
        checked, _ = verify_one_orbit(n, c, step, lo1, hi1, target_z)
        gcd1_checks += checked

# gcd(a,q)=2: x=delta/A in (1/4,5/19), reduced q-order step is -delta mod A.
lo2, hi2 = Fraction(1, 4), Fraction(5, 19)
gcd2_claims = (
    (7, 4, (Fraction(1), Fraction(-1)), 4),
    (17, 6, (Fraction(-5), Fraction(22)), 6),
    (24, 8, (Fraction(-16), Fraction(64)), 8),
)
gcd2_checks = 0
formula_counts = []
for n, C, expected_aff, expected_const in gcd2_claims:
    checked, formulas = verify_two_orbits(
        n, C, lo2, hi2, expected_aff, expected_const
    )
    gcd2_checks += checked
    formula_counts.append((n, C, len(formulas)))

# Exact integer comparisons used with the frozen resonance R^2<16/15.
assert 2**46 > 3**29
assert 16**23 < 15**23 * 9**6
assert 2**65 > 3**41
assert 16**65 < 15**65 * 9**8

print("RL244 low-counterflow tail-rigidity verifier: PASS")
print("gcd1_piece_checks=", gcd1_checks)
print("gcd2_piece_checks=", gcd2_checks)
print("gcd2_formula_counts=", formula_counts)
print("exact_power_comparisons=4")
print("classification=R4_BRIDGE_REDUCED")
