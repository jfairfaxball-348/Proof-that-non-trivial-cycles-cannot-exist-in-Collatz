from itertools import product
from math import gcd
from collections import Counter


def Qword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    L=len(pos)
    return sum((1<<(p-1))*3**(L-k-1) for k,p in enumerate(pos))


def rot(w,m):
    m%=len(w)
    return w[m:]+w[:m]


def primitive(w):
    A=len(w)
    return all(w != rot(w,m) for m in range(1,A))


def linear_flow(a,b):
    # Cumulative target-source count on each internal edge.
    s=0; out=[]
    for i in range(len(a)-1):
        s += b[i]-a[i]
        out.append(s)
    assert s + (b[-1]-a[-1]) == 0
    return out


def linear_dist(a,b):
    return sum(abs(x) for x in linear_flow(a,b))


def components(a,b):
    f=linear_flow(a,b)
    out=[]; start=None
    for i,x in enumerate(f):
        if x!=0 and start is None:
            start=i
        if x==0 and start is not None:
            out.append((start,i))  # vertex interval start..i, run length i-start
            start=None
    if start is not None:
        out.append((start,len(a)-1))
    return out


def bezout(a,b):
    old_r,r=a,b; old_s,s=1,0; old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    return old_r,old_s,old_t


def modpow_signed(a,e,n):
    if e>=0:
        return pow(a,e,n)
    return pow(pow(a,-1,n),-e,n)


def Hseq(w):
    A=len(w); L=sum(w); p=0; H=[0]
    for i,b in enumerate(w,1):
        p += b
        H.append(A*p-i*L)
    assert H[-1]==0
    return H


def prefix_diff(source,target):
    # G_i = ones(target[:i])-ones(source[:i]), for i=0,...,A-1.
    A=len(source); out=[0]; s=0
    for i in range(A-1):
        s += target[i]-source[i]
        out.append(s)
    return out


def solve_rotation_from_flow(A,m,F):
    # F length A-1; solve d[r+m]-d[r]=delta[r].
    delta=[0]*A
    prev=0
    for i in range(A-1):
        delta[i]=F[i]-prev
        prev=F[i]
    delta[A-1]=-prev

    H=gcd(A,m)
    partial=[{}]
    for r0 in range(H):
        vals={r0:0}; r=r0
        while True:
            nr=(r+m)%A
            nv=vals[r]+delta[r]
            if nr in vals:
                if nv!=vals[nr]:
                    return []
                break
            vals[nr]=nv; r=nr
        lo=min(vals.values()); hi=max(vals.values())
        if hi-lo>1:
            return []
        opts=[]
        for c in range(-lo,2-hi):
            z={r:vals[r]+c for r in vals}
            if all(v in (0,1) for v in z.values()):
                opts.append(z)
        if not opts:
            return []
        partial=[{**base,**o} for base in partial for o in opts]
    return [[z[i] for i in range(A)] for z in partial]


# ---------------------------------------------------------------------------
# A. Pure linear distance-3 classification and exact local Q coefficients.
# ---------------------------------------------------------------------------
linear_pairs=0
connected_patterns=set()
partition_counts=Counter()
for n in range(2,9):
    for aa in product((0,1), repeat=n):
        for bb in product((0,1), repeat=n):
            if aa==bb or sum(aa)!=sum(bb):
                continue
            a=list(aa); b=list(bb)
            if linear_dist(a,b)!=3:
                continue
            linear_pairs += 1
            f=linear_flow(a,b)
            assert all(x in (-1,0,1) for x in f)
            assert sum(1 for x in f if x)!=0
            assert sum(1 for x in f if x)==3
            # Nonzero runs cannot change sign without passing through 0.
            for x,y in zip(f,f[1:]):
                assert not (x*y<0)
            lens=tuple(sorted((hi-lo for lo,hi in components(a,b)), reverse=True))
            assert lens in ((3,),(2,1),(1,1,1))
            partition_counts[lens]+=1
            if lens==(3,):
                lo,hi=components(a,b)[0]
                sub=a[lo:hi+1]; sub2=b[lo:hi+1]
                connected_patterns.add((tuple(sub),tuple(sub2),Qword(sub2)-Qword(sub)))

expected_connected={
    ((1,0,0,0),(0,0,0,1),7),
    ((1,0,1,0),(0,0,1,1),13),
    ((1,1,0,0),(0,1,0,1),9),
    ((1,1,1,0),(0,1,1,1),19),
    ((0,0,0,1),(1,0,0,0),-7),
    ((0,0,1,1),(1,0,1,0),-13),
    ((0,1,0,1),(1,1,0,0),-9),
    ((0,1,1,1),(1,1,1,0),-19),
}
assert connected_patterns==expected_connected

# ---------------------------------------------------------------------------
# B. Connected self-rotation geometry: coefficient 13 forces H=gcd(A,m)=3.
# Exhaustively certificate the local orbit statement in a broad finite range;
# the report gives the analytic three-case proof via q=3a mod A.
# ---------------------------------------------------------------------------
connected_h1_13=[]
connected_h_checks=0
for A in range(5,80):
    for m in range(1,A):
        H=gcd(A,m)
        if H not in (1,3):
            continue
        # Put the connected support on edges 0,1,2 with right-flow sign -1.
        F=[0]*(A-1)
        F[0]=F[1]=F[2]=-1
        for d in solve_rotation_from_flow(A,m,F):
            if sum(d) in (0,A):
                continue
            connected_h_checks += 1
            t=rot(d,m)
            assert linear_dist(d,t)==3 and components(d,t)==[(0,3)]
            c=Qword(t[:4])-Qword(d[:4])
            if abs(c)==13 and H==1:
                connected_h1_13.append((A,m,tuple(d)))
assert connected_h1_13==[]

# ---------------------------------------------------------------------------
# C. Constructive exact radius-3 self-rotation scan through A<=40.
# Quotient cyclic translation by placing the first used edge at 0 and choosing
# an unused boundary edge. This covers every cyclic distance-3 support.
# ---------------------------------------------------------------------------
MAX_A=40
structural_solutions=0
branch_counts=Counter()
delta_divisible=[]
q_divisible=[]
primitive_delta_divisible=[]

for A in range(4,MAX_A+1):
    for m in range(1,A):
        for j in range(1,A-1):
            for k in range(j+1,A-1):
                for signs in product((-1,1), repeat=3):
                    # Adjacent nonzero flow edges must have the same sign.
                    if j==1 and signs[1]!=signs[0]:
                        continue
                    if k==j+1 and signs[2]!=signs[1]:
                        continue
                    F=[0]*(A-1)
                    F[0]=signs[0]; F[j]=signs[1]; F[k]=signs[2]
                    for d in solve_rotation_from_flow(A,m,F):
                        L=sum(d)
                        if not (0<L<A):
                            continue
                        D=(1<<A)-3**L
                        if D<=1:
                            continue
                        t=rot(d,m)
                        assert linear_flow(d,t)==F
                        assert linear_dist(d,t)==3
                        structural_solutions += 1
                        lens=tuple(sorted((hi-lo for lo,hi in components(d,t)), reverse=True))
                        branch_counts[lens]+=1
                        e=A*sum(d[:m])-m*L
                        assert abs(e) in (1,3)
                        assert gcd(A,L) in (1,3)
                        if abs(e)==1:
                            assert gcd(A,L)==1 and gcd(A,m)==1
                        dq=Qword(t)-Qword(d)
                        if dq % D == 0:
                            row=(A,L,D,m,j,k,signs,tuple(d),dq//D,lens)
                            delta_divisible.append(row)
                            if primitive(d):
                                primitive_delta_divisible.append(row)
                        if Qword(d)%D==0:
                            q_divisible.append((A,L,D,m,tuple(d),lens))

# Exactly the threefold trivial parity cycle, with orientations/shifts in m.
assert primitive_delta_divisible==[]
assert len(delta_divisible)==6
assert all(x[0:3]==(6,3,37) for x in delta_divisible)
assert {x[7] for x in delta_divisible}=={
    (1,0,1,0,1,0),(0,1,0,1,0,1)
}
# Any D-divisible solution in this normalized structural scan is the same repeat.
assert q_divisible
assert all((A,L,D)==(6,3,37) and not primitive(list(w))
           for A,L,D,m,w,lens in q_divisible)

# ---------------------------------------------------------------------------
# D. The Q geometric-sum identity and coprime three-jump normal forms.
# Check on every coprime structural solution through A<=18.
# ---------------------------------------------------------------------------
geom_checks=0
mixed_sparse_checks=0
same_sparse_checks=0
for A in range(5,19):
    for m in range(1,A):
        for j in range(1,A-1):
            for k in range(j+1,A-1):
                for signs in product((-1,1), repeat=3):
                    if j==1 and signs[1]!=signs[0]:
                        continue
                    if k==j+1 and signs[2]!=signs[1]:
                        continue
                    F=[0]*(A-1); F[0]=signs[0];F[j]=signs[1];F[k]=signs[2]
                    for d in solve_rotation_from_flow(A,m,F):
                        L=sum(d)
                        if not (0<L<A) or gcd(A,L)!=1:
                            continue
                        D=(1<<A)-3**L
                        if D<=1:
                            continue
                        target=rot(d,m)
                        G=prefix_diff(d,target)
                        assert sum(abs(x) for x in G)==3
                        H=Hseq(d)
                        e=H[m]
                        if abs(e) not in (1,3):
                            continue
                        # recurrence H_{i+m}=H_i+e+A G_i on cyclic prefix indices
                        for i in range(A):
                            assert H[(i+m)%A] == H[i] + e + A*G[i]

                        gg,rcoef,scoef=bezout(L,A)
                        assert gg==1 and rcoef*L+scoef*A==1
                        theta=(modpow_signed(2,rcoef,D)*modpow_signed(3,scoef,D))%D
                        assert pow(theta,L,D)==2%D
                        assert pow(theta,A,D)==3%D

                        Z=sum(modpow_signed(theta,-H[i],D) for i in range(A))%D
                        assert (4*Qword(d)-pow(3,L,D)*Z)%D==0
                        geom_checks += 1

                        # We orient only the positive discrepancy cases; reversing m
                        # covers the negative ones in the theorem statement.
                        if e==1:
                            assert gcd(A,m)==1
                            events=[]
                            for tt in range(A):
                                idx=(tt*m)%A
                                if G[idx]:
                                    events.append((tt,G[idx]))
                            assert len(events)==3 and sum(s for _,s in events)==-1
                            rr=pow(theta,-1,D)
                            # theta-1 is a unit: theta==1 mod p would imply 2==1 mod p.
                            assert gcd((theta-1)%D,D)==1
                            ts=[x for x,_ in events]; sig=tuple(s for _,s in events)
                            vals=[pow(rr,t,D) for t in ts]
                            if sig==(-1,-1,1):
                                form=(vals[0]+3*vals[1]-3*vals[2])%D
                            elif sig==(-1,1,-1):
                                form=(vals[0]-vals[1]+vals[2])%D
                            elif sig==(1,-1,-1):
                                form=(-vals[0]+vals[1]+3*vals[2])%D
                            else:
                                raise AssertionError(sig)
                            # D|Q iff the sparse form vanishes.
                            assert (Qword(d)%D==0) == (form==0)
                            mixed_sparse_checks += 1

                        if e==3 and gcd(A,m)==1:
                            events=[]
                            for tt in range(A):
                                idx=(tt*m)%A
                                if G[idx]:
                                    events.append((tt,G[idx]))
                            assert len(events)==3 and all(s==-1 for _,s in events)
                            sbase=modpow_signed(theta,-3,D)
                            assert gcd((1-sbase)%D,D)==1
                            vals=[pow(sbase,t,D) for t,_ in events]
                            form=(vals[0]+3*vals[1]+9*vals[2])%D
                            assert (Qword(d)%D==0) == (form==0)
                            same_sparse_checks += 1

print('RL-10 radius-3 verifier: PASS')
print('linear distance-3 pairs checked:', linear_pairs)
print('linear support partition counts:', dict(partition_counts))
print('connected local Q patterns:', sorted(connected_patterns))
print('connected H in {1,3} constructive checks through A<80:', connected_h_checks)
print('connected coefficient-13 / H=1 survivors:', connected_h1_13)
print('structural radius-3 solutions through A<=40:', structural_solutions)
print('structural branch counts:', dict(branch_counts))
print('D|DeltaQ structural survivors:', len(delta_divisible))
print('unique D|DeltaQ survivor words:', sorted({(x[0],x[1],x[2],x[7]) for x in delta_divisible}))
print('primitive D|DeltaQ structural survivors:', primitive_delta_divisible)
print('Q geometric identity checks:', geom_checks)
print('mixed e=+1 sparse-normal-form checks:', mixed_sparse_checks)
print('same-direction e=+3, H=1 sparse-normal-form checks:', same_sparse_checks)
