#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def wt(w):
    return sum(w)


def Q(w):
    ell = wt(w)
    rank = 0
    total = 0
    for i,b in enumerate(w):
        if b:
            rank += 1
            total += (2**i) * (3**(ell-rank))
    return total


def F(w, x):
    return Fraction(3**wt(w)*x + Q(w), 2**len(w))


def cat(*ws):
    out=[]
    for w in ws: out.extend(w)
    return tuple(out)


def rep(w,q):
    return tuple(w)*q

# Basic normalization checks for special pumps.
assert Q((1,0)) == 1
assert Q((1,0,1)) == 7
assert F((1,0), Fraction(1)) == 1
assert F((1,0,1), Fraction(-7)) == -7

checks = 0
degenerate = 0
positive_M_checks = 0
valuation_checks = 0

def vp(z,p):
    z=abs(int(z))
    assert z != 0
    v=0
    while z % p == 0:
        z//=p; v+=1
    return v
for la in range(0,4):
  for lb in range(0,4):
    for lc in range(1,4):
      for A in product((0,1), repeat=la):
       for B in product((0,1), repeat=lb):
        for c in product((0,1), repeat=lc):
         # Skip delta=0, where RL74's divided-delta Möbius normalization is singular.
         n=len(c); s=wt(c); P=2**n; R=3**s; C=Q(c); delta=R-P
         if delta == 0:
            continue
         LA=len(A); wB=wt(B)
         X0=2**(len(A)+len(B))
         Y0=3**(wt(A)+wt(B))
         Astar = delta*(3**wB)*Q(A) + (2**LA)*(3**wB)*C + 4*delta*Y0
         Bstar = delta*(2**LA)*Q(B) - (2**LA)*(3**wB)*C
         Dstar = Astar*X0 + Bstar*Y0
         pref=(2**LA)*(3**wB)
         for q in range(1,4):
            v=cat(A, rep(c,q), B)
            ell=wt(v)
            M=2**len(v)-3**ell
            if M == 0:
                continue
            N=Fraction(Q(v)+4*3**ell, M)
            x=F(A, N+4)
            y=x
            for _ in range(q):
                y=F(c,y)

            # RL75 physical-drift identities.
            lhs1=Fraction(Astar) + delta*N*Y0
            rhs1=pref*(delta*x+C)
            assert lhs1 == rhs1

            lhs2=delta*N*X0 - Bstar
            rhs2=pref*(delta*y+C)
            assert lhs2 == rhs2

            # Affine pump drift scales exactly by R/P each copy.
            assert delta*y+C == Fraction(R**q, P**q)*(delta*x+C)

            # Determinant factorization through the actual pump-entry drift.
            fact = Fraction(pref*(delta*x+C)*M, P**q)
            assert Fraction(Dstar) == fact
            fact_suffix = Fraction(pref*(delta*y+C)*M, R**q)
            assert Fraction(Dstar) == fact_suffix

            # Therefore (for M != 0) determinant zero iff the pump fixes x.
            assert (Dstar == 0) == (F(c,x) == x)
            if Dstar == 0:
                degenerate += 1
            if M > 0:
                positive_M_checks += 1
            # In a genuine integral completion, physical pump-entry/exit states are integers.
            # The determinant factorization then forces 2-adic prefix and 3-adic suffix
            # transversality inequalities whenever the drift is nonzero.
            if M > 0 and N.denominator == 1 and x.denominator == 1 and y.denominator == 1 and Dstar != 0:
                phix = delta*int(x)+C
                phiy = delta*int(y)+C
                assert phix != 0 and phiy != 0
                assert n*q <= LA + vp(phix,2)
                if s > 0:
                    assert s*q <= wB + vp(phiy,3)
                valuation_checks += 1
            checks += 1

# Special pumps: drift factors have fixed sign on the positive nontrivial domain.
for x in range(2,101):
    # c=10: delta=-1,C=1 => 1-x < 0.
    assert (3-4)*x + 1 < 0
    # c=101: delta=1,C=7 => x+7 > 0.
    assert (9-8)*x + 7 > 0

# Full-phase pair + every genuine cycle phase nonzero mod 3 gives a small residue refinement.
# N == 3 mod 8 and both N,N+4 are nonzero mod 3 => N == 19 mod 24.
residue_checks=0
for N in range(1,2000):
    if N % 8 == 3 and N % 3 != 0 and (N+4) % 3 != 0:
        assert N % 24 == 19
        residue_checks += 1

print('RL75 pump-transversality verifier: PASS')
print('exhaustive drift/factorization checks =', checks)
print('positive-M checks =', positive_M_checks)
print('algebraic determinant-zero instances =', degenerate)
print('integral transversality valuation checks =', valuation_checks)
print('special-pump sign checks =', 99*2)
print('full-phase mod-24 residue checks =', residue_checks)
