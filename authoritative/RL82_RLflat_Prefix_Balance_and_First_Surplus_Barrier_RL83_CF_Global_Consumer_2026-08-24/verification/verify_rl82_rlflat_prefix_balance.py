#!/usr/bin/env python3
"""Fast exact audit for RL82 RL-flat maximum-state results.

The analytic proofs live in the RL82 mathematics note.  This verifier is a
transcription/algebra guard.  It checks:

1. the inherited top triple and mod-54 split;
2. the new one-layer mod-162 sharpening;
3. the general affine backward-word recurrence for all O/E words through a
   bounded depth;
4. the exact fixed-(i,o) maximum of the additive numerator B_i;
5. the prefix-balanced/unbounded-cylinder criterion on bounded words;
6. the all-O immortal cylinder for many depths and parameters;
7. the complete-cycle denominator/max-rotation identities on bounded words.

No bounded loop below is presented as an infinite proof.
"""

from itertools import product
from math import gcd

TOP_CHECKS = 0
MOD162_CHECKS = 0
WORD_CHECKS = 0
BMAX_CHECKS = 0
BALANCED_CHECKS = 0
ALLODD_CHECKS = 0
CYCLE_IDENTITY_CHECKS = 0


def inv_step(x, symbol):
    if symbol == "E":
        return 2 * x
    assert symbol == "O"
    assert x % 3 == 2
    y = (2 * x - 1) // 3
    assert y > 0 and y % 2 == 1
    return y


def word_data(word):
    b = 0
    o = 0
    out = []
    for i, ch in enumerate(word, start=1):
        if ch == "E":
            b = 2 * b
        elif ch == "O":
            b = 2 * b + 3**o
            o += 1
        else:
            raise ValueError(ch)
        out.append((i, o, b))
    return out


def residue_for_word(word):
    data = word_data(word)
    if not data:
        return 0, 1
    d, o, b = data[-1]
    mod = 3**o
    if mod == 1:
        return 0, 1
    inv = pow(2**d, -1, mod)
    return (b * inv) % mod, mod


def execute(word, M):
    x = M
    xs = []
    for ch in word:
        x = inv_step(x, ch)
        xs.append(x)
    return xs


# ---------------------------------------------------------------------------
# 1. Inherited seed and 2. new mod-162 sharpening.
# ---------------------------------------------------------------------------
for r in range(0, 5000):
    M = 18 * r + 8
    P = 12 * r + 5
    Q = 8 * r + 3
    assert (3 * P + 1) // 2 == M
    assert (3 * Q + 1) // 2 == P
    assert M % 2 == 0 and P % 2 == 1 and Q % 2 == 1
    TOP_CHECKS += 5

    # One-step extendability at Q gives r != 0 mod 3.
    even_q = 2 * Q
    odd_q_ok = (2 * Q - 1) % 3 == 0
    even_q_extendable = (even_q % 3 == 2)  # even_q > M/2, so only odd pred can extend it
    assert odd_q_ok == (r % 3 == 1)
    assert even_q_extendable == (r % 3 == 2)
    if r % 3 == 0:
        assert not odd_q_ok and not even_q_extendable
    TOP_CHECKS += 3

# New exact case split.  We audit the algebra over many s/t values and also
# compare with a direct bounded predecessor-tree existence test.
def preds(M, x):
    out = []
    if 2 * x <= M:
        out.append(2 * x)
    if x % 3 == 2:
        y = (2 * x - 1) // 3
        if y > 0 and y % 2 == 1:
            out.append(y)
    return out


def has_backward_path(M, depth):
    frontier = {M}
    for _ in range(depth):
        nxt = set()
        for x in frontier:
            nxt.update(preds(M, x))
        frontier = nxt
        if not frontier:
            return False
    return True

# For any genuine cycle of period >=5, five predecessor layers exist.  The
# analytic note separately excludes positive nontrivial periods <=4.
seen_mod162 = set()
for M in range(8, 1000, 2):
    if has_backward_path(M, 5):
        # Restrict to candidates having the universal two-odd top geometry.
        Pnum = 2 * M - 1
        if Pnum % 3:
            continue
        P = Pnum // 3
        if P <= 1 or P % 2 == 0:
            continue
        Qnum = 2 * P - 1
        if Qnum % 3:
            continue
        Q = Qnum // 3
        if Q % 2 == 0:
            continue
        seen_mod162.add(M % 162)
        assert M % 162 in {26, 80, 152}
        MOD162_CHECKS += 1
assert seen_mod162 == {26, 80, 152}

# Direct algebra for the two seed branches.
for s in range(0, 5000):
    # Branch A: r=3s+1, M=54s+26, actual x3 is odd R=16s+7.
    M = 54 * s + 26
    R = 16 * s + 7
    assert R <= M and R % 2 == 1
    E = 2 * R
    O_ok = (R % 3 == 2)
    assert O_ok == (s % 3 == 1)
    assert E > M / 2 and E <= M
    E_extendable = (E % 3 == 2)
    assert E_extendable == (s % 3 == 0)
    # s=2 mod3 has neither an odd predecessor of R nor an extendable even one.
    if s % 3 == 2:
        assert not O_ok and not E_extendable
    else:
        assert M % 162 in {26, 80}
    MOD162_CHECKS += 7

    # Branch B: r=3s+2, M=54s+44.  x3 is even, x4 forced odd,
    # and x4 lies above M/2, so x5 forced odd; this requires s=2 mod3.
    M2 = 54 * s + 44
    R2 = 48 * s + 38
    S2 = 32 * s + 25
    assert R2 > M2 / 2 and R2 <= M2
    assert R2 % 3 == 2
    assert (2 * R2 - 1) // 3 == S2
    assert S2 > M2 / 2 and S2 <= M2
    can_extend = (S2 % 3 == 2)
    assert can_extend == (s % 3 == 2)
    if can_extend:
        assert M2 % 162 == 152
    MOD162_CHECKS += 7


# ---------------------------------------------------------------------------
# 3. General affine word formula and unique 3-adic cylinder.
# ---------------------------------------------------------------------------
MAX_DEPTH = 9
for d in range(1, MAX_DEPTH + 1):
    for tup in product("OE", repeat=d):
        w = "".join(tup)
        data = word_data(w)
        i, o, b = data[-1]
        r, mod = residue_for_word(w)

        # Final congruence implies every earlier odd inverse is integral.
        # Pick a large even representative in the cylinder.
        # Because mod is odd, adding mod toggles parity.
        M = r
        if M <= 0:
            M += mod
        while M < 10**7:
            M += mod
        if M % 2:
            M += mod
        assert M % mod == r

        x = M
        o_running = 0
        b_running = 0
        for j, ch in enumerate(w, start=1):
            if ch == "E":
                b_running = 2 * b_running
                x2 = 2 * x
            else:
                # Congruence selected by the full word must make this legal.
                assert x % 3 == 2
                x2 = (2 * x - 1) // 3
                assert x2 % 2 == 1
                b_running = 2 * b_running + 3**o_running
                o_running += 1
            assert x2 == (2**j * M - b_running) // (3**o_running)
            assert (2**j * M - b_running) % (3**o_running) == 0
            x = x2
            WORD_CHECKS += 3

        assert o_running == o and b_running == b
        assert (2**d * M - b) % (3**o) == 0
        WORD_CHECKS += 2


# ---------------------------------------------------------------------------
# 4. Exact fixed-(i,o) maximum B_i: all O's before all E's.
# ---------------------------------------------------------------------------
for i in range(1, 11):
    by_o = {}
    for tup in product("OE", repeat=i):
        w = "".join(tup)
        _, o, b = word_data(w)[-1]
        by_o.setdefault(o, []).append(b)
    for o, vals in by_o.items():
        e = i - o
        if o == 0:
            expected = 0
        else:
            expected = 2**e * (3**o - 2**o)
        assert max(vals) == expected
        BMAX_CHECKS += len(vals)


# ---------------------------------------------------------------------------
# 5. Prefix-balanced criterion: if 2^i <= 3^{o_i} at every prefix,
# ceiling is automatic; if a positive defect occurs, M is bounded above.
# ---------------------------------------------------------------------------
for d in range(1, 9):
    for tup in product("OE", repeat=d):
        w = "".join(tup)
        data = word_data(w)
        r, mod = residue_for_word(w)
        balanced = all(2**i <= 3**o for i, o, _ in data)
        positive_bounds = [b / (2**i - 3**o)
                           for i, o, b in data if 2**i > 3**o]
        if balanced:
            # Take two arbitrarily separated large even representatives.
            for jump in (10**5, 10**8):
                M = r + mod * jump
                if M % 2:
                    M += mod
                xs = execute(w, M)
                assert all(0 < x <= M for x in xs)
                BALANCED_CHECKS += len(xs)
        else:
            assert positive_bounds
            U = min(positive_bounds)
            # Any legal representative above U must violate the ceiling at
            # at least one surplus prefix.
            M = r
            if M <= U + 1000:
                k = int((U + 1000 - M) // mod) + 1
                M += k * mod
            if M % 2:
                M += mod
            # Execute arithmetically; ceiling failure is what matters.
            xs = execute(w, M)
            assert any(x > M for x in xs)
            BALANCED_CHECKS += len(xs)


# ---------------------------------------------------------------------------
# 6. All-O immortal cylinder.
# ---------------------------------------------------------------------------
for d in range(1, 40):
    for q in (1, 3, 5, 17, 101):  # odd q -> even M
        M = 3**d * q - 1
        assert M % 2 == 0
        x = M
        for i in range(1, d + 1):
            assert x % 3 == 2
            x = (2 * x - 1) // 3
            expected = 2**i * 3**(d - i) * q - 1
            assert x == expected
            assert x > 0 and x < M and x % 2 == 1
            ALLODD_CHECKS += 5


# ---------------------------------------------------------------------------
# 7. Complete-cycle denominator and max-rotation inequalities.
# We check the algebra on every bounded word with positive denominator and on
# those formal words for which M=B/D is a positive integer.
# ---------------------------------------------------------------------------
for d in range(2, 10):
    for tup in product("OE", repeat=d):
        w = "".join(tup)
        data = word_data(w)
        _, ell, B = data[-1]
        if ell == 0:
            continue
        D = 2**d - 3**ell
        if D <= 0:
            continue
        if B % D:
            continue
        M = B // D
        if M <= 0:
            continue
        # Formal closure identity.
        assert (2**d - 3**ell) * M == B
        # If the word is actually legal from M, verify exact return and the
        # prefix maximum inequalities algebraically.
        r, mod = residue_for_word(w)
        if M % mod != r:
            continue
        try:
            xs = execute(w, M)
        except AssertionError:
            continue
        assert xs[-1] == M
        for i, o, b in data[:-1]:
            lhs = (2**i - 3**o) * B
            rhs = b * D
            assert (xs[i-1] <= M) == (lhs <= rhs)
            CYCLE_IDENTITY_CHECKS += 1


# ---------------------------------------------------------------------------
# 8. External-floor fixed-count frontier: conditional on inherited R#>=2^71.
# ---------------------------------------------------------------------------
FLOOR = 2**71
FLOOR_PAIR_CHECKS = 0
for i in range(1, 184):
    for o in range(0, i + 1):
        D = 2**i - 3**o
        if D <= 0:
            continue
        e = i - o
        Bmax = 0 if o == 0 else 2**e * (3**o - 2**o)
        # U(i,o)=Bmax/D is strictly below the inherited floor.
        assert Bmax < FLOOR * D
        FLOOR_PAIR_CHECKS += 1
# The coarse count envelope first fails at depth 184 for (o,e)=(116,68).
i, o = 184, 116
e = i - o
D = 2**i - 3**o
Bmax = 2**e * (3**o - 2**o)
assert Bmax > FLOOR * D

# ---------------------------------------------------------------------------
# 9. Critical minimal-density balanced word and its mod-162 seed.
# ---------------------------------------------------------------------------
critical = []
oprev = 0
for i in range(1, 31):
    oi = 0
    while 3**oi < 2**i:
        oi += 1
    critical.append("O" if oi > oprev else "E")
    oprev = oi
critical_word = "".join(critical)
assert critical_word.startswith("OOEOOEOOEOEOO")
for d in range(1, 31):
    pref = critical_word[:d]
    data = word_data(pref)
    assert all(2**ii <= 3**oo for ii, oo, _ in data)
assert critical_word[:5] == "OOEOO"
r5, mod5 = residue_for_word(critical_word[:5])
# Convert the mod-81 cylinder to its even class mod 162.
even5 = r5 if r5 % 2 == 0 else r5 + mod5
assert mod5 == 81 and even5 % 162 == 152

# ---------------------------------------------------------------------------
# 10. Exact capped-surplus red-team witness M=890.
# ---------------------------------------------------------------------------
WITNESS_WORD = "OOOOEOOOEOOEOEOOOOEEOOEEOEE"
WITNESS_STATES = [
    593, 395, 263, 175, 350, 233, 155, 103, 206, 137, 91, 182,
    121, 242, 161, 107, 71, 47, 94, 188, 125, 83, 166, 332, 221,
    442, 884,
]
assert len(WITNESS_WORD) == 27 and WITNESS_WORD.count("O") == 17
assert 2**27 > 3**17
assert execute(WITNESS_WORD, 890) == WITNESS_STATES
assert max(WITNESS_STATES) < 890
wi, wo, wb = word_data(WITNESS_WORD)[-1]
assert (2**wi * 890 - wb) // 3**wo == 884

print("RL82 RL-flat prefix-balance verifier: PASS")
print(f"top seed checks = {TOP_CHECKS}")
print(f"mod-162 sharpening checks = {MOD162_CHECKS}")
print(f"affine word/cylinder checks = {WORD_CHECKS}")
print(f"fixed-count B-max checks = {BMAX_CHECKS}")
print(f"prefix-balanced/bounded-cylinder checks = {BALANCED_CHECKS}")
print(f"all-O immortal-ray checks = {ALLODD_CHECKS}")
print(f"formal complete-cycle/max-rotation checks = {CYCLE_IDENTITY_CHECKS}")
print(f"external-floor prefix-pair checks (i<=183) = {FLOOR_PAIR_CHECKS}")
print("critical balanced prefix[1:13] = OOEOOEOOEOEOO")
print("exact capped-surplus witness = M=890, depth=27, odd-count=17")
print("necessary maximum residues mod 162 = {26, 80, 152}")
