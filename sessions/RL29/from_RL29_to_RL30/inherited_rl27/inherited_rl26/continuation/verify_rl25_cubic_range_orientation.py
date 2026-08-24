from fractions import Fraction
from itertools import combinations
import sympy as sp

R,t=sp.symbols('R t', positive=True)
C=(27*R+19)/(27*R)
T=256*R/(256*R-319)
J=sp.factor(T**3/C**5)
CH=sp.factor((4*(C-1)+sp.Rational(151,200)*(J-1))/(12-sp.Rational(9,2)*(J-1)))


def shifted_positive(expr,shift=161):
    num,den=sp.fraction(sp.together(expr))
    pn=sp.Poly(sp.expand(num.subs(R,t+shift)),t)
    pd=sp.Poly(sp.expand(den.subs(R,t+shift)),t)
    return (all(c>=0 for c in pn.all_coeffs()) and any(c>0 for c in pn.all_coeffs())
            and all(c>0 for c in pd.all_coeffs()))

# RL24 majorant is strictly below 1/(4R) on R>=161.
assert shifted_positive(sp.Rational(1,4)-R*CH)

# Near-resonant cube-root cap z<(46/45).
assert 46**3 * 15 > 45**3 * 16

# Fixed-weight Q floor sanity: Q >= 3^e-2^e, equality at 1^e 0^(b-e).
def Qword(bits):
    e=sum(bits); p=0; q=0
    for i,bit in enumerate(bits):
        if bit:
            q += (1<<i)*3**(e-1-p)
            p += 1
    return q

for b in range(2,11):
    for e in range(1,b):
        qmin=3**e-2**e
        vals=[]
        for pos in combinations(range(b),e):
            bits=[0]*b
            for i in pos: bits[i]=1
            vals.append(Qword(bits))
        assert min(vals)==qmin

# Orientation-specific and residue-specific cubic lattice lower bounds.
# Set B>Y in representative exact pairs and brute a generous primitive box.
for b,e in [(65,41),(149,94),(214,135)]:
    B=1<<b; Y=3**e
    assert B>Y
    for N in range(1,40):
        for K in range(1,40):
            if N==K: continue
            mod3=(N%3==0 or K%3==0 or (N-K)%3==0)
            if not mod3: continue
            a=Y*K+B*N
            c=(B+Y)*K-Y*N
            if K>N: # H>G
                assert max(abs(a),abs(c)) >= 2*B+3*Y
            if N>K: # G>H
                assert max(abs(a),abs(c)) >= 3*B+Y

            # With the universal shared prefix r=2, 4 == 1 (mod 3).
            # If R == 2 mod 3, actual x,y nonzero mod 3 force N,K !=1 mod3.
            if N%3!=1 and K%3!=1:
                assert max(abs(a),abs(c)) >= 2*B+3*Y

# Physical-gap coefficients from RL24: z-1 < z e CH and z<46/45.
cH=Fraction(46,45)*Fraction(1,4)          # 23/90
cG=Fraction(91,45)*cH                     # 2093/4050
assert cH==Fraction(23,90)
assert cG==Fraction(2093,4050)

# H>G: K>=3 after mod-3 exclusion of (K,N)=(2,1).
# So H>=3*2^r and H<(23/90)e.
for r,emin in [(2,47),(3,94),(4,188)]:
    # strict necessary inequality e > (270/23) 2^r
    threshold=Fraction(270*(1<<r),23)
    assert emin-1 <= threshold < emin

# G>H: N>=3 and G<(2093/4050)e.
for r,emin in [(2,24),(3,47),(4,93)]:
    threshold=Fraction(12150*(1<<r),2093)
    assert emin-1 <= threshold < emin

# Stronger numerator upper constants:
# global Delta < Y[(4/5)e-3+3(2/3)^e]
# H>G Delta < Y[(8/15)e-2+2(2/3)^e].
def glob_rhs(e):
    return Fraction(4*e,5)-3+3*Fraction(2,3)**e

def up_rhs(e):
    return Fraction(8*e,15)-2+2*Fraction(2,3)**e

assert glob_rhs(23) < 16 and glob_rhs(24) > 16
assert up_rhs(41) < 20 and up_rhs(42) > 20

# Exact terminal near-resonance arithmetic below e=188.
near=[]
for e in range(1,188):
    for b in range(1,2*e+3):
        B=1<<b; Y=3**e
        if B>Y and 15*B**3 < 16*Y**3:
            near.append((b,e))
assert near==[(65,41),(149,94),(214,135),(233,147)]
# Hence H>G (analytic e>=47) skips the sole e<94 terminal pair.
assert [p for p in near if p[1]>=47][0]==(149,94)

# If the first terminal pair (65,41) is considered analytically without the
# inherited huge-R CF gate, the physical bounds plus G>H localize gaps.
# Enumerate all multiples of four under the RL24 coarse caps, require all
# three block-start phases nonzero mod 3, and then impose the mod-16 low-state
# residue set {7,11,15}.
E=41
Gmax=Fraction(2093,4050)*E
Hmax=Fraction(23,90)*E
allowed16={7,11,15}
patterns=[]
for G in range(4,100,4):
    if not Fraction(G,1)<Gmax: continue
    for H in range(4,G,4):
        if not Fraction(H,1)<Hmax: continue
        for r3 in (1,2):
            if (r3+G)%3==0 or (r3+H)%3==0: continue
            roots=[]
            for r16 in allowed16:
                if (r16+G)%16 in allowed16 and (r16+H)%16 in allowed16:
                    roots.append(r16)
            if roots:
                patterns.append((G,H,r3,tuple(sorted(roots))))
assert patterns==[
    (12,4,1,(11,)),
    (12,8,2,(15,)),
    (16,4,1,(7,11)),
    (20,8,2,(7,)),
]

# Monotone-lift/Qmin refinement in the G>H orientation gives
# x-y < z(z-1)R - z*q0.  The coarse z(z-1)R cap at e=41 is
# (46/45)*(23/90)*41; q0=1-(2/3)^41. This is < 12, so the
# two patterns with G-H=12 are impossible, leaving exactly two.
Dcap=Fraction(46,45)*Fraction(23,90)*41 - Fraction(46,45)*(1-Fraction(2,3)**41)
assert Dcap < 12
survive=[p for p in patterns if p[0]-p[1] < Dcap]
assert survive==[(12,4,1,(11,)),(12,8,2,(15,))]

print('RL25 cubic range/orientation verifier: PASS')
print('R*C_H(R) < 1/4 for R>=161')
print('global numerator upper: Delta < Y[(4/5)e-3+3(2/3)^e]')
print('H>G numerator upper: Delta < Y[(8/15)e-2+2(2/3)^e]')
print('H>G physical consequence: e>=47; exact near-resonance terminal consequence: e>=94')
print('G>H physical consequence at common r=2: e>=24')
print('near-resonant terminal pairs with e<188 =',near)
print('e=41 coarse gap patterns =',patterns)
print('e=41 patterns after monotone-lift refinement =',survive)
