from math import gcd
from decimal import Decimal, getcontext

# RL-11 verifier for the mixed radius-3 branch.
# Standard-library only. The external Laurent-Mignotte-Nesterenko (LMN)
# theorem is not re-proved here; this script certifies every finite/numeric
# step used after invoking that published estimate.


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


def rho_mod(A,L,D):
    gg,r,s=bezout(L,A)
    assert gg==1 and r*L+s*A==1
    theta=(modpow_signed(2,r,D)*modpow_signed(3,s,D))%D
    assert pow(theta,L,D)==2%D
    assert pow(theta,A,D)==3%D
    return pow(theta,-1,D)


def canonical_bits(A,L,x,s):
    # Canonical cyclic event order: -1 at 0, +1 at x, -1 at s.
    g=[0]*A
    g[0]=-1; g[x]=1; g[s]=-1
    b=[]
    for t in range(A):
        w=sum(g[(t-r)%A] for r in range(1,L+1))
        b.append(-w)
    return b


# ---------------------------------------------------------------------------
# A. Canonical window lemma: binary solvability iff 0<x<s<=min(L,A-L).
# Verify the exact equivalence exhaustively in an abstract cyclic domain.
# ---------------------------------------------------------------------------
triangle_checks=0
triangle_valid=0
for A in range(4,41):
    for L in range(1,A):
        if gcd(A,L)!=1:
            continue
        for x in range(1,A):
            for s in range(x+1,A):
                b=canonical_bits(A,L,x,s)
                binary=all(v in (0,1) for v in b) and sum(b)==L
                triangle=(s<=min(L,A-L))
                assert binary==triangle, (A,L,x,s,b)
                triangle_checks += 1
                triangle_valid += int(binary)


# ---------------------------------------------------------------------------
# B. Boundary [2,1] classification in canonical coordinates.
# Natural adjacency changes rotation time by -L mod A.  Under the triangle,
# the two negative events are adjacent iff s=min(L,A-L).  The middle source
# bit is 0 for L<A/2 and 1 for L>A/2.
# ---------------------------------------------------------------------------
boundary_checks=0
for A in range(5,120):
    for L in range(2,A-1):
        if gcd(A,L)!=1:
            continue
        n=min(L,A-L)
        if n<2:
            continue
        s=n
        for x in range(1,s):
            b=canonical_bits(A,L,x,s)
            assert all(v in (0,1) for v in b)
            # Event t corresponds to cyclic natural edge; +1 natural edge
            # sends t -> t-L (mod A).
            neg={0,s}
            adjacent = ((-L)%A in neg) or ((s-L)%A in neg)
            assert adjacent
            if 2*L<A:
                # first natural negative edge is t=s, then t=0; middle bit b_s
                assert b[s]==0
            elif 2*L>A:
                # first natural negative edge is t=0, then t=s; middle bit b_0
                assert b[0]==1
            else:
                raise AssertionError("coprime excludes A=2L")
            boundary_checks += 1


# ---------------------------------------------------------------------------
# C. Elementary closure of the s=L boundary (L<A-L).
# Canonical congruence would force D | 2^(A-L+x)-1, but
# D>2^(A-1) while A-L+x <= A-1.
# ---------------------------------------------------------------------------
elementary_size_checks=0
for A in range(4,500):
    for L in range(1,A):
        if gcd(A,L)!=1 or 2*L>=A:
            continue
        D=(1<<A)-3**L
        if D<=1:
            continue
        # Since L<A/2, L <= (A-1)/2, so 3^L<2^(A-1).
        assert 3**L < (1<<(A-1))
        assert D > (1<<(A-1))
        for x in range(1,L):
            n=A-L+x
            assert n<=A-1
            assert (1<<n)-1 < (1<<(A-1)) < D
            elementary_size_checks += 1


# ---------------------------------------------------------------------------
# D. LMN numerical constants used in the infinite cutoff.
# Published estimate (for a1=2,a2=3,b1=A,b2=L):
# log Lambda >= -22*M^2*log2*log3,
# M=max(log(A/log3+L/log2)+0.06,21).
# After the resultant barrier, for L>=5 we have A<=2L and hence
# A/log3+L/log2 < 4L.  We certify that for every L>=52000 the LMN
# lower bound contradicts log Lambda < log 2 - c L, c=log(2/sqrt(3)).
# ---------------------------------------------------------------------------
getcontext().prec=80
D2=Decimal(2); D3=Decimal(3)
ln2=D2.ln(); ln3=D3.ln(); c=ln2-ln3/Decimal(2)
assert ln2 < Decimal('0.694')
assert ln3 < Decimal('1.099')
assert c > Decimal('0.1438')
L0=Decimal(52000)
# Constant M=21 branch.
LMN_const=Decimal(22)*(Decimal(21)**2)*Decimal('0.694')*Decimal('1.099')
upper_exponent=Decimal('0.1438')*L0-Decimal('0.694')
assert LMN_const < Decimal(7400)
assert upper_exponent > Decimal('7476')
assert upper_exponent > LMN_const
# Logarithmic M branch at L0, with S<4L.  The ratio
# (log(4L)+.06)^2/L decreases once log(4L)+.06>2, so this endpoint
# check covers all larger L.
logbranch=Decimal(22)*Decimal('0.694')*Decimal('1.099')*((Decimal(4)*L0).ln()+Decimal('0.06'))**2
assert logbranch < Decimal(2600)
assert upper_exponent > logbranch
assert (Decimal(4)*L0).ln()+Decimal('0.06') > 2


# ---------------------------------------------------------------------------
# E. Exact finite denominator-barrier scan for L<52000.
# For the remaining mixed cases s<L and s<=B=A-L, the nonzero resultant
# plus root-of-unity AM-GM estimate gives
#     D < 2^B * 3^(L/2),
# equivalently D^2 < 2^(2B) * 3^L.
# For L>=5 this barrier implies D/2^A < (sqrt(3)/2)^L < 1/2,
# so A is the least exponent with 2^A>3^L.  We scan that A exactly.
# Small L=3,4 are handled explicitly below.  L<3 cannot have 0<x<s<L.
# ---------------------------------------------------------------------------
expected=[
    (5,3,2,5),
    (7,4,3,47),
    (8,5,3,13),
    (13,8,5,1631),
    (27,17,10,5077565),
]
barrier_hits=[]

# Small L=3,4: enumerate A until the relative barrier fails; thereafter it
# can never recover because delta=1-3^L/2^A increases with A.
for L in (3,4):
    p3=3**L
    A=L+1
    while (1<<A)<=p3:
        A+=1
    while True:
        B=A-L; D=(1<<A)-p3
        barrier=(B>=2 and D>1 and D*D < (1<<(2*B))*p3)
        if barrier and gcd(A,L)==1:
            barrier_hits.append((A,L,B,D))
        if not barrier:
            break
        A+=1

# L>=5: the barrier itself forces A to be minimal.
p3=3**4
Amin=1
p2=2
# initialize Amin,p2 correctly for L=4
while p2<=p3:
    Amin+=1; p2<<=1
for L in range(5,52000):
    p3*=3
    while p2<=p3:
        Amin+=1; p2<<=1
    A=Amin; B=A-L; D=p2-p3
    if B>=2 and D>1 and gcd(A,L)==1 and D*D < (1<<(2*B))*p3:
        barrier_hits.append((A,L,B,D))

assert barrier_hits==expected, barrier_hits


# ---------------------------------------------------------------------------
# F. Exact modular elimination of every finite barrier candidate.
# Check all canonical triples 0<x<s<=min(L,B), with s<L (the s=L boundary
# was already eliminated in C).  There are no zeros.
# ---------------------------------------------------------------------------
finite_triples=0
finite_zeros=[]
for A,L,B,D in barrier_hits:
    rho=rho_mod(A,L,D)
    assert pow(rho,L,D)==pow(2,-1,D)
    assert pow(rho,A,D)==pow(3,-1,D)
    for s in range(2,min(L,B)+1):
        if s>=L:
            continue
        for x in range(1,s):
            finite_triples += 1
            val=(1-pow(rho,x,D)+pow(rho,s,D))%D
            if val==0:
                finite_zeros.append((A,L,B,D,x,s))
assert finite_zeros==[]


print("RL-11 mixed radius-3 closure verifier: PASS")
print("canonical triangle equivalence checks:", triangle_checks)
print("canonical binary triples:", triangle_valid)
print("[2,1] boundary/local-pattern checks:", boundary_checks)
print("elementary s=L size checks:", elementary_size_checks)
print("certified c=log(2/sqrt(3)) > 0.1438:", c)
print("LMN constant-branch upper magnitude bound:", LMN_const)
print("LMN log-branch magnitude at L=52000:", logbranch)
print("finite exact denominator-barrier candidates (L<52000):", barrier_hits)
print("canonical triples checked on finite candidates:", finite_triples)
print("finite canonical zeros:", finite_zeros)

# ---------------------------------------------------------------------------
# G. Forward-looking same-direction one-orbit arc-cover lemma.
# For e=+3 and gcd(A,m)=gcd(A,L)=1, put kappa=m^{-1} mod A and
# r=-kappa mod A. Then 3r == L (mod A). Three negative flow events each
# contribute an r-arc; if u is the cover multiplicity, the source bit is
# b=u-j where 3r=L+jA. Binary solvability is exactly u in {j,j+1}.
# This does not close the same-direction branch; it is checked here as the
# next structural normal form.
# ---------------------------------------------------------------------------
from itertools import combinations
cover_checks=0
for A in range(5,25):
    for L in range(1,A):
        if gcd(A,L)!=1 or A%3==0:
            continue
        rs=[r for r in range(1,A) if (3*r-L)%A==0]
        assert len(rs)==1
        r=rs[0]
        j=(3*r-L)//A
        assert j in (0,1,2)
        for qs in combinations(range(A),3):
            u=[0]*A
            for q in qs:
                for z in range(1,r+1):
                    u[(q+z)%A]+=1
            b=[v-j for v in u]
            binary=all(v in (0,1) for v in b)
            cover=all(v in (j,j+1) for v in u)
            assert binary==cover
            if binary:
                assert sum(b)==L
            cover_checks += 1
print("same-direction arc-cover checks:", cover_checks)
