#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement

RHO = Fraction(2, 3)
THRESH = Fraction(17, 2)


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def J_of(d, T):
    return T + 3**d - 2**d


def rl_step(d, T, H, x, y):
    num = (3**y) * T + x * 3**(d + y - 1) - y
    if num % 2:
        return None
    d2 = d + y - x
    if d2 < 1:
        return None
    return d2, num // 2, H + d - 1


def step_from_x(d, J, H, x):
    T = J - 3**d + 2**d
    if J & 1:
        y = x
    else:
        y = 1 - x
        if x == 1 and d <= 1:
            return None
    out = rl_step(d, T, H, x, y)
    if out is None:
        return None
    d2, T2, H2 = out
    return d2, J_of(d2, T2), H2, y


def one_positions(w):
    return [i for i, b in enumerate(w) if b]


def rank_data(xw, yw):
    aa = one_positions(xw)
    bb = one_positions(yw)
    assert len(aa) == len(bb)
    delta = [a - b for a, b in zip(aa, bb)]
    r = len(aa)
    Qx = sum((1 << a) * 3**(r - j) for j, a in enumerate(aa, 1))
    Qy = sum((1 << b) * 3**(r - j) for j, b in enumerate(bb, 1))
    return aa, bb, delta, Qx, Qy


def weighted_prefix(u):
    return sum((1 << i) * RHO**v for i, v in enumerate(u))


def x_prefix_from_u(u):
    bits = []
    ones = 0
    for target in u:
        while ones < target:
            bits.append(1)
            ones += 1
        bits.append(0)
    return tuple(bits)


def replay_prefix(prefix):
    d, J, H = 1, -13, 0
    xw, yw = [], []
    for x in prefix:
        st = step_from_x(d, J, H, x)
        if st is None:
            return None
        d, J, H, y = st
        xw.append(x)
        yw.append(y)
    return d, J, H, tuple(xw), tuple(yw)


def close_with_ones(prefix, max_steps=128):
    got = replay_prefix(prefix)
    if got is None:
        return ("illegal",)
    d, J, H, xw, yw = got
    xw, yw = list(xw), list(yw)
    seen = set()
    for _ in range(max_steps):
        m = len(xw)
        if d == 1 and is_power_of_two(J) and J >= 8:
            k = J.bit_length() - 1
            r = sum(xw)
            a = m + k + 1
            ell = r + 3
            aa, bb, delta, Qx, Qy = rank_data(tuple(xw), tuple(yw))
            assert H == sum(delta)
            assert 3 * Qx - Qy == 14 * 3**r + 2**(a - 1) - 2**(a - k - 1)
            ratio_ok = 3**ell < 2**a and 81 * 2**a < 160 * 3**ell
            return ("terminal", k, H, m, r, a, ell, ratio_ok)
        key = (d, J)
        assert key not in seen, ("unexpected all-one cycle", prefix, key)
        seen.add(key)
        st = step_from_x(d, J, H, 1)
        if st is None:
            return ("stop", d, J, H, len(xw))
        d, J, H, y = st
        xw.append(1)
        yw.append(y)
    raise AssertionError(("all-one closure too long", prefix, d, J, H))


def all_one_run(prefix, max_steps=128):
    got = replay_prefix(prefix)
    if got is None:
        return None
    d, J, H, xw, yw = got
    steps = 0
    seen = set()
    while steps < max_steps:
        if d == 1 and is_power_of_two(J) and J >= 8:
            return steps
        key = (d, J)
        assert key not in seen, ("unexpected all-one cycle", prefix, key)
        seen.add(key)
        st = step_from_x(d, J, H, 1)
        if st is None:
            return steps
        d, J, H, _ = st
        steps += 1
    raise AssertionError(("all-one run too long", prefix, d, J, H))


def exact_max_below(n):
    """Exact max of S_n below THRESH, with no arbitrary rank cutoff.

    At a prefix ending with lower rank `prev`, if the next rank is u then the
    largest possible completion uses u for every remaining coordinate. Once
    that upper envelope is <= the current best, all larger u are safely pruned.
    """
    best = Fraction(0)
    witness = None

    def dfs(prefix, prev, s, j):
        nonlocal best, witness
        if j == n:
            if s < THRESH and s > best:
                best = s
                witness = tuple(prefix)
            return
        u = prev
        while True:
            upper = s + ((1 << n) - (1 << j)) * RHO**u
            if upper <= best:
                break
            s2 = s + (1 << j) * RHO**u
            if s2 < THRESH:
                dfs(prefix + [u], u, s2, j + 1)
            u += 1

    dfs([], 0, Fraction(0), 0)
    return best, witness


def bounded_admissible(n, bound):
    out = []

    def rec(prefix, prev, s, j):
        if j == n:
            if s > THRESH:
                out.append(tuple(prefix))
            return
        for u in range(prev, bound + 1):
            s2 = s + (1 << j) * RHO**u
            upper = s2 + sum((1 << q) * RHO**u for q in range(j + 1, n))
            if upper <= THRESH:
                break
            rec(prefix + [u], u, s2, j + 1)

    rec([], 0, Fraction(0), 0)
    return out


def five_zero_crossing_family():
    # Reproduce the already-promoted RL277 five-zero family.
    admissible = [u for u in combinations_with_replacement(range(12), 5)
                  if weighted_prefix(u) > THRESH]
    assert len(admissible) == 206
    legal = [u for u in admissible if replay_prefix(x_prefix_from_u(u)) is not None]
    assert len(legal) == 72
    assert max(u[-1] for u in legal) == 7
    runs = [all_one_run(x_prefix_from_u(u)) for u in legal]
    assert max(runs) == 11
    return legal, max(runs)


def six_zero_certificate():
    # Exact gap below the five-zero threshold.
    M5, witness5 = exact_max_below(5)
    assert M5 == Fraction(501898, 59049)
    assert witness5 == (1, 1, 1, 2, 10)
    gap5 = THRESH - M5
    assert gap5 == Fraction(37, 118098)

    # If S5 < THRESH but S6 > THRESH, the sixth term must bridge gap5.
    assert 32 * RHO**28 > gap5
    assert 32 * RHO**29 < gap5
    below_branch_bound = 28

    # If S5 > THRESH, RL277's exact legal five-zero family is finite.
    # Its all-one closure allows at most 11 further one-columns before terminal/stop.
    legal5, max_run5 = five_zero_crossing_family()
    assert max_run5 == 11
    assert max(u[-1] for u in legal5) + max_run5 == 18
    above_branch_bound = 18

    B6 = max(below_branch_bound, above_branch_bound)
    assert B6 == 28

    admissible6 = bounded_admissible(6, B6)
    assert len(admissible6) == 7081

    legal6 = []
    for u in admissible6:
        prefix = x_prefix_from_u(u)
        if replay_prefix(prefix) is not None:
            legal6.append((u, prefix))
    assert len(legal6) == 458
    assert max(u[-1] for u, _ in legal6) == 14

    terminals = []
    box = []
    dangerous = []
    for u, prefix in legal6:
        out = close_with_ones(prefix)
        if out[0] == "terminal":
            terminals.append((u, out))
            if out[-1]:
                box.append((u, out))
                if out[2] < out[1]:
                    dangerous.append((u, out))

    assert len(terminals) == 170
    assert len(box) == 47
    assert dangerous == []
    pairs = sorted(set((o[1], o[2]) for _, o in box))
    assert pairs == [
        (3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10),(3,11),
        (5,18),(5,19),(5,20),(5,21),(5,22),(5,23),(5,25),(5,26),(5,31)
    ]

    return {
        "M5": M5,
        "witness5": witness5,
        "gap5": gap5,
        "B6": B6,
        "admissible6": len(admissible6),
        "legal6": len(legal6),
        "terminals6": len(terminals),
        "box6": len(box),
        "pairs6": pairs,
        "dangerous6": len(dangerous),
    }


def induction_sanity():
    # Reproduce exact sub-threshold maxima as a regression certificate.
    M4, w4 = exact_max_below(4)
    M5, w5 = exact_max_below(5)
    assert M4 == Fraction(25, 3)
    assert w4 == (0, 0, 2, 2)
    assert M5 == Fraction(501898, 59049)
    assert w5 == (1, 1, 1, 2, 10)
    # THRESH has denominator 2 in lowest terms, whereas every S_n has odd
    # denominator, so equality S_n=THRESH is impossible at every fixed n.
    assert THRESH.denominator == 2
    return M4, w4, M5, w5


def main():
    M4, w4, M5, w5 = induction_sanity()
    c = six_zero_certificate()
    print("PASS RL278 exact six-zero verifier")
    print("threshold=17/2")
    print("max_below_S4=", M4, "witness=", w4)
    print("max_below_S5=", M5, "witness=", w5)
    print("gap5=", c["gap5"])
    print("six_zero_rank_bound_u6<=", c["B6"])
    print("six_zero_admissible_tuples=", c["admissible6"])
    print("six_zero_canonical_prefixes=", c["legal6"])
    print("six_zero_terminals=", c["terminals6"])
    print("six_zero_ratio_box_terminals=", c["box6"])
    print("six_zero_ratio_box_pairs=", c["pairs6"])
    print("six_zero_gate_violators=", c["dangerous6"])
    print("promoted=H_can<k => m0>=7 => z>=k+5")
    print("classification=GLOBAL_SIX_ZERO_GATE_A_CONTRACTION_PROVED")
    print("subordinate=FIXED_ZERO_EXACT_FINITE_REDUCTION_ENGINE_IDENTIFIED")


if __name__ == "__main__":
    main()
