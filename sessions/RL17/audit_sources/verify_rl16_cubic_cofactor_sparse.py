from itertools import product
from math import gcd

# Finite structural audit for RL-L104.
# This is NOT the proof of the infinite lemma; the proof is algebraic in the
# companion note.  The audit checks all identities on a broad constructive
# sample of exact gcd(A,L)=3, gcd(A,m)=1, e=+3 radius-3 flows through A<25.


def Qword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    L=len(pos)
    return sum((1<<(p-1))*3**(L-k-1) for k,p in enumerate(pos))


def rot(w,m):
    return w[m:]+w[:m]


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

checks=0
sparse_implication_checks=0
third_repeat_identity_checks=0

for A in range(6,25,3):
    a=A//3
    for m in range(1,A):
        if gcd(A,m)!=1:
            continue
        for j in range(1,A-1):
            for k in range(j+1,A-1):
                # Same-direction orientation G=-1 on all three used edges.
                F=[0]*(A-1); F[0]=F[j]=F[k]=-1
                for d in solve_rotation_from_flow(A,m,F):
                    L=sum(d)
                    if gcd(A,L)!=3:
                        continue
                    ell=L//3
                    DD=(1<<A)-3**L
                    if DD<=1:
                        continue
                    p=sum(d[:m])
                    if a*p-m*ell!=1:
                        continue

                    X=1<<a; Y=3**ell
                    C=X*X+X*Y+Y*Y
                    assert DD==(X-Y)*C
                    omega=X*pow(Y,-1,C)%C
                    assert (omega*omega+omega+1)%C==0
                    assert pow(omega,3,C)==1

                    theta=pow(pow(2,m,C),-1,C)*pow(3,p,C)%C
                    rho=pow(theta,-1,C)
                    assert pow(theta,a,C)==3*pow(omega,-m,C)%C
                    assert pow(theta,ell,C)==2*pow(omega,-p,C)%C
                    assert 27*pow(rho,3*a,C)%C==1

                    target=rot(d,m)
                    G=prefix_diff(d,target)
                    events=[]; N=0; S=0
                    for t in range(A):
                        i=(t*m)%A
                        Pi=sum(d[:i])
                        K=a*Pi-i*ell
                        # Actual equality follows from the recurrence once the
                        # canonical representative i_t is used; modulo 3a is
                        # enough for the phase identity and is audited here.
                        assert (K-(t-a*N))%(3*a)==0
                        T=p*i-m*Pi
                        assert i==m*K+a*T
                        assert (T-m*N)%3==0

                        W=pow(2,i,C)*pow(pow(3,Pi,C),-1,C)%C
                        phase=pow(rho,t,C)*pow(3,N,C)%C
                        assert W==phase
                        S=(S+W)%C

                        if G[i]:
                            assert G[i]==-1
                            events.append(t)
                            N+=1

                    assert len(events)==3 and N==3
                    alpha,beta,gamma=events
                    sparse=(pow(rho,alpha,C)+3*pow(rho,beta,C)+9*pow(rho,gamma,C))%C
                    assert ((1-rho)*S-2*rho*sparse)%C==0
                    assert (4*Qword(d)-pow(3,L,C)*S)%C==0
                    if Qword(d)%C==0:
                        assert sparse==0
                    sparse_implication_checks+=1

                    # Algebraic singularity of exact a-spaced jump times.
                    sing=(1+3*pow(rho,a,C)+9*pow(rho,2*a,C))%C
                    assert sing==(1+pow(omega,m,C)+pow(omega,2*m,C))%C
                    assert sing==0
                    third_repeat_identity_checks+=1
                    checks+=1

print('RL-16 cubic-cofactor sparse-reduction audit: PASS')
print('exact gcd(A,L)=3 one-orbit structural solutions audited:',checks)
print('cofactor sparse implication checks:',sparse_implication_checks)
print('exact-third-repeat singularity checks:',third_repeat_identity_checks)
