from fractions import Fraction
from itertools import product
from math import gcd


def Qword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    L=len(pos)
    return sum((1 << (p-1))*3**(L-k-1) for k,p in enumerate(pos))

def block_Q(w):
    return Qword(w)

def step(x,b):
    return (3*x+1)/2 if b else x/2

checks=0
for A in range(4,13):
    for w0 in product([0,1], repeat=A):
        w=list(w0); L=sum(w)
        if not (0<L<A):
            continue
        D=(1<<A)-3**L
        if D<=0:
            continue
        g=gcd(A,L)
        if g<=1:
            continue
        a=A//g; ell=L//g
        X=1<<a; Y=3**ell
        Q=Qword(w)
        R=Fraction(Q,D)  # rational fixed point of the word

        # Exact phase orbit from the rational fixed point.
        xs=[R]
        x=R
        for b in w:
            x=step(x,b)
            xs.append(x)
        assert xs[-1]==R

        # Block starts and imbalance path.
        K=0; E=[0]; r=[]; Qb=[]; y=[]
        for j in range(g):
            B=w[j*a:(j+1)*a]
            rr=sum(B); r.append(rr); K += rr
            E.append(K-(j+1)*ell)
            Qb.append(block_Q(B))
        assert E[-1]==0
        for j in range(g+1):
            y.append(xs[j*a] * Fraction(1,3**E[j]) if E[j]>=0 else xs[j*a]*3**(-E[j]))

        c=[]
        for j in range(g):
            scale=Fraction(1,3**E[j+1]) if E[j+1]>=0 else Fraction(3**(-E[j+1]),1)
            cj=scale*Qb[j]
            c.append(cj)
            assert cj == X*y[j+1]-Y*y[j]

        z=Fraction(X,Y)
        F=sum((z**j)*c[j] for j in range(g))
        assert F == Y*(z**g-1)*R
        assert (Y**(g-1))*F == Q
        checks += 1

print('RL20 canonical block-coboundary verifier: PASS')
print('exact rational word/block checks:', checks)
