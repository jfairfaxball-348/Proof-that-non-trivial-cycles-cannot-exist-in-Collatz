from fractions import Fraction

# Exact height-one synchronized positive 2-edge pump in J coordinates:
# J=3 --11--> 5 --00--> 3.
# A full forward pump multiplies g by 4/3 and contributes aligned zero mass (2/3)g_in.
for m in range(1,20):
    g0 = Fraction(7,20)
    g = g0
    mass = Fraction(0)
    J = 3
    for _ in range(m):
        assert J == 3
        J = (3*J+1)//2       # 11
        g *= Fraction(2,3)
        assert J == 5
        mass += g             # aligned 00 zero weight
        J = (J+1)//2          # 00
        g *= 2
    closed = 2*g0*(Fraction(4,3)**m - 1)
    assert J == 3
    assert g == g0*Fraction(4,3)**m
    assert mass == closed

print('J=3<->5 m-pump formula: PASS')
print('g_out = g_in*(4/3)^m')
print('aligned mass = 2*g_in*((4/3)^m-1)')
print('event increments per pump: Delta i=2, Delta p=1, Delta x-zero count=1')
