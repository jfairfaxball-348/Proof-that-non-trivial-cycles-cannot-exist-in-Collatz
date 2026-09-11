#!/usr/bin/env python3
"""RL298 exact selector / physical frontier verifier.

Fast mode replays the exact integer selector scan and all frozen arithmetic
envelope assertions.  --spot-physical checks named physical witnesses.
--full-physical replays the finite physical stopping certificate through the
frozen maximum quotient ceiling; it is intentionally expensive and may be
sharded with --h-start/--h-stop.
"""

from __future__ import annotations
from math import gcd
import argparse

A_LIMIT = 301_994
FIRST_ENVELOPE_A = 100_000
EXPECTED_SELECTOR_COUNT_100K = 2_648
EXPECTED_SELECTOR_COUNT_ALL = 8_057
EXPECTED_MAX_NSTAR_100K = 803_113
EXPECTED_MAX_NSTAR_ALL = 136_073_747
EXPECTED_MAX_STOP_100K = 291
EXPECTED_MAX_STOP_ALL = 588

EXPECTED_FIRST_EIGHT = [
    (1100,694,406,317,200,14,4),
    (1119,706,413,802,506,14,10),
    (1287,812,475,485,306,16,6),
    (1417,894,523,317,200,18,4),
    (1436,906,530,1119,706,18,14),
    (1753,1106,647,1436,906,22,18),
    (1772,1118,654,485,306,22,6),
    (1921,1212,709,802,506,24,10),
]
EXPECTED_LAST = (301994,190537,111457,50508,31867,3725,623)

def min_x_for_mass(b: int) -> int:
    x = 1
    while (x*x)//4 < b+2:
        x += 1
    return x

def capacity_a_min(b: int) -> int:
    return 3*b + min_x_for_mass(b) - 1

def det_solutions(a: int, ell: int):
    g = gcd(a, ell)
    if 2 % g:
        return []
    aa, ll, rhs = a//g, ell//g, -2//g
    q0 = (rhs * pow(ll, -1, aa)) % aa
    out = []
    for j in range(g):
        q = q0 + j*aa
        if 0 < q < a:
            r = (q*ell + 2)//a
            if a*r - q*ell == 2:
                out.append((q,r))
    return out

def exact_selector_scan(limit=A_LIMIT):
    out = []
    p2 = 1
    p4 = 1
    ell = 0
    p3 = 1
    p9 = 1

    for a in range(1, limit+1):
        p2 <<= 1
        p4 *= 4

        # ell = max{e : 3^e < 2^a}
        while p3*3 < p2:
            p3 *= 3
            p9 *= 9
            ell += 1

        emin = (147*a + 232)//233
        emax = (12*a - 1)//19
        if not (emin <= ell <= emax):
            continue
        if not (p2 > p3 and 15*p4 < 16*p9):
            continue

        z = a-ell
        for q,r in det_solutions(a,ell):
            B = q-r
            H = 19*z - 7*a
            n = 19*B - 7*q
            if H <= 0:
                continue

            halving = (H % 2 == 0 and n % 2 == 0)
            bmin = 260 if halving else 356
            if z < bmin+27 or a < capacity_a_min(bmin):
                continue
            if not halving and a - 36*H < 1068:
                continue

            # Exact determinant-coordinate identities.
            assert B*H - z*n == 14
            assert q*H - a*n == 38
            assert r*H - ell*n == 24

            kmax = z+2
            if kmax % 2 == 0:
                kmax -= 1
            assert kmax >= 31

            rho = ell-3
            M = p2-p3
            top = 237*(p3//27) - (1 << (a-kmax+1))
            nstar = top//M + 2

            out.append((a,ell,z,q,r,H,n,kmax,nstar))
    return out

def half_step(n: int) -> int:
    return n//2 if n % 2 == 0 else (3*n+1)//2

def stopping_steps(n: int, cap: int = 100_000) -> int:
    for s in range(cap+1):
        if n == 1:
            return s
        n = half_step(n)
    raise AssertionError("cap exhausted")

def physical_pair(N: int):
    assert N % 24 == 19
    A0 = (9*N+5)//8
    B0 = (27*N+127)//8
    return A0,B0

def fast_arithmetic_checks():
    sels = exact_selector_scan()
    assert len(sels) == EXPECTED_SELECTOR_COUNT_ALL

    bare = [x[:7] for x in sels]
    assert bare[:8] == EXPECTED_FIRST_EIGHT
    assert bare[-1] == EXPECTED_LAST
    assert all(x[0] < 1436 for x in sels[:4])
    assert not any(1418 <= x[0] < 1436 for x in sels)

    s100 = [x for x in sels if x[0] <= FIRST_ENVELOPE_A]
    post = [x for x in sels if FIRST_ENVELOPE_A < x[0] <= A_LIMIT]
    assert len(s100) == EXPECTED_SELECTOR_COUNT_100K
    assert len(post) == 5_409

    max100 = max(s100, key=lambda x: x[-1])
    maxall = max(sels, key=lambda x: x[-1])
    assert max100[-1] == EXPECTED_MAX_NSTAR_100K
    assert max100[:7] == (75235,47468,27767,25781,16266,928,318)
    assert maxall[-1] == EXPECTED_MAX_NSTAR_ALL
    assert maxall[:7] == EXPECTED_LAST

    def excess(x):
        a,ell = x[0],x[1]
        rho = ell-3
        mmax = a-32
        return 2*rho-mmax

    assert min(excess(x) for x in s100) == 314
    assert min(excess(x) for x in post) == 26_214

    fifth = sels[4]
    assert fifth[:7] == (1436,906,530,1119,706,18,14)
    assert fifth[-1] == 525

    print("selector_count_100k", len(s100))
    print("selector_count_all", len(sels))
    print("max_nstar_100k", max100[-1], max100[:7])
    print("max_nstar_all", maxall[-1], maxall[:7])
    print("min_excess_100k", min(excess(x) for x in s100))
    print("min_excess_post100k", min(excess(x) for x in post))
    print("FAST_ARITHMETIC_GREEN")

def spot_physical_checks():
    # Historical extremal from the <=803113 envelope.
    N = 767_899
    A0,B0 = physical_pair(N)
    assert stopping_steps(A0) == 69
    assert stopping_steps(B0) == 291

    # Fifth selector strongest exact longest-horizon one-count witness.
    N = 91
    A0,B0 = physical_pair(N)
    m = 1436-32
    def odd_count(n, steps):
        c = 0
        for _ in range(steps):
            c += n & 1
            n = half_step(n)
        return c
    assert odd_count(A0,m) == 705
    assert odd_count(B0,m) == 705
    print("SPOT_PHYSICAL_GREEN")

def full_physical(h_start: int, h_stop: int):
    """Replay a shard of N=19+24h through the frozen largest envelope.

    Each h checks both physical starts.  The full frozen range is
    h=0..5_669_738 inclusive.  The asserted global maximum 588 is obtained
    only when the entire range is replayed.
    """
    assert 0 <= h_start <= h_stop <= 5_669_739
    local_max = 0
    local_h = None
    local_side = None
    for h in range(h_start,h_stop):
        N = 19 + 24*h
        A0,B0 = physical_pair(N)
        sa = stopping_steps(A0, EXPECTED_MAX_STOP_ALL)
        sb = stopping_steps(B0, EXPECTED_MAX_STOP_ALL)
        if sa > local_max:
            local_max,local_h,local_side = sa,h,"A"
        if sb > local_max:
            local_max,local_h,local_side = sb,h,"B"
    print("physical_shard", h_start, h_stop, "max_stop", local_max,
          "at_h", local_h, "side", local_side)
    return local_max

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spot-physical", action="store_true")
    ap.add_argument("--full-physical", action="store_true")
    ap.add_argument("--h-start", type=int, default=0)
    ap.add_argument("--h-stop", type=int, default=5_669_739)
    args = ap.parse_args()

    fast_arithmetic_checks()
    if args.spot_physical:
        spot_physical_checks()
    if args.full_physical:
        m = full_physical(args.h_start,args.h_stop)
        if args.h_start == 0 and args.h_stop == 5_669_739:
            assert m == EXPECTED_MAX_STOP_ALL
            print("FULL_PHYSICAL_GREEN")

if __name__ == "__main__":
    main()
