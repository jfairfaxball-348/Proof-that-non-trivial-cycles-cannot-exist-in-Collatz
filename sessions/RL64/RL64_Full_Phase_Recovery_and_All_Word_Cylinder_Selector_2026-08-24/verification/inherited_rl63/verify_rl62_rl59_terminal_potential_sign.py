#!/usr/bin/env python3
from fractions import Fraction as F

# Exact conventions inherited from RL47/RL48/RL59:
# d = 1 + p_y - p_x, g = 2^i / 3^p_x.
# At the terminal internal state: d=1, J=2^k,
# g_end = 27*zeta/2^(k+1).

# 1) General suffix-count algebra.
# If current x-one count is p and height is d, then y-one count is p+d-1.
# Total internal x/y weights are ell-3, hence future one counts are
# Xrem = ell-3-p, Yrem = ell-p-d-2 = Xrem-(d-1).
# RL59's displayed bound corresponds instead to Yrem=Xrem+(d-1).
for ell in (41, 100):
    for p in range(0, min(20, ell-3)):
        for d in range(1, 6):
            if p+d-1 <= ell-3:
                xr = ell-3-p
                yr = ell-p-d-2
                assert yr == xr-(d-1)

# 2) Exact RL47 (65,41), t=2 structural witness.
EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()

def step(d,J,x,y):
    if (x,y)==(0,0):
        n=J+3**d-2**d; assert n%2==0; return d,n//2
    if (x,y)==(1,1):
        n=3*J+2**d-1; assert n%2==0; return d,n//2
    if (x,y)==(0,1):
        n=3*J+3**(d+1)-2**d-1; assert n%2==0; return d+1,n//2
    assert (x,y)==(1,0) and d>1 and J%2==0
    return d-1,J//2

d=1; J=-13; i=0; p=0
states=[]
for e in EDGES:
    x,y=map(int,e)
    states.append((i,p,d,J,e,F(2**i,3**p)))
    d,J=step(d,J,x,y)
    i+=1; p+=x

assert (i,p,d,J)==(59,38,1,32)
pen=states[-1]
assert pen[:5]==(58,37,2,64,'10')
A=65; ELL=41; k=5
zeta=F(2**A,3**ELL)
g=pen[5]
JG=pen[3]*g
rl59_claim = zeta*3**(4-pen[2])/2
correct = zeta*3**(pen[2]+2)/2
assert JG == correct
assert JG == 9*rl59_claim

# Terminal equality for corrected bound.
g_end=F(2**59,3**38)
assert g_end == 27*zeta/F(2**(k+1),1)
assert J*g_end == zeta*3**3/2

# 3) Concrete RL59 four-pump Type-B exit.
# State from bundled verifier: (i,p,d,J)=(84,53,2,15), 5 late x-zero events.
# Future x ones = ELL-56; actual future y ones = ELL-57, not ELL-55.
A2=123139092617126647266
ELL2=77692117359936589403
Q2=A2-ELL2
ZU=F(136,135)
i2,p2,d2,J2,r_late=84,53,2,15,5
py2=p2+d2-1
xrem=ELL2-3-p2
yrem=ELL2-3-py2
assert xrem == ELL2-56
assert yrem == ELL2-57
assert xrem-yrem == d2-1
P_exit=(1<<r_late)*J2
# P_end=2^(Q2-24) symbolically; do not materialize this enormous integer.
# Dropping negative affine corrections gives corrected homogeneous cap.
# Algebraically this equals zeta*3^57/2^80; use safe zeta upper bound.
correct_cap = ZU*F(3**57,2**80)
old_cap = ZU*F(3**55,2**80)
assert old_cap < P_exit
assert P_exit < correct_cap

# 4) Correct positive terminal potential is exactly the inherited monotone-W bound:
# J*g <= (9/2) zeta * 3^d = zeta*3^(d+2)/2.
# At d=1 the old and corrected formulas coincide; at d=2 they differ by 9.
for d0 in range(1,5):
    old = F(3**(4-d0),2)
    new = F(3**(d0+2),2)
    if d0==1:
        assert old==new
    else:
        assert old!=new

print('RL62 RL59 terminal-potential sign audit: PASS')
print('RL47 witness penultimate state:', pen[:5])
print('exact Jg / RL59 claimed cap =', JG/rl59_claim)
print('exact Jg equals corrected cap:', JG==correct)
print('Type-B P_exit =', P_exit)
print('RL59 old safe cap =', float(old_cap))
print('corrected safe cap =', float(correct_cap))
print('actual future Type-B one counts: x=',xrem,'y=',yrem,'difference=',xrem-yrem)
