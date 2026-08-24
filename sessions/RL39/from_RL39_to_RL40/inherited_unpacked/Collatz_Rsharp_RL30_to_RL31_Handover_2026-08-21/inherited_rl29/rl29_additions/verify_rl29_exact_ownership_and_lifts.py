from fractions import Fraction
from math import gcd
import sympy as sp

# Exact sanity verifier for the RL29 session claims.
# This certifies algebra / finite residue arithmetic only; the analytic proof
# obligations are stated separately in RL29_SESSION_RESULTS_TO_AUDIT.md.

# ------------------------------------------------------------------
# 1. Least-state lifting in the exceptional root class
# ------------------------------------------------------------------
def T(n):
    return (3*n+1)//2 if n & 1 else n//2

def parity_and_affine(r,c,k):
    x=r+c; A=1; C=c; den=1
    out=[]
    for _ in range(k):
        bit=x&1
        out.append((bit,A,C,den))
        if bit:
            x=(3*x+1)//2
            C=3*C+den; A=3*A
        else:
            x//=2
        den*=2
    out.append((None,A,C,den))
    return out

def interval_constraints(r,k):
    lo=1; hi=None
    for c in (0,12,4):
        for bit,A,C,den in parity_and_affine(r,c,k):
            q=A-den
            if q==0:
                if C<0: return None
            elif q>0:
                if C<0: lo=max(lo,(-C+q-1)//q)
            else:
                cap=C//(-q)
                hi=cap if hi is None else min(hi,cap)
                if hi<lo: return None
    return lo,hi

def first_mod9(r,k,lo):
    M=1<<k
    t0=((1-r)%9)*pow(M,-1,9)%9
    base=r+M*t0
    step=9*M
    if base<lo:
        base += ((lo-base+step-1)//step)*step
    return base

def viable(r,k):
    iv=interval_constraints(r,k)
    if iv is None: return False,None
    lo,hi=iv
    first=first_mod9(r,k,lo)
    return (hi is None or first<=hi),(lo,hi,first)

surv=[27]
meta={}
for k in range(6,11):
    old=1<<(k-1); ns=[]; nm={}
    for r in surv:
        for rr in (r,r+old):
            ok,m=viable(rr,k)
            if ok:
                ns.append(rr); nm[rr]=m
    surv=ns; meta=nm

# At depth 10, the only unbounded least-state residue branches are 155 and 667 mod1024.
# They are the same class mod512.  The r=91 branch is bounded to R=91 itself.
assert set(surv)=={91,155,667}
assert meta[91][1]==91 and meta[91][2]==91
assert meta[155][1] is None and meta[667][1] is None
assert 155%512==667%512==155
# CRT with R==1 mod9 gives R==667 mod4608.
assert 667%512==155 and 667%9==1
for n in range(20):
    x=667+4608*n
    assert x%512==155 and x%9==1

# R=91 and R=667 are not least on their actual forward trajectories.
def first_drop(r,limit=200):
    x=r
    for j in range(1,limit+1):
        x=T(x)
        if x<r: return j,x
    return None
assert first_drop(91)==(45,61)
assert first_drop(667)==(24,572)
# Therefore any genuine survivor in this class has R>=667+4608=5275.

# Forced nine-bit prefixes for R == 155 mod512.
def parity_bits(x,k):
    out=[]
    for _ in range(k):
        out.append(x&1); x=T(x)
    return out
for r in (155,667,1179,1691):
    assert r%512==155
    assert parity_bits(r,9)==[1,1,0,1,1,1,1,0,1]
    assert parity_bits(r+12,9)==[1,1,1,0,1,1,0,1,1]
    assert parity_bits(r+4,9)==[1,1,1,1,1,0,1,1,1]

# ------------------------------------------------------------------
# 2. Forced synchronization formulas at s=0,2,6,9
# ------------------------------------------------------------------
R=sp.symbols('R', integer=True, positive=True)
def T_aff(x,b):
    return sp.factor((3*x+1)/2 if b else x/2)
seqs={
    'u':[1,1,0,1,1,1,1,0,1],
    'v':[1,1,1,0,1,1,0,1,1],
    'w':[1,1,1,1,1,0,1,1,1],
}
starts={'u':R,'v':R+12,'w':R+4}
vals={}; counts={}
for name,bits in seqs.items():
    x=starts[name]; c=0
    vals[name]=[x]; counts[name]=[0]
    for bit in bits:
        c+=bit; x=T_aff(x,bit)
        vals[name].append(x); counts[name].append(c)

assert [counts[n][6] for n in ('u','v','w')]==[5,5,5]
assert sp.simplify(vals['u'][6]-(243*R+287)/64)==0
assert sp.simplify(vals['v'][6]-(243*R+3167)/64)==0
assert sp.simplify(vals['w'][6]-(243*R+1183)/64)==0
assert sp.simplify(vals['v'][6]-vals['u'][6])==45
assert sp.simplify(vals['w'][6]-vals['u'][6])==14
assert [counts[n][9] for n in ('u','v')]==[7,7]
assert sp.simplify(vals['v'][9]-vals['u'][9])==51

S0=sp.expand(sum(vals[n][0] for n in ('u','v','w')))
S2=sp.expand(sum(vals[n][2] for n in ('u','v','w')))
S6=sp.expand(sum(vals[n][6] for n in ('u','v','w')))
assert sp.simplify(4*S2-9*S0)==15
assert sp.simplify(64*S6-243*S0)==749
assert gcd(15,749)==1
assert sp.simplify(200*S2-207*S0-64*S6)==1

# Hence if A_s=(B-Y)S_s at synchronized rotations,
# gcd(A0,A2,A6)=B-Y and the displayed Bezout extraction is exact.

# ------------------------------------------------------------------
# 3. Eisenstein relative-factor ownership
# ------------------------------------------------------------------
# Represent a+b*w by pair (a,b), with w^2=-1-w.
def eadd(x,y): return (sp.expand(x[0]+y[0]),sp.expand(x[1]+y[1]))
def emul(x,y):
    a,b=x; c,d=y
    return (sp.expand(a*c-b*d),sp.expand(a*d+b*c-b*d))
def enorm(x):
    a,b=x; return sp.expand(a*a-a*b+b*b)

alpha0=(-4,8)      # gaps (12,4)
alpha6=(-14,31)    # gaps (45,14)
assert enorm(alpha0)==112
assert enorm(alpha6)==1591
assert gcd(112,1591)==1
assert eadd(emul((-19,-11),alpha0),emul((5,3),alpha6))==(1,0)

B,Y=sp.symbols('B Y', integer=True, positive=True)
mu=(-B-Y,-B)       # B*w^2-Y
F0=emul(mu,alpha0)
F6=emul(mu,alpha6)
assert eadd(emul((-19,-11),F0),emul((5,3),F6))==mu

# Expand the claimed integer extraction from physical numerators.
U0,V0,W0,U6,V6,W6=sp.symbols('U0 V0 W0 U6 V6 W6')
FF0=(U0-W0,V0-W0); FF6=(U6-W6,V6-W6)
C=eadd(emul((-19,-11),FF0),emul((5,3),FF6))
Bexpr=sp.expand(-C[1]); Yexpr=sp.expand(C[1]-C[0])
assert Bexpr==11*U0+8*V0-19*W0-3*U6-2*V6+5*W6
assert Yexpr==8*U0-19*V0+11*W0-2*U6+5*V6-3*W6

# ------------------------------------------------------------------
# 4. e >= 67 gate from the pair synchronization at s=9
# ------------------------------------------------------------------
K9=sp.factor((R+12)*(2187*R+29143)/((R+4)*(2187*R+3031)))
comparison=sp.factor(sp.together(K9-3*R/(3*R-59)))
num,den=sp.fraction(comparison)
assert sp.expand(num)==1791*R**2-2255057*R-20633244
assert num.subs(R,5275)>0
# derivative is positive from R>=5275, so polynomial stays positive there.
assert sp.diff(num,R).subs(R,5275)>0

print('RL29 exact ownership / lift verifier: PASS')
print('forced large-root class: R == 667 mod4608; first possible R after excluding 667 is 5275')
print('forced synchronization: s=6 gaps (45,14), norm 1591; root norm 112; gcd=1')
print('absolute extraction: B-Y = 200 A2 - 207 A0 - 64 A6')
print('relative Bezout: (-19-11w) alpha0 + (5+3w) alpha6 = 1')
print('pair-tail gate sanity: K9 > 3R/(3R-59) for R>=5275, supporting e>=67 proof')
