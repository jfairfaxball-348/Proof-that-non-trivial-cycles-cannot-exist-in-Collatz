#!/usr/bin/env python3
from itertools import product


def Q(bits):
    L, seen, out = sum(bits), 0, 0
    for p, b in enumerate(bits):
        if b:
            out += 2 ** p * 3 ** (L - 1 - seen)
            seen += 1
    return out


def D(bits):
    return 2 ** len(bits) - 3 ** sum(bits)


checked = bound_checked = divisible_checked = 0
for A in range(2, 13):
    for bits in product((0, 1), repeat=A):
        L, Z = sum(bits), A - sum(bits)
        if L == 0 or Z == 0:
            continue
        d, q = D(bits), Q(bits)
        b0, rotated = bits[0], bits[1:] + bits[:1]
        qr = Q(rotated)
        if b0 == 0:
            assert 2 * qr == q
        else:
            assert 2 * qr == 3 * q + d
        checked += 1
        if bits[0] == 1 and bits[-1] == 0:
            assert q <= 2 ** (Z - 1) * (3 ** L - 2 ** L)
            bound_checked += 1
        if d > 0 and q % d == 0:
            n, nr = q // d, qr // d
            if b0 == 0:
                assert n % 2 == 0 and nr == n // 2
            else:
                assert n % 2 == 1 and nr == (3 * n + 1) // 2
            divisible_checked += 1

print('RL130 rotation/bound red-team: PASS')
print(f'rotation_words_checked={checked}')
print(f'transition_root_bounds_checked={bound_checked}')
print(f'exact_divisible_rotation_events_checked={divisible_checked}')
