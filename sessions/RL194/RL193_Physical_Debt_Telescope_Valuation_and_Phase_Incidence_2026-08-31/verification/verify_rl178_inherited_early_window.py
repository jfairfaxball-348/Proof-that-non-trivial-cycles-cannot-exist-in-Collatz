#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
t=L-p
assert A*p-L*u==1
assert p+37<L


def B(j):
    return (A*j)//L

def c(j):
    return B(j+1)-B(j)

def v2(n):
    n=abs(n)
    assert n
    return (n & -n).bit_length()-1

# Frozen v=37,H=0 interface from RL177.
J=23
k=J+1
v=37
assert B(J)==36
assert c(J)==2
assert c(k)==1
assert [c(i) for i in range(24,30)]==[1,2,1,2,1,2]
r24=(A*24)%L
assert (r24*p)%L==24
assert ((r24-1)*p)%L==t+24
assert ((r24+1)*p)%L==p+24

# RL176 extremal quantization: v2(g_p)=37 and 0<g_p<2^38 imply g_p=2^37.
gp=2**37
w=gp//(2**v)
assert w==1

# At phase J the common-prefix state gap is exactly 2*3^23.
prefix_gap=(3**J)*gp//(2**B(J))
assert prefix_gap==2*(3**23)

# --- Positive first mismatch d=+1 is impossible. ---
# After a_J=1, a_{p+J}=2, the phase-k states X=y_k, Z=y_{p+k}
# satisfy 2 Z - X = 3^k and have heights (1,0).
Cplus=3**k
Mplus=3*Cplus+1              # 2(3Z+1) - (3X+1)
assert Mplus==3**25+1
assert v2(Mplus)==2
# Height caps from c_24=1 force beta=1 and alpha in {1,2}.
# alpha=1 would give unequal term valuations 1 and 2, hence v2(M)=1.
# alpha=2 gives equal term valuations 2 and 2, hence cancellation v2(M)>=3.
# Exact v2(M)=2 allows neither.
positive_next=[]
for alpha in (1,2):
    beta=1
    left_val=1+beta
    right_val=alpha
    if left_val!=right_val:
        required=min(left_val,right_val)
        ok=(v2(Mplus)==required)
    else:
        ok=(v2(Mplus)>left_val)
    if ok:
        positive_next.append((alpha,beta))
assert positive_next==[]

# --- Negative first mismatch d=-1 survives, but its next pair is forced. ---
# Z - 2 X = 3^k and heights are (0,1).
Cminus=3**k
Mminus=3*Cminus-1            # (3Z+1) - 2(3X+1)
assert Mminus==3**25-1
assert v2(Mminus)==1
# c_24=1 forces alpha=1 and beta in {1,2}; beta=2 would require
# equal valuation 2 with cancellation above 2, impossible. beta=1 is forced.
negative_next=[]
alpha=1
for beta in (1,2):
    left_val=beta
    right_val=1+alpha
    if left_val!=right_val:
        required=min(left_val,right_val)
        ok=(v2(Mminus)==required)
    else:
        ok=(v2(Mminus)>left_val)
    if ok:
        negative_next.append((alpha,beta))
assert negative_next==[(1,1)]

# Generic exact necessary transition automaton.  A state is (h,hp,C), where
# g=h-hp.  For g>0, C=2^g Z-X (odd); for g<0, C=Z-2^-g X (odd);
# for g=0, C=Z-X (positive even).  Every physical path must occur in this
# propagation, though a surviving state is not promoted as physical existence.
def step(i, state):
    h,hp,C=state
    g=h-hp
    digit=c(i)
    out=[]
    for a in range(1,h+digit+1):
        for b in range(1,hp+digit+1):
            gp2=g+b-a
            if g>0:
                N=3*C+(1<<g)-1
                wv=v2(N)
                vg_b=g+b
                if a<vg_b:
                    if gp2<=0 or wv!=a: continue
                    C2=N>>a
                elif a>vg_b:
                    if gp2>=0 or wv!=vg_b: continue
                    C2=N>>vg_b
                else:
                    if gp2!=0 or wv<=a: continue
                    C2=N>>a
            elif g<0:
                e=-g
                N=3*C+1-(1<<e)
                wv=v2(N)
                ve_a=e+a
                if b<ve_a:
                    if gp2>=0 or wv!=b: continue
                    C2=N>>b
                elif b>ve_a:
                    if gp2<=0 or wv!=ve_a: continue
                    C2=N>>ve_a
                else:
                    if gp2!=0 or wv<=b: continue
                    C2=N>>b
            else:
                N=3*C
                wv=v2(N)
                if b<a:
                    if gp2>=0 or wv!=b: continue
                    C2=N>>b
                elif b>a:
                    if gp2<=0 or wv!=a: continue
                    C2=N>>a
                else:
                    if gp2!=0 or wv<=a: continue
                    C2=N>>a
            h2=h+digit-a
            hp2=hp+digit-b
            assert h2>=0 and hp2>=0 and h2-hp2==gp2
            if gp2:
                assert C2&1
            else:
                assert C2%2==0
            out.append((h2,hp2,C2,a,b))
    return out

# Start at phase 24 in the surviving d=-1 state.
states={(0,1,3**24)}
counts={24:1}
nonnegative_first=None
positive_types=[]
for i in range(24,30):
    nxt=set()
    local=[]
    for st in states:
        for h2,hp2,C2,a,b in step(i,st):
            ns=(h2,hp2,C2)
            nxt.add(ns)
            local.append((st,a,b,ns))
    states=nxt
    counts[i+1]=len(states)
    if nonnegative_first is None and any(h>=hp for h,hp,_ in states):
        nonnegative_first=i+1
    if i+1==29:
        positive_types=sorted({(h,hp) for h,hp,_ in states if h>hp})
        assert not any(h==hp for h,hp,_ in states)

assert counts=={24:1,25:1,26:2,27:2,28:5,29:10,30:16}
assert nonnegative_first==29
assert positive_types==[(1,0),(2,0),(2,1)]

# Exact first admissible positive-return quanta at phase 29.
b29=B(29)
assert b29==45
quanta=set()
for h,hp in positive_types:
    g=h-hp
    q=Fraction(2**(b29-h),3**29)
    quanta.add(q*(2**g-1))
expected={
    Fraction(2**43,3**29),
    Fraction(2**43,3**28),
    Fraction(2**44,3**29),
}
assert quanta==expected

print('PASS: RL178 second-transition certificate completed successfully.')
print('v=37,H=0,d=+1: excluded at phase 24->25')
print('v=37,H=0,d=-1: a_24=a_{p+24}=1 forced')
print('necessary-state counts phases 24..30:', counts)
print('G_i<0 for i=24..28; earliest admissible G_i>=0 is i=29')
print('phase-29 G=0: impossible in the exact necessary interface')
print('phase-29 positive height pairs:', positive_types)
print('phase-29 positive quanta:', sorted(str(x) for x in quanta))
