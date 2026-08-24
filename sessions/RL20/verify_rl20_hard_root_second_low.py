from fractions import Fraction

R0 = 1 << 71

# theta=log2(3/2).  A plateau (s,t) contributes multiplicative slope factor
# 2^t/(3/2)^s to lambda=2^A/3^L.
def slope_factor(s, t):
    return Fraction(2**(s+t), 3**s)

root = slope_factor(2, 1)   # hard root departure
close = slope_factor(1, 1)  # n_close=t_close=1 forces s_close=1, mu_close=0
pair = root * close
assert root == Fraction(8, 9)
assert close == Fraction(4, 3)
assert pair == Fraction(32, 27)

# If every other plateau is non-low, its factor is >=1, so lambda>=32/27.
# Under RL20 packing:
# log lambda <= 1/(3R)+(1/9)log(1+3(L-1)/R), hence
# L >= 1 + R/3*(lambda^9*exp(-3/R)-1).
# For R>=2^71 and lambda>=32/27, use exp(-x)>1-x and prove exactly that
# (32/27)^9*(1-3/R0) > 23/5.  Then L>1+6R/5.
x = Fraction(32, 27)**9 * Fraction(R0 - 3, R0)
assert x > Fraction(23, 5)

# The older near-resonant threshold 16/15 is strictly below 32/27.
assert Fraction(16, 15) < Fraction(32, 27)

print('RL20 hard-root second-low verifier: PASS')
print('root factor =', root)
print('universal close factor =', close)
print('root*close =', pair)
print('(32/27)^9*(1-3/2^71) > 23/5 =', x > Fraction(23,5))
print('conditional huge branch: lambda >=32/27 => L > 1 + 6R#/5')
print('otherwise an additional plateau with 2^(s+t) < 3^s is necessary')
