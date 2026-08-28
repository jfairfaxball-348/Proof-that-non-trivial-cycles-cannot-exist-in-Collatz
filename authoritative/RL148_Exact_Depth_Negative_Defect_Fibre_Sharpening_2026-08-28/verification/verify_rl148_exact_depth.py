#!/usr/bin/env python3
"""Fast exact sanity checks for RL148 fixed-depth entry/exit congruences."""
checked = 0
for d in range(1, 20):
    modulus = 2 ** (d + 2)
    entries = []
    for y in range(3, 1000, 4):
        z, e = 2 ** d * y, (3 * y + 1) // 2
        assert z % modulus == (3 * 2 ** d) % modulus
        assert e % 3 == 2
        assert 3 * z + 2 ** d == 2 ** (d + 1) * e
        entries.append(z); checked += 1
    assert all(right-left >= modulus for left, right in zip(entries, entries[1:]))
assert checked > 1000
print("RL148 fast verifier: PASS")
print("checked exact-depth entry/exit instances =", checked)
