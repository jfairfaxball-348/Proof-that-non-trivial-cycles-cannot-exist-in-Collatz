from fractions import Fraction

g=Fraction(7,20)
J=3
A=Fraction(0)
CAP_ZERO=Fraction(17,30)
CAP_G=Fraction(17,15)
psi0=g*(J+1)/2
weights=[]
for c in range(4):
    # 11 at height one: J -> (3J+1)/2, g -> 2g/3, Psi unchanged.
    assert J%2==1
    J=(3*J+1)//2
    g*=Fraction(2,3)
    assert J==5
    # 00: J -> (J+1)/2, aligned zero of weight g, then g -> 2g.
    assert g < CAP_ZERO
    weights.append(g); A+=g
    J=(J+1)//2
    g*=2
    assert J==3
    assert g < CAP_G
psi1=g*(J+1)/2
assert A==Fraction(245,162)
assert A>Fraction(5,4)
assert psi1-psi0==A
assert psi0==Fraction(7,10)
assert psi1==Fraction(896,405)

# RL58 sharpened cut ceiling: inherited zeta squeeze + K>=25 + audited Zx_late>253/60.
delta=Fraction(199,53126622932283508654080)
psi_end_up=Fraction(27,4)*(1+delta)*(1+Fraction(1,2**25))
psi_cut_ceiling=psi_end_up-Fraction(253,60)
assert psi1 < psi_cut_ceiling

print('positive synchronized pump: PASS')
print('weights =', ', '.join(str(x) for x in weights))
print('aligned mass =', A, '=', float(A), '> 5/4')
print('g_out =', g, '=', float(g), '< 17/15')
print('Psi:', psi0, '->', psi1, '; below sharpened cut ceiling', psi_cut_ceiling, '=', float(psi_cut_ceiling))
print('Conclusion: cap + Psi cut + zero defect do not imply M0_late<=5/4; terminal/excursion arithmetic is essential.')
