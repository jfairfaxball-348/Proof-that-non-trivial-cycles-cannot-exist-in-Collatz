from fractions import Fraction

# Inherited RL49/RL50 phase squeeze:
# zeta - 1 < (398/45)/2^71 = 199/53126622932283508654080.
delta = Fraction(199, 53126622932283508654080)
zeta_up = 1 + delta

# Terminal K is odd and K>=25.  At d=1,
# Psi_end = (27*zeta/4)*(1+2^-K), maximized by K=25 under this uniform zeta bound.
psi_end_up = Fraction(27,4) * zeta_up * (1 + Fraction(1,2**25))

# Independently audited RL58 total-prefix theorem gives
# Zx_late > 143/12 - 77/10 = 253/60.
zx_late_lb = Fraction(253,60)
psi_cut_up = psi_end_up - zx_late_lb

assert float(psi_end_up) < 6.750000202
assert float(psi_cut_up) < 2.533333535

print('sharp phase squeeze delta =', delta, '=', float(delta))
print('Psi_end <', psi_end_up, '=', float(psi_end_up))
print('Zx_late >', zx_late_lb, '=', float(zx_late_lb))
print('Psi_cut <', psi_cut_up, '=', float(psi_cut_up))
print('RL58 sharp Psi-cut consequence: PASS')
