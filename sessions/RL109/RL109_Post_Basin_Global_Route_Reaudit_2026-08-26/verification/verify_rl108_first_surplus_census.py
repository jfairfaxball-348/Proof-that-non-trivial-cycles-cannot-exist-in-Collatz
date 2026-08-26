#!/usr/bin/env python3
"""Gap-free RL108 first-surplus census for 1 <= odd count O <= 19.

Enumerates every balanced first-surplus inverse word, computes its exact least
positive even 3-adic cylinder representative, applies the terminal maximum cap,
and reconstructs every capped trajectory.  No interrupted RL107 enumeration is
used.
"""

EXPECTED = {
    1: (2, 1, 1),
    2: (4, 1, 0),
    3: (5, 2, 0),
    4: (7, 3, 0),
    5: (8, 7, 0),
    6: (10, 12, 0),
    7: (12, 30, 0),
    8: (13, 85, 0),
    9: (15, 173, 0),
    10: (16, 476, 0),
    11: (18, 961, 0),
    12: (20, 2652, 0),
    13: (21, 8045, 0),
    14: (23, 17637, 0),
    15: (24, 51033, 0),
    16: (26, 108950, 0),
    17: (27, 312455, 5),
    18: (29, 663535, 0),
    19: (31, 1900470, 0),
}

EXPECTED_17 = {
    "111101110110101111001100100": (890, 884, 6),
    "111101110110101111001110000": (890, 880, 10),
    "111101110110101111101000010": (890, 874, 16),
    "111101110110101111101001000": (890, 872, 18),
    "111101110110101111101100000": (890, 864, 26),
}


def first_surplus_length(O: int) -> int:
    n = 1
    target = 3 ** O
    while 2 ** n <= target:
        n += 1
    assert 2 ** (n - 1) <= target < 2 ** n
    return n


def least_even_rep(B: int, N: int, O: int) -> int:
    mod3 = 3 ** O
    r = (B * pow(pow(2, N, mod3), -1, mod3)) % mod3
    if r == 0:
        return 2 * mod3
    return r if r % 2 == 0 else r + mod3


def reconstruct(word: str, M: int, O: int):
    x = M
    o = 0
    B = 0
    states = []
    N = len(word)
    for i, c in enumerate(word, 1):
        if c == "0":
            x *= 2
            B *= 2
        else:
            num = 2 * x - 1
            assert num % 3 == 0
            x = num // 3
            B = 2 * B + 3 ** o
            o += 1
        assert 0 < x <= M
        if i < N:
            assert 2 ** i <= 3 ** o
        states.append(x)
    assert o == O
    assert 2 ** N > 3 ** O
    assert 2 ** N * M - B == 3 ** O * x
    return states[-1], B


def census(O: int):
    N = first_surplus_length(O)
    total = 0
    capped = []

    # Final first-surplus symbol is E=0, so enumerate the N-1 balanced prefix.
    def dfs(i: int, o: int, B: int, word: str):
        nonlocal total
        if i == N - 1:
            if o != O:
                return
            word_final = word + "0"
            B_final = 2 * B
            total += 1
            M = least_even_rep(B_final, N, O)
            D = 2 ** N - 3 ** O
            if D * M <= B_final:
                end, B_check = reconstruct(word_final, M, O)
                assert B_check == B_final
                slack = B_final - D * M
                assert slack == 3 ** O * (M - end)
                capped.append((word_final, M, end, M - end))
            return

        remaining = (N - 1) - i
        need = O - o
        if need < 0 or need > remaining:
            return
        j = i + 1

        if need > 0:
            new_o = o + 1
            if 2 ** j <= 3 ** new_o:
                dfs(i + 1, new_o, 2 * B + 3 ** o, word + "1")

        if remaining - 1 >= need and 2 ** j <= 3 ** o:
            dfs(i + 1, o, 2 * B, word + "0")

    dfs(0, 0, 0, "")
    return N, total, capped


grand_total = 0
grand_capped = 0
for O in range(1, 20):
    N, total, capped = census(O)
    exp_N, exp_total, exp_capped = EXPECTED[O]
    assert (N, total, len(capped)) == (exp_N, exp_total, exp_capped)
    grand_total += total
    grand_capped += len(capped)

    if O == 1:
        assert capped == [("10", 2, 2, 0)]
    elif O == 17:
        got = {w: (M, end, gap) for w, M, end, gap in capped}
        assert got == EXPECTED_17
        for _, M, _, _ in capped:
            assert M % 162 == 80
            assert M & (M - 1) != 0
    else:
        assert not capped

assert grand_total == 3_066_528
assert grand_capped == 6

print("RL108 first-surplus census verifier: PASS")
print("balanced words checked =", grand_total)
print("capped least-cylinder realizations =", grand_capped)
print("nontrivial capped words = 5, common M = 890")
