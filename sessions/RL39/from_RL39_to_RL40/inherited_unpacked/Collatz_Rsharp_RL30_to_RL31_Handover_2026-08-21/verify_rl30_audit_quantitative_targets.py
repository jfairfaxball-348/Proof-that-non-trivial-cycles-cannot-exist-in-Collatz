from fractions import Fraction
from decimal import Decimal, getcontext
from math import log

# Exact quarter-margin arithmetic.
c0 = Fraction(457841,1843200)
delta = Fraction(1,4) - c0
assert delta == Fraction(2959,1843200)
assert c0 < Fraction(1,4)

# Next-CF-gate scale quoted in the inherited RL23/RL24 notes.
# This is not an RL contradiction threshold; it is only the coefficient
# that would push a simple Legendre window through the next denominator.
getcontext().prec = 50
R0 = Decimal(2) ** 71
qnext = Decimal(65470613321)
ln2 = Decimal(2).ln()
c_cf = R0 * ln2 / (Decimal(2) * qnext * qnext)
c0d = Decimal(c0.numerator) / Decimal(c0.denominator)
assert Decimal('0.19090') < c_cf < Decimal('0.19092')
assert c0d - c_cf > Decimal('0.05748')

# In the order-3 branch L=3e, a coefficient improvement dc corresponds
# asymptotically to an extra log-product saving 3*dc*e/R.
quarter_saving = Decimal(3) * (Decimal(delta.numerator)/Decimal(delta.denominator))
cf_saving = Decimal(3) * (c0d-c_cf)

# Best-case normalized saving of replacing an odd state at R by one at 2.9R.
kappa = Decimal('2.9')
per_high_odd = (Decimal(1)/Decimal(3))*(Decimal(1)-Decimal(1)/kappa)

print('RL30 quantitative audit verifier: PASS')
print('c0 =', c0d)
print('1/4-c0 =', Decimal(delta.numerator)/Decimal(delta.denominator))
print('next-CF gate coefficient ~=', c_cf)
print('current-to-next-CF delta ~=', c0d-c_cf)
print('order3 extra log-saving to erase quarter margin ~=', quarter_saving, '* e/R')
print('order3 extra log-saving to next CF gate ~=', cf_saving, '* e/R')
print('best-case normalized saving per odd phase moved R -> 2.9R ~=', per_high_odd)
