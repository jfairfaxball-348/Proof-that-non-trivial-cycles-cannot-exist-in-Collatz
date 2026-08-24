#!/usr/bin/env python3
from fractions import Fraction
from math import ceil

CAP = Fraction(17,30)
ZX_REQ = Fraction(143,12)
Q = 45446975257190057863
ELL = 77692117359936589403
C = Q - 24

# ---------- exact inherited J/T dynamics ----------
def jstep(d,J,x,y):
    if (x,y)==(0,0):
        num=J+3**d-2**d
        assert num%2==0
        return d,num//2
    if (x,y)==(1,1):
        num=3*J+2**d-1
        assert num%2==0
        return d,num//2
    if (x,y)==(0,1):
        num=3*J+3**(d+1)-2**d-1
        assert num%2==0
        return d+1,num//2
    if (x,y)==(1,0):
        assert J%2==0 and d>1
        return d-1,J//2
    raise AssertionError

def tstep(d,T,x,y):
    num=(3**y)*T + x*3**(d+y-1)-y
    assert num%2==0
    return d+y-x,num//2

def det_y(d,J,x):
    # Parity forces y uniquely.  The only failure is x=1,J even at height 1,
    # because the forced y=0 would leave the one-excursion half-plane.
    if x==0:
        return 0 if J&1 else 1
    if J&1:
        return 1
    return None if d==1 else 0

def det_step(d,J,x):
    y=det_y(d,J,x)
    if y is None:
        return None
    return (*jstep(d,J,x,y),y)

# Cross-check deterministic parity rule against both J and T formulas on a
# large finite state window.  This is symbolic-by-parity in the note; the
# loop is only a regression guard.
for d in range(1,9):
    for J in range(-200,201):
        T=J-3**d+2**d
        for x in (0,1):
            y=det_y(d,J,x)
            legal=[]
            for yy in (0,1):
                dn=d+yy-x
                if dn<1: continue
                # test integrality directly without assertions
                num=(3**yy)*T + x*3**(d+yy-1)-yy
                if num%2==0:
                    legal.append(yy)
            if y is None:
                assert legal==[]
            else:
                assert legal==[y]
                dn,Jn,_=det_step(d,J,x)
                d2,Tn=tstep(d,T,x,y)
                assert dn==d2 and Jn==Tn+3**d2-2**d2

# ---------- greedy first-26 schedule is locally impossible ----------
pstar=[2,4,5,7,9,10,12,14,16,17,19,21,22,24,26,28,29,31,33,34,36,38,40,41,43,45]
u=[pstar[j-1]+j-1 for j in range(1,27)]
assert u[-1]==70
zeros=set(u)
d,J=1,-13
T=-14
kill=None
trace=[]
for i in range(71):
    x=0 if i in zeros else 1
    y=det_y(d,J,x)
    if y is None:
        kill=i
        break
    dn,Jn=jstep(d,J,x,y)
    d2,Tn=tstep(d,T,x,y)
    assert dn==d2 and Jn==Tn+3**dn-2**dn
    trace.append((i,x,y,d,J,dn,Jn))
    d,J,T=dn,Jn,Tn
assert kill==20
assert trace[-1][:3]==(19,1,0)
assert trace[-1][5:]==(1,-6)
# At column 20 the state has d=1,J=-6 (T=-7); parity forces y=0 for x=1,
# which would make d=0, while y=1 is nonintegral.

# ---------- exact legal-prefix mass maximization for 26 x-zeros ----------
# State g=2^i/3^p.  x controls y deterministically through (d,J).
# Arbitrarily many x=1 columns are allowed.  Branch-and-bound uses the same
# rigorous future-mass envelope as RL50, now intersected with exact legality.
p2=[1]
p3=[1]
def gval(i,p):
    while len(p2)<=i: p2.append(p2[-1]*2)
    while len(p3)<=p: p3.append(p3[-1]*3)
    return Fraction(p2[i],p3[p])

N=26
seen={}
best=Fraction(-1)
best_word=None
nodes=0

def rec(i,p,rem,total,d,J,word):
    global best,best_word,nodes
    nodes += 1
    key=(i,p,rem,d,J)
    old=seen.get(key)
    if old is not None and total<=old:
        return
    seen[key]=total
    g=gval(i,p)
    if rem==0:
        if total>best:
            best=total; best_word=word
        return
    ub=total+min(rem*CAP,(2**rem-1)*g)
    if ub<=best:
        return
    if g<=CAP:
        st=det_step(d,J,0)
        if st is not None:
            dn,Jn,y=st
            rec(i+1,p,rem-1,total+g,dn,Jn,word+'0')
    st=det_step(d,J,1)
    if st is not None:
        dn,Jn,y=st
        rec(i+1,p+1,rem,total,dn,Jn,word+'1')

rec(0,0,N,Fraction(0),1,-13,'')
assert best < ZX_REQ
gap=ZX_REQ-best
assert gap>Fraction(3,10)  # much larger than the old tiny-error target
best_zeros=[i for i,ch in enumerate(best_word) if ch=='0']
assert len(best_zeros)==26

# ---------- fixed 2^-1000 uniform target is impossible for small K ----------
# g_end = 27*zeta/2^(K+1), zeta>1.  For the last x-zero, if c>=0 columns
# follow it then w_last=(g_end/2)*(3/2)^c >= g_end/2 > 27/2^(K+2).
# Hence K<=1001 (odd K) makes w_last>2^-1000 regardless of terminal grammar.
for K in range(5,1002,2):
    assert Fraction(27,2**(K+2)) > Fraction(1,2**1000)
# K=1003 is the first odd exponent for which this elementary lower bound no
# longer by itself forbids a 2^-1000 upper bound.
assert Fraction(27,2**1005) < Fraction(1,2**1000)

# ---------- transformed terminal coordinate P=2^r J ----------
# r = remaining late x-zero budget.  Backward maps are:
# 11: P -> (2P-2^r(2^d-1))/3
# 10: P -> 2P
# 00: P -> P-2^(r-1)(3^d-2^d)
# 01: P -> P/3 - 2^(r-1)(3^d-2^(d-1)-1)/3
# All affine constants except 10 are nonpositive for legal d.
for d0 in range(1,12):
    assert 3**d0-2**d0 > 0
    assert 2**d0-1 > 0
    if d0>1:
        assert 3**d0-2**(d0-1)-1 > 0

# At terminal, R=z-27 and K=q-z+3 give K+R=q-24=C, so P_end=2^C.
# For a full suffix after the 26th x-zero, let counts be a=11,b=10,c=00,e=01.
# X=c+e=R, Y=b+c=R+delta with 0<=delta<=4.  Put M=a+e.
# Then L=R+M+delta.  The transformed coefficient is exactly
# 2^delta*(2/3)^M, with only nonpositive affine corrections.
# The genuine suffix length is L=ell+R-48, hence M+delta=ell-48.
# Therefore, if J_cut>0,
# J_cut <= zeta*3^(48+delta)/2^72.
# Use inherited safe zeta^2<136/135, hence zeta<136/135, for a rational cap.
zeta_upper=Fraction(136,135)
pos_caps=[]
for delta in range(5):
    cap=zeta_upper*Fraction(3**(48+delta),2**72)
    pos_caps.append(cap)
assert max(pos_caps)<1379

# If the first-26 x schedule were greedy, g immediately after column 70 is
# exactly 2^71/3^45.  Monotonic W=gJ/3^d >= -13/3 and d=1+delta<=5 then gives
# J > -1318.  (The greedy schedule is already locally impossible above; this
# endpoint interval is retained as a uniform structural cross-check.)
gcut=Fraction(2**71,3**45)
neg_lowers=[]
for d0 in range(1,6):
    lo=-Fraction(13*3**(d0-1),1)/gcut
    neg_lowers.append(lo)
assert min(neg_lowers)>-1318

print('RL54 legal-prefix / uniform-terminal obstruction verifier: PASS')
print('greedy first-26 x schedule dies locally at column',kill)
print('exact max Zx with 26 legal x-zeros under sequential cap =',best)
print('decimal legal-26 maximum =',float(best))
print('required Zx > 143/12 =',float(ZX_REQ))
print('late-mass contradiction threshold Delta =',gap,'=',float(gap))
print('maximizing legal 26-zero positions =',best_zeros)
print('search nodes =',nodes,'memo states =',len(seen))
print('fixed 2^-1000 late-weight target cannot be uniform: K<=1001 already violates it at the last zero')
print('terminal scaling invariant: K+R = q-24 =',C)
print('positive greedy-cut J caps by delta=0..4 =',[float(x) for x in pos_caps])
print('uniform rational positive cap < 1379; monotone-W greedy-cut lower bound > -1318')
