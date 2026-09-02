#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
from functools import lru_cache

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
B=A-L
R=L-B
GAP_LOWER=128_081_997_553
GAP_UPPER=293_591_818_782
K_LO=128_081_997_553
K_HI=146_795_909_391
T=5*3**35
H=20

def ceil_div(a,b): return (a+b-1)//b
def v2(x): return (x & -x).bit_length()-1
def cbit(r): return 1 if r<R else 2

late_max={j:(0 if j==0 else ceil_div(j*B,L)) for j in range(40)}
height_envelope={j:1+late_max[j] for j in range(40)}
rows=defaultdict(list)
for tau in range(26,40):
    ell0=(tau*B)//L
    ell1=ceil_div(tau*B,L)
    for h0 in (0,1):
        lo=GAP_LOWER*(2**h0)
        hi=GAP_UPPER*(2**h0)
        step=2**tau
        for k in range(lo//step+1,(hi-1)//step+1):
            C0=k*step
            vv=v2(C0)
            odd=C0>>vv
            TT=(3**tau)*odd
            for ell in sorted({ell0,ell1}):
                HH=h0+tau+ell-vv
                if HH<1 or HH>height_envelope[tau]:
                    continue
                if not (GAP_LOWER*(2**HH)<TT<GAP_UPPER*(2**HH)):
                    continue
                rlo=max(0,tau*B-ell*L)
                rhi=min(L-1,tau*B-(ell-1)*L-1)
                if rlo<=rhi:
                    rows[(TT,HH)].append((tau,h0,C0,vv,odd,ell,rlo,rhi))

assert T==250_157_725_494_998_535
rs=rows[(T,H)]
assert {r[0] for r in rs}=={32,33,34,35}

def word_before_terminal(r_terminal,n):
    return tuple(cbit((r_terminal-(n-j)*B)%L) for j in range(n))
def backward_gaps(word,terminal):
    ds=[None]*(len(word)+1); ds[-1]=terminal
    for j in range(len(word)-1,-1,-1):
        ds[j]=ds[j+1]*(2**word[j])/3
    return tuple(ds)
def full_prefix_core(rawlo,rawhi,tau,terminal):
    bounds={rawlo,rawhi+1}
    for j in range(tau):
        shift=(tau-j)*B
        for threshold in (0,R):
            q=(threshold+shift)%L
            if rawlo<q<=rawhi: bounds.add(q)
    bounds=sorted(bounds); good=[]
    for x,y in zip(bounds,bounds[1:]):
        lo,hi=x,y-1
        if lo>hi: continue
        w=word_before_terminal(lo,tau)
        assert word_before_terminal(hi,tau)==w
        ds=backward_gaps(w,terminal)
        if all(Fraction(GAP_LOWER)<d<Fraction(GAP_UPPER) for d in ds):
            good.append((lo,hi))
    merged=[]
    for lo,hi in good:
        if merged and merged[-1][1]+1==lo:
            merged[-1]=(merged[-1][0],hi)
        else: merged.append((lo,hi))
    return merged

terminal=Fraction(T,2**H)
cores={}
for tau in (32,33,34,35):
    cs=[]
    for rr in rs:
        if rr[0]==tau:
            cs.extend(full_prefix_core(rr[-2],rr[-1],tau,terminal))
    cs.sort(); merged=[]
    for a,b in cs:
        if merged and a<=merged[-1][1]+1:
            merged[-1]=(merged[-1][0],max(merged[-1][1],b))
        else: merged.append((a,b))
    cores[tau]=merged

assert cores[32]==[(96_166_487_668,98_855_162_143)]
for tau in (33,34,35):
    assert any(a<=96_166_487_668 and b>=98_855_162_143 for a,b in cores[tau])
FULL=(96_166_487_668,98_855_162_143)

# Exact rational exp/log bounds copied in form from the inherited RL231 verifier.
def ln_bounds_int(x,N=100):
    x=Fraction(x)
    z=(x-1)/(x+1); z2=z*z; term=z; s=Fraction(0)
    for n in range(N):
        s += term/Fraction(2*n+1)
        term *= z2
    lo=2*s
    tail=2*term/Fraction(2*N+1)/(1-z2)
    return lo,lo+tail

@lru_cache(maxsize=None)
def exp_bounds_pos(x,N=60):
    assert 0<=x<1
    term=Fraction(1); s=term
    for k in range(1,N+1):
        term=term*x/k; s += term
    nxt=term*x/Fraction(N+1)
    tail=nxt/(1-x/Fraction(N+2))
    return s,s+tail

l2_lo,l2_hi=ln_bounds_int(2)
l3_lo,l3_hi=ln_bounds_int(3)
d_lo=A*l2_lo-L*l3_hi
d_hi=A*l2_hi-L*l3_lo
s_lo=p*l3_lo-u*l2_hi
s_hi=p*l3_hi-u*l2_lo
assert 0<d_lo<d_hi<Fraction(1,1000)
assert 0<s_lo<s_hi<Fraction(1,1000)

def exp_x_bounds(r):
    q=(p*r)//L
    xlo=r*s_lo+q*d_lo
    xhi=r*s_hi+q*d_hi
    elo,_=exp_bounds_pos(xlo)
    _,ehi=exp_bounds_pos(xhi)
    return elo,ehi

# K = terminal / exp(x). Prove lower K-compatible endpoint is below K_HI
# and upper endpoint is above K_LO. Positivity of s,d makes K decrease in r.
KCORE_LO=96_351_434_735
KCORE_HI=98_855_162_143
elo,_=exp_x_bounds(KCORE_LO)
_,ehi_prev=exp_x_bounds(KCORE_LO-1)
_,ehi=exp_x_bounds(KCORE_HI)
assert terminal/elo < K_HI
assert terminal/ehi_prev > K_HI
assert terminal/ehi > K_LO
assert FULL[0] <= KCORE_LO <= KCORE_HI == FULL[1]

U=Fraction(1,2**25)
x=Fraction(128,7)*U
y=Fraction(4,3)*U
charge=3*x+y
generic=Fraction(1,2**21)
assert charge/U==Fraction(1180,21)
assert generic/U==16
assert (charge-generic)/U==Fraction(844,21)

# Even the maximum physical K-priced budget over the whole corridor is insufficient.
max_k_priced=Fraction(K_HI,T)
assert charge > max_k_priced

# The penalized RL231 H20 maximal family is a distinct terminal invariant.
RL231_H20_PENALIZED=(3**36,20,(31,32,33,34,35,36))
assert (T,H,(32,33,34,35)) != RL231_H20_PENALIZED

print("PASS: RL234 stop-and-repair charging-gap certificate")
print("counter_T=250157725494998535 H=20 owners=32,33,34,35")
print("full_prefix_core=96166487668..98855162143")
print("K_compatible_core=96351434735..98855162143")
print("RL231_charge_U=1180/21 generic_H20_budget_U=16 uncovered_excess_U=844/21")
print("first_invalid_dependency=RL231_sparse_family_charging_coverage")
print("classification=STOP_AND_REPAIR")
