from fractions import Fraction

ROOT_CLASSES = [7,43,55,79,91,127]
HARD_CLASSES = [43,91]

# In the inherited k=0 branch R# mod9 is 1 or 7.
for c in ROOT_CLASSES:
    assert c % 9 in (1,7)

# For n_close=1, physical-state compatibility gives 2^t R == 2 (mod9).
# Enumerate one period of odd t modulo 6.
solutions = {}
for r in (1,7):
    good = [t for t in range(1,7,2) if ((1 << t) * r - 2) % 9 == 0]
    assert len(good) == 1
    solutions[r] = good[0] % 6
assert solutions == {1:1, 7:3}

# Hard root s=2,t_exit=1 means R# == 11 mod16; among inherited classes this
# leaves exactly 43 and 91 mod144.
assert [c for c in ROOT_CLASSES if c % 16 == 11] == HARD_CLASSES
assert 43 % 9 == 7 and 91 % 9 == 1
assert solutions[43 % 9] == 3
assert solutions[91 % 9] == 1

# Therefore t_close=1 occurs only in the 91 mod144 hard class.
exceptional = [c for c in HARD_CLASSES if solutions[c % 9] == 1]
assert exceptional == [91]

# Outside the exception, every hard-root close has t_close>=3, so
# e_close = 1-2^{-t} >= 7/8.
for t in (3,5,7,9):
    e = Fraction((1 << t) - 1, 1 << t)
    assert e >= Fraction(7,8)

print('RL20 final-return phase-compatibility verifier: PASS')
print('n_close=1 address: R mod9=1 -> t=1 mod6; R mod9=7 -> t=3 mod6')
print('hard-root classes mod144 =', HARD_CLASSES)
print('unique t_close=1 hard class mod144 =', exceptional[0])
