#!/usr/bin/env python3
"""Exact bounded checks for the RL201 local coupled-strip translation theorem.

This verifies 168 local arithmetic witnesses: 2 actual-rank fixtures, 2 state
templates per fixture, 2 terminal signs, and every nu in 1..21. It also verifies
the affine identity symbolically over Fraction and an actual mechanical seam.
It does not enumerate physical cycles or certify global realization.
"""

from fractions import Fraction
import hashlib
import json

A = 217976794617
L = 137528045312
B = A - L
R = 2 * L - A
P = 65470613321
U0, REM = divmod(A * P, L)
T = 7 * 3**35
DELETIONS = {
    26058127773, 26058127774, 28746802249, 28746802250,
    31435476726, 34124151202, 36398517184, 36398517185,
    36812825678, 39087191660, 39087191661, 41775866136,
}


def bit(i):
    return A * (i + 1) // L - A * i // L


def eps(i):
    return A * (i + P) // L - A * i // L - U0


def valuation2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def endpoints(eta):
    return [2**34 * eta - 1, 2**34 * (eta + 21) - 1]


def reverse_row(row, aa):
    numerators = [2**a * y - 1 for a, y in zip(aa, row)]
    assert all(n % 3 == 0 for n in numerators)
    previous = [n // 3 for n in numerators]
    assert all(y > 0 and y % 2 == 1 and y % 3 for y in previous)
    assert all(valuation2(3 * x + 1) == a for x, a in zip(previous, aa))
    assert all((3 * x + 1) // 2**a == y for x, a, y in zip(previous, aa, row))
    return previous


def geometry(terminal_rank, depth):
    assert 25583192106 <= terminal_rank <= 41775866136
    assert terminal_rank not in DELETIONS
    start_rank = (terminal_rank - 34 * B) % L
    phase = P * start_rank % L
    assert phase * B % L == start_rank
    assert eps(phase) == 0
    local_time_labels = {(phase + sigma * P + t) % L
                         for sigma in (0, 1) for t in range(-depth, 35)}
    assert len(local_time_labels) == 2 * (depth + 35)
    cs = [(bit(phase - j), bit(phase + P - j)) for j in range(1, depth + 1)]
    carries = [eps(phase - j) for j in range(depth + 1)]
    assert cs[:3] == [(2, 2), (1, 1), (2, 2)]
    for j in range(depth + 1):
        q = (phase - j) * B % L
        assert carries[j] == int(q == L - 1)
        if j:
            assert cs[j - 1][0] == (1 if q < R else 2)
            assert cs[j - 1][1] == (1 if (q + 1) % L < R else 2)
        cm = sum(c[0] for c in cs[:j])
        cp = sum(c[1] for c in cs[:j])
        assert cp - cm == -carries[j]
    ht = 1
    for t in range(33):
        assert bit(phase + t) == bit(phase + P + t)
        ht += bit(phase + t) - 1
    assert ht == 20
    assert bit(phase + 33) == bit(phase + P + 33) == 2
    return phase, cs, carries


def make_state0_word(cs):
    """One deterministic jointly chosen witness, then the entire word is fixed."""
    eta = 18
    row = endpoints(eta)
    height = [1, 1]
    word = []
    for j, cc in enumerate(cs, 1):
        if j == 1:
            aa = (1, 1)
        elif j == 2:
            aa = (3, 2)
        else:
            # Choose one common offset q and an upper offset in {0,1}.
            # This is coupled construction; the subsequent theorem fixes aa.
            offset = int(row[0] % 3 != row[1] % 3)
            for q in range(1, 61):
                candidate = (q, q + offset)
                nums = [2**a * y - 1 for a, y in zip(candidate, row)]
                hh = [h + a - c for h, a, c in zip(height, candidate, cc)]
                if all(n % 3 == 0 and n % 9 for n in nums) and min(hh) >= 1:
                    aa = candidate
                    break
            else:
                raise AssertionError("No witness within declared q range 1..60")
        row = reverse_row(row, aa)
        height = [h + a - c for h, a, c in zip(height, aa, cc)]
        assert min(height) >= 0
        word.append(aa)
    return eta, word


def replay(eta, word, cs, carries):
    rows = [endpoints(eta)]
    heights = [[1, 1]]
    # Independently propagate the exact affine expressions Y=u*eta+v.
    affine = [[(Fraction(2**34), Fraction(-1)),
               (Fraction(2**34), Fraction(21 * 2**34 - 1))]]
    gaps = []
    numerators = []
    ordinary_coefficients = []
    cumulative_c = [0, 0]
    cumulative_a = [0, 0]
    for j in range(len(word) + 1):
        if j:
            aa, cc = word[j - 1], cs[j - 1]
            rows.append(reverse_row(rows[-1], aa))
            heights.append([h + a - c for h, a, c in zip(heights[-1], aa, cc)])
            affine.append([(u * Fraction(2**a, 3), (v * 2**a - 1) / 3)
                           for (u, v), a in zip(affine[-1], aa)])
            cumulative_c = [x + c for x, c in zip(cumulative_c, cc)]
            cumulative_a = [x + a for x, a in zip(cumulative_a, aa)]
        row, hh, aff = rows[-1], heights[-1], affine[-1]
        assert min(hh) >= 0
        assert all(y > 0 and y % 2 == 1 and y % 3 for y in row)
        assert all(u * eta + v == y for (u, v), y in zip(aff, row))
        assert hh == [1 + e - c for e, c in zip(cumulative_a, cumulative_c)]
        coeff = [u / 2**h for (u, _), h in zip(aff, hh)]
        assert coeff == [Fraction(2**(33 + c), 3**j) for c in cumulative_c]
        assert 2**carries[j] * coeff[1] - coeff[0] == 0
        ordinary_coefficients.append(coeff[1] - coeff[0])
        gap = 2**carries[j] * Fraction(row[1], 2**hh[1]) - Fraction(row[0], 2**hh[0])
        gap_aff = (2**carries[j] * aff[1][1] / 2**hh[1]
                   - aff[0][1] / 2**hh[0])
        assert gap == gap_aff and gap > 0
        numerator = gap * 2**max(hh)
        assert numerator.denominator == 1
        gaps.append(gap)
        numerators.append(numerator.numerator)
    return rows, heights, gaps, numerators, ordinary_coefficients


def terminal_check(eta, sign, nu):
    assert eta > 0 and eta % 9 in (0, 8)
    assert (eta % 2 == 0) == (sign == 1)
    params = [eta, eta + 21]
    for t in range(33):
        row = [2**(34 - t) * 3**t * s - 1 for s in params]
        nextrow = [2**(33 - t) * 3**(t + 1) * s - 1 for s in params]
        assert all(valuation2(3 * y + 1) == 1 for y in row)
        assert [(3 * y + 1) // 2 for y in row] == nextrow
    pre = [2 * 3**33 * s - 1 for s in params]
    aa = [valuation2(3 * y + 1) for y in pre]
    yy = [(3 * y + 1) // 2**a for y, a in zip(pre, aa)]
    hh = [22 - a for a in aa]
    assert min(hh) >= 0 and max(hh) == 21
    assert hh[0] - hh[1] == sign * nu
    assert sorted(aa) == [1, 1 + nu]
    numerator = 2**(21 - hh[1]) * yy[1] - 2**(21 - hh[0]) * yy[0]
    assert numerator == T


def spectrum_eta(eta0, depth, sign, nu):
    ternary_modulus = 3**(depth + 1)
    binary_modulus = 2**(nu + 1)
    odd_s = (pow(3**34, -1, binary_modulus) + 2**nu) % binary_modulus
    desired_eta = (odd_s - (21 if sign == 1 else 0)) % binary_modulus
    t = ((desired_eta - eta0) * pow(ternary_modulus, -1, binary_modulus)) % binary_modulus
    return eta0 + ternary_modulus * t


def verify_fixture(rank, depth):
    phase, cs, carries = geometry(rank, depth)
    eta0, word0 = make_state0_word(cs)
    base0 = replay(eta0, word0, cs, carries)
    assert base0[1][1] == [0, 0]
    assert base0[1][2] == [2, 1]
    # A second state template: a1 rises by one; each a2 falls by one.
    word1 = [(2, 2), tuple(a - 1 for a in word0[1])] + word0[2:]
    modulus = 3**(depth + 1)
    eta1 = eta0 + (-pow(2**36, -1, modulus)) % modulus
    assert eta1 % 9 == 8 and eta1 >= eta0
    base1 = replay(eta1, word1, cs, carries)
    assert base1[1][1] == [1, 1]
    assert base1[1][2:] == base0[1][2:]
    assert base1[2] == base0[2]
    assert base1[3][1] == 2 * base0[3][1]
    assert base1[3][2:] == base0[3][2:]
    witness_records = []
    for state, seed, word, base in [("011", eta0, word0, base0),
                                    ("111", eta1, word1, base1)]:
        # Both trajectories leading to the ordered tau34 labels have forced
        # even/odd source heights at tau36, independently of this state.
        assert base[1][2][0] % 2 == 0 and base[1][2][1] % 2 == 1
        for sign in (-1, 1):
            for nu in range(1, 22):
                eta = spectrum_eta(seed, depth, sign, nu)
                assert eta >= seed and (eta - seed) % modulus == 0
                assert eta % 9 == seed % 9
                result = replay(eta, word, cs, carries)
                assert result[1:] == base[1:]
                for j, (old, new) in enumerate(zip(base[0], result[0])):
                    for sigma in range(2):
                        esum = sum(aa[sigma] for aa in word[:j])
                        predicted = Fraction(2**(34 + esum) * (eta - seed), 3**j)
                        assert predicted.denominator == 1
                        assert new[sigma] - old[sigma] == predicted
                        assert (new[sigma] - old[sigma]) % 6 == 0
                terminal_check(eta, sign, nu)
                expected_class = {("011", 1): 0, ("111", 1): 8,
                                  ("011", -1): 9, ("111", -1): 17}[state, sign]
                assert eta % 18 == expected_class
                witness_records.append([state, sign, nu, eta])
    if rank == 31435476725:
        assert phase == 72057431995
        assert carries == [0, 0, 0, 0, 1, 0, 0]
        # Scope check: this is a local arithmetic seam regression. Its plus
        # layer4 is canonical phase0 but has height4, so it does NOT impose
        # the inherited global canonical anchor h_0=0.
        assert (phase + P - 4) % L == 0
        assert base0[1][4][1] == base1[1][4][1] == 4
        assert base0[4][4] != 0
        translated = replay(eta0 + modulus, word0, cs, carries)
        old_ordinary = (Fraction(base0[0][4][1], 2**base0[1][4][1])
                        - Fraction(base0[0][4][0], 2**base0[1][4][0]))
        new_ordinary = (Fraction(translated[0][4][1], 2**translated[1][4][1])
                        - Fraction(translated[0][4][0], 2**translated[1][4][0]))
        assert old_ordinary != new_ordinary
        assert base0[2] == translated[2]
    else:
        assert not any(carries)
        assert all(c == 0 for c in base0[4])
    digest = hashlib.sha256(json.dumps(witness_records, separators=(",", ":")).encode()).hexdigest()
    return {
        "terminal_rank": rank,
        "tau34_phase": phase,
        "depth": depth,
        "state0_eta_seed": eta0,
        "state1_eta_seed": eta1,
        "state0_exponents": word0,
        "mechanical_bits": cs,
        "carry_layers": [j for j, e in enumerate(carries) if e],
        "canonical_anchor_scope": (
            "local seam regression only: phase0 plus height4, not inherited h_0=0"
            if rank == 31435476725 else "no global anchor compatibility claimed"
        ),
        "max_local_height": max(h for hh in base0[1] for h in hh),
        "witness_count": len(witness_records),
        "witness_sha256": digest,
    }


def main():
    assert B == 80448749305 and R == 57079296007
    assert REM == 1 and U0 == 103768467013 and P * B % L == 1
    fixtures = [verify_fixture(30000000000, 16), verify_fixture(31435476725, 6)]
    assert sum(f["witness_count"] for f in fixtures) == 168
    print(json.dumps({
        "status": "PASS",
        "scope": "local coupled-strip arithmetic; no global realization",
        "terminal_spectrum": "2 signs x every nu in 1..21, per fixed state template",
        "fixtures": fixtures,
    }, indent=2))


if __name__ == "__main__":
    main()
