#!/usr/bin/env python3
"""Exact finite sanity certificate for RL42 moved-rank sparse bridge.

Checks every equal-weight binary word pair through length 10:
  * ordered-rank Q formula;
  * rho = sum ordered-rank displacement;
  * displaced-rank count = sum excursion local odd weights;
  * direct difference formula has <=2P pre-collection monomials.

The general statements are proved analytically in the note.
"""
from itertools import combinations


def Qword(w):
    ell=sum(w)
    p=0
    q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(ell-1-p)
            p += 1
    return q


def positions(w):
    return [i for i,b in enumerate(w) if b]


def q_rank(w):
    pos=positions(w)
    ell=len(pos)
    return sum((3**(ell-1-m))*(1<<r) for m,r in enumerate(pos))


def transport_and_excursion_mass(u,v):
    # d_j is prefix odd-count difference before column j.
    d=0
    rho=0
    P=0
    in_exc=False
    c0_u=c0_v=0
    for x,y in zip(u,v):
        rho += abs(d)
        if d==0 and x!=y:
            in_exc=True
            c0_u=c0_v=0
        if in_exc:
            c0_u += x
            c0_v += y
        nd=d+y-x
        if in_exc and nd==0:
            assert c0_u==c0_v and c0_u>=1
            P += c0_u
            in_exc=False
        d=nd
    assert d==0 and not in_exc
    return rho,P


def word_from_positions(n,pos):
    s=set(pos)
    return tuple(1 if i in s else 0 for i in range(n))

pairs=0
nontrivial=0
for n in range(1,11):
    for ell in range(n+1):
        words=[word_from_positions(n,c) for c in combinations(range(n),ell)]
        for u in words:
            iu=positions(u)
            assert Qword(u)==q_rank(u)
            for v in words:
                pairs += 1
                iv=positions(v)
                assert Qword(v)==q_rank(v)
                direct=sum((3**(ell-1-m))*((1<<iu[m])-(1<<iv[m])) for m in range(ell))
                assert direct==Qword(u)-Qword(v)
                moved=[m for m in range(ell) if iu[m]!=iv[m]]
                rho_rank=sum(abs(iu[m]-iv[m]) for m in moved)
                rho,P=transport_and_excursion_mass(u,v)
                assert rho==rho_rank
                assert P==len(moved)
                # Expanded direct relation has two signed monomials per moved rank before collection.
                assert 2*len(moved) <= 2*P
                if u!=v:
                    nontrivial += 1
                    assert P>=1

print('RL42 moved-rank sparse bridge verifier: PASS')
print('equal-weight ordered pairs checked =',pairs)
print('nontrivial pairs checked =',nontrivial)
print('verified: P = displaced-rank count and rho = total rank displacement through length 10')
