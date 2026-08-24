#!/usr/bin/env python3
from fractions import Fraction
import heapq

# Certified (65,41) witness from RL46, used to regression-check the exact identities.
EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()

def witness_check():
    A,L,t=65,41,2
    k=t+3; r=L-3; m=A-k-1
    apos=[i for i,e in enumerate(EDGES) if e[0]=='1']
    bpos=[i for i,e in enumerate(EDGES) if e[1]=='1']
    assert len(EDGES)==m and len(apos)==len(bpos)==r
    # Prefix positivity d>=1 is equivalent to the j-th y=1 occurring no later
    # than the j-th x=1.
    assert all(b<=a for a,b in zip(apos,bpos))
    H=sum(a-b for a,b in zip(apos,bpos))
    assert H==104

    # Unrolled T recurrence, normalized by 3^r.
    zeta=Fraction(1<<A,3**L)
    lhs=Fraction(14,1)+Fraction(27,2)*zeta*(1-Fraction(1,1<<k))
    rhs=sum(Fraction(1<<a,3**j)*(3-Fraction(1,1<<(a-b)))
            for j,(a,b) in enumerate(zip(apos,bpos),1))
    assert lhs==rhs

    # Also check the integer unrolling before normalization.
    T0=-14; Tm=(1<<k)-1
    int_rhs=(3**r)*T0 + sum((3**(r-j))*(3*(1<<a)-(1<<b))
                            for j,(a,b) in enumerate(zip(apos,bpos),1))
    assert (1<<m)*Tm==int_rhs
    return H,lhs

def cap_upper_position(A,L,j):
    # At the j-th x=1 transition, with 0-based position a_j, current n=a_j+1
    # and p_alpha=j-1. Prefix cap:
    #   2^(a_j+3) 3^(2L) <= 3^(j+1) 2^(2A).
    # Thus 2^a_j <= floor(3^(j+1)2^(2A)/(8*3^(2L))).
    N=(3**(j+1))*(1<<(2*A))
    D=8*(3**(2*L))
    q=N//D
    return q.bit_length()-1 if q else -1

def relaxed_violation_upper(A,L,t):
    """Rigorous upper bound for the rank-position RHS under H <= k-1.

    We relax all parity/T constraints and all coupling between the displacement
    variables except their total area budget. If even this enlarged class cannot
    reach the exact terminal RHS, a strict violation is impossible.
    """
    q=A-L; k=t+3; B=k-1; r=L-3; m=A-k-1
    assert t>=2 and t%2==0 and r>=1 and m>=r

    U=[cap_upper_position(A,L,j) for j in range(1,r+1)]
    # a_j are strictly increasing, lie in [0,m-1], and must leave room for
    # the remaining moved ranks. Since every RHS weight increases with a_j,
    # this backward recursion gives a coordinatewise upper envelope A_j.
    Au=[0]*r
    nxt=m
    for jj in range(r-1,-1,-1):
        Au[jj]=min(U[jj],nxt-1)
        nxt=Au[jj]
    if Au[0]<0:
        return Fraction(0), terminal_rhs(A,L,k), Au, []

    w=[Fraction(1<<a,3**j) for j,a in enumerate(Au,1)]
    baseline=2*sum(w,Fraction(0))

    # For delta_j=a_j-b_j >=0,
    #   3-2^-delta = 2 + (1-2^-delta).
    # One additional unit of delta on rank j has marginal w_j/2^(delta+1).
    # The marginal sequence is decreasing, so greedily taking the B largest
    # marginals is the exact maximum of this relaxed separable concave problem.
    heap=[]
    delta=[0]*r
    for j,wj in enumerate(w):
        heap.append((-wj,j))  # first marginal is w_j/2; store doubled below
    # Fraction has no cheap negative-priority convention with /2 prebuilt.
    heap=[(-wj/2,j) for j,wj in enumerate(w)]
    heapq.heapify(heap)
    enhance=Fraction(0)
    for _ in range(B):
        neg,j=heapq.heappop(heap)
        marg=-neg
        enhance += marg
        delta[j]+=1
        heapq.heappush(heap,(-w[j]/(1<<(delta[j]+1)),j))
    return baseline+enhance, terminal_rhs(A,L,k), Au, delta

def terminal_rhs(A,L,k):
    zeta=Fraction(1<<A,3**L)
    return Fraction(14,1)+Fraction(27,2)*zeta*(1-Fraction(1,1<<k))

def excluded_ts(A,L):
    q=A-L
    out=[]
    for t in range(2,q,2):
        ub,target,_,_=relaxed_violation_upper(A,L,t)
        if ub < target:
            out.append(t)
    return out

if __name__=='__main__':
    H,val=witness_check()
    print('RL47 rank-transport identity witness: PASS')
    print('witness H=sum(a_j-b_j)=',H)
    print('witness normalized terminal identity: exact PASS')
    expected={
        (46,29):2,
        (65,41):2,
        (149,94):32,
        (214,135):60,
        (363,229):116,
    }
    for pair,first in expected.items():
        xs=excluded_ts(*pair)
        assert xs and xs[0]==first, (pair,xs[:5],first)
        # Once the relaxed room/cap envelope excludes a t in these regression
        # pairs it continues to exclude all larger admissible even t.
        assert xs==list(range(first,pair[0]-pair[1],2)), (pair,xs[-5:])
        print('pair',pair+(pair[0]-pair[1],),'strict-violation t excluded analytically from',first,'through',xs[-1])
    print('RL47 rank-transport relaxed-bound verifier: PASS')
