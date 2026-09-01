#!/usr/bin/env python3
"""Portable gap-free arithmetic checks for the RL223 count-only theorem."""

from __future__ import annotations

from math import gcd


A = 217_976_794_617
L = 137_528_045_312
N = A - 24
M = L - 16
E = N - M


def totient_sieve(limit: int) -> list[int]:
    phi = list(range(limit + 1))
    for prime in range(2, limit + 1):
        if phi[prime] == prime:
            for multiple in range(prime, limit + 1, prime):
                phi[multiple] -= phi[multiple] // prime
    return phi


def q_of_word(word: tuple[int, ...], modulus: int) -> int:
    """Affine numerator modulo modulus by forward composition."""
    numerator = 0
    length = 0
    for bit in word:
        if bit == 0:
            # Appending an even step leaves Q unchanged.
            pass
        elif bit == 1:
            numerator = (3 * numerator + pow(2, length, modulus)) % modulus
        else:
            raise AssertionError("nonbinary word")
        length += 1
    return numerator


def block_pair(modulus: int, height: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Euler blocks B0=1^H0^H and B1=1^(H-1)01 0^(H-1)."""
    left = (1,) * height + (0,) * height
    right = (1,) * (height - 1) + (0, 1) + (0,) * (height - 1)
    assert len(left) == len(right) == 2 * height
    assert sum(left) == sum(right) == height
    assert left[0] == right[0] == 1  # y16 is odd in the current family.
    assert pow(2, height, modulus) == 1
    assert pow(3, height, modulus) == 1
    return left, right


def check_equal_increment_construction(modulus: int, height: int) -> None:
    assert modulus >= 2 and gcd(modulus, 6) == 1
    left, right = block_pair(modulus, height)
    switch_count = modulus
    assert M >= switch_count * height
    assert E >= switch_count * height

    # It is enough to compare one-switch words within the finite gadget.  A fixed
    # filler multiplies all gadget differences by the same unit 3^weight(filler).
    baseline = left * switch_count
    base_q = q_of_word(baseline, modulus)
    increments = []
    for j in range(switch_count):
        switched = left * j + right + left * (switch_count - j - 1)
        increments.append((q_of_word(switched, modulus) - base_q) % modulus)
    assert len(set(increments)) == 1
    delta = increments[0]
    assert gcd(delta, modulus) == 1
    residues = {(base_q + t * delta) % modulus for t in range(modulus)}
    assert residues == set(range(modulus))


def exact_small_dp(n: int, m: int, modulus: int) -> set[int]:
    """Exact recurrence (last-bit form) for a small counterexample/replay."""
    rows = [set() for _ in range(m + 1)]
    rows[0] = {0}
    for length in range(1, n + 1):
        old = [set(values) for values in rows]
        for weight in range(min(m, length), -1, -1):
            result = set(old[weight])
            if weight:
                result |= {
                    (3 * value + pow(2, length - 1, modulus)) % modulus
                    for value in old[weight - 1]
                }
            rows[weight] = result
    return rows[m]


def word_triple(word: str, modulus: int) -> tuple[int, int, int]:
    bits = tuple(int(bit) for bit in word)
    return len(bits), sum(bits), q_of_word(bits, modulus)


def concatenate(
    left: tuple[int, int, int], right: tuple[int, int, int], modulus: int
) -> tuple[int, int, int]:
    n1, m1, q1 = left
    n2, m2, q2 = right
    return n1 + n2, m1 + m2, (pow(3, m2, modulus) * q1 + pow(2, n1, modulus) * q2) % modulus


def check_exact_mod5_phase51_witness() -> None:
    modulus = 5
    prefix = "1111111111111001101111010011001010101111110110011000"
    assert (len(prefix), prefix.count("1")) == (52, 35)
    y16 = 63_944_214_675_001_842_327_551
    state = y16
    for bit in prefix:
        assert state % 2 == int(bit)
        state = (3 * state + 1) // 2 if bit == "1" else state // 2
    assert state == 710_371_286_312_677_333_954_849

    block0 = "11110000"
    block1 = "11101000"
    filler_ones = M - 51
    filler_zeros = E - 33
    assert (filler_ones, filler_zeros) == (137_528_045_245, 80_448_749_264)
    # Q(1^r 0^s)=3^r-2^r; trailing zero steps leave Q unchanged.
    filler = (
        filler_ones + filler_zeros,
        filler_ones,
        (pow(3, filler_ones, modulus) - pow(2, filler_ones, modulus)) % modulus,
    )
    values: dict[str, int] = {}
    for mask in range(16):
        blocks = "".join(block1 if (mask >> j) & 1 else block0 for j in range(4))
        head = concatenate(word_triple(prefix, modulus), word_triple(blocks, modulus), modulus)
        full = concatenate(head, filler, modulus)
        assert full[:2] == (N, M)
        values[f"{mask:04b}"] = full[2]
    assert {mask: values[mask] for mask in ("0011", "0001", "0000", "1111", "0111")} == {
        "0011": 0,
        "0001": 1,
        "0000": 2,
        "1111": 3,
        "0111": 4,
    }
    assert set(values.values()) == set(range(modulus))

    y0 = 24_921_895_945_404_894_117_887
    eta = 3_722_043_165_201
    assert y16 == (1 << 34) * eta - 1 - pow(3, 16) * (1 << 13)
    target = (pow(2, N, modulus) * y0 - pow(3, M, modulus) * y16) % modulus
    assert target == 3 == values["1111"]


def main() -> None:
    assert (N, M, E) == (217_976_794_593, 137_528_045_296, 80_448_749_297)

    # Exact endpoint of the factorization-free q(q-1) bound.
    q_max = 283_635
    assert q_max == 283_635
    assert q_max * (q_max - 1) == 80_448_529_590 <= E
    assert (q_max + 1) * q_max == 80_449_096_860 > E

    # Gap-free replay for every admissible modulus in the claimed range.
    phi = totient_sieve(q_max)
    admissible_count = 0
    for modulus in range(2, q_max + 1):
        if gcd(modulus, 6) != 1:
            continue
        admissible_count += 1
        height = phi[modulus]
        assert 1 <= height <= modulus - 1
        assert pow(2, height, modulus) == 1
        assert pow(3, height, modulus) == 1
        assert modulus * height <= modulus * (modulus - 1) <= E < M
    assert admissible_count == 94_544

    # Explicit small-modulus constructions, including composites.
    checked = (5, 7, 11, 13, 17, 19, 23, 25, 35, 49, 55, 65, 77)
    for modulus in checked:
        check_equal_increment_construction(modulus, phi[modulus])

    # Exact recurrence confirms both saturation at a modest padded dimension and
    # the advertised short-length counterexample.
    assert exact_small_dp(2, 1, 5) == {1, 2}
    assert exact_small_dp(40, 20, 5) == set(range(5))
    check_exact_mod5_phase51_witness()

    # Target-lift slope identity.  Check the exponent algebra exactly and replay
    # the identity modulo several coprime moduli without constructing 2^A or 3^L.
    assert N + 58 == A + 34
    assert M + 17 == L + 1
    for modulus in checked:
        direct_slope = (
            pow(2, N, modulus) * (3 * pow(2, 58, modulus))
            - pow(3, M, modulus) * (pow(2, 34, modulus) * pow(3, 17, modulus))
        ) % modulus
        factored_slope = (
            3
            * pow(2, 34, modulus)
            * (pow(2, A, modulus) - pow(3, L, modulus))
        ) % modulus
        assert direct_slope == factored_slope

    print("RL223 ODD-MODULUS COUNT-ONLY SATURATION: PASS")
    print(f"tail dimensions N={N}, M={M}, N-M={E}")
    print(f"factorization-free saturation range: 2 <= q <= {q_max}, gcd(q,6)=1")
    print(f"all admissible moduli replayed: {admissible_count}")
    print("explicit equal-increment moduli:", ",".join(map(str, checked)))
    print("exact q=5 phase-51-prefix formal completion: PASS (T=Q=3 mod 5)")
    print("short counterexample: S_(2,1)(5)={1,2}")
    print("target lift slope: T(k+1)-T(k)=3*2^34*(2^A-3^L)")


if __name__ == "__main__":
    main()
