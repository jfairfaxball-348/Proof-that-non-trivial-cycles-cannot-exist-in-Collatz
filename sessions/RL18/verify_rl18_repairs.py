from math import gcd
from itertools import product
from decimal import Decimal, getcontext

getcontext().prec = 120
D0 = Decimal
ln2 = D0(2).ln(); ln3 = D0(3).ln()
beta = ln3/ln2


def bezout(a,b):
    old_r,r=a,b; old_s,s=1,0; old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    return old_r,old_s,old_t


def modpow_signed(a,e,n):
    if e>=0: return pow(a,e,n)
    return pow(pow(a,-1,n),-e,n)


def theta_sigma(A,L,D):
    g,u,v=bezout(L,A)
    assert g==1
    th=(modpow_signed(2,u,D)*modpow_signed(3,v,D))%D
    assert pow(th,L,D)==2%D and pow(th,A,D)==3%D
    return th,pow(th,-3,D)

# ------------------------------------------------------------------
# 1. j=1 coefficient-3 P2 boundary: analytic inequalities sanity.
# A=2L+3h, h>=1. Nonzero resultant R obeys
# |R| < 4^t 7^h <= 4^(L-1)7^h <= (7/32)2^A,
# while D >= (29/32)2^A.  Boundary needs L>=2.
# ------------------------------------------------------------------
for L in range(2,80):
    for h in range(1,30):
        A=2*L+3*h
        assert 4**(L-1)*7**h <= (D0(7)/D0(32))*D0(2)**A
        D=(1<<A)-3**L
        assert D > D0(29)/D0(32)*D0(2)**A

# ------------------------------------------------------------------
# 2. j=2 coefficient-3 P2 boundary.
# A=L+3h. A boundary zero forces D < 2^L 7^h, equivalently
# delta < (7/8)^h < (7/8)^(L/6).
# ------------------------------------------------------------------
qj2=(D0(7)/D0(8))**(D0(1)/D0(6))
cj2=(D0(8)/D0(7)).ln()/D0(6)
lmn21=D0(22)*(D0(21)**2)*ln2*ln3
assert lmn21 < D0(7400)
assert cj2*D0(335000)-ln2 > lmn21
assert (D0(4)*D0(335000)).ln()+D0('0.06') < D0(21)
assert qj2**D0(341) < ln2/(D0(4)*D0(341))
assert qj2*D0(342)/D0(341) < 1

# CF of log3/log2 through the LMN cutoff.
x=beta; cf=[]; conv=[]
p_m2,p_m1=0,1; q_m2,q_m1=1,0
for _ in range(30):
    aa=int(x); cf.append(aa)
    p=aa*p_m1+p_m2; qq=aa*q_m1+q_m2
    conv.append((p,qq,D0(p)/D0(qq)-beta))
    p_m2,p_m1=p_m1,p; q_m2,q_m1=q_m1,qq
    if qq>335000: break
    x=1/(x-D0(aa))
expected_cf=[1,1,1,2,2,3,1,5,2,23,2,2,1,1,55]
assert cf[:len(expected_cf)]==expected_cf
j2_cf=[(p,q) for p,q,d in conv if 341<=q<335000 and d>0 and (p-q)%3==0]
assert j2_cf==[(24727,15601)], j2_cf
for A,L in j2_cf:
    h=(A-L)//3
    D=(1<<A)-3**L
    assert not (D < (1<<L)*7**h)

# Exact barrier pairs below Legendre threshold.  Monotone h-loop uses
# 2^L(8^h-7^h)<3^L, exactly equivalent to D<2^L 7^h.
j2_small=[]
for L in range(1,341):
    h=1
    while (1<<L)*(8**h-7**h) < 3**L:
        A=L+3*h; D=(1<<A)-3**L
        if D>1 and gcd(A,L)==1:
            j2_small.append((A,L,h,D))
        h+=1
expected_j2=[(4,1),(5,2),(7,4),(8,5),(13,7),(22,13),(23,14),
             (31,19),(65,41),(73,46),(89,56),(97,61),(317,200)]
assert [(A,L) for A,L,h,D in j2_small]==expected_j2
j2_tests=0; j2_zeros=[]
for A,L,h,D in j2_small:
    if L<2: continue
    _,sig=theta_sigma(A,L,D)
    for t in range(1,L):
        j2_tests+=1
        if (3+4*pow(sig,t,D))%D==0:
            j2_zeros.append((A,L,h,t,D))
assert j2_tests==456
assert j2_zeros==[]

# ------------------------------------------------------------------
# 3. Omitted gcd(A,L)=gcd(A,m)=3 sector.
# A=3a,L=3ell,m=3n. Generic P2 norm barrier is D^2<61^a.
# ------------------------------------------------------------------
q=D0(61).sqrt()/D0(8)
ca=(D0(8)/D0(61).sqrt()).ln()
cell=beta*ca
assert ca > D0('0.024')
assert cell*D0(195000) + (D0(3)/D0(2)).ln() > lmn21
assert (D0(4)*D0(195000)).ln()+D0('0.06') < D0(21)
assert q**(beta*D0(149)) < D0(3)*ln2/(D0(4)*D0(149))
assert (q**beta)*D0(150)/D0(149) < 1

# CF upper convergents in the large finite band; structural equation requires 3∤a.
x=beta; conv2=[]
p_m2,p_m1=0,1; q_m2,q_m1=1,0
for _ in range(30):
    aa=int(x)
    p=aa*p_m1+p_m2; qq=aa*q_m1+q_m2
    conv2.append((p,qq,D0(p)/D0(qq)-beta))
    p_m2,p_m1=p_m1,p; q_m2,q_m1=q_m1,qq
    if qq>195000: break
    x=1/(x-D0(aa))
cubic_cf=[(p,qq) for p,qq,d in conv2 if 149<=qq<195000 and d>0 and p%3!=0]
expected_cubic_cf=[(485,306),(24727,15601),(125743,79335),(301994,190537)]
assert cubic_cf==expected_cubic_cf, cubic_cf
for a,ell in cubic_cf:
    D=8**a-27**ell
    assert D>0
    assert not (D*D < 61**a)

# Exact small barrier pairs.
cubic_small=[]
for ell in range(1,149):
    for a in range(1,2*ell+3):
        if a%3==0 or gcd(a,ell)!=1: continue
        D=8**a-27**ell
        if D>1 and D*D < 61**a:
            cubic_small.append((a,ell,D))
expected_cubic=[(2,1),(5,3),(7,4),(8,5),(13,8),(35,22),(43,27),(46,29),(65,41),(149,94)]
assert [(a,e) for a,e,D in cubic_small]==expected_cubic

# Unique rho from rho^a=1/3 and rho^(3ell)=1/8; scan all three orbit populations.
cubic_comps=0; cubic_zeros=[]
for a,ell,D in cubic_small:
    g,u,v=bezout(a,3*ell)
    assert g==1
    rho=(modpow_signed(3,-u,D)*modpow_signed(8,-v,D))%D
    assert pow(rho,a,D)==pow(3,-1,D)
    assert pow(rho,3*ell,D)==pow(8,-1,D)
    for e0 in range(a+1):
        for e1 in range(a+1):
            e2=3*ell-e0-e1
            if not (0<=e2<=a): continue
            cubic_comps+=1
            if (1+2*pow(rho,e0,D)+4*pow(rho,e0+e1,D))%D==0:
                cubic_zeros.append((a,ell,e0,e1,e2))
assert cubic_comps==19630
assert cubic_zeros==[(2,1,1,1,1)]

# At (a,ell)=(2,1), structural data force A=6,L=3,m=3,p=2.
# Exhaust all words and confirm the sole D-divisible structural realization is (10)^3.
def Qword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    LL=len(pos)
    return sum((1<<(p-1))*3**(LL-k-1) for k,p in enumerate(pos))

def rot(w,m): return w[m:]+w[:m]

def prefix_diff(source,target):
    A=len(source); out=[0]; s=0
    for i in range(A-1):
        s += target[i]-source[i]; out.append(s)
    return out

structural=[]
A=6; L=3; m=3; D=(1<<A)-3**L
for bits in product([0,1], repeat=A):
    w=list(bits)
    if sum(w)!=L or sum(w[:m])!=2: continue
    G=prefix_diff(w,rot(w,m))
    if sum(abs(v) for v in G)!=3 or [v for v in G if v]!=[-1,-1,-1]: continue
    pops=[sum(w[h+3*s] for s in range(2)) for h in range(3)]
    if pops!=[1,1,1]: continue
    if Qword(w)%D==0:
        structural.append(tuple(w))
assert structural==[(1,0,1,0,1,0)]

print('RL18 repair verifier: PASS')
print('LMN rational-specialization constant 22*21^2 ln2 ln3 <', lmn21)
print('j=2 P2 LMN cutoff L < 335000; Legendre threshold 341')
print('j=2 large-band CF candidates:', j2_cf)
print('j=2 small exact barrier pairs:', [(A,L) for A,L,h,D in j2_small])
print('j=2 exact boundary tests:', j2_tests, 'zeros:', j2_zeros)
print('cubic three-orbit LMN cutoff ell < 195000; Legendre threshold 149')
print('cubic large-band CF candidates:', cubic_cf)
print('cubic small exact barrier pairs:', [(a,e) for a,e,D in cubic_small])
print('cubic admissible population compositions:', cubic_comps)
print('cubic arithmetic zeros:', cubic_zeros)
print('cubic structural D-divisible realizations at the sole zero:', structural)
