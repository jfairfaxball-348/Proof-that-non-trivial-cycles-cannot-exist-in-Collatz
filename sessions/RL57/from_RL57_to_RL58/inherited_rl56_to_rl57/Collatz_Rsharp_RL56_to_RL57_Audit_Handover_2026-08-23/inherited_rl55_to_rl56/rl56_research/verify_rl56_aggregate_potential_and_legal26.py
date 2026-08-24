#!/usr/bin/env python3
from fractions import Fraction

# RL56 exact verifier for:
#  1. the new monotone Xi lift;
#  2. the zero-mass-majorizing Psi lift;
#  3. exact terminal ceilings Xi<68/5 and Psi<153/20;
#  4. exclusion of the old legal-26 mass maximizer by Xi;
#  5. exhaustive branch-and-bound certificate that every terminal-compatible
#     legal prefix containing 26 x-zeros has Zx_26 <= 107/10.

CAP = Fraction(17,30)
XI_CAP = Fraction(68,5)
PSI_CAP = Fraction(153,20)
TARGET = Fraction(107,10)
ZX_REQ = Fraction(143,12)
N = 26

# ---------- analytic local formulas ----------
# Xi = g * ((T-1)/3^(d-1) + 1/2^(d-1)).
# Psi = g + Xi/2.
# For an edge xy starting at height d with pre-edge scalar g, direct
# substitution into the inherited T recurrence gives Xi increments:
#   00: g(2^(1-d)-3^(1-d))
#   01: 0
#   11: g(1-2^(1-d)/3)
#   10: g(1+2^(1-d)/3-3^(1-d))   (d>=2)
# and Psi increments:
#   00: g[1+2^(-d)-1/(2*3^(d-1))] >= g
#   01: g
#   11: g[1/6-1/(3*2^d)] >= 0
#   10: g[1/6+1/(3*2^d)-1/(2*3^(d-1))] > 0.
# Hence Xi and Psi are monotone, and every x-zero edge contributes at most
# its Psi increment.

def xi_inc_formula(d,x,y):
    if (x,y)==(0,0): return Fraction(1,2**(d-1))-Fraction(1,3**(d-1))
    if (x,y)==(0,1): return Fraction(0)
    if (x,y)==(1,1): return Fraction(1)-Fraction(1,3*2**(d-1))
    if (x,y)==(1,0):
        assert d>=2
        return Fraction(1)+Fraction(1,3*2**(d-1))-Fraction(1,3**(d-1))
    raise AssertionError

def psi_inc_formula(d,x,y):
    if (x,y)==(0,0): return Fraction(1)+Fraction(1,2**d)-Fraction(1,2*3**(d-1))
    if (x,y)==(0,1): return Fraction(1)
    if (x,y)==(1,1): return Fraction(1,6)-Fraction(1,3*2**d)
    if (x,y)==(1,0):
        assert d>=2
        return Fraction(1,6)+Fraction(1,3*2**d)-Fraction(1,2*3**(d-1))
    raise AssertionError

for d in range(1,80):
    assert xi_inc_formula(d,0,0)>=0
    assert xi_inc_formula(d,0,1)==0
    assert xi_inc_formula(d,1,1)>0
    if d>=2: assert xi_inc_formula(d,1,0)>0
    assert psi_inc_formula(d,0,0)>=1
    assert psi_inc_formula(d,0,1)==1
    assert psi_inc_formula(d,1,1)>=0
    if d>=2: assert psi_inc_formula(d,1,0)>0

# ---------- exact transition regression ----------
def jstep(d,J,x,y):
    if (x,y)==(0,0):
        num=J+3**d-2**d; assert num%2==0; return d,num//2
    if (x,y)==(1,1):
        num=3*J+2**d-1; assert num%2==0; return d,num//2
    if (x,y)==(0,1):
        num=3*J+3**(d+1)-2**d-1; assert num%2==0; return d+1,num//2
    if (x,y)==(1,0):
        assert d>1 and J%2==0; return d-1,J//2
    raise AssertionError

def tstep(d,T,x,y):
    num=(3**y)*T + x*3**(d+y-1)-y
    assert num%2==0
    return d+y-x,num//2

def det_step(d,J,x):
    if x==0:
        y=0 if J&1 else 1
    else:
        if J&1: y=1
        elif d>1: y=0
        else: return None
    dn,Jn=jstep(d,J,x,y)
    return dn,Jn,y

def xi(d,J,g):
    T=J-3**d+2**d
    return g*(Fraction(T-1,3**(d-1))+Fraction(1,2**(d-1)))

def psi(d,J,g):
    return g+xi(d,J,g)/2

# Direct exact difference check over a broad integer state window wherever the
# edge is integral/legal. This is a regression check for the displayed
# algebraic formulas above.
for d in range(1,8):
    for J in range(-60,61):
        T=J-3**d+2**d
        for x in (0,1):
            st=det_step(d,J,x)
            if st is None: continue
            dn,Jn,y=st
            g=Fraction(1)
            gn=g*(2 if x==0 else Fraction(2,3))
            assert xi(dn,Jn,gn)-xi(d,J,g) == g*xi_inc_formula(d,x,y)
            assert psi(dn,Jn,gn)-psi(d,J,g) == g*psi_inc_formula(d,x,y)

# Terminal d=1, J=2^K, g=27*zeta/2^(K+1). Under inherited zeta<136/135
# and K>=3:
#   Xi_end = (27*zeta/2)(1-2^-K) < 68/5.
#   Psi_end = (27*zeta/4)(1+2^-K) < 153/20.
zeta_up=Fraction(136,135)
for K in range(3,101,2):
    xi_end_up=Fraction(27,2)*zeta_up*(1-Fraction(1,2**K))
    psi_end_up=Fraction(27,4)*zeta_up*(1+Fraction(1,2**K))
    assert xi_end_up < XI_CAP
    assert psi_end_up <= PSI_CAP
assert Fraction(27,4)*zeta_up*Fraction(9,8) == PSI_CAP

# ---------- old legal-26 maximizer is terminal-incompatible ----------
old_zeros=[2,5,7,10,14,15,18,21,25,26,29,32,34,37,40,44,45,48,51,53,56,59,62,64,67,70]
d,J,px=1,-13,0
Z=Fraction(0)
for i in range(71):
    x=0 if i in old_zeros else 1
    g=Fraction(2**i,3**px)
    if x==0: Z+=g
    st=det_step(d,J,x); assert st is not None
    d,J,y=st
    px+=x
assert (d,J,px)==(1,24,45)
gcut=Fraction(2**71,3**45)
assert xi(d,J,gcut)==23*gcut
assert xi(d,J,gcut)>XI_CAP
old_best=Fraction(34057930625026471931596,2954312706550833698643)
assert Z==old_best

# ---------- fast exact legal-26 terminal-compatible decision certificate ----------
# Accumulated zero mass at state (i,p) is represented as Znum/3^p.
# This is integral under the recurrences:
#   x=0: Znum -> Znum+2^i
#   x=1: Znum -> 3*Znum.
# The search is relaxed in the survivor's favor:
#   * zero cap uses <=17/30 rather than strict <;
#   * terminal Xi/Psi use the larger rational ceilings above;
#   * future zero mass is bounded by three independent relaxations:
#       rem*CAP,
#       (2^rem-1)g,
#       PSI_CAP-Psi(current), since every future x-zero is paid by monotone Psi.
# If all three cannot beat TARGET, the branch is safely pruned.

p2=[1]; p3=[1]
def ensure2(n):
    while len(p2)<=n: p2.append(p2[-1]*2)
def ensure3(n):
    while len(p3)<=n: p3.append(p3[-1]*3)

def potnums(i,p,d,J):
    ensure2(max(i,d)); ensure3(p+d+2)
    T=J-p3[d]+p2[d]
    Dxi=p3[p+d-1]*p2[d-1]
    nxi=p2[i]*((T-1)*p2[d-1]+p3[d-1])
    D=2*Dxi
    npsi=p2[i]*(p3[d-1]*p2[d] + (T-1)*p2[d-1]+p3[d-1])
    return nxi,Dxi,npsi,D

def step_fast(d,J,x):
    ensure2(d+1); ensure3(d+1)
    if x==0: y=0 if J&1 else 1
    else:
        if J&1: y=1
        elif d>1: y=0
        else: return None
    if x==0 and y==0: return d,(J+p3[d]-p2[d])//2
    if x==1 and y==1: return d,(3*J+p2[d]-1)//2
    if x==0 and y==1: return d+1,(3*J+p3[d+1]-p2[d]-1)//2
    return d-1,J//2

seen={}
nodes=0
pr_xi=pr_cap=pr_ub=pr_psiub=0

def rec(i,p,rem,Znum,d,J):
    global nodes,pr_xi,pr_cap,pr_ub,pr_psiub
    nodes+=1
    ensure2(i+rem+2); ensure3(p+d+2)
    nxi,Dxi,npsi,D=potnums(i,p,d,J)
    if 5*nxi >= 68*Dxi:
        pr_xi+=1; return False
    if 20*npsi >= 153*D:
        pr_cap+=1; return False
    den=p3[p]
    # UB1: Z + rem*17/30 <= 107/10
    if 300*Znum +170*rem*den <=3210*den:
        pr_ub+=1; return False
    # UB2: Z +(2^rem-1)g <= 107/10
    if 10*(Znum +(p2[rem]-1)*p2[i]) <=107*den:
        pr_ub+=1; return False
    # UB3: Z +153/20 - Psi <=107/10, i.e. Z-Psi<=61/20.
    zD=Znum*p3[d-1]*p2[d]
    if 20*(zD-npsi) <=61*D:
        pr_psiub+=1; return False
    key=(i,p,rem,d,J)
    old=seen.get(key)
    if old is not None and Znum<=old:
        return False
    seen[key]=Znum
    if rem==0:
        # Reaching here would certify Z>107/10. It must not happen.
        return True
    # Relax strict zero cap to <=.
    if 30*p2[i] <=17*den:
        st=step_fast(d,J,0)
        if st and rec(i+1,p,rem-1,Znum+p2[i],*st): return True
    st=step_fast(d,J,1)
    if st and rec(i+1,p+1,rem,3*Znum,*st): return True
    return False

hit=rec(0,0,N,0,1,-13)
assert not hit
new_gap=ZX_REQ-TARGET
assert new_gap==Fraction(73,60)

# Negative-cycle barrier for the scalar potential route.
# Each complete h=1 negative macro 11,00,11 has one x-zero, scales g by 8/9,
# and contributes (2/3)g to Zx. After r macros:
#   Zpre=6(1-(8/9)^r), Psi=-6(8/9)^r.
r=26
h=Fraction(8,9)**r
zpre=6*(1-h)
psipre=-6*h
assert zpre>5
assert PSI_CAP-psipre>new_gap

print('RL56 aggregate potential / legal-prefix theorem: PASS')
print('Xi terminal ceiling < 68/5 and Psi terminal ceiling <= 153/20: PASS')
print('old legal-26 maximizer endpoint Xi =',float(23*gcut),'> 68/5, so it cannot extend to terminal')
print('terminal-compatible legal first-26 mass <= 107/10 = 10.7')
print('new required late mass > 73/60 =',float(new_gap))
print('decision-search nodes =',nodes,'memo states =',len(seen))
print('prunes: Xi=',pr_xi,'PsiCap=',pr_cap,'futureUB=',pr_ub,'PsiFuture=',pr_psiub)
print('negative-cycle barrier: after 26 neutral macros Zpre=',float(zpre),'Psi=',float(psipre))
print('therefore the new scalar potential alone does not yet prove late mass < 73/60')
