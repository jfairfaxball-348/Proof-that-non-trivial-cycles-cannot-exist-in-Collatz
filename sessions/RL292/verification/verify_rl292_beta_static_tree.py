#!/usr/bin/env python3
"""RL292 regression for the static 2-adic preimage-tree representation of RL283 Beta.

Analytic theorem in CHECKPOINT.md. This script checks the identity on bounded
integer samples and the explicit family showing that the four D/K wall forms
cannot dominate future boundary hazard.
"""
from fractions import Fraction
from itertools import product


def v2_int(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def v2_frac(q):
    q = Fraction(q)
    return v2_int(q.numerator) - v2_int(q.denominator) if q.denominator != 1 else v2_int(q.numerator)


def C(n):
    return n//2 if n % 2 == 0 else (3*n+1)//2


def hazard(n):
    e = 3*n+2 if n % 2 == 0 else n+1
    return v2_int(e)


def beta_direct(n, T):
    best = 0
    cur = n
    for _ in range(T+1):
        best = max(best, hazard(cur))
        cur = C(cur)
    return best


def Q_word(w):
    # C_w(z)=(3^r z+Q_w)/2^t
    Q = 0
    r = sum(w)
    seen = 0
    for j,b in enumerate(w):
        if b:
            ones_after = r-seen-1
            Q += (2**j)*(3**ones_after)
            seen += 1
    return Q


def root(w, alpha):
    t=len(w); r=sum(w); Q=Q_word(w)
    return (Fraction((2**t),1)*alpha - Q) / (3**r)


def beta_static(n,T):
    roots=(Fraction(-1,1), Fraction(-2,3))
    best=-10**9
    for t in range(T+1):
        for w in product((0,1), repeat=t):
            for a in roots:
                rho=root(w,a)
                score=v2_frac(Fraction(n,1)-rho)-t
                best=max(best,score)
    return best


def check_static():
    checked=0
    for n in range(1,151):
        for T in range(0,7):
            a=beta_direct(n,T)
            b=beta_static(n,T)
            assert a==b,(n,T,a,b)
            checked+=1
    return checked


def check_four_form_evasion():
    # all-zero pullback of alpha_1=-1: n_R=2^L(2^R-1).
    # After L retained zero steps it becomes 2^R-1, exposing hazard R.
    L=4
    rows=[]
    for R in range(5,25):
        n=(2**L)*(2**R-1)
        J=2*n+1
        d=1
        K=J+1
        forms=(K,3*K-3**d+1,3*K+1,K-3**(d-1))
        vals=tuple(v2_int(z) for z in forms)
        assert vals==(1,2,0,0), (R,vals)
        # exactly R is already visible by time L; later behavior is irrelevant.
        assert beta_direct(n,L)==R, (R,beta_direct(n,L))
        rows.append((R,n,J,vals))
    return rows


def main():
    c=check_static()
    rows=check_four_form_evasion()
    print('RL292 static Beta preimage-tree regression: PASS')
    print('direct_vs_static_checks=',c)
    print('hazard_roots=alpha1:-1,alpha0:-2/3')
    print('explicit_allzero_pullback_L=4')
    print('R_range=5..24')
    print('wall_four_form_valuations=',rows[0][3])
    print('truncated_Beta_on_family=R')
    print('classification_candidate=STATIC_BOUNDARY_HAZARD_PREIMAGE_TREE_AND_FINITE_TEMPLATE_BARRIER_PROVED')

if __name__=='__main__':
    main()
