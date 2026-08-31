#!/usr/bin/env python3
"""RL195: complete local realizability of the RL194 depth-3 graph.

Two local positive odd accelerated trajectories are not a
cycle, an actual p-separated pair, or a physical high-branch realization.
Every path through all 42 roots and the common word (2, 1, 2) is tested.
No transition at depth >= 4 and no chronological speed extension is run.
"""

from collections import Counter
from hashlib import sha256


C0 = 3**37
DIGITS = (2, 1, 2)
INITIAL = tuple(sorted(
    {(21, j, C0) for j in range(21)}
    | {(j, 21, C0) for j in range(21)}
))


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def numerator(h, hp, x, z):
    if h >= hp:
        return (z << (h - hp)) - x
    return z - (x << (hp - h))


def transitions(state, c):
    """Independent integer implementation of the inherited necessary rule."""
    h, hp, C = state
    assert C > 0 and ((C & 1) == 0) == (h == hp)
    g = h - hp
    if g >= 0:
        N = 3 * C + (1 << g) - 1
        extra_z, extra_x = g, 0
    else:
        N = 3 * C + 1 - (1 << -g)
        extra_z, extra_x = 0, -g
    assert N > 0
    w = v2(N)
    for a in range(1, h + c + 1):
        for b in range(1, hp + c + 1):
            u, v = extra_x + a, extra_z + b
            if u == v:
                allowed = w > u
            else:
                allowed = w == min(u, v)
            if not allowed:
                continue
            ns = h + c - a, hp + c - b, N >> min(u, v)
            assert min(ns) >= 0
            yield ns, a, b


def word_residue(word):
    """Unique seed class for the prescribed exact odd acceleration word.

    x_n = (3**n * x_0 + S_n) / 2**U_n; endpoint oddness is both necessary
    and sufficient for every preceding exact valuation in the word.
    """
    U, S = 0, 0
    for a in word:
        assert a >= 1
        S = 3 * S + (1 << U)
        U += a
    modulus = 1 << (U + 1)
    residue = (((1 << U) - S) * pow(3**len(word), -1, modulus)) % modulus
    assert residue & 1
    return residue, modulus, U, S


def merge_dyadic(r1, m1, r2, m2):
    assert m1 & (m1 - 1) == 0 and m2 & (m2 - 1) == 0
    assert (r1 - r2) % min(m1, m2) == 0
    return (r1 % m1, m1) if m1 >= m2 else (r2 % m2, m2)


def divide_dyadic(b, d, modulus):
    """Solve 2**d * t = b modulo a power of two."""
    exponent = modulus.bit_length() - 1
    b %= modulus
    if d >= exponent:
        assert b == 0
        return 0, 1
    assert b % (1 << d) == 0
    return b >> d, modulus >> d


def seed_class(initial, aa, bb):
    h, hp, C = initial
    g = h - hp
    rx, mx, U, Sx = word_residue(aa)
    rz, mz, V, Sz = word_residue(bb)
    # The final parity compatibility condition, checked independently from
    # pairwise merging of the two seed congruences.
    if g >= 0:
        N = 3**len(aa) * C + (1 << g) * Sz - Sx
        u, v = U, g + V
        rt, mt = divide_dyadic(C + rx, g, mx)
        r, m = merge_dyadic(rz, mz, rt, mt)
    else:
        d = -g
        N = 3**len(aa) * C + Sz - (1 << d) * Sx
        u, v = d + U, V
        rt, mt = divide_dyadic(rz - C, d, mz)
        r, m = merge_dyadic(rx, mx, rt, mt)
    assert (N + (1 << u) - (1 << v)) % (1 << (min(u, v) + 1)) == 0
    assert r & 1
    return r, m, N, min(u, v)


def choose_seed(initial, residue, modulus, odd_modulus=3**5, odd_residue=1):
    """Select a positive seed in the dyadic class and an arbitrary odd class.

    The finite replay uses the nontrivial initial constraint t = 1 mod 3**5.
    The proof permits every odd modulus and every prescribed residue.
    """
    assert odd_modulus > 0 and odd_modulus & 1
    odd_residue %= odd_modulus
    h, hp, C = initial
    g = h - hp
    k = ((odd_residue - residue) * pow(modulus, -1, odd_modulus)) % odd_modulus
    t = residue + modulus * k
    stride = modulus * odd_modulus
    threshold = C // (1 << g) + 1 if g >= 0 else 1
    if t < threshold:
        t += ((threshold - t + stride - 1) // stride) * stride
    assert t > 0 and t % modulus == residue and t % odd_modulus == odd_residue
    if g >= 0:
        x, z = (t << g) - C, t
    else:
        x, z = t, (t << -g) + C
    assert x > 0 and z > 0 and x & 1 and z & 1
    # Compatible initial classes include t=0 mod3. Those local starting
    # states may be multiples of3; only successors must be nonzero mod3.
    # The full path replay still chooses t=1 mod3**5.
    if C % 3 == 0:
        assert (x % 3 == 0) == (z % 3 == 0) == (t % 3 == 0)
    assert numerator(h, hp, x, z) == C
    return x, z, t, stride


def check_helper_odd_classes():
    """Bounded regressions for the repaired general odd-class interface."""
    classes = ((1, 0), (1, 1), (3, 0), (3, 1), (9, -1), (9, 10), (5, 0), (3**5, 1))
    count = 0
    initial_mod3_zero_cases = 0
    for root in INITIAL:
        ns, a, b = next(transitions(root, DIGITS[0]))
        residue, modulus, _, _ = seed_class(root, (a,), (b,))
        for odd_modulus, odd_residue in classes:
            x, z, t, _ = choose_seed(root, residue, modulus, odd_modulus, odd_residue)
            assert t % odd_modulus == odd_residue % odd_modulus
            assert v2(3*x+1) == a and v2(3*z+1) == b
            xx, zz = (3*x+1) >> a, (3*z+1) >> b
            assert xx % 3 and zz % 3
            assert numerator(ns[0], ns[1], xx, zz) == ns[2]
            initial_mod3_zero_cases += int(x % 3 == z % 3 == 0)
            count += 1
    assert count == 336 and initial_mod3_zero_cases > 0
    return count, initial_mod3_zero_cases


def check_path(initial, records):
    aa = tuple(a for _, a, _ in records)
    bb = tuple(b for _, _, b in records)
    residue, modulus, N, normalization = seed_class(initial, aa, bb)
    assert N >> normalization == records[-1][0][2]
    x, z, t, stride = choose_seed(initial, residue, modulus)
    x0, z0 = x, z
    h, hp, C = initial
    for c, (ns, a, b) in zip(DIGITS, records):
        assert v2(3 * x + 1) == a
        assert v2(3 * z + 1) == b
        x = (3 * x + 1) >> a
        z = (3 * z + 1) >> b
        h, hp = h + c - a, hp + c - b
        assert (h, hp) == ns[:2]
        assert min(h, hp) >= 0
        assert x > 0 and z > 0 and x & 1 and z & 1
        assert x % 3 and z % 3
        assert numerator(h, hp, x, z) == ns[2]
        C = ns[2]
    # A second positive member of the infinite CRT family verifies that the
    # construction is a congruence family, rather than a one-seed accident.
    t2 = t + stride
    g0 = initial[0] - initial[1]
    if g0 >= 0:
        xx, zz = (t2 << g0) - initial[2], t2
    else:
        xx, zz = t2, (t2 << -g0) + initial[2]
    for a, b in zip(aa, bb):
        assert v2(3 * xx + 1) == a and v2(3 * zz + 1) == b
        xx, zz = (3 * xx + 1) >> a, (3 * zz + 1) >> b
    return aa, bb, x0, z0, residue, modulus


def verify():
    assert len(INITIAL) == 42
    helper_counts = check_helper_odd_classes()
    graph_states = set(INITIAL)
    graph_counts = []
    cache = {}
    for depth, c in enumerate(DIGITS):
        next_states = set()
        edge_count = 0
        for st in sorted(graph_states):
            edges = tuple(transitions(st, c))
            cache[(depth, st)] = edges
            edge_count += len(edges)
            next_states.update(ns for ns, _, _ in edges)
        signs = Counter((h > hp) - (h < hp) for h, hp, _ in next_states)
        graph_counts.append((len(next_states), edge_count, dict(sorted(signs.items()))))
        graph_states = next_states
    assert graph_counts == [
        (540, 540, {-1: 268, 0: 2, 1: 270}),
        (4202, 4517, {-1: 2182, 0: 16, 1: 2004}),
        (25417, 30977, {-1: 14766, 0: 16, 1: 10635}),
    ]

    all_paths = [(root, ()) for root in INITIAL]
    path_counts = []
    digest = sha256()
    first_zero_witnesses = {}
    last_witnesses = {}
    for depth, c in enumerate(DIGITS):
        next_paths = []
        for root, records in all_paths:
            st = records[-1][0] if records else root
            for edge in cache[(depth, st)]:
                nrecords = records + (edge,)
                witness = check_path(root, nrecords)
                digest.update(repr((root, nrecords, witness)).encode("ascii") + b"\n")
                if depth == 0 and edge[0][0] == edge[0][1]:
                    first_zero_witnesses[root] = witness
                last_witnesses[root] = witness
                next_paths.append((root, nrecords))
        all_paths = next_paths
        path_counts.append(len(all_paths))
    assert set(last_witnesses) == set(INITIAL)
    assert {root for root, _ in all_paths} == set(INITIAL)
    assert len(first_zero_witnesses) == 2
    assert path_counts == [540, 4517, 34039]
    sign_patterns = {
        tuple((h > hp) - (h < hp) for h, hp, _ in (root,) + tuple(
            edge[0] for edge in records
        ))
        for root, records in all_paths
    }
    assert len(sign_patterns) == 44
    assert digest.hexdigest() == "34837dc796e7637e7044c1ad3393a31a2baef7129ea9b9154d7775928810277f"
    print("PASS: complete local odd-trajectory realizability of depth-3 parity graph")
    print("local relaxation only, not a physical p-edge or cycle")
    print("initial_pairs=42; common_word=212; exact_transition_depth=3")
    print("graph_state_edge_sign_counts=", graph_counts)
    print("exact_path_counts_by_depth=", path_counts)
    print("locally_realizable_four_source_sign_patterns=", len(sign_patterns))
    print("all_paths_witnessed_at_every_depth; arbitrary_odd_modulus_CRT_lemma")
    print("finite_replay_additional_seed_constraint=t mod 3**5 == 1")
    print("helper_odd_class_regressions_total_initial_mod3_zero=", helper_counts)
    print("deterministic_witness_digest=", digest.hexdigest())
    print("immediate_zero_witnesses_(a_word,b_word,X0,Z0,residue,modulus)=")
    for root, witness in sorted(first_zero_witnesses.items()):
        print(root, witness)
    print("not_certified: depth>=4, p-step coupling, period closure, H21 incidence")


if __name__ == "__main__":
    verify()
