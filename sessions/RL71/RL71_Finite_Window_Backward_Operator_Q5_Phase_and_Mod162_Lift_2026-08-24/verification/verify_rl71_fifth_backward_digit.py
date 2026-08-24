#!/usr/bin/env python3
"""RL71 bounded falsification/audit for the fifth backward digit and mod-162 lift.

This independently recomputes canonical RL states from the exact recurrence
through MAX_M=18.  It carries the RL69/RL70 nested ordered descent one 3-adic
digit higher, retaining exactly the two latest earlier x-ranks that become
visible.  It verifies:

  * T_p^- modulo 27;
  * T_(p-1)^- modulo 9;
  * the next pre-b_(p-2) trit and delta_(p-3) parity selector;
  * the q=5 full-phase rank-tail digit when the bounded denominator is positive;
  * the nested terminal selector delta_* modulo 162 and its residue floor.

This scan is an audit/falsification tool only.  The analytic statements are
proved separately in the RL71 mathematics note.
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
local_backward_polynomial_checks = 0
nested = 0
terminal_exact_identity_checks = 0
lift_tp27 = 0
lift_tq9 = 0
push_tr3 = 0
rank_p3_parity = 0
phase_rank5 = 0
mod162_lifts = 0
floor_checks = 0
low_k_exact_checks = 0

# Nonzero second-rank (r=p-2) correction incidence, to demonstrate that the
# new terms are genuinely needed in the bounded sample.
r_post_bstar = 0
r_between_bp_bstar = 0
r_at_bp = 0
r_between_bq_bp = 0
r_at_bq = 0

for m in range(MAX_M + 1):
    for d, T, H, xw, yw in states:
        J = J_of(d, T)
        if d != 1 or not is_power_of_two(J) or J < 8 or T != J - 1:
            continue
        terminal += 1
        k = J.bit_length() - 1
        aa, bb, delta, rnk = rank_data(xw, yw)

        # General exact consecutive-y backward polynomial (all terminal paths).
        rep_all = replay(xw, yw)
        for j in range(len(bb) - 1):
            bj = bb[j]
            bn = bb[j + 1]
            Tnext = rep_all[bn - 1][1] if bn else -14
            Tplus = rep_all[bj][1]
            lhs = (1 << (bn - bj - 1)) * Tnext
            rhs = Tplus + sum(
                (1 << (aa[i] - bj - 1)) * 3 ** (j - i + 1)
                for i in range(j + 1)
                if bj < aa[i] < bn
            )
            assert lhs == rhs
            Tpre = rep_all[bj - 1][1] if bj else -14
            simultaneous = sum(
                3 ** (j - i + 1)
                for i in range(j + 1)
                if aa[i] == bj
            )
            assert 2 * Tplus + 1 == 3 * Tpre + simultaneous
            local_backward_polynomial_checks += 1

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
        r = q - 1
        h = r - 1

        rep = rep_all
        bp = bb[p]
        bstar = bb[js]
        ap = aa[p]
        astar = aa[js]
        bq = bb[q]
        beta = bstar - bp
        lam = ap - bstar
        ds = delta[js]

        TC = rep[ap - 1][1]
        z_num = (1 << lam) * TC + 1
        assert z_num % 3 == 0
        Z = z_num // 3
        R = rep[astar][2]

        aq = aa[q]
        ar = aa[r] if r >= 0 else None

        # Exact nested terminal finite-window identities before truncation.
        actual_star_minus_exact = rep[bstar - 1][1] if bstar else -14
        assert Z == actual_star_minus_exact + sum(
            (1 << (aa[i] - bstar)) * 3 ** (q - i + 2)
            for i in range(q + 1)
            if aa[i] >= bstar
        )
        assert (1 << (beta - 1)) * actual_star_minus_exact == rep[bp][1] + sum(
            (1 << (aa[i] - bp - 1)) * 3 ** (q - i + 2)
            for i in range(q + 1)
            if bp < aa[i] < bstar
        )
        actual_p_pre_exact = rep[bp - 1][1] if bp else -14
        assert 2 * rep[bp][1] + 1 == 3 * actual_p_pre_exact + sum(
            3 ** (q - i + 2)
            for i in range(q + 1)
            if aa[i] == bp
        )
        terminal_exact_identity_checks += 1

        # One-power-higher terminal descent.  Rank q contributes at the 9-level,
        # rank r at the 27-level; every earlier rank is divisible by 81.
        alpha_q = pow(2, aq - bstar, 9) if aq >= bstar else 0
        alpha_r = (
            pow(2, ar - bstar, 3)
            if r >= 0 and ar >= bstar
            else 0
        )
        if alpha_r:
            r_post_bstar += 1
        Tstar_minus_81 = (Z - 9 * alpha_q - 27 * alpha_r) % 81
        actual_star_minus = rep[bstar - 1][1] if bstar else -14
        assert Tstar_minus_81 == actual_star_minus % 81

        # Propagate from b_p to b_* modulo 81.
        kappa_q = (
            pow(2, aq - bp - 1, 9) if bp < aq < bstar else 0
        )
        kappa_r = (
            pow(2, ar - bp - 1, 3)
            if r >= 0 and bp < ar < bstar
            else 0
        )
        if kappa_r:
            r_between_bp_bstar += 1
        Up = (
            pow(2, beta - 1, 81) * Tstar_minus_81
            - 9 * kappa_q
            - 27 * kappa_r
        ) % 81
        assert Up == rep[bp][1] % 81

        chi_q = 1 if aq == bp else 0
        chi_r = 1 if r >= 0 and ar == bp else 0
        if chi_r:
            r_at_bp += 1
        num = (2 * Up + 1 - 9 * chi_q - 27 * chi_r) % 81
        assert num % 3 == 0
        V27 = (num // 3) % 27
        Tp_pre = rep[bp - 1][1] if bp else -14
        assert V27 == Tp_pre % 27
        lift_tp27 += 1

        # Reverse the lift to reconstruct Z modulo 81 solely from V27 and the
        # local correction data.
        U_from_V = (
            (3 * V27 - 1 + 9 * chi_q + 27 * chi_r)
            * pow(2, -1, 81)
        ) % 81
        z81 = (
            pow(2, 1 - beta, 81)
            * (U_from_V + 9 * kappa_q + 27 * kappa_r)
            + 9 * alpha_q
            + 27 * alpha_r
        ) % 81
        assert z81 == Z % 81

        # Terminal compatibility modulo 243 selects delta_* modulo 162.
        rhs243 = (9 * pow(2, lam, 243) - 1 + 3 * z81) % 243
        assert (pow(2, ds, 243) * (2 * R - 5)) % 243 == rhs243
        candidates162 = [
            e
            for e in range(1, 163)
            if (pow(2, e, 243) * (2 * R - 5)) % 243 == rhs243
        ]
        c162 = ds % 162 or 162
        assert candidates162 == [c162]
        mod162_lifts += 1

        assert H >= delta[p] + c162
        floor_checks += 1
        if H < k and k <= 165:
            assert ds == c162
            low_k_exact_checks += 1

        # Push across b_q at modulo 27.  Rank q is the 3-level correction and
        # rank r the 9-level correction; deeper ranks vanish modulo 27.
        gamma = bp - bq
        tau_q = pow(2, aq - bq - 1, 9) if bq < aq < bp else 0
        tau_r = (
            pow(2, ar - bq - 1, 3)
            if r >= 0 and bq < ar < bp
            else 0
        )
        if tau_r:
            r_between_bq_bp += 1
        Uq = (
            pow(2, gamma - 1, 27) * V27 - 3 * tau_q - 9 * tau_r
        ) % 27
        assert Uq == rep[bq][1] % 27

        sigma_q = 1 if aq == bq else 0
        sigma_r = 1 if r >= 0 and ar == bq else 0
        if sigma_r:
            r_at_bq += 1
        qnum = (2 * Uq + 1 - 3 * sigma_q - 9 * sigma_r) % 27
        assert qnum % 3 == 0
        S9 = (qnum // 3) % 9
        Tq_pre = rep[bq - 1][1] if bq else -14
        assert S9 == Tq_pre % 9
        lift_tq9 += 1

        # One more RL70-style push across b_r, recovering T_r^- modulo 3.
        if r >= 0:
            br = bb[r]
            theta = bq - br
            dr = delta[r]
            tau_small = pow(2, dr - 1, 3) if 0 < dr < theta else 0
            sigma_small = 1 if dr == 0 else 0
            Ur = (pow(2, theta - 1, 9) * S9 - 3 * tau_small) % 9
            assert Ur == rep[br][1] % 9
            rnum = (2 * Ur + 1 - 3 * sigma_small) % 9
            assert rnum % 3 == 0
            S3 = (rnum // 3) % 3
            Tr_pre = rep[br - 1][1] if br else -14
            assert S3 == Tr_pre % 3
            push_tr3 += 1

            # The trit selects delta_(p-3) parity when that rank exists.
            if h >= 0:
                gap = br - bb[h]
                assert S3 in (1, 2)
                assert S3 == (1 if gap % 2 else 2)
                gap_parity = 1 if S3 == 1 else 0
                recovered = ((aa[h] - br) & 1) ^ gap_parity
                assert recovered == delta[h] % 2
                rank_p3_parity += 1

                # Match the q=5 full-phase rank-tail digit.
                n_tail, s_tail = max_sync_suffix(xw, yw)
                a_full = m + k + 1
                ell = rnk + 3
                M = (1 << a_full) - 3**ell
                if M > 0:
                    v = (1, 1, 1) + yw + (0,) * (k - 2)
                    Vpoly = qpoly(v)
                    Y = 3**ell
                    mod = 3 ** (s_tail + 6)
                    Nres = (
                        ((Vpoly + 4 * Y) % mod) * pow(M, -1, mod)
                    ) % mod

                    ids = [js, p, q, r, h]
                    weights = [1, 3, 9, 27, 81]
                    C5 = 0
                    for jj, weight in zip(ids, weights):
                        Ej = (1 << bb[jj]) * ((1 << delta[jj]) - 1)
                        C5 += weight * Ej
                    want = (
                        2
                        - pow(2, 1 - k, mod)
                        - 4
                        * 3 ** (s_tail + 1)
                        * pow(2, -a_full, mod)
                        * C5
                    ) % mod
                    assert Nres == want

                    C4 = 0
                    for jj, weight in zip(ids[:4], weights[:4]):
                        Ej = (1 << bb[jj]) * ((1 << delta[jj]) - 1)
                        C4 += weight * Ej
                    base4 = (
                        2
                        - pow(2, 1 - k, mod)
                        - 4
                        * 3 ** (s_tail + 1)
                        * pow(2, -a_full, mod)
                        * C4
                    ) % mod
                    correction = 0
                    if recovered:
                        correction = (
                            4
                            * pow(2, bb[h] - a_full, mod)
                            * 3 ** (s_tail + 5)
                        ) % mod
                    assert Nres == (base4 - correction) % mod
                    phase_rank5 += 1

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

print('RL71 fifth-backward-digit verifier: PASS')
print('bounded canonical terminal paths =', terminal)
print('exact consecutive-y polynomial checks =', local_backward_polynomial_checks)
print('nested g=0 terminal interfaces =', nested)
print('exact nested terminal polynomial checks =', terminal_exact_identity_checks)
print('T_p^- mod-27 lifts =', lift_tp27)
print('T_(p-1)^- mod-9 lifts =', lift_tq9)
print('pre-b_(p-2) mod-3 pushes =', push_tr3)
print('delta_(p-3) parity-selector checks =', rank_p3_parity)
print('full-phase q=5 digit matches =', phase_rank5)
print('nested delta_* mod-162 lifts =', mod162_lifts)
print('mod-162 residue-floor checks =', floor_checks)
print('bounded low-k exact-value implications triggered =', low_k_exact_checks)
print('nonzero r correction after/at b_* =', r_post_bstar)
print('nonzero r correction between b_p and b_* =', r_between_bp_bstar)
print('r simultaneous correction at b_p =', r_at_bp)
print('nonzero r correction between b_q and b_p =', r_between_bq_bp)
print('r simultaneous correction at b_q =', r_at_bq)
