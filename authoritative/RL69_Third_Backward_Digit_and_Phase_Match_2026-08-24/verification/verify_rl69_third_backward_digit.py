#!/usr/bin/env python3
from fractions import Fraction


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


def affine_word(word):
    # Exact affine J-map J_out=A*J_in+B, without parity assumptions.
    d = 1
    A = Fraction(1)
    B = Fraction(0)
    for x, y in word:
        D = 3**d - 2**d
        d2 = d + y - x
        D2 = 3**d2 - 2**d2
        A2 = Fraction(3**y, 2) * A
        B2 = (
            Fraction(3**y, 2) * (B - D)
            + Fraction(x * 3 ** (d + y - 1) - y, 2)
            + D2
        )
        d, A, B = d2, A2, B2
    assert d == 1
    return A, B


# Mirror the four analytic H=5 sub-block formulas used in the proof.
A, B = affine_word(((0,1),(0,1),(1,0),(0,0),(1,0)))
assert (A, B) == (Fraction(9,32), Fraction(51,16))
A2, B2 = affine_word(((0,1),(0,0),(0,1),(1,0),(1,0)))
assert (A2, B2) == (Fraction(9,32), Fraction(17,4))
A3, B3 = affine_word(((0,1),(0,1),(1,0),(1,0)))
assert (A3, B3) == (Fraction(9,16), Fraction(31,8))
A4, B4 = affine_word(((0,1),(1,1),(0,1),(1,0),(1,0)))
assert (A4, B4) == (Fraction(27,32), Fraction(5,1))
for P0 in (-6, -28, -4):
    assert A * P0 + B != int(A * P0 + B) or A * P0 + B < 3
    assert A2 * P0 + B2 != int(A2 * P0 + B2) or A2 * P0 + B2 < 3
    assert A4 * P0 + B4 < 3
for P in (-4, 0):
    val = A3 * P + B3
    assert val.denominator != 1 or val < 3


MAX_M = 18
states = [(1, -14, 0, (), ())]
terminal = 0
nested = 0
nested_with_q = 0
rank_before_p_parity = 0
phase_rank3 = 0
mod18_lifts = 0
third_backward = 0
mod54_lifts = 0
nested_H6 = 0

for m in range(MAX_M + 1):
    for d, T, H, xw, yw in states:
        J = J_of(d, T)
        if d != 1 or not is_power_of_two(J) or J < 8 or T != J - 1:
            continue
        terminal += 1
        k = J.bit_length() - 1
        aa, bb, delta, r = rank_data(xw, yw)
        active = [j for j, z in enumerate(delta) if z > 0]
        assert len(active) >= 2
        js = active[-1]
        p = active[-2]
        if js != p + 1 or aa[p] <= bb[js]:
            continue

        nested += 1
        rep = replay(xw, yw)
        bp = bb[p]
        bstar = bb[js]
        ap = aa[p]
        astar = aa[js]
        beta = bstar - bp
        lam = ap - bstar
        ds = delta[js]
        TC = rep[ap - 1][1]
        R = rep[astar][2]
        assert rep[ap - 1][0] == 3
        assert TC == rep[ap - 1][2] - 19

        # RL68 second backward digit.
        z_num = (1 << lam) * TC + 1
        assert z_num % 3 == 0
        Z = z_num // 3
        Q = (pow(2, beta - 1, 9) * (Z % 9)) % 9
        assert Q in (1, 7)
        Tp_pre = rep[bp - 1][1] if bp else -14
        assert Q == (1 if Tp_pre % 3 == 1 else 7)

        # New: the immediate rank q=p-1 parity is already selected by Q.
        q = p - 1
        Aprev = aa[q] if q >= 0 else None
        if q >= 0:
            nested_with_q += 1
            gamma = bp - bb[q]
            gamma_parity = 1 if Q == 1 else 0
            assert gamma % 2 == gamma_parity
            recovered = ((Aprev - bp) & 1) ^ gamma_parity
            assert recovered == delta[q] % 2
            rank_before_p_parity += 1

        # New mod-18 lift of delta_* from Q.
        z9 = (pow(pow(2, beta - 1, 9), -1, 9) * Q) % 9
        rhs27 = (9 * pow(2, lam, 27) - 1 + 3 * z9) % 27
        assert (pow(2, ds, 27) * (2 * R - 5)) % 27 == rhs27
        candidates18 = [
            e for e in range(1, 19)
            if (pow(2, e, 27) * (2 * R - 5)) % 27 == rhs27
        ]
        assert candidates18 == [ds % 18 or 18]
        mod18_lifts += 1

        # New compact correction trits determined solely by placement of a_{p-1}.
        chi = 1 if Aprev is not None and Aprev == bp else 0
        kappa = (
            pow(2, Aprev - bp - 1, 3)
            if Aprev is not None and bp < Aprev < bstar
            else 0
        )
        if Aprev is None or Aprev < bstar:
            alpha = 0
        elif Aprev == bstar:
            alpha = 1
        else:
            alpha = pow(2, Aprev - bstar, 3)

        # Third backward digit: T immediately before b_p modulo 9.
        U = (
            pow(2, beta - 1, 27) * ((Z - 9 * alpha) % 27)
            - 9 * kappa
        ) % 27
        assert U == rep[bp][1] % 27
        num = (2 * U + 1 - 9 * chi) % 27
        assert num % 3 == 0
        V = (num // 3) % 9
        assert V == Tp_pre % 9
        third_backward += 1

        # New mod-54 lift from V and the three local correction trits.
        U_from_V = ((3 * V + 9 * chi - 1) * pow(2, -1, 27)) % 27
        z27 = (
            pow(pow(2, beta - 1, 27), -1, 27) * (U_from_V + 9 * kappa)
            + 9 * alpha
        ) % 27
        assert z27 == Z % 27
        rhs81 = (9 * pow(2, lam, 81) - 1 + 3 * z27) % 81
        assert (pow(2, ds, 81) * (2 * R - 5)) % 81 == rhs81
        candidates54 = [
            e for e in range(1, 55)
            if (pow(2, e, 81) * (2 * R - 5)) % 81 == rhs81
        ]
        assert candidates54 == [ds % 54 or 54]
        mod54_lifts += 1

        # Analytic theorem mirrored: nested terminal paths have H>=6.
        assert H >= 6
        nested_H6 += 1

        # Full-phase q=3 digit when the bounded full-phase denominator is positive.
        if q >= 0:
            n, s = max_sync_suffix(xw, yw)
            a_full = m + k + 1
            ell = r + 3
            M = (1 << a_full) - 3**ell
            if M > 0:
                v = (1, 1, 1) + yw + (0,) * (k - 2)
                Vpoly = qpoly(v)
                Y = 3**ell
                mod = 3 ** (s + 4)
                Nres = ((Vpoly + 4 * Y) % mod) * pow(M, -1, mod) % mod
                Ejs = (1 << bb[js]) * ((1 << delta[js]) - 1)
                Ep = (1 << bb[p]) * ((1 << delta[p]) - 1)
                Eq = (1 << bb[q]) * ((1 << delta[q]) - 1)
                C3 = Ejs + 3 * Ep + 9 * Eq
                want = (
                    2
                    - pow(2, 1 - k, mod)
                    - 4 * 3 ** (s + 1) * pow(2, -a_full, mod) * C3
                ) % mod
                assert Nres == want
                C2 = Ejs + 3 * Ep
                base2 = (
                    2
                    - pow(2, 1 - k, mod)
                    - 4 * 3 ** (s + 1) * pow(2, -a_full, mod) * C2
                ) % mod
                chi_q = delta[q] % 2
                correction = 0
                if chi_q:
                    correction = (
                        4 * pow(2, bb[q] - a_full, mod) * 3 ** (s + 3)
                    ) % mod
                assert Nres == (base2 - correction) % mod
                # State-side Q selector and phase-side chi_q agree.
                gamma_parity = 1 if Q == 1 else 0
                state_chi = ((aa[q] - bp) & 1) ^ gamma_parity
                assert state_chi == chi_q
                phase_rank3 += 1

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

print('RL69 third-backward-digit verifier: PASS')
print('bounded canonical terminal paths =', terminal)
print('nested g=0 terminal interfaces =', nested)
print('nested interfaces with rank q=p-1 present =', nested_with_q)
print('rank-before-p parity selector checks =', rank_before_p_parity)
print('full-phase q=3 digit matches =', phase_rank3)
print('nested delta_* mod-18 lifts =', mod18_lifts)
print('third backward T mod-9 checks =', third_backward)
print('nested delta_* mod-54 lifts =', mod54_lifts)
print('nested H>=6 checks =', nested_H6)
