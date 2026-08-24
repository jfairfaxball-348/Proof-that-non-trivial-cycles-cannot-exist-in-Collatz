#!/usr/bin/env python3
from fractions import Fraction
PATH='11011'+'1010111011'+'1100100110'+'1101101101'+'1011011011'+'0110100101'+'111111001110101010'
assert len(PATH)==73
CAP=Fraction(17,30)
# RL58/RL59 terminal necessary ceilings, conservative exact rationals
AA=27*10**18+2
AB=2*10**18
KMIN=25

def pots(i,p,d,J):
    T=J-3**d+2**d
    xi=Fraction(2**i*((T-1)*2**(d-1)+3**(d-1)),3**(p+d-1)*2**(d-1))
    psi=Fraction(2**i*(3**(d-1)*2**d+(T-1)*2**(d-1)+3**(d-1)),2*3**(p+d-1)*2**(d-1))
    return xi,psi

def step(i,p,d,J,Dnum,x):
    if x==0: y=0 if J&1 else 1
    else:
        if J&1: y=1
        elif d>1: y=0
        else: raise AssertionError('illegal x=1 at even height-one J')
    if (x,y)==(0,0):
        num=J+3**d-2**d; assert num%2==0
        J2=num//2; d2=d; p2=p
        D2=Dnum+2**i*(3**(d-1)-1)
    elif (x,y)==(1,1):
        num=3*J+2**d-1; assert num%2==0
        J2=num//2; d2=d; p2=p+1
        D2=3*Dnum
    elif (x,y)==(0,1):
        num=3*J+3**(d+1)-2**d-1; assert num%2==0
        J2=num//2; d2=d+1; p2=p
        D2=3*Dnum+2**i*3**d
    else:
        assert d>1 and J%2==0
        J2=J//2; d2=d-1; p2=p+1
        D2=Dnum-2**i
    return i+1,p2,d2,J2,D2,y

i=p=0; d=1; J=-13; Dnum=0
maxzero=Fraction(0); zeros=0
for xch in PATH:
    x=int(xch)
    if x==0:
        w=Fraction(2**i,3**p)
        assert w < CAP
        maxzero=max(maxzero,w); zeros+=1
    # exact terminal-compatible necessary cuts used by the DP
    xi,psi=pots(i,p,d,J)
    # Xi < 13.500000001-ish safe value encoded in original DP by AA/AB checks.
    # We replay the exact same inequalities below.
    # Xi < AA/AB
    assert xi < Fraction(AA,AB)
    # W lower/upper encoded in DP
    assert 3*AB*2**i*J < AA*3**(p+d)
    assert 3*2**i*J >= -13*3**(p+d)
    i,p,d,J,Dnum,y=step(i,p,d,J,Dnum,x)

assert (i,p,d,J,zeros)==(73,47,1,3,26)
D=Fraction(Dnum,3**(p+d-1))
assert D < Fraction(5,3)
assert Dnum==22521943623158297371116
assert 3**47==26588814358957503287787
print('RL59 defect-compatible four-pump entry witness: PASS')
print('x_path=',PATH)
print('target=(i,p,d,J,zeros)=',(i,p,d,J,zeros))
print('defect=',Dnum,'/',3**47,'=',float(D))
print('max_xzero_weight=',float(maxzero))
# Append 4 exact pumps and forced Type-B exit, verify state and threatening mass.
g0=Fraction(2**73,3**47)
A4=2*g0*(Fraction(4,3)**4-1)
assert A4>Fraction(5,4)
for xch in '10'*4+'110':
    x=int(xch)
    if x==0: assert Fraction(2**i,3**p)<CAP
    i,p,d,J,Dnum,y=step(i,p,d,J,Dnum,x)
assert (i,p,d,J)==(84,53,2,15)
print('four_pump_aligned_mass=',float(A4),'> 1.25')
print('typeB_exit=(i,p,d,J,Q)=',(i,p,d,J,J+2**d-1))
print('exit_g=',float(Fraction(2**i,3**p)))
print('exit_D_raw=',float(Fraction(Dnum,3**(p+d-1))))
