#!/usr/bin/env python3
"""Complete small checks supplementing QUOTIENT_MODULE_THEOREM.md; no global conclusion."""

from itertools import product
from math import gcd
import json


def matmul(left, right):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*right)] for row in left]


def matvec(matrix, vector):
    return [sum(x * y for x, y in zip(row, vector)) for row in matrix]


def determinant(matrix):
    """Fraction-free elimination; every division is checked."""
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign, old_pivot = 1, 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % old_pivot == 0
                a[i][j] = numerator // old_pivot
            a[i][k] = 0
        old_pivot = pivot
    return sign * a[-1][-1]


def bezout(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    assert old_s * a + old_t * b == old_r
    return old_r, old_s, old_t


def raw_q(bits):
    weight, prefix, q = sum(bits), 0, 0
    for i, bit in enumerate(bits):
        if bit:
            q += (2 ** i) * (3 ** (weight - 1 - prefix))
        prefix += bit
    return q


def matrices(bits):
    n = len(bits)
    a = [3 ** bit for bit in bits]
    b = [[0] * n for _ in range(n)]
    numerator = [[0] * n for _ in range(n)]
    for i in range(n):
        b[i][i] = -a[i]
        b[i][(i + 1) % n] = 2
        for k in range(n):
            coefficient = 2 ** k
            for h in range(k + 1, n):
                coefficient *= a[(i + h) % n]
            numerator[i][(i + k) % n] = coefficient
    return a, b, numerator


def check_unimodular_reduction(b, c, modulus):
    n = len(b)
    alpha, beta = c[0], c[-1]
    g, u, v = bezout(alpha, beta)
    assert g == 1
    u_matrix = [[0] * n for _ in range(n)]
    u_matrix[0][0], u_matrix[-1][0] = u, v
    for j in range(1, n - 1):
        u_matrix[j][j] = 1
        u_matrix[0][j] = -c[j] * u
        u_matrix[-1][j] = -c[j] * v
    u_matrix[0][-1], u_matrix[-1][-1] = -beta, alpha
    assert determinant(u_matrix) == 1
    assert matmul([c], u_matrix) == [[1] + [0] * (n - 1)]
    w = [[0] * n for _ in range(n)]
    w[0][0] = 1
    for i in range(1, n - 1):
        w[i] = b[i][:]
    w[-1] = [-v * b[0][j] + u * b[-1][j] for j in range(n)]
    assert abs(determinant(w)) == 1
    sw = [row[:] for row in w]
    sw[0] = [modulus * value for value in sw[0]]
    assert matmul(u_matrix, sw) == b


def main():
    counts = {
        "matrix_words_A_2_to_9": 0,
        "annihilator_word_modulus_pairs_A_2_to_4_M_1_to_9": 0,
        "annihilator_coefficient_vectors": 0,
        "kernel_forcings_A_2_to_5_entries_minus1_to_1": 0,
        "quotient_residue_exceptions_D_gt_1": 0,
    }
    for n in range(2, 10):
        for bits in product((0, 1), repeat=n):
            weight = sum(bits)
            modulus = 2 ** n - 3 ** weight
            if not (0 < weight < n and modulus > 0):
                continue
            counts["matrix_words_A_2_to_9"] += 1
            a, b, numerator = matrices(bits)
            c = numerator[0]
            expected = [[modulus * int(i == j) for j in range(n)] for i in range(n)]
            assert matmul(b, numerator) == expected
            assert matmul(numerator, b) == expected
            assert determinant(b) == ((-1) ** (n - 1)) * modulus
            assert gcd(modulus, 6) == 1
            assert c[-1] == 2 ** (n - 1)
            check_unimodular_reduction(b, c, modulus)

            # Two coprime maximal proper minors independently check the invariant factors.
            first_minor = determinant([row[1:] for row in b[:-1]])
            second_minor = determinant([row[:-1] for row in b[:-1]])
            assert first_minor == 2 ** (n - 1)
            assert second_minor == ((-1) ** (n - 1)) * 3 ** (weight - bits[-1])
            assert gcd(first_minor, second_minor) == 1

            q_rotations = [raw_q(bits[i:] + bits[:i]) for i in range(n)]
            assert matvec(numerator, bits) == q_rotations
            assert q_rotations[0] == sum(x * y for x, y in zip(c, bits))
            g = gcd(modulus, q_rotations[0])
            increment = modulus // g
            assert all(value % g == 0 for value in q_rotations)
            scaled_states = [value // g for value in q_rotations]
            assert matvec(b, scaled_states) == [increment * bit for bit in bits]

            if modulus > 1:
                # The image vector B e_0 has zero charge mod D but quotient residue one.
                f = [row[0] for row in b]
                charge = sum(x * y for x, y in zip(c, f))
                assert charge == modulus and charge % modulus == 0
                assert (charge // modulus) % modulus == 1
                counts["quotient_residue_exceptions_D_gt_1"] += 1

            if n <= 5:
                for f in product((-1, 0, 1), repeat=n):
                    charges = matvec(numerator, f)
                    assert (charges[0] % modulus == 0) == all(
                        charge % modulus == 0 for charge in charges
                    )
                    if charges[0] % modulus == 0:
                        x = [charge // modulus for charge in charges]
                        assert matvec(b, x) == list(f)
                    counts["kernel_forcings_A_2_to_5_entries_minus1_to_1"] += 1

            if n <= 4:
                for m in range(1, 10):
                    expected_annihilators = {
                        tuple(t * value % m for value in c)
                        for t in range(m)
                        if (modulus * t) % m == 0
                    }
                    found = set()
                    for coefficient in product(range(m), repeat=n):
                        if all(
                            (2 * coefficient[(j - 1) % n] - a[j] * coefficient[j]) % m == 0
                            for j in range(n)
                        ):
                            found.add(coefficient)
                        counts["annihilator_coefficient_vectors"] += 1
                    assert found == expected_annihilators
                    assert len(found) == gcd(modulus, m)
                    for t in range(m):
                        if (modulus * t) % m != 0:
                            continue
                        effective = m // gcd(m, t)
                        assert gcd(modulus, m) % effective == 0
                        assert ((t * raw_q(bits)) % m == 0) == (raw_q(bits) % effective == 0)
                    counts["annihilator_word_modulus_pairs_A_2_to_4_M_1_to_9"] += 1

    proper_factor_bits = (1, 1, 0, 0, 0, 0)
    assert raw_q(proper_factor_bits) == 5
    assert 2 ** 6 - 3 ** 2 == 55
    assert raw_q(proper_factor_bits) % 5 == 0
    assert raw_q(proper_factor_bits) % 55 != 0
    print(json.dumps({"status": "PASS", "scope": "exact finite verification at declared ranges", **counts}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
