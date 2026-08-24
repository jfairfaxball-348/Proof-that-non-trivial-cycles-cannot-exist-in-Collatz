#!/usr/bin/env python3
"""RL70 bounded falsification/audit for the fourth backward parity digit.

This independently recomputes canonical RL states from the exact recurrence
through MAX_M=18.  It reconstructs the inherited RL69 V mod 9 digit, pushes it
one y-rank earlier across b_(p-1), checks the unique height-two correction,
recovers T immediately before b_(p-1) modulo 3, selects delta_(p-2) parity,
and checks the matching q=4 full-phase rank-tail digit whenever the bounded
full-phase denominator is positive.

The scan is an audit/falsification tool only; the analytic statements are
proved separately in the RL70 mathematics note.
"""


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def J_of(d, T):
    return T + 3**d - 2**d


def rl_step(d, T, H, x, y):
    num = (3**y) * T + x * 3 ** (d + y - 1) - y
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
    return aa, bb, [a - b for a, b in zip(aa, bb)], len(aa)


def replay(xw, yw):
    d, T, H = 1, -14, 0
    out = []
    for x, y in zip(xw, yw):
        z = rl_step(d, T, H, x, y)
        assert z is not None
        d, T, H = z
        out.append((d, T, J_of(d, T), H))
    return out


def max_sync_suffix(xw, yw):
    n = 0
    for x, y in zip(reversed(xw), reversed(yw)):
        if x != y:
            break
        n += 1
    w = () if n == 0 else xw[-n:]
    return len(w), sum(w)


def qpoly(w):
    ell = sum(w)
    rank = 0
    q = 0
    for i, bit in enumerate(w):
        if bit:
            rank += 1
            q += (1 << i) * 3 ** (ell - rank)
    return q


MAX_M = 18
states = [(1, -14, 0, (), ())]
terminal = 0
nested = 0
nested_with_q = 0
fourth_backward = 0
rank_p2_parity = 0
phase_rank4 = 0
q_zero = 0
q_interior = 0
q_at_bp = 0
q_after_bp = 0

for m in range(MAX_M + 1):
    for d, T, H, xw, yw in states:
        J = J_of(d, T)
        if d != 1 or not is_power_of_two(J) or J < 8 or T != J - 1:
            continue
        terminal += 1
        k = J.bit_length() - 1
        aa, bb, delta, rnk = rank_data(xw, yw)
        active = [j for j, z in enumerate(delta) if z > 0]
        assert len(active) >= 2
        js = active[-1]
        p = active[-2]
        if js != p + 1 or aa[p] <= bb[js]:
            continue

        nested += 1
        q = p - 1
        if q < 0:
            continue
        nested_with_q += 1

        rep = replay(xw, yw)
        bp = bb[p]
        bstar = bb[js]
        ap = aa[p]
        astar = aa[js]
        bq = bb[q]
        beta = bstar - bp
        lam = ap - bstar

        # Reconstruct the inherited RL69 third backward digit V = T_p^- mod 9.
        TC = rep[ap - 1][1]
        z_num = (1 << lam) * TC + 1
        assert z_num % 3 == 0
        Z = z_num // 3
        Aprev = aa[q]
        chi = 1 if Aprev == bp else 0
        kappa = pow(2, Aprev - bp - 1, 3) if bp < Aprev < bstar else 0
        if Aprev < bstar:
            alpha = 0
        elif Aprev == bstar:
            alpha = 1
        else:
            alpha = pow(2, Aprev - bstar, 3)
        U = (
            pow(2, beta - 1, 27) * ((Z - 9 * alpha) % 27)
            - 9 * kappa
        ) % 27
        num = (2 * U + 1 - 9 * chi) % 27
        assert num % 3 == 0
        V = (num // 3) % 9
        Tp_pre = rep[bp - 1][1] if bp else -14
        assert V == Tp_pre % 9

        # RL70: push V across b_q.  Only q itself can close at height two
        # strictly between b_q and b_p.  All earlier closures are >= height 3
        # and hence vanish modulo 9.
        gamma = bp - bq
        dq = delta[q]
        if dq == 0:
            q_zero += 1
        elif dq < gamma:
            q_interior += 1
        elif dq == gamma:
            q_at_bp += 1
        else:
            q_after_bp += 1

        tau = pow(2, dq - 1, 3) if 0 < dq < gamma else 0
        sigma = 1 if dq == 0 else 0
        Uq = (pow(2, gamma - 1, 9) * V - 3 * tau) % 9
        Tq_plus = rep[bq][1]
        assert Uq == Tq_plus % 9

        pre_num = (2 * Uq + 1 - 3 * sigma) % 9
        assert pre_num % 3 == 0
        S = (pre_num // 3) % 3
        Tq_pre = rep[bq - 1][1] if bq else -14
        assert S == Tq_pre % 3
        fourth_backward += 1

        # The recovered pre-b_q trit gives the preceding y-gap parity and
        # therefore delta_(p-2) parity when that rank exists.
        rr = q - 1
        if rr >= 0:
            gap = bq - bb[rr]
            assert S in (1, 2)
            assert S == (1 if gap % 2 else 2)
            gap_parity = 1 if S == 1 else 0
            recovered = ((aa[rr] - bq) & 1) ^ gap_parity
            assert recovered == delta[rr] % 2
            rank_p2_parity += 1

            # Match the next (q=4) full-phase rank-tail digit.
            n, s = max_sync_suffix(xw, yw)
            a_full = m + k + 1
            ell = rnk + 3
            M = (1 << a_full) - 3**ell
            if M > 0:
                v = (1, 1, 1) + yw + (0,) * (k - 2)
                Vpoly = qpoly(v)
                Y = 3**ell
                mod = 3 ** (s + 5)
                Nres = ((Vpoly + 4 * Y) % mod) * pow(M, -1, mod) % mod

                Ejs = (1 << bb[js]) * ((1 << delta[js]) - 1)
                Ep = (1 << bb[p]) * ((1 << delta[p]) - 1)
                Eq = (1 << bb[q]) * ((1 << delta[q]) - 1)
                Er = (1 << bb[rr]) * ((1 << delta[rr]) - 1)
                C4 = Ejs + 3 * Ep + 9 * Eq + 27 * Er
                want = (
                    2
                    - pow(2, 1 - k, mod)
                    - 4 * 3 ** (s + 1) * pow(2, -a_full, mod) * C4
                ) % mod
                assert Nres == want

                C3 = Ejs + 3 * Ep + 9 * Eq
                base3 = (
                    2
                    - pow(2, 1 - k, mod)
                    - 4 * 3 ** (s + 1) * pow(2, -a_full, mod) * C3
                ) % mod
                correction = 0
                if recovered:
                    correction = (
                        4 * pow(2, bb[rr] - a_full, mod) * 3 ** (s + 4)
                    ) % mod
                assert Nres == (base3 - correction) % mod
                phase_rank4 += 1

    nxt = []
    for d, T, H, xw, yw in states:
        for x in (0, 1):
            for y in (0, 1):
                z = rl_step(d, T, H, x, y)
                if z is None:
                    continue
                d2, T2, H2 = z
                nxt.append((d2, T2, H2, xw + (x,), yw + (y,)))
    states = nxt

print('RL70 fourth-backward-parity verifier: PASS')
print('bounded canonical terminal paths =', terminal)
print('nested g=0 terminal interfaces =', nested)
print('nested interfaces with q=p-1 present =', nested_with_q)
print('q zero-displacement cases =', q_zero)
print('q closes strictly before b_p =', q_interior)
print('q closes at b_p =', q_at_bp)
print('q closes after b_p =', q_after_bp)
print('pre-b_q mod-3 recoveries =', fourth_backward)
print('delta_(p-2) parity-selector checks =', rank_p2_parity)
print('full-phase q=4 digit matches =', phase_rank4)
