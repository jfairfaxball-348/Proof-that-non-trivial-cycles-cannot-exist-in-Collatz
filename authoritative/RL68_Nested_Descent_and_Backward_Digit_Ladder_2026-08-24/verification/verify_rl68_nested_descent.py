#!/usr/bin/env python3
from collections import Counter


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


def one_positions(w):
    return [i for i, b in enumerate(w) if b]


def rank_data(xw, yw):
    aa = one_positions(xw)
    bb = one_positions(yw)
    assert len(aa) == len(bb)
    return aa, bb, [a - b for a, b in zip(aa, bb)]


def replay(xw, yw):
    d, T, H = 1, -14, 0
    out = []
    for x, y in zip(xw, yw):
        z = rl_step(d, T, H, x, y)
        assert z is not None
        d, T, H = z
        out.append((d, T, J_of(d, T), H))
    return out


MAX_M = 18
states = [(1, -14, 0, (), ())]
terminal = 0
nested = 0
poly_checks = 0
mod9_gap_checks = 0
parity_checks = 0
mod6_lifts = 0
backward_digit_checks = 0
nested_H5_checks = 0
stack_counts = Counter()
max_stack = 0

for m in range(MAX_M + 1):
    for d, T, H, xw, yw in states:
        J = J_of(d, T)
        if d != 1 or not is_power_of_two(J) or J < 8 or T != J - 1:
            continue
        terminal += 1
        aa, bb, delta = rank_data(xw, yw)
        active = [j for j, z in enumerate(delta) if z > 0]
        assert len(active) >= 2
        js = active[-1]
        p = active[-2]
        if js != p + 1:
            continue
        ap = aa[p]
        bstar = bb[js]
        if ap <= bstar:
            continue

        nested += 1
        rep = replay(xw, yw)
        bp = bb[p]
        astar = aa[js]
        ds = delta[js]
        dp = delta[p]
        beta = bstar - bp
        lam = ap - bstar
        mu = astar - ap
        assert beta >= 1 and lam >= 1 and mu >= 1
        assert dp == beta + lam
        assert ds == lam + mu

        C = rep[ap - 1][2]
        TC = rep[ap - 1][1]
        assert rep[ap - 1][0] == 3
        assert TC == C - 19
        R = rep[astar][2]
        assert C - 10 == (1 << (ds - lam)) * (2 * R - 5)

        # Earlier x-ranks still outstanding immediately after b_* are exactly
        # the x-ones strictly between b_* and a_p.  Their positions form an
        # ordered y-silent descent stack.
        cpos = [a for a in aa[:p] if bstar < a < ap]
        t = len(cpos)
        stack_counts[t] += 1
        max_stack = max(max_stack, t)
        assert rep[bstar][0] == t + 3
        TS = rep[bstar][1]
        assert rep[bstar][2] == TS + 3 ** (t + 3) - 2 ** (t + 3)

        # Exact ordered descent polynomial:
        # 2^(lam-1) T_C = T_S + sum_i 2^(c_i-b_*-1) 3^(t+2-i), i=0..t-1.
        rhs = TS
        for i, c in enumerate(cpos):
            rhs += (1 << (c - bstar - 1)) * 3 ** (t + 2 - i)
        lhs = (1 << (lam - 1)) * TC
        assert lhs == rhs
        poly_checks += 1

        # Every ordered-stack correction is a multiple of 27, so one gets
        # a robust mod-9 gap selector after the y-one at b_*.
        theta_state = ((1 << (lam - 1)) * TC) % 9
        theta_terminal = ((1 << (ds - 1)) * (2 * R - 5)) % 9
        assert theta_state == theta_terminal
        want = 1 if beta % 2 else 7
        assert theta_terminal == want
        mod9_gap_checks += 1

        # The previously unresolved nested parity is now recovered.
        recovered_dp = (lam + (1 if theta_terminal == 1 else 0)) % 2
        assert recovered_dp == dp % 2
        parity_checks += 1

        # Since 2 generates the units mod 9, R mod 9 plus beta parity selects
        # delta_* mod 6 uniquely.
        candidates = []
        for e in range(1, 7):
            if R % 3 != (1 + pow(2, e, 3)) % 3:
                continue
            if (pow(2, e - 1, 9) * (2 * R - 5)) % 9 == want:
                candidates.append(e)
        assert len(candidates) == 1
        actual = ds % 6 or 6
        assert candidates[0] == actual
        mod6_lifts += 1

        # One further backward digit.  Let T_- be the T-state immediately
        # before b_*, and T_p^+ the state immediately after b_p.
        # The exact descent polynomial and height divisibility imply
        # Z=(2^lam T_C+1)/3 == T_- (mod 9), then
        # Q=2^(beta-1) Z == T_p^+ (mod 9).
        z_num = (1 << lam) * TC + 1
        assert z_num % 3 == 0
        Z = z_num // 3
        Tminus = rep[bstar - 1][1] if bstar else -14
        assert Z % 9 == Tminus % 9
        Q = (pow(2, beta - 1, 9) * (Z % 9)) % 9
        Tpplus = rep[bp][1]
        assert Q == Tpplus % 9
        assert Q in (1, 7)
        Tpre_p = rep[bp - 1][1] if bp else -14
        assert Tpre_p % 3 in (1, 2)
        assert Q == (1 if Tpre_p % 3 == 1 else 7)
        backward_digit_checks += 1

        # Analytic theorem mirrored: nested terminal paths have H>=5.
        assert H >= 5
        nested_H5_checks += 1

    if m == MAX_M:
        break

    nxt = []
    for d, T, H, xw, yw in states:
        J = J_of(d, T)
        opts = ((0, 0), (1, 1)) if J & 1 else ((0, 1), (1, 0))
        for x, y in opts:
            if (x, y) == (1, 0) and d <= 1:
                continue
            out = rl_step(d, T, H, x, y)
            if out is None:
                continue
            d2, T2, H2 = out
            nxt.append((d2, T2, H2, xw + (x,), yw + (y,)))
    states = nxt

print('RL68 nested-descent verifier: PASS')
print('bounded canonical terminal paths =', terminal)
print('nested g=0 terminal interfaces =', nested)
print('exact ordered nested-descent polynomial checks =', poly_checks)
print('nested mod-9 terminal gap-selector checks =', mod9_gap_checks)
print('nested previous-active parity recoveries =', parity_checks)
print('nested delta_* mod-6 lifts =', mod6_lifts)
print('nested second backward-digit checks =', backward_digit_checks)
print('nested H>=5 checks =', nested_H5_checks)
print('maximum earlier-x stack depth seen =', max_stack)
print('stack depth histogram =', dict(sorted(stack_counts.items())))
