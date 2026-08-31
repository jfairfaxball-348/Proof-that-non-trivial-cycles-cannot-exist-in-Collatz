#!/usr/bin/env python3
"""RL194 exact three-transition necessary owned-pair interface.

All 42 ordered unequal endpoint-height pairs of maximum 21
are propagated under the actual common mechanical word (2, 1, 2).
Survival is necessary only, never a physical realization certificate.
"""

from collections import Counter
from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
B = A - L
R = 2 * L - A
ELO, EHI = 72_797_034_370, 103_818_202_602
Q = 88_514_772_733
C0 = 3**37


def v2(n):
    assert n
    n = abs(n)
    return (n & -n).bit_length() - 1


def advance(state, digit):
    """Complete ordinary, common-mechanical necessary transition relation.

    For odd orbit states X,Z, state=(h,hp,C) encodes
    C=2^g Z-X if g=h-hp>0, C=Z-2^-g X if g<0, and C=Z-X if g=0.
    alpha=v2(3X+1), beta=v2(3Z+1). Heights remain nonnegative.
    """
    h, hp, C = state
    g = h - hp
    assert h >= 0 and hp >= 0 and C > 0
    assert (C % 2 == 0) == (g == 0)
    if g >= 0:
        N = 3 * C + (1 << g) - 1
        left_extra, right_extra = g, 0
    else:
        N = 3 * C + 1 - (1 << (-g))
        left_extra, right_extra = 0, -g
    assert N > 0
    w = v2(N)
    out = []
    for alpha in range(1, h + digit + 1):
        for beta in range(1, hp + digit + 1):
            vl, vr = left_extra + beta, right_extra + alpha
            if vl == vr:
                if w <= vl:
                    continue
            elif w != min(vl, vr):
                continue
            h1, hp1 = h + digit - alpha, hp + digit - beta
            C1 = N >> min(vl, vr)
            state1 = (h1, hp1, C1)
            assert h1 - hp1 == g + beta - alpha
            assert (C1 % 2 == 0) == (h1 == hp1)
            eps = Fraction(1, 2**hp) - Fraction(1, 2**h)
            assert (2**digit) * Fraction(C1, 2**max(h1, hp1)) == (
                3 * Fraction(C, 2**max(h, hp)) + eps
            )
            out.append((state1, alpha, beta))
    return out


def rank_cells(depth):
    """Gap-free integer cells with fixed source mechanical words.

    Split at every rotated rank 0, R and L-1, so the common-mechanical and
    carry predicates are constant on each cell; no billion-rank scan.
    """
    cuts = {ELO, EHI + 1, Q}
    for j in range(depth + 1):
        for x in (0, R - 1, R, L - 1):
            cut = (x - j * B) % L
            if ELO <= cut <= EHI:
                cuts.add(cut)
                cuts.add(cut + 1)
    points = sorted(cuts)
    return [(lo, hi - 1) for lo, hi in zip(points, points[1:]) if lo < hi]


def verify():
    initial = {(21, j, C0) for j in range(21)} | {
        (j, 21, C0) for j in range(21)
    }
    assert len(initial) == 42
    assert v2(3**38 - 1) == 3
    assert v2(3**38 + 7) == 5

    # The first three transitions have ordinary sources and ordinary targets.
    # At each source its p-shift companion is rank r+1 and shares its digit.
    cells = rank_cells(3)
    assert cells[0][0] == ELO and cells[-1][1] == EHI
    assert all(a[1] + 1 == b[0] for a, b in zip(cells, cells[1:]))
    for lo, hi in cells:
        for rank in (lo, hi):
            for j in range(3):
                r = (rank + j * B) % L
                rn = (r + B) % L
                assert r not in (R - 1, L - 1)
                assert rn != L - 1
                assert (1 if r < R else 2) == (2, 1, 2)[j]
                assert (1 if (r + 1) % L < R else 2) == (2, 1, 2)[j]

    first = {st: advance(st, 2) for st in sorted(initial)}
    assert all(first.values())
    zero_entries = {
        (st, a, b, ns)
        for st, edges in first.items()
        for ns, a, b in edges
        if ns[0] == ns[1]
    }
    expected_zero = {
        ((21, 18, C0), 4, 1, (19, 19, (3**38 + 7) // 16)),
        ((20, 21, C0), 1, 2, (21, 21, (3**38 - 1) // 4)),
    }
    assert zero_entries == expected_zero
    for _, _, _, ns in zero_entries:
        assert v2(ns[2]) == 1
        assert all(nns[0] != nns[1] for nns, _, _ in advance(ns, 1))

    # Nonexceptional sign retention and forced accelerated exponents.
    for st, edges in first.items():
        g = st[0] - st[1]
        for ns, alpha, beta in edges:
            g1 = ns[0] - ns[1]
            if g in (1, 2):
                assert alpha == g and g1 > 0
            elif g >= 4:
                assert alpha == 3 and g1 > 0
            elif g <= -2:
                assert beta == 1 and g1 < 0

    states = set(initial)
    paths = {(st, (st[0] - st[1],)) for st in initial}
    counts = []
    for digit in (2, 1, 2):
        next_states = set()
        next_paths = set()
        edge_count = 0
        for st in states:
            edges = advance(st, digit)
            edge_count += len(edges)
            next_states.update(ns for ns, _, _ in edges)
        for st, signature in paths:
            next_paths.update(
                (ns, signature + (ns[0] - ns[1],))
                for ns, _, _ in advance(st, digit)
            )
        states, paths = next_states, next_paths
        signs = Counter((h > hp) - (h < hp) for h, hp, _ in states)
        counts.append((len(states), edge_count, dict(sorted(signs.items()))))
    assert counts == [
        (540, 540, {-1: 268, 0: 2, 1: 270}),
        (4202, 4517, {-1: 2182, 0: 16, 1: 2004}),
        (25417, 30977, {-1: 14766, 0: 16, 1: 10635}),
    ]
    assert {signature[0] for _, signature in paths} == set(range(-21, 0)) | set(range(1, 22))
    assert not any(g1 == 0 and g2 == 0 for _, (_, g1, g2, _) in paths)
    sign_patterns = {
        tuple((g > 0) - (g < 0) for g in signature) for _, signature in paths
    }
    assert len(sign_patterns) == 44
    print("PASS: exact owned-prefix necessary interface")
    print("initial_height_pairs=42; common_word=212; both_atoms_covered")
    print("complete_transition_depth=3; no_carry_or_switch_transition")
    print("state_edge_sign_counts=", counts)
    print("immediate_zero_entries=", sorted(zero_entries))
    print("consecutive_G1_G2_zeros=impossible")
    print("four_source_sign_pattern_count=", len(sign_patterns))
    print("all42_initial_pairs_survive_depth3")
    print("survival_is_not_realization; no_atom_exclusion; H21_budget_unchanged")


if __name__ == "__main__":
    verify()
