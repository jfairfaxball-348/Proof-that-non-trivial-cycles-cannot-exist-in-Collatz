#!/usr/bin/env python3
"""Exact RL282 H<=22 positive-checkpoint certificate.

This verifier uses only the normalized (d,J,H) recurrence. It has no J cutoff
and no arbitrary word-length cutoff.

Completeness:
* Nonpositive phase: exhaustive BFS over all legal transitions with H<=22,
  stopping a branch at its first positive d=1 state.
* Positive phase: positive even d=1 states are checkpoints. From each,
  exhaustively enumerate every first return to d=1 within the remaining height.
  After the launch, d>=2 until first return, so every interior step adds at
  least one unit of height; the height cap makes each search finite.
* Positive odd d=1 returns are quotiented exactly: one boundary branch exits
  to an even checkpoint and the other stays odd. Follow the unique stay-odd
  branch until an odd state repeats, collecting every even exit. No orbit/J
  cutoff is used for the certified result.

The output asserts the exact state counts and the power-of-two height minima
used to close odd terminal exponents k=5,...,23.
"""
from collections import deque, defaultdict
from functools import lru_cache

R = 22

def k_step(d, K, x):
    if K % 2 == 0:
        if x == 1:
            return d, 3 * K // 2
        return d, (K + 3 ** d - 1) // 2
    if x == 1:
        if d <= 1:
            return None
        return d - 1, (K - 1) // 2
    return d + 1, 3 * (K + 3 ** d) // 2

def step_JH(d, J, H, x):
    K = J + 2 ** d - 1
    st = k_step(d, K, x)
    if st is None:
        return None
    d2, K2 = st
    J2 = K2 - 2 ** d2 + 1
    return d2, J2, H + d - 1

def nonpositive_phase():
    start = (1, -13, 0)
    q = deque([start])
    seen = {start}
    first_positive = defaultdict(set)
    edge_count = 0

    while q:
        d, J, H = q.popleft()
        for x in (0, 1):
            st = step_JH(d, J, H, x)
            if st is None:
                continue
            d2, J2, H2 = st
            if H2 > R:
                continue
            edge_count += 1
            if d2 == 1 and J2 > 0:
                first_positive[H2].add(J2)
                continue
            if st not in seen:
                seen.add(st)
                q.append(st)

    return len(seen), first_positive, edge_count

def boundary_exits(J):
    assert J > 0 and J % 2 == 1
    seen = set()
    exits = set()
    cur = J

    while cur not in seen:
        seen.add(cur)
        j0 = (cur + 1) // 2
        j1 = (3 * cur + 1) // 2

        even = [v for v in (j0, j1) if v % 2 == 0]
        odd = [v for v in (j0, j1) if v % 2 == 1]
        assert len(even) == len(odd) == 1

        exits.add(even[0])
        cur = odd[0]

    return tuple(sorted(exits)), len(seen)

def launch_even_checkpoint(J):
    st = step_JH(1, J, 0, 0)
    assert st is not None and st[0] == 2 and st[2] == 0
    return st[0], st[1]

@lru_cache(maxsize=None)
def first_returns(J, remaining_height):
    d0, J0 = launch_even_checkpoint(J)
    stack = [(d0, J0, 0)]
    seen = {(d0, J0, 0)}
    out = set()

    while stack:
        d, curJ, added = stack.pop()
        assert d >= 2
        for x in (0, 1):
            st = step_JH(d, curJ, added, x)
            if st is None:
                continue
            d2, J2, added2 = st
            if added2 > remaining_height:
                continue
            if d2 == 1:
                out.add((J2, added2))
            else:
                key = (d2, J2, added2)
                if key not in seen:
                    seen.add(key)
                    stack.append(key)

    return tuple(sorted(out))

def positive_phase(first_positive):
    checkpoints = set()
    q = deque()
    odd_cache = {}
    max_trace = 0

    def add_boundary_state(J, H):
        nonlocal max_trace
        assert J > 0
        if J % 2 == 0:
            key = (J, H)
            if key not in checkpoints:
                checkpoints.add(key)
                q.append(key)
            return

        if J not in odd_cache:
            odd_cache[J] = boundary_exits(J)
            max_trace = max(max_trace, odd_cache[J][1])

        for even_exit in odd_cache[J][0]:
            key = (even_exit, H)
            if key not in checkpoints:
                checkpoints.add(key)
                q.append(key)

    for H, values in first_positive.items():
        for J in values:
            add_boundary_state(J, H)

    while q:
        J, H = q.popleft()
        remaining = R - H
        for Jret, added in first_returns(J, remaining):
            H2 = H + added
            assert Jret > 0
            add_boundary_state(Jret, H2)

    return checkpoints, odd_cache, max_trace

def main():
    nonpos_count, first_positive, nonpos_edges = nonpositive_phase()

    assert nonpos_count == 3_254_996, nonpos_count
    assert sum(len(v) for v in first_positive.values()) == 169
    assert nonpos_edges == 3_813_525, nonpos_edges

    checkpoints, odd_cache, max_trace = positive_phase(first_positive)

    assert len(checkpoints) == 146_341, len(checkpoints)
    assert len(odd_cache) == 13_583, len(odd_cache)
    assert max_trace == 263, max_trace

    minima = {}
    for J, H in checkpoints:
        if J > 0 and (J & (J - 1)) == 0:
            k = J.bit_length() - 1
            minima[k] = min(minima.get(k, 10**9), H)

    expected_minima = {
        1: 3,
        3: 3,
        5: 9,
        7: 15,
        9: 15,
        11: 18,
        13: 18,
        15: 22,
    }
    assert minima == expected_minima, minima

    safe = []
    for k in range(5, 24, 2):
        if k in minima:
            assert minima[k] >= k
        else:
            assert not any(J == 2**k for J, H in checkpoints)
        safe.append(k)

    print("RL282 H<=22 exact positive-checkpoint certificate: PASS")
    print(f"height_cap={R}")
    print(f"nonpositive_states={nonpos_count}")
    print(f"nonpositive_edges={nonpos_edges}")
    print(f"first_positive_entries={sum(len(v) for v in first_positive.values())}")
    print(f"positive_even_checkpoints={len(checkpoints)}")
    print(f"odd_boundary_origins={len(odd_cache)}")
    print(f"max_stay_odd_trace={max_trace}")
    print("power_of_two_minima=" + ",".join(
        f"k{k}:H{minima[k]}" for k in sorted(minima)
    ))
    print("certified_gate_A_safe_odd_k=" + ",".join(map(str, safe)))
    print("certified_residual=odd k>=25 with H_can<k")

if __name__ == "__main__":
    main()
