#!/usr/bin/env python3
"""RL292 first-positive analytic over-approximation through H<=26.

Purpose
-------
Close the residual terminal exponent k=27 without enumerating the full negative
fixed-seed ancestry tree.

Analytic inputs (promoted before RL292):
1. RL288 first-positive theorem. At the first state with J>0, with
      M = J + 2^d - 2,  A = H + d - 1,
   one has 0 < M < 3^d and nu_2(M) <= A, with equality only at
   (d,J,H)=(3,2,1).
2. RL281 mod-3 reachability invariant: J mod 3 lies in {0, (-1)^d}.
3. The depth-area lower bound used in RL288:
      A >= d(d-1)/2,
   hence H >= (d-1)(d-2)/2 at any first-positive state of depth d.
4. RL279 positive forward invariance: once J>0, every legal future has J>0.

Construction
------------
Enumerate EVERY physical first-positive state allowed by those necessary
conditions at its smallest analytically permitted height. This is a strict
over-approximation of the genuine fixed-seed first-positive set. Then close all
legal positive futures by minimum height through H=26.

Shortest-path dominance is exact: transitions depend only on (d,J) and every
edge adds d-1 >= 0, so a larger-height duplicate of the same physical state can
never improve a future minimum-height query.

If (1,2^27) is absent even from this relaxed closure through H=26, then no
genuine k=27 Gate-A violator exists, because H<27 implies H<=26.
"""
from collections import deque

R = 26
INF = 10**18
TARGET = (1, 2**27)


def v2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def step(d, J, x):
    K = J + 2**d - 1
    if K % 2 == 0:
        if x == 1:
            d2, K2 = d, 3*K//2
        else:
            d2, K2 = d, (K + 3**d - 1)//2
    else:
        if x == 1:
            if d <= 1:
                return None
            d2, K2 = d-1, (K-1)//2
        else:
            d2, K2 = d+1, 3*(K + 3**d)//2
    J2 = K2 - 2**d2 + 1
    return d2, J2, d-1


def first_positive_relaxed_seeds():
    seeds = {}
    # H<=26 and H >= (d-1)(d-2)/2 force d<=8.
    for d in range(1, 9):
        eps = 1 if d % 2 == 0 else 2  # (-1)^d mod 3
        maxJ = 3**d - 2**d + 1       # M<3^d, J integer
        area_floor = (d-1)*(d-2)//2
        for J in range(1, maxJ+1):
            if J % 3 not in (0, eps):
                continue
            M = J + 2**d - 2
            t = v2(M)
            # nu_2(M) <= H+d-1.
            Hmin = max(area_floor, t-d+1)
            # Equality is globally unique at (d,J,H)=(3,2,1).
            if not (d == 3 and J == 2 and Hmin == 1):
                Hmin = max(Hmin, t-d+2)
            Hmin = max(Hmin, 0)
            if Hmin <= R:
                seeds[(d,J)] = min(seeds.get((d,J), INF), Hmin)
    return seeds


def relaxed_positive_closure(seeds):
    dist = dict(seeds)
    buckets = [deque() for _ in range(R+1)]
    for state, H in seeds.items():
        buckets[H].append(state)

    processed = 0
    power_minima = {}
    for H in range(R+1):
        q = buckets[H]
        while q:
            d, J = q.popleft()
            if dist.get((d,J)) != H:
                continue
            processed += 1
            assert J > 0
            if d == 1 and J > 0 and (J & (J-1)) == 0:
                k = J.bit_length()-1
                power_minima[k] = min(power_minima.get(k, INF), H)
            for x in (0,1):
                out = step(d,J,x)
                if out is None:
                    continue
                d2,J2,dh = out
                H2 = H + dh
                if H2 > R:
                    continue
                # Promoted positive-forward-invariance theorem.
                assert J2 > 0
                s2 = (d2,J2)
                if H2 < dist.get(s2, INF):
                    dist[s2] = H2
                    buckets[H2].append(s2)
    return dist, processed, power_minima


def main():
    seeds = first_positive_relaxed_seeds()
    assert len(seeds) == 6224, len(seeds)

    dist, processed, powers = relaxed_positive_closure(seeds)

    assert processed == len(dist)
    assert len(dist) == 11_380_217, len(dist)
    assert TARGET not in dist
    assert 27 not in powers

    expected_powers = {
        1:2, 3:2, 5:8, 7:14, 9:14, 11:17,
        13:17, 15:21, 17:24, 19:25, 21:23,
    }
    assert powers == expected_powers, powers

    # In particular the relaxed closure also has no k=23 or k=25 terminal
    # through H=26, consistent with / stronger than the earlier finite checks.
    assert 23 not in powers and 25 not in powers

    print('RL292 first-positive analytic over-approx H<=26: PASS')
    print(f'height_cap={R}')
    print(f'relaxed_first_positive_seed_states={len(seeds)}')
    print(f'relaxed_positive_physical_states={len(dist)}')
    print('relaxed_power_minima=' + ','.join(
        f'k{k}:H{powers[k]}' for k in sorted(powers)
    ))
    print('k27_checkpoint_under_H26=ABSENT')
    print('proof_logic=every genuine trajectory has a first-positive state contained in relaxed seeds; positive future closure is exhaustive by shortest-path dominance')
    print('classification_candidate=FIRST_POSITIVE_ANALYTIC_OVERAPPROX_H26_K27_GATE_A_CLOSURE')
    print('new_residual_candidate=odd k>=29 with H_can<k')


if __name__ == '__main__':
    main()
