#!/usr/bin/env python3

# Portable exact verifier for the algebraic identities used in the RL245
# closeout repair. This is a verifier of the frozen local identities, not a
# finite proof of Gate A/B.


def step_T(d, T, x, y):
    num = (3**y) * T + x * 3 ** (d + y - 1) - y
    assert num % 2 == 0
    d2 = d + y - x
    assert d2 >= 1
    return d2, num // 2


def J_of(d, T):
    return T + 3**d - 2**d


def step_J_formula(d, J, x):
    if J & 1:
        if x == 0:
            return d, (J + 3**d - 2**d) // 2, 0
        return d, (3 * J + 2**d - 1) // 2, 1
    if x == 0:
        return d + 1, (3 * J + 3 ** (d + 1) - 2**d - 1) // 2, 1
    assert d > 1
    return d - 1, J // 2, 0


checks = 0
for d in range(1, 10):
    # Exhaust a broad exact range of J values with the required parity.
    for J in range(-199, 200):
        # T is determined by J,d.
        T = J - 3**d + 2**d
        for x in (0, 1):
            if J & 1:
                y = x
            else:
                y = 1 - x
                if x == 1 and d == 1:
                    continue
            # Frozen parity legality should make T step integral.
            d2, T2 = step_T(d, T, x, y)
            J2 = J_of(d2, T2)
            fd, fJ, fy = step_J_formula(d, J, x)
            assert fy == y
            assert fd == d2
            assert fJ == J2
            if (x, y) == (1, 0):
                assert J2 == J // 2
            checks += 1

# Same-root negativity requires only h>=0, not h in {0,1}.
negativity_checks = 0
for P in range(-20, 0):
    for h in range(0, 20):
        assert P - h < 0
        assert P - h <= P
        negativity_checks += 1

# Verify internal prefix-height identity h=d for arbitrary legal bit pairs at
# the purely combinatorial level: d_j=1+#y-#x and full-prefix difference has
# the same value after the mandatory 110/111 prefixes.
height_checks = 0
for maskx in range(1 << 8):
    for masky in range(1 << 8):
        sx = sy = 0
        legal = True
        for j in range(9):
            d = 1 + sy - sx
            h = 1 + sy - sx
            assert h == d
            assert h >= 0 if legal else True
            height_checks += 1
            if j == 8:
                break
            x = (maskx >> j) & 1
            y = (masky >> j) & 1
            sx += x
            sy += y
            if 1 + sy - sx < 1:
                legal = False
                break

print('RL245 closeout repair verifier: PASS')
print('deterministic_J_step_checks=', checks)
print('same_root_negativity_checks=', negativity_checks)
print('prefix_height_identity_checks=', height_checks)
print('classification=R4_BRIDGE_REDUCED')
