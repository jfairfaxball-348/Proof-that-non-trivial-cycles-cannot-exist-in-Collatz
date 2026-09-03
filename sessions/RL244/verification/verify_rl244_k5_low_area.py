#!/usr/bin/env python3
"""
RL244 exact low-area k=5 terminal certificate.

This is an exhaustive finite-state certificate, not a bounded-depth scan.
It replays the frozen RL67 exact recurrence, prunes only H>=5 (irrelevant to
a hypothetical k=5 Gate-A survivor H<k), and proves that the complete state
set repeats before any terminal (d,J,H)=(1,32,H<5) occurs.
"""


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


states = {(1, -14, 0)}
seen = {}
depth = 0
checked_states = 0

while True:
    key = tuple(sorted(states))
    if key in seen:
        first = seen[key]
        period = depth - first
        assert first == 13
        assert depth == 16
        assert period == 3
        assert len(states) == 47
        print("RL244 k=5 low-area automaton certificate: PASS")
        print(f"first_repeat_depth={first}")
        print(f"repeat_depth={depth}")
        print(f"period={period}")
        print(f"repeated_state_count={len(states)}")
        print(f"checked_state_occurrences={checked_states}")
        print("target=(d=1,J=32,H<5): absent for all depths")
        break

    seen[key] = depth

    for d, T, H in states:
        checked_states += 1
        assert H <= 4
        J = J_of(d, T)
        assert not (d == 1 and J == 32)

    nxt = set()
    for d, T, H in states:
        J = J_of(d, T)
        options = ((0, 0), (1, 1)) if (J & 1) else ((0, 1), (1, 0))
        for x, y in options:
            if (x, y) == (1, 0) and d <= 1:
                continue
            out = rl_step(d, T, H, x, y)
            if out is None:
                continue
            if out[2] <= 4:
                nxt.add(out)

    states = nxt
    depth += 1
