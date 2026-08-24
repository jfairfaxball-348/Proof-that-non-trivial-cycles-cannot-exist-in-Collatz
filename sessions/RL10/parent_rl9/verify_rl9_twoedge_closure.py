from itertools import combinations
from math import gcd

# ---------- helpers ----------
def Qword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    L=len(pos)
    return sum((1<<(p-1))*3**(L-k-1) for k,p in enumerate(pos))

def primitive(w):
    N=len(w)
    return all(w != w[m:]+w[:m] for m in range(1,N))

def rot(w,m): return w[m:]+w[:m]

def jacobi(a,n):
    assert n>0 and n%2==1
    a%=n; out=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): out=-out
        a,n=n,a
        if a%4==3 and n%4==3: out=-out
        a%=n
    return out if n==1 else 0

# ---------- RL9-A: Jacobi signature for D=2^A-3^L ----------
jacobi_checks=0
for A in range(3,100):
    for L in range(1,A):
        D=(1<<A)-3**L
        if D<=1: continue
        assert gcd(D,6)==1
        assert jacobi(2,D)==((-1)**L)
        assert jacobi(-1,D)==((-1)**(L+1))
        assert jacobi(3,D)==((-1)**(A+L+1))
        jacobi_checks+=1

# Plus resonance consequences: coprime L even impossible; coprime L odd => k even.
plus_symbol_checks=0
for A in range(3,260):
    for L in range(1,A):
        if gcd(A,L)!=1: continue
        D=(1<<A)-3**L
        if D<=1: continue
        r2={}
        for u in range(2,A-1):
            r2.setdefault((1<<u)%D,[]).append(u)
        r3=1
        for v in range(1,L):
            r3=(r3*3)%D
            for u in r2.get((-r3)%D,[]):
                plus_symbol_checks+=1
                assert L%2==1
                k=u*L-v*A
                assert k%2==0

# ---------- local path helpers ----------
def swap_internal(w,i):
    if not (0<=i<len(w)-1) or w[i]==w[i+1]: return None
    z=w.copy(); z[i],z[i+1]=z[i+1],z[i]
    return z

def move_sign(w,i): return 1 if w[i:i+2]==[1,0] else -1

def edge_weight(w,i): return (1<<i)*3**sum(w[i+2:])

# ---------- RL9-B: exhaustive exact cyclic length-two audit ----------
# Enumerate explicit ordered two-edge paths, then test when endpoint is a nontrivial rotation.
# This independently checks the analytic branch classification in a finite domain.
path_instances=0
primitive_divisible_survivors=[]
branch_counts={'overlap':0,'disjoint_same':0,'disjoint_opposite':0}
g1_parity_checks=0
g2_formula_checks=0
opp_kzero_checks=0

for A in range(3,14):
    for comb_len in range(1,A):
        L=comb_len
        D=(1<<A)-3**L
        if D<=1: continue
        for comb in combinations(range(A),L):
            base=[0]*A
            for p in comb: base[p]=1
            # Work cyclically by testing cuts that make a chosen pair of cyclic edges internal.
            # Simpler finite audit: rotate base through every cut and use internal edges.
            seen_paths=set()
            for cut in range(A):
                w=rot(base,cut)
                for i in range(A-1):
                    w1=swap_internal(w,i)
                    if w1 is None: continue
                    for j in range(A-1):
                        if j==i: continue
                        w2=swap_internal(w1,j)
                        if w2 is None or w2==w: continue
                        # endpoint must be a nontrivial rotation of this cut word
                        ms=[m for m in range(1,A) if rot(w,m)==w2]
                        if not ms: continue
                        key=(tuple(w),i,j,tuple(w2))
                        if key in seen_paths: continue
                        seen_paths.add(key)
                        path_instances+=1
                        m=ms[0]
                        P=sum(w[:m])
                        sdelta=A*P-m*L
                        if abs(i-j)==1:
                            branch_counts['overlap']+=1
                            assert abs(sdelta)==2
                        else:
                            left=min(i,j); right=max(i,j)
                            # for disjoint edges, signs can be read in the original word
                            eps_l=move_sign(w,left); eps_r=move_sign(w,right)
                            u=right-left
                            b_l=sum(w[left+2:]); b_r=sum(w[right+2:]); v=b_l-b_r
                            assert u>=2 and v>=1
                            if eps_l==eps_r:
                                branch_counts['disjoint_same']+=1
                                assert abs(sdelta)==2
                                g=gcd(A,L)
                                assert 2%g==0
                                # If coprime, determinant parity must be odd combinatorially.
                                if g==1:
                                    k=u*L-v*A
                                    assert k%2!=0
                                    g1_parity_checks+=1
                                # If g=2, orient path so both moves are right by reversing if necessary,
                                # then jointly rotate so first start is zero and verify half-det formulas.
                                if g==2:
                                    # Normalize original endpoint order to right moves.
                                    ww=w
                                    mm=m
                                    li,ri=left,right
                                    if eps_l==-1: # reverse path: w2 -> w, rotation becomes A-m
                                        ww=w2
                                        mm=(A-m)%A
                                        # in reversed word both old 01 pairs are now 10 at same starts
                                    # rotate first swap start to zero
                                    shift=li
                                    ww=rot(ww,shift)
                                    mm=mm
                                    u0=u
                                    assert ww[:2]==[1,0] and ww[u0:u0+2]==[1,0]
                                    a=A//2; ell=L//2; c=a-ell
                                    vv=sum(ww[:u0])
                                    k0=u0*ell-vv*a
                                    H=gcd(A,mm)
                                    assert H in (1,2)
                                    if H==1:
                                        rr=pow(mm,-1,A)
                                        U=(rr*u0)%A
                                        assert k0==a-U
                                        assert abs(k0)<a
                                    else:
                                        assert mm%2==0 and a%2==1 and u0%2==1
                                        n=mm//2
                                        rr=pow(n,-1,a)
                                        ww2=(u0-1)//2
                                        V=(rr*ww2)%a
                                        T=(rr*(ww2+1))%a
                                        assert V and T
                                        assert 2*k0==a-V-T
                                        assert abs(k0)<a
                                    if k0==0:
                                        assert u0==a and vv==ell
                                        assert ww[:a]==ww[a:]
                                    g2_formula_checks+=1
                            else:
                                branch_counts['disjoint_opposite']+=1
                                assert sdelta==0
                                g=gcd(A,L)
                                assert g>1
                                a=A//g; ell=L//g
                                assert m%a==0
                                H=gcd(A,m)
                                assert H>=2 and u%H==0
                                # orient so left edge is right and right edge is left, possibly reverse path
                                ww=w
                                if eps_l==-1:
                                    ww=w2
                                # positions remain left/right; now left pair is 10 and right pair 01
                                assert ww[left:left+2]==[1,0]
                                assert ww[right:right+2]==[0,1]
                                vv=sum(ww[left:right])
                                assert u*L==vv*A
                                opp_kzero_checks+=1

                        if Qword(w)%D==0 and primitive(w):
                            primitive_divisible_survivors.append((A,L,tuple(w),i,j,m))

assert primitive_divisible_survivors==[], primitive_divisible_survivors

# ---------- RL9-C: constructive g=2 determinant formulas, much larger than word brute force ----------
def solve_g2_word(A,m,u):
    # Solve d[r+m]-d[r]=delta[r] for two right swaps at starts 0,u.
    delta=[0]*A
    for p in (0,u):
        delta[p]-=1; delta[p+1]+=1
    H=gcd(A,m)
    if H not in (1,2): return []
    comps=[]; seen=set()
    for r0 in range(H):
        vals={r0:0}; orbit=[]; r=r0
        while True:
            orbit.append(r); seen.add(r)
            nr=(r+m)%A; nv=vals[r]+delta[r]
            if nr in vals:
                if nv!=vals[nr]: return []
                break
            vals[nr]=nv; r=nr
        arrvals=[vals[r] for r in orbit]
        mn,mx=min(arrvals),max(arrvals)
        if mx-mn>1: return []
        opts=[]
        for c0 in range(-mn,2-mx):
            z={r:vals[r]+c0 for r in orbit}
            if all(b in (0,1) for b in z.values()): opts.append(z)
        if not opts: return []
        comps.append(opts)
    out=[{}]
    for opts in comps:
        out=[{**b,**o} for b in out for o in opts]
    return [[z[r] for r in range(A)] for z in out]

constructive_g2=0
for a in range(2,46):
    for ell in range(1,a):
        if gcd(a,ell)!=1: continue
        A=2*a;L=2*ell
        # m ell == -1 mod a; at most two lifts modulo 2a
        base=(-pow(ell,-1,a))%a
        for m in sorted({base,base+a}):
            if not (0<m<A): continue
            if (m*ell+1)%a: continue
            for u in range(2,A-1):
                for d in solve_g2_word(A,m,u):
                    if sum(d)!=L or d[:2]!=[1,0] or d[u:u+2]!=[1,0]: continue
                    v=sum(d[:u]); k0=u*ell-v*a
                    H=gcd(A,m)
                    if H==1:
                        rr=pow(m,-1,A); U=(rr*u)%A
                        assert k0==a-U and abs(k0)<a
                    else:
                        assert a%2==1 and u%2==1
                        rr=pow(m//2,-1,a); w=(u-1)//2
                        V=(rr*w)%a; T=(rr*(w+1))%a
                        assert V and T and 2*k0==a-V-T and abs(k0)<a
                    if k0==0:
                        assert u==a and v==ell and d[:a]==d[a:]
                    constructive_g2+=1

# ---------- RL9-D: half-denominator arithmetic check for g=2 ----------
halfden_checks=0
for a in range(2,150):
    for ell in range(1,a):
        if gcd(a,ell)!=1: continue
        X=1<<a;Y=3**ell
        if X<=Y: continue
        Dp=X+Y
        # For every formal interior (u,v), if plus resonance holds, verify half-det congruence.
        D=(X-Y)*Dp
        r2={}
        for u in range(2,2*a-1): r2.setdefault((1<<u)%D,[]).append(u)
        rv=1
        for v in range(1,2*ell):
            rv=(rv*3)%D
            for u in r2.get((-rv)%D,[]):
                k0=u*ell-v*a
                if k0:
                    assert abs(k0)>=a
                else:
                    assert u==a and v==ell
                # exact D+ determinant congruence
                if k0>=0:
                    lhs=pow(2,k0,Dp)
                else:
                    lhs=pow(pow(2,-k0,Dp),-1,Dp)
                assert lhs==((-1)**(ell-v))%Dp
                halfden_checks+=1

# ---------- strengthened finite plus-resonance scan through A<=2000 ----------
# Size pruning: max proper plus numerator is 2^(A-2)+3^(L-1).
plus_hits=[]; size_candidates=0
for A in range(3,2001):
    # only the largest L with 3^L < 2^A can satisfy the max-size necessity;
    # determine it exactly without floating point.
    # rough seed from logs is avoided; increment powers iteratively per A would be slower, so binary search.
    lo,hi=1,A-1
    Lmax=0
    while lo<=hi:
        mid=(lo+hi)//2
        if 3**mid < (1<<A): Lmax=mid;lo=mid+1
        else: hi=mid-1
    if Lmax<1: continue
    for L in (Lmax,):
        D=(1<<A)-3**L
        if D<=1 or D>((1<<(A-2))+3**(L-1)): continue
        size_candidates+=1
        r2={}
        for u in range(2,A-1):r2.setdefault((1<<u)%D,[]).append(u)
        r3=1
        found=[]
        for v in range(1,L):
            r3=(r3*3)%D
            for u in r2.get((-r3)%D,[]): found.append((u,v))
        if found: plus_hits.append((A,L,D,gcd(A,L),tuple(found)))
assert [(x[0],x[1],x[2]) for x in plus_hits]==[(4,2,7),(8,5,13)], plus_hits

print('RL-9 verifier: PASS')
print('Jacobi signature checks:',jacobi_checks)
print('coprime plus-resonance symbol checks:',plus_symbol_checks)
print('exact cyclic two-edge path instances through A<=13:',path_instances)
print('branch counts:',branch_counts)
print('coprime determinant-parity checks:',g1_parity_checks)
print('g=2 half-determinant formula checks in word audit:',g2_formula_checks)
print('opposite-direction k=0 checks:',opp_kzero_checks)
print('primitive D-divisible length-two survivors:',primitive_divisible_survivors)
print('constructive g=2 formula checks through a<=45:',constructive_g2)
print('g=2 half-denominator arithmetic hits checked through a<=149:',halfden_checks)
print('plus-resonance size candidates through A<=2000:',size_candidates)
print('plus-resonance hits through A<=2000:',plus_hits)
