from math import gcd
from itertools import combinations

# RL-12 verifier: same-direction canonical gap reductions.
# Standard-library only.  The BCZ and LMN external theorems used for the
# non-effective finiteness statement are NOT re-proved here.


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


def theta_sigma(A,L,D):
    gg,r,s=bezout(L,A)
    assert gg==1 and r*L+s*A==1
    theta=(modpow_signed(2,r,D)*modpow_signed(3,s,D))%D
    assert pow(theta,L,D)==2%D
    assert pow(theta,A,D)==3%D
    sigma=pow(theta,-3,D)
    assert pow(sigma,L,D)==pow(8,-1,D)
    assert pow(sigma,A,D)==pow(27,-1,D)
    return theta,sigma


def cyclic_gaps(A,qs):
    q=sorted(qs)
    return (q[1]-q[0], q[2]-q[1], A-q[2]+q[0])


def cover(A,r,qs):
    u=[0]*A
    for q in qs:
        for z in range(1,r+1):
            u[(q+z)%A]+=1
    return u

# ---------------------------------------------------------------------------
# A. RL-L75: exact circular-gap simplex for the one-orbit arc cover.
# ---------------------------------------------------------------------------
gap_checks=0
gap_valid=0
adjacency_checks=0
for A in range(5,46):
    if A%3==0:
        continue
    for L in range(1,A):
        if gcd(A,L)!=1:
            continue
        r=(L*pow(3,-1,A))%A
        assert 1<=r<A
        j=(3*r-L)//A
        assert j in (0,1,2)
        h=min(r,A-r)
        for q1,q2 in combinations(range(1,A),2):
            qs=(0,q1,q2)
            d=cyclic_gaps(A,qs)
            u=cover(A,r,qs)
            binary_cover=all(v in (j,j+1) for v in u)
            if j==0:
                predicted=all(x>=r for x in d)
                if predicted:
                    slack=tuple(x-r for x in d)
                    assert sum(slack)==A-L
            elif j==2:
                R=A-r
                predicted=all(x>=R for x in d)
                if predicted:
                    slack=tuple(x-R for x in d)
                    assert sum(slack)==L
            else:
                predicted=all(x<=h for x in d)
                if predicted:
                    slack=tuple(h-x for x in d)
                    assert sum(slack)==min(L,A-L)
            assert binary_cover==predicted, (A,L,r,j,qs,d,u)
            if binary_cover:
                # Natural adjacent flow edges differ by +/-r in event time.
                q=list(qs)
                adj=0
                for x,y in combinations(q,2):
                    dd=(y-x)%A
                    if dd in (r,A-r):
                        adj+=1
                assert adj==sum(v==0 for v in slack), (A,L,r,j,qs,d,slack,adj)
                adjacency_checks += 1
                gap_valid += 1
            gap_checks += 1

# ---------------------------------------------------------------------------
# B. RL-L76: the one-orbit sparse form reduces to P2 or P3 on the simplex.
# P2=1+2 X^x+4 X^(x+y), side L.
# P3=4+6 X^x+9 X^(x+y), side B=A-L.
# ---------------------------------------------------------------------------
canonical_identity_checks=0
boundary_identity_checks=0
for A in range(5,90):
    if A%3==0:
        continue
    p2A=1<<A
    p3=1
    for L in range(1,A):
        p3*=3
        if gcd(A,L)!=1 or p2A<=p3:
            continue
        D=p2A-p3
        if D<=1:
            continue
        theta,sigma=theta_sigma(A,L,D)
        r=(L*pow(3,-1,A))%A
        j=(3*r-L)//A
        assert pow(sigma,r,D)==(pow(2*pow(3,j),-1,D))%D
        for d1 in range(1,A-1):
            for d2 in range(1,A-d1):
                d3=A-d1-d2
                d=(d1,d2,d3)
                if j==0:
                    valid=all(v>=r for v in d)
                    if not valid: continue
                    x1,x2,x3=(v-r for v in d)
                    N=A-L; typ='P3'; x,y=x1,x2
                    assert x1+x2+x3==N
                    F=(1+3*pow(sigma,d1,D)+9*pow(sigma,d1+d2,D))%D
                    P=(4+6*pow(sigma,x,D)+9*pow(sigma,x+y,D))%D
                    assert (4*F-P)%D==0
                elif j==2:
                    R=A-r
                    valid=all(v>=R for v in d)
                    if not valid: continue
                    x1,x2,x3=(v-R for v in d)
                    N=L; typ='P2'; x,y=x1,x2
                    assert x1+x2+x3==N
                    F=(1+3*pow(sigma,d1,D)+9*pow(sigma,d1+d2,D))%D
                    P=(1+2*pow(sigma,x,D)+4*pow(sigma,x+y,D))%D
                    assert (F-P)%D==0
                else:
                    h=min(r,A-r)
                    valid=all(v<=h for v in d)
                    if not valid: continue
                    x1,x2,x3=(h-v for v in d)
                    N=min(L,A-L)
                    assert x1+x2+x3==N
                    F=(1+3*pow(sigma,d1,D)+9*pow(sigma,d1+d2,D))%D
                    if 2*L<A:
                        typ='P2'; assert N==L
                        x,y=x2,x1
                        P=(1+2*pow(sigma,x,D)+4*pow(sigma,x+y,D))%D
                        factor=(4*pow(sigma,x1+x2,D))%D
                        assert (factor*F-P)%D==0
                    else:
                        typ='P3'; assert N==A-L
                        x,y=x2,x1
                        P=(4+6*pow(sigma,x,D)+9*pow(sigma,x+y,D))%D
                        factor=(9*pow(sigma,x1+x2,D))%D
                        assert (factor*F-P)%D==0
                canonical_identity_checks += 1

                # If exactly one simplex coordinate vanishes, cyclic relabeling
                # gives the two equivalent binomial boundary presentations.
                xx=[x1,x2,x3]
                if sum(v==0 for v in xx)==1:
                    k0=xx.index(0)
                    t=xx[(k0+1)%3]
                    z=xx[(k0+2)%3]
                    if typ=='P2':
                        assert N==L and t+z==L
                        b1=(3+4*pow(sigma,t,D))%D
                        b2=(1+6*pow(sigma,z,D))%D
                        assert (b1==0)==(b2==0)
                    else:
                        assert N==A-L and t+z==A-L
                        b1=(10+9*pow(sigma,t,D))%D
                        b2=(4+15*pow(sigma,z,D))%D
                        assert (b1==0)==(b2==0)
                    boundary_identity_checks += 1

# ---------------------------------------------------------------------------
# C. RL-L77: gcd(A,m)=3 branch.  Exactly one G=-1 event per prefix-index
# residue mod 3; orbit populations ell_0+ell_1+ell_2=L give the same P2 form.
# ---------------------------------------------------------------------------
def Qword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    LL=len(pos)
    return sum((1<<(p-1))*3**(LL-k-1) for k,p in enumerate(pos))


def rot(w,m):
    return w[m:]+w[:m]


def Hseq(w):
    A=len(w); L=sum(w); p=0; H=[0]
    for i,b in enumerate(w,1):
        p+=b; H.append(A*p-i*L)
    assert H[-1]==0
    return H


def prefix_diff(source,target):
    A=len(source); out=[0]; s=0
    for i in range(A-1):
        s += target[i]-source[i]
        out.append(s)
    return out


def solve_rotation_from_flow(A,m,F):
    delta=[0]*A; prev=0
    for i in range(A-1):
        delta[i]=F[i]-prev; prev=F[i]
    delta[A-1]=-prev
    H=gcd(A,m); partial=[{}]
    for r0 in range(H):
        vals={r0:0}; r=r0
        while True:
            nr=(r+m)%A; nv=vals[r]+delta[r]
            if nr in vals:
                if nv!=vals[nr]: return []
                break
            vals[nr]=nv; r=nr
        lo=min(vals.values()); hi=max(vals.values())
        if hi-lo>1: return []
        opts=[]
        for c in range(-lo,2-hi):
            z={r:vals[r]+c for r in vals}
            if all(v in (0,1) for v in z.values()): opts.append(z)
        if not opts: return []
        partial=[{**base,**o} for base in partial for o in opts]
    return [[z[i] for i in range(A)] for z in partial]

three_orbit_structural=0
three_orbit_sparse_checks=0
three_orbit_residue_checks=0
for A in range(6,37,3):
    a=A//3
    for m in range(3,A,3):
        if gcd(A,m)!=3:
            continue
        n=m//3
        kappa=pow(n,-1,a)
        for j1,j2 in combinations(range(1,A-1),2):
            F=[0]*(A-1)
            F[0]=F[j1]=F[j2]=-1
            for d in solve_rotation_from_flow(A,m,F):
                L=sum(d)
                if not (0<L<A) or gcd(A,L)!=1:
                    continue
                D=(1<<A)-3**L
                if D<=1:
                    continue
                target=rot(d,m)
                G=prefix_diff(d,target)
                e=A*sum(d[:m])-m*L
                if e!=3:
                    continue
                assert sum(abs(v) for v in G)==3
                assert [v for v in G if v]==[-1,-1,-1]
                events=[i for i,v in enumerate(G) if v==-1]
                assert len(events)==3
                # Orbit consistency forces exactly one event in each residue class.
                assert sorted(i%3 for i in events)==[0,1,2]
                three_orbit_residue_checks += 1

                ev={i%3:i for i in events}
                ss={h:(ev[h]-h)//3 for h in range(3)}
                pp={h:(kappa*ss[h])%a for h in range(3)}
                direct=tuple(sum(d[h+3*s] for s in range(a)) for h in range(3))
                ell0,ell1,ell2=direct
                # The first two orbit populations are exact lifted event-time
                # differences; a coincident endpoint can give 0 or a depending
                # on the orbit's constant source bit, and the lift by d[0],d[1]
                # records that case automatically.
                assert ell0==pp[1]-pp[0]+a*d[0], (A,m,L,d,events,pp,direct)
                assert ell1==pp[2]-pp[1]+a*d[1], (A,m,L,d,events,pp,direct)
                ells=direct
                assert sum(ells)==L

                theta,sigma=theta_sigma(A,L,D)
                H=Hseq(d)
                Z=sum(modpow_signed(theta,-H[i],D) for i in range(A))%D
                T=sum(pow(sigma,u,D) for u in range(a))%D
                assert T*(1-sigma)%D == (1-pow(sigma,a,D))%D
                assert pow(sigma,a,D)==pow(3,-1,D)
                assert gcd(T,D)==1
                P=(1+2*pow(sigma,ell0,D)+4*pow(sigma,ell0+ell1,D))%D
                # exponent 1-a+pp0 may be negative.
                factor=(T*modpow_signed(sigma,1-a+pp[0],D))%D
                assert Z==(factor*P)%D, (A,m,L,d,events,ells,Z,P,factor)
                assert (Qword(d)%D==0)==(P==0)
                three_orbit_sparse_checks += 1
                three_orbit_structural += 1

# ---------------------------------------------------------------------------
# D. RL-L78/L79 exact boundary identities and Jacobi filters.
# ---------------------------------------------------------------------------
p2_boundary_checks=0
p2_evenL_killed=0
p3_boundary_checks=0
p3_mod5_killed=0
p3_jacobi_killed=0
for A in range(5,260):
    p2A=1<<A; p3=1
    for L in range(1,A):
        p3*=3
        if gcd(A,L)!=1 or p2A<=p3:
            continue
        D=p2A-p3
        if D<=1:
            continue
        theta,sigma=theta_sigma(A,L,D)
        # Determine which canonical family applies.
        if A%3==0:
            typ,N='P2',L
        else:
            r=(L*pow(3,-1,A))%A
            j=(3*r-L)//A
            if j==0:
                typ,N='P3',A-L
            elif j==2:
                typ,N='P2',L
            elif 2*L<A:
                typ,N='P2',L
            else:
                typ,N='P3',A-L
        for t in range(1,N):
            if typ=='P2':
                b=(3+4*pow(sigma,t,D))%D
                k=A-2*L+3*t
                # If the boundary congruence vanishes, theta^k=-1.
                if b==0:
                    assert modpow_signed(theta,k,D)==D-1
                    assert k!=0
                    nn=abs(k)
                    assert (pow(2,nn,D)-((-1)**L))%D==0
                    assert (pow(3,nn,D)-((-1)**A))%D==0
                # Jacobi theorem says no zero is possible for L even.
                if L%2==0:
                    assert b!=0
                    p2_evenL_killed += 1
                p2_boundary_checks += 1
            else:
                b=(10+9*pow(sigma,t,D))%D
                k=3*t-2*A+L
                if D%5==0:
                    assert b!=0
                    p3_mod5_killed += 1
                # Compute (5/D)=(D/5), valid when 5 does not divide D.
                if D%5:
                    chi5=1 if D%5 in (1,4) else -1
                    jacobi_possible=(chi5*((-1)**(L*k)) == ((-1)**(L+1)))
                    if not jacobi_possible:
                        assert b!=0
                        p3_jacobi_killed += 1
                if b==0:
                    assert D%5
                    assert (5*modpow_signed(theta,k,D)+1)%D==0
                p3_boundary_checks += 1

# ---------------------------------------------------------------------------
# E. RL-F12: exact canonical no-zero diagnostic through A<=500.
# This scans a superset of structural cases: all P2/P3 compositions allowed
# by the new canonical lemmas.  O(N) per parameter pair via a power lookup.
# ---------------------------------------------------------------------------
scan_pairs=0
scan_x_tests=0
scan_zeros=[]
scan_family={'P2':0,'P3':0}
for A in range(5,501):
    p2A=1<<A; p3=1
    for L in range(1,A):
        p3*=3
        if gcd(A,L)!=1 or p2A<=p3:
            continue
        D=p2A-p3
        if D<=1:
            continue
        if A%3==0:
            typ,N='P2',L
        else:
            r=(L*pow(3,-1,A))%A
            j=(3*r-L)//A
            if j==0:
                typ,N='P3',A-L
            elif j==2:
                typ,N='P2',L
            elif 2*L<A:
                typ,N='P2',L
            else:
                typ,N='P3',A-L
        theta,sigma=theta_sigma(A,L,D)
        pw=[]; v=1; maxidx={}
        for e in range(N+1):
            pw.append(v); maxidx[v]=e; v=(v*sigma)%D
        c0,c1,c2=(1,2,4) if typ=='P2' else (4,6,9)
        invc2=pow(c2,-1,D)
        for x in range(N+1):
            target=(-(c0+c1*pw[x])*invc2)%D
            if maxidx.get(target,-1)>=x:
                # Rare-path exact enumeration if a lookup says a zero may occur.
                for s in range(x,N+1):
                    if pw[s]==target:
                        scan_zeros.append((A,L,D,typ,N,x,s))
            scan_x_tests += 1
        scan_pairs += 1
        scan_family[typ] += 1

assert scan_zeros==[], scan_zeros

print('RL-12 same-direction canonical verifier: PASS')
print('one-orbit gap triples checked:', gap_checks)
print('valid equal-arc covers:', gap_valid)
print('adjacency/slack-zero checks:', adjacency_checks)
print('one-orbit canonical sparse identities:', canonical_identity_checks)
print('[2,1] cyclic boundary identity checks:', boundary_identity_checks)
print('three-orbit structural solutions checked:', three_orbit_structural)
print('three-orbit one-event-per-residue checks:', three_orbit_residue_checks)
print('three-orbit P2 sparse equivalence checks:', three_orbit_sparse_checks)
print('P2 boundary instances checked:', p2_boundary_checks)
print('P2 even-L instances excluded by Jacobi:', p2_evenL_killed)
print('P3 boundary instances checked:', p3_boundary_checks)
print('P3 instances excluded because 5|D:', p3_mod5_killed)
print('additional P3 instances excluded by Jacobi:', p3_jacobi_killed)
print('canonical parameter pairs through A<=500:', scan_pairs, scan_family)
print('O(N) canonical x-tests through A<=500:', scan_x_tests)
print('canonical zeros through A<=500:', scan_zeros)

# ---------------------------------------------------------------------------
# F. RL-L78/RL-L79: gcd(A,m)=3 denominator barrier tail + finite certificate.
# Analytic input proved in the report:
#   every surviving three-orbit P2 composition with A=3a forces D^2 < 61^a.
# External tail input: the same LMN theorem already used in RL-11.
# The finite reduction uses Legendre's continued-fraction criterion.
# ---------------------------------------------------------------------------
from decimal import Decimal, getcontext
getcontext().prec=120
ln2=Decimal(2).ln(); ln3=Decimal(3).ln()
root61=Decimal(61).sqrt()
q=root61/Decimal(8)
c=(Decimal(8)/root61).ln()
assert c > Decimal('0.024')
# For a>=310000, delta<D/8^a<q^a and q^a<1/2 imply
# log Lambda < log 2 - c a.  In the M=21 LMN branch this already
# contradicts the published lower bound.
lmn_const=Decimal(22)*(Decimal(21)**2)*ln2*ln3
assert lmn_const < Decimal(7400)
assert Decimal('0.024')*Decimal(310000)-Decimal('0.694') > Decimal(7439)
assert Decimal('0.024')*Decimal(310000)-Decimal('0.694') > lmn_const
# At a=310000 the logarithmic M branch has not started; once it starts,
# (log(6a)+.06)^2/a is decreasing, so the linear upper exponent only wins more.
assert (Decimal(6)*Decimal(310000)).ln()+Decimal('0.06') < Decimal(21)

# Legendre threshold.  For a>=291, q^a < log(3)/(4a); the left/right ratio
# thereafter decreases because q*(a+1)/a < 1.
assert q**Decimal(291) < ln3/(Decimal(4)*Decimal(291))
assert q*(Decimal(292)/Decimal(291)) < 1

# Continued fraction prefix for beta=log(8)/log(3), enough to pass denominator
# 310000.  Decimal.ln is used only to certify this finite CF prefix; all
# denominator-barrier tests below are exact integer arithmetic.
beta=(Decimal(8).ln()/ln3)
cf=[]; conv=[]
x=beta
p_m2,p_m1=0,1; q_m2,q_m1=1,0
for _ in range(20):
    aa=int(x)
    cf.append(aa)
    p=aa*p_m1+p_m2; qq=aa*q_m1+q_m2
    conv.append((p,qq))
    p_m2,p_m1=p_m1,p; q_m2,q_m1=q_m1,qq
    if qq>310000:
        break
    x=1/(x-Decimal(aa))
expected_cf=[1,1,8,3,18,2,7,2,8,1,1,18]
assert cf==expected_cf, (cf,conv)
cf_below=[]
for p,qq in conv:
    if 291<=qq<310000 and Decimal(p)/Decimal(qq) < beta:
        cf_below.append((qq,p))
expected_cf_below=[(513,971),(7891,14936),(142579,269872),(301994,571611)]
assert cf_below==expected_cf_below, cf_below
cf_barrier_fail=[]
for a,L in cf_below:
    D=pow(8,a)-pow(3,L)
    assert D>0
    ok=(D*D < pow(61,a))
    cf_barrier_fail.append((a,L,ok))
assert all(not ok for _,_,ok in cf_barrier_fail)

# Exact small-denominator barrier scan for a<291.  These are the only pairs
# in that range satisfying gcd(3a,L)=1, D>1, and D^2<61^a.
small_barrier=[]
for a in range(1,291):
    A=3*a
    p8=pow(8,a); p3=1
    for L in range(1,A):
        p3*=3
        D=p8-p3
        if D<=1:
            break
        if gcd(A,L)==1 and D*D < pow(61,a):
            small_barrier.append((a,L,D))
expected_small_pairs=[
    (1,1),(3,4),(3,5),(4,7),(5,8),(6,11),(7,13),(9,16),(9,17),
    (11,20),(15,28),(17,32),(20,37),(22,41),(23,43),(25,47),
    (26,49),(33,62),(37,70),(44,83),(55,104),(64,121),(83,157),
    (93,176),(102,193),(121,229),
]
assert [(a,L) for a,L,D in small_barrier]==expected_small_pairs

# Exact elimination of every admissible three-orbit population composition on
# those 26 barrier pairs.  Each orbit has size a, so 0<=ell_h<=a and sum=L.
small_compositions=0
small_zeros=[]
for a,L,D in small_barrier:
    A=3*a
    theta,sigma=theta_sigma(A,L,D)
    for ell0 in range(a+1):
        for ell1 in range(a+1):
            ell2=L-ell0-ell1
            if not (0<=ell2<=a):
                continue
            small_compositions += 1
            val=(1+2*pow(sigma,ell0,D)+4*pow(sigma,ell0+ell1,D))%D
            if val==0:
                small_zeros.append((a,L,D,ell0,ell1,ell2))
assert small_zeros==[], small_zeros

print('three-orbit LMN cutoff a<:', 310000)
print('three-orbit continued-fraction lower candidates [291,310000):', cf_below)
print('continued-fraction barrier outcomes:', cf_barrier_fail)
print('three-orbit small exact barrier pairs (a<291):', [(a,L) for a,L,D in small_barrier])
print('three-orbit admissible compositions checked on barrier pairs:', small_compositions)
print('three-orbit finite canonical zeros:', small_zeros)
