#!/usr/bin/env python3
"""RL292 exact minimum-height certificate through H<=24.

Purpose: close the residual terminal exponent k=25 by proving that the physical
checkpoint J=2^25 has minimum canonical height >24 (indeed it is absent from
the exact closure at height <=24).

This is a shortest-path/minimum-height certificate, not a count of all histories.
Dominance lemma: future transitions depend only on (d,J), every edge has
nonnegative height cost d-1, so among two histories reaching the same physical
state only the smaller height can matter for any future minimum-height query.
"""
from functools import lru_cache
import heapq

R = 24
INF = 10**18


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
    return d2, K2 - 2**d2 + 1, d-1


def upstream_minima():
    start = (1, -13)
    dist = {start: 0}
    buckets = [__import__('collections').deque() for _ in range(R+1)]
    buckets[0].append(start)
    first_d1_positive = {}
    for H in range(R+1):
      q = buckets[H]
      while q:
        d, J = q.popleft()
        if H != dist[(d, J)]:
            continue
        for x in (0, 1):
            out = step(d, J, x)
            if out is None:
                continue
            d2, J2, dh = out
            H2 = H + dh
            if H2 > R:
                continue
            if d2 == 1 and J2 > 0:
                if H2 < first_d1_positive.get(J2, INF):
                    first_d1_positive[J2] = H2
                continue
            s2 = (d2, J2)
            if H2 < dist.get(s2, INF):
                dist[s2] = H2
                buckets[H2].append(s2)
    return dist, first_d1_positive


def boundary_exits(J):
    assert J > 0 and J % 2 == 1
    seen = set()
    exits = set()
    cur = J
    while cur not in seen:
        seen.add(cur)
        j0 = (cur + 1)//2
        j1 = (3*cur + 1)//2
        if j0 % 2 == 0:
            exits.add(j0)
            cur = j1
        else:
            exits.add(j1)
            cur = j0
    return tuple(sorted(exits)), len(seen)


@lru_cache(maxsize=None)
def first_returns(J, remaining):
    launch = step(1, J, 0)
    assert launch is not None and launch[0] == 2 and launch[2] == 0
    stack = [(launch[0], launch[1], 0)]
    seen = {(launch[0], launch[1], 0)}
    out = set()
    while stack:
        d, curJ, added = stack.pop()
        assert d >= 2
        for x in (0, 1):
            nxt = step(d, curJ, x)
            if nxt is None:
                continue
            d2, J2, dh = nxt
            a2 = added + dh
            if a2 > remaining:
                continue
            if d2 == 1:
                out.add((J2, a2))
            else:
                key = (d2, J2, a2)
                if key not in seen:
                    seen.add(key)
                    stack.append(key)
    return tuple(sorted(out))


def positive_minima(first):
    dist = {}
    pq = []
    odd_cache = {}

    def add_boundary(J, H):
        if J % 2 == 0:
            if H < dist.get(J, INF):
                dist[J] = H
                heapq.heappush(pq, (H, J))
            return
        if J not in odd_cache:
            odd_cache[J] = boundary_exits(J)
        for even_exit in odd_cache[J][0]:
            if H < dist.get(even_exit, INF):
                dist[even_exit] = H
                heapq.heappush(pq, (H, even_exit))

    for J, H in first.items():
        add_boundary(J, H)

    while pq:
        H, J = heapq.heappop(pq)
        if H != dist[J]:
            continue
        rem = R - H
        for Jret, added in first_returns(J, rem):
            add_boundary(Jret, H + added)

    return dist, odd_cache


def power_minima(dist, cap):
    out = {}
    for J, H in dist.items():
        if H <= cap and J > 0 and (J & (J-1)) == 0:
            k = J.bit_length() - 1
            out[k] = min(out.get(k, INF), H)
    return out


def main():
    upstream, first = upstream_minima()
    checkpoints, odd_cache = positive_minima(first)

    # Independent regression against the promoted RL282 H<=22 power minima.
    expected22 = {
        1: 3, 3: 3, 5: 9, 7: 15, 9: 15, 11: 18, 13: 18, 15: 22
    }
    got22 = power_minima(checkpoints, 22)
    assert got22 == expected22, (got22, expected22)

    expected24 = {
        1: 3, 3: 3, 5: 9, 7: 15, 9: 15, 11: 18, 13: 18,
        15: 22, 21: 24
    }
    got24 = power_minima(checkpoints, 24)
    assert got24 == expected24, (got24, expected24)

    assert 2**25 not in checkpoints
    assert 25 not in got24

    first_expected = {
        2:3, 3:3, 5:6, 6:10, 12:10, 14:13, 15:13, 39:13,
        9:15, 23:15, 24:15, 66:15, 8:16, 32:16, 20:18,
        11:21, 41:21, 42:22, 30:24,
    }
    assert first == first_expected, first

    max_trace = max(n for _, n in odd_cache.values())
    assert len(upstream) == 7_396_469, len(upstream)
    assert len(first) == 19, len(first)
    assert len(checkpoints) == 320_762, len(checkpoints)
    assert len(odd_cache) == 58_132, len(odd_cache)
    assert max_trace == 356, max_trace
    assert sum(1 for H in checkpoints.values() if H <= 22) == 75_232

    print('RL292 exact minimum-height H<=24 certificate: PASS')
    print(f'height_cap={R}')
    print(f'upstream_min_physical_states={len(upstream)}')
    print(f'first_positive_d1_min_states={len(first)}')
    print(f'positive_even_min_checkpoints={len(checkpoints)}')
    print(f'positive_even_min_checkpoints_H22={sum(1 for H in checkpoints.values() if H <= 22)}')
    print(f'odd_boundary_origins={len(odd_cache)}')
    print(f'max_stay_odd_trace={max_trace}')
    print('power_minima_H22=' + ','.join(f'k{k}:H{got22[k]}' for k in sorted(got22)))
    print('power_minima_H24=' + ','.join(f'k{k}:H{got24[k]}' for k in sorted(got24)))
    print('k25_checkpoint_under_H24=ABSENT')
    print('classification_candidate=EXACT_MINIMUM_HEIGHT_H24_K25_GATE_A_CLOSURE')
    print('new_residual_candidate=odd k>=27 with H_can<k')


if __name__ == '__main__':
    main()
