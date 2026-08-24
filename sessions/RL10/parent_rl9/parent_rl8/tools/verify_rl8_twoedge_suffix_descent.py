from fractions import Fraction
from itertools import combinations
from math import gcd

# ---------- full parity helpers ----------
def Qword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    L=len(pos)
    return sum((1<<(p-1))*3**(L-k-1) for k,p in enumerate(pos))

def rotations(w):
    return [w[j:]+w[:j] for j in range(len(w))]

def primitive(w):
    N=len(w)
    return all(w != w[m:]+w[:m] for m in range(1,N))

def swap_internal(w,i):
    if w[i]==w[i+1]: return None
    z=w.copy(); z[i],z[i+1]=z[i+1],z[i]
    return z

def move_sign(w,i):
    # +1 means 10->01, which raises Q for an internal edge.
    return 1 if w[i:i+2]==[1,0] else -1

def edge_weight(w,i):
    # Magnitude of Q change on internal edge i,i+1 (0-based).
    b=sum(w[i+2:])
    return (1<<i)*3**b

# RL-L53 local two-edge reduction.
internal_twoedge_checks=0
overlap_unit_checks=0
overlap_five_checks=0
disjoint_binomial_checks=0
for N in range(3,11):
    for mask in range(1<<N):
        w=[(mask>>i)&1 for i in range(N)]
        if sum(w) in (0,N): continue
        for i in range(N-1):
            w1=swap_internal(w,i)
            if w1 is None: continue
            for j in range(N-1):
                w2=swap_internal(w1,j)
                if w2 is None or w2==w: continue
                dQ=Qword(w2)-Qword(w)
                assert dQ != 0
                internal_twoedge_checks += 1
                if i==j:
                    raise AssertionError('same edge should cancel')
                if abs(i-j)==1:
                    a=min(i,j)
                    # Use the common monomial gcd stripped only of 2,3 factors.
                    x=abs(dQ)
                    while x%2==0: x//=2
                    while x%3==0: x//=3
                    # 100<->001 gives a pure 2^a 3^b unit; 110<->011 gives 5 times one.
                    assert x in (1,5), (w,i,j,w2,dQ,x)
                    if x==1: overlap_unit_checks += 1
                    else: overlap_five_checks += 1
                elif abs(i-j)>=2:
                    left=min(i,j); right=max(i,j)
                    # Disjoint local pairs are unchanged by performing the other swap.
                    assert w[left]!=w[left+1] and w[right]!=w[right+1]
                    wl=edge_weight(w,left)
                    wr=edge_weight(w,right)
                    eps_l=move_sign(w,left)
                    eps_r=move_sign(w,right)
                    assert dQ==eps_l*wl + eps_r*wr
                    b_left=sum(w[left+2:]); b_right=sum(w[right+2:])
                    u=right-left
                    v=b_left-b_right
                    assert u>=2 and v>=1
                    common=(1<<left)*3**b_right
                    expected=common*(eps_l*3**v + eps_r*(1<<u))
                    assert dQ==expected
                    disjoint_binomial_checks += 1

# Cyclic two-edge self-rotation finite diagnostic.
def cyclic_neighbors(w):
    N=len(w)
    for i in range(N):
        j=(i+1)%N
        if w[i]!=w[j]:
            z=w.copy(); z[i],z[j]=z[j],z[i]
            yield z

def self_rotation_exact2(w):
    N=len(w)
    rots={tuple(w[m:]+w[:m]):m for m in range(1,N) if w[m:]+w[:m] != w}
    if not rots: return None
    one={tuple(z) for z in cyclic_neighbors(w)}
    for z in cyclic_neighbors(w):
        for z2 in cyclic_neighbors(z):
            t=tuple(z2)
            if z2!=w and t in rots and t not in one:
                return rots[t]
    return None

selfrot2_count=0
selfrot2_divisible=[]
for N in range(3,17):
    for L in range(1,N):
        D=(1<<N)-3**L
        if D<=1: continue
        for comb in combinations(range(N),L):
            w=[0]*N
            for p in comb: w[p]=1
            m=self_rotation_exact2(w)
            if m is None: continue
            selfrot2_count += 1
            if Qword(w)%D==0:
                selfrot2_divisible.append((N,L,tuple(w),m,Qword(w)//D,primitive(w)))
assert selfrot2_divisible==[
    (4,2,(1,0,1,0),3,1,False),
    (4,2,(0,1,0,1),3,2,False),
], selfrot2_divisible


# Proper binomial-resonance diagnostic tied directly to RL-L53.
# Search 2<=u<=A-2, 1<=v<=L-1 for D | 2^u +/- 3^v.
resonance_pairs=[]
for A in range(3,201):
    for L in range(1,A):
        D=(1<<A)-3**L
        if D<=1: continue
        r2={}
        for u in range(2,A-1):
            r2.setdefault((1<<u)%D,[]).append(u)
        found=[]
        r3=1
        for v in range(1,L):
            r3=(r3*3)%D
            for u in r2.get((-r3)%D,[]):
                found.append((u,v,'+'))
            for u in r2.get(r3,[]):
                if (1<<u)!=3**v:
                    found.append((u,v,'-'))
        if found:
            for u,v,sgn in found:
                # sgn '+' means 2^u + 3^v == 0 mod D, so sigma=-1 in 2^u=sigma*3^v.
                sigma=-1 if sgn=='+' else 1
                k=u*L-v*A
                if k==0:
                    assert pow(sigma,L,D)==1%D and pow(sigma,A,D)==1%D
                else:
                    kk=abs(k)
                    assert ((1<<kk)-pow(sigma,L))%D==0
                    assert (3**kk-pow(sigma,A))%D==0
            resonance_pairs.append((A,L,D,gcd(A,L),tuple(found)))
assert [(x[0],x[1],x[2]) for x in resonance_pairs]==[(4,2,7),(5,3,5),(8,5,13)], resonance_pairs

# ---------- RL-L54 minimum-rotation suffix and prefix rescue ----------
def max_prefix_Q(m,p):
    if p==0: return 0
    return (1<<(m-p))*(3**p-(1<<p))

suffix_checks=0
prefix_rescue_checks=0
qmin_words=0
for N in range(2,15):
    for mask in range(1,1<<N):
        w=[(mask>>i)&1 for i in range(N)]
        L=sum(w)
        if L in (0,N): continue
        D=(1<<N)-3**L
        if D<=0: continue
        rs=rotations(w)
        qs=[Qword(z) for z in rs]
        r0=min(range(N), key=lambda r: qs[r])
        d=rs[r0]
        x0=Fraction(Qword(d),D)
        qmin_words += 1
        for m in range(1,N):
            # Proper suffix ending at the least rotation must have multiplicative slope <1.
            p=sum(d[N-m:])
            assert 3**p < (1<<m), (N,L,d,m,p)
            suffix_checks += 1

            # If a proper prefix is undercritical, its additive numerator must rescue it.
            pp=sum(d[:m])
            if (1<<m)>3**pp:
                B=Qword(d[:m])
                den=(1<<m)-3**pp
                xm=Fraction(Qword(d[m:]+d[:m]),D)
                assert xm>=x0
                assert B>=den*x0
                assert B<=max_prefix_Q(m,pp)
                # Strict for a primitive rotation class (no proper return to same state/word).
                if primitive(d):
                    assert B>den*x0
                prefix_rescue_checks += 1

# Exact inherited external-floor diagnostic: R#>=2^71 forces all proper root prefixes
# through length 183 to be supercritical. At 184 the generic rescue bound first reaches it.
threshold=1<<71
first_reachable=None
threshold_pairs=0
for m in range(1,500):
    maxb=Fraction(0,1)
    maxp=None
    for p in range(1,m+1):
        if (1<<m)>3**p:
            b=Fraction(max_prefix_Q(m,p),(1<<m)-3**p)
            threshold_pairs += 1
            if b>maxb:
                maxb,maxp=b,p
    if maxb>=threshold:
        first_reachable=(m,maxp,maxb)
        break
assert first_reachable is not None
assert first_reachable[0:2]==(184,116), first_reachable
# Explicitly recheck all m<=183 are below floor.
for m in range(1,184):
    for p in range(1,m+1):
        if (1<<m)>3**p:
            assert Fraction(max_prefix_Q(m,p),(1<<m)-3**p) < threshold

# ---------- RL-L55 proper-factor block congruence ----------
def block_counts(w,a):
    return [sum(w[j*a:(j+1)*a]) for j in range(len(w)//a)]

def block_congruence_rhs(w,A,L,g):
    a=A//g; ell=L//g
    D0=(1<<a)-3**ell
    K=0
    rhs=0
    for j in range(g):
        bj=w[j*a:(j+1)*a]
        r=sum(bj)
        K += r
        E=K-(j+1)*ell
        # 3^{-E} modulo D0, times a common invertible factor 3^(L-ell).
        weight=pow(3,-E,D0)
        rhs=(rhs + weight*(Qword(bj)%D0))%D0
    return (pow(3,L-ell,D0)*rhs)%D0

block_congruence_checks=0
factor_divisibility_examples=0
for A in range(4,13):
    for L in range(2,A):
        g=gcd(A,L)
        if g<=1: continue
        D=(1<<A)-3**L
        if D<=0: continue
        a=A//g; ell=L//g
        D0=(1<<a)-3**ell
        if D0<=1: continue
        assert D%D0==0
        for comb in combinations(range(A),L):
            w=[0]*A
            for p in comb: w[p]=1
            assert Qword(w)%D0 == block_congruence_rhs(w,A,L,g)
            block_congruence_checks += 1
            if Qword(w)%D0==0 and primitive(w):
                factor_divisibility_examples += 1

# Explicit balanced primitive counterexample to naive D0 descent.
w=[1,0,0,0,0,1]
A=6;L=2;g=2;a=3;ell=1
D=(1<<A)-3**L
D0=(1<<a)-3**ell
assert D==55 and D0==5
assert primitive(w)
assert block_counts(w,a)==[1,1]
blocks=[w[:3],w[3:]]
assert [Qword(b) for b in blocks]==[1,4]
assert Qword(w)==35 and Qword(w)%D0==0 and Qword(w)%D!=0
assert block_congruence_rhs(w,A,L,g)==0

print('RL-8 verifier: PASS')
print('internal two-edge path checks:', internal_twoedge_checks)
print('overlap unit-factor checks:', overlap_unit_checks)
print('overlap factor-5 checks:', overlap_five_checks)
print('disjoint binomial checks:', disjoint_binomial_checks)
print('cyclic exact-two self-rotations through A<=16:', selfrot2_count)
print('D-divisible exact-two self-rotations:', selfrot2_divisible)
print('proper binomial-resonance parameter pairs through A<=200:', resonance_pairs)
print('least-rotation words audited:', qmin_words)
print('proper suffix slope checks:', suffix_checks)
print('underdense prefix rescue checks:', prefix_rescue_checks)
print('external-floor threshold pairs checked:', threshold_pairs)
print('first generic rescue bound reaching 2^71: m,p =', first_reachable[0], first_reachable[1])
print('block congruence checks:', block_congruence_checks)
print('primitive D0-divisible examples in block audit:', factor_divisibility_examples)
print('naive descent counterexample: A=6,L=2,w=100001,Q=35,D0=5,D=55')
