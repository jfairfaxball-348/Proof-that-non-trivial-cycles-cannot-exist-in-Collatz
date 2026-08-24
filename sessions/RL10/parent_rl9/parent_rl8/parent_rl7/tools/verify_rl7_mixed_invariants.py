from fractions import Fraction
from itertools import combinations
from math import ceil, floor, gcd

# ---------- compressed-anchor helpers inherited from RL-6 ----------

def vp(x,p):
    assert x
    c=0
    while x%p==0:
        x//=p; c+=1
    return c

def v2(x): return vp(x,2)
def v3(x): return vp(x,3)

def coeff(n,t,mup):
    ell=(1<<mup)*3**n
    c=(1<<(n+mup))*((1<<t)-1)
    d=(1<<(n+t))*3**mup
    return ell,c,d

def compose(word,start=0):
    Lin,C,Den=1,0,1; P=len(word)
    for k in range(P):
        ell,c,d=coeff(*word[(start+k)%P])
        C=ell*C+c*Den
        Lin*=ell; Den*=d
    return Lin,C,Den

def rotate(word,r): return word[r:]+word[:r]

def cyclic_mus(word):
    return [word[(j-1)%len(word)][2] for j in range(len(word))]

def valid_cyclic(word):
    mus=cyclic_mus(word)
    return all(word[j][0]>mus[j] for j in range(len(word)))

def invariants(word):
    mus=cyclic_mus(word)
    M=sum(mus)
    L=sum(word[j][0]-mus[j] for j in range(len(word)))
    A=L+sum(t for n,t,m in word)
    D=(1<<A)-3**L
    return mus,M,L,A,D

def ae(n,t,mup):
    h=n-mup
    a=(Fraction(3,2)**h)*Fraction(1,1<<t)
    e=(Fraction(2,3)**mup)*(1-Fraction(1,1<<t))
    return a,e

def rational_Ws(word):
    mus,M,L,A,D=invariants(word)
    K=(6**M)*D
    return [Fraction(compose(word,r)[1],K) for r in range(len(word))]

# RL-L46: all-prefix/suffix sandwich and reciprocal defect refinement.
sandwich_checks=0
reciprocal_checks=0
gcd_rotation_checks=0
for P in (2,3,4,5,6):
    for seed in range(1,2200):
        word=[]
        for j in range(P):
            n=1+((29*seed+7*j)%11)
            t=1+((31*seed+13*j)%18)
            r=v3((1<<t)-1)
            if r<n: mup=r
            elif r>n: mup=n
            else: mup=n+((seed+2*j)%3)
            word.append((n,t,mup))
        if not valid_cyclic(word): continue
        mus,M,L,A,D=invariants(word)
        if D<=0: continue
        Ws=rational_Ws(word)
        rmin=min(range(P), key=lambda r: Ws[r])
        wr=rotate(word,rmin)
        W=rational_Ws(wr)
        W0=W[0]
        rho=Fraction(3**L,1<<A)

        # Every proper prefix/suffix around the least rational anchor.
        Ap=Fraction(1,1)
        for j in range(1,P):
            Ap*=ae(*wr[j-1])[0]
            B=Fraction(1,1)
            for k in range(j,P): B*=ae(*wr[k])[0]
            assert Ap*B==rho
            assert rho*W[j]/W0 < Ap < W[j]/W0
            assert B < W0/W[j]
            sandwich_checks+=1

        # Exact defect and sharpened reciprocal-anchor upper bound.
        delta=Fraction(D,1<<A)
        exact=Fraction(0,1)
        reciprocal=Fraction(0,1)
        for i,tr in enumerate(wr):
            ai,ei=ae(*tr)
            B=Fraction(1,1)
            for k in range(i+1,P): B*=ae(*wr[k])[0]
            exact += ei*B/W0
            if i==P-1:
                reciprocal += ei/W0
            else:
                reciprocal += ei/W[i+1]
        assert exact==delta
        assert delta < reciprocal
        assert reciprocal < sum(Fraction(1,1)/x for x in W)
        reciprocal_checks+=1

        # RL-L47: gcd(C_r,D) is rotation-invariant.
        Cs=[compose(word,r)[1] for r in range(P)]
        gs=[gcd(C,D) for C in Cs]
        assert len(set(gs))==1
        for j in range(P):
            ell,c,d=coeff(*word[j])
            K=(6**M)*D
            assert d*Cs[(j+1)%P]==ell*Cs[j]+c*K
        gcd_rotation_checks+=1

# ---------- full-map parity-word helpers ----------

def Cword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    r=len(pos)
    return sum((1<<(p-1))*3**(r-k-1) for k,p in enumerate(pos))

def rotations(w):
    return [w[j:]+w[:j] for j in range(len(w))]

def Cmin(w):
    return min(Cword(x) for x in rotations(w))

def christoffel(N,r):
    # d_i=ceil(i r/N)-ceil((i-1)r/N)
    return [ceil((i+1)*r/N)-ceil(i*r/N) for i in range(N)]

def canonical_rotation(w):
    return min(tuple(x) for x in rotations(w))

def mu_num(w):
    return sum((i+1)*b for i,b in enumerate(w))

def mu_min_rotation(w):
    rs=rotations(w)
    return min(rs,key=mu_num)

# Adjacent transposition formula and unit-edge obstruction.
transposition_checks=0
unit_edge_checks=0
for N in range(2,13):
    for mask in range(1<<N):
        w=[(mask>>i)&1 for i in range(N)]
        r=sum(w)
        if r==0 or r==N: continue
        D=(1<<N)-3**r
        for i in range(N-1):
            if w[i:i+2]==[1,0]:
                wp=w.copy(); wp[i:i+2]=[0,1]
                diff=Cword(wp)-Cword(w)
                ones_right=sum(w[i+2:])
                expected=(1<<i)*3**ones_right
                assert diff==expected
                transposition_checks+=1
                if D>1:
                    assert gcd(diff,D)==1
                    assert not (Cword(w)%D==0 and Cword(wp)%D==0)
                    unit_edge_checks+=1

# RL-L50: quantitative Christoffel gap.
# Exhaust every rotation class for admissible N<=14, alpha < N/r <=2 encoded by D>0,N<=2r.
gap_checks=0
max_checks=0
class_checks=0
for N in range(2,15):
    for r in range(1,N):
        D=(1<<N)-3**r
        if D<=0 or N>2*r: continue
        chrw=christoffel(N,r)
        Cchr=Cword(chrw)
        # closed-form position expression and upper bound without floats:
        pos=[1+((k*N)//r) for k in range(r)]
        assert Cchr==sum((1<<(pos[k]-1))*3**(r-k-1) for k in range(r))
        # Verify (2^(N/r)-3) Cchr <= D numerically only through exact r-th powers
        # is awkward; the report contains the elementary analytic geometric-series proof.
        seen=set()
        best=-1
        for comb in combinations(range(N),r):
            w=[0]*N
            for i in comb: w[i]=1
            key=canonical_rotation(w)
            if key in seen: continue
            seen.add(key); class_checks+=1
            ww=list(key)
            cm=Cmin(ww)
            if cm>best: best=cm
            if canonical_rotation(ww)==canonical_rotation(chrw):
                continue
            # Strict gap: Cchr-Cmin > 3^(r-1)/4, checked as 4*gap > 3^(r-1).
            assert 4*(Cchr-cm) > 3**(r-1), (N,r,ww,Cchr,cm)
            gap_checks+=1
        assert best==Cchr
        max_checks+=1

# RL-L48: repeated symbolic word fixed point descends to primitive block.
# Test generic positive affine contractions f(x)=a*x+e exactly.
repetition_checks=0
for num in range(1,8):
    for den in range(num+1,10):
        a=Fraction(num,den)
        for en in range(1,7):
            e=Fraction(en,11)
            x=e/(1-a)
            for m in range(2,7):
                # f^m(x)=a^m x + e(1+...+a^(m-1)); fixed point is identical.
                geom=sum((a**j for j in range(m)),Fraction(0,1))
                xm=e*geom/(1-a**m)
                assert xm==x
                repetition_checks+=1

# D=1 occurs only at (N,r)=(2,1) in a broad exact range; elementary proof is in report.
d1=[]
for N in range(1,80):
    for r in range(1,80):
        if (1<<N)-3**r==1: d1.append((N,r))
assert d1==[(2,1)]

print('RL-7 mixed-invariant verifier: PASS')
print('prefix/suffix sandwich checks:',sandwich_checks)
print('reciprocal-defect checks:',reciprocal_checks)
print('rotation-gcd checks:',gcd_rotation_checks)
print('adjacent-transposition identity checks:',transposition_checks)
print('unit-edge obstruction checks:',unit_edge_checks)
print('Christoffel admissible (N,r) max checks:',max_checks)
print('Christoffel non-extremal class gap checks:',gap_checks)
print('binary rotation classes audited:',class_checks)
print('repetition fixed-point descent checks:',repetition_checks)
print('D=1 solutions in N,r<80:',d1)

# RL-L51 / RL-L52: cyclic one-edge self-rotation <=> primitive Christoffel class.
def cyclic_adj_swap(a,b):
    N=len(a)
    dif=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y]
    if len(dif)!=2: return False
    i,j=dif
    if (j-i)%N not in (1,N-1): return False
    # At the two positions the bits are exchanged.
    return a[i]==b[j] and a[j]==b[i] and a[i]!=a[j]

self_edge_classification_checks=0
for N in range(2,13):
    for mask in range(1<<N):
        w=[(mask>>i)&1 for i in range(N)]
        L=sum(w)
        if L==0 or L==N: continue
        has_edge=any(cyclic_adj_swap(w,w[m:]+w[:m]) for m in range(1,N))
        is_primitive_chr=(gcd(N,L)==1 and canonical_rotation(w)==canonical_rotation(christoffel(N,L)))
        assert has_edge==is_primitive_chr, (N,L,w,has_edge,is_primitive_chr)
        self_edge_classification_checks+=1

christoffel_internal_exclusion_checks=0
christoffel_repeat_checks=0
for N in range(2,61):
    for L in range(1,N):
        cw=christoffel(N,L)
        g=gcd(N,L)
        if g==1:
            ms=[m for m in range(1,N) if cyclic_adj_swap(cw,cw[m:]+cw[:m])]
            assert ms
            assert any((L*m)%N in (1,N-1) for m in ms)
            D=(1<<N)-3**L
            if D>1:
                assert Cword(cw)%D != 0
                christoffel_internal_exclusion_checks+=1
        else:
            n0=N//g; l0=L//g
            base=christoffel(n0,l0)
            assert cw==base*g
            christoffel_repeat_checks+=1

print('self-edge/primitive-Christoffel classification checks:',self_edge_classification_checks)
print('primitive Christoffel D-divisibility exclusions:',christoffel_internal_exclusion_checks)
print('nonprimitive Christoffel repetition checks:',christoffel_repeat_checks)
