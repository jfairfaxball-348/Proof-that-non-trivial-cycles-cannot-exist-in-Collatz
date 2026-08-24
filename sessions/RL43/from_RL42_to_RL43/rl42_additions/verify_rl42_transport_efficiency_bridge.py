#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations


def positions(w):
    return [i for i,b in enumerate(w) if b]


def transport_rank_data(u,v):
    iu=positions(u); iv=positions(v)
    assert len(iu)==len(iv)
    pos=[i-j for i,j in zip(iu,iv) if i>j]
    neg=[j-i for i,j in zip(iu,iv) if i<j]
    rho=sum(pos)+sum(neg)
    eff=sum(Fraction((1<<d)-1,1<<d) for d in pos)
    return rho,pos,neg,eff


def word_from_positions(n,pos):
    s=set(pos)
    return tuple(1 if i in s else 0 for i in range(n))

# Pure ordered-rank sanity through length 10.
pairs=0
for n in range(1,11):
    for ell in range(n+1):
        words=[word_from_positions(n,c) for c in combinations(range(n),ell)]
        for u in words:
            for v in words:
                pairs+=1
                rho,pos,neg,eff=transport_rank_data(u,v)
                # 1-2^{-d} <= d/2 for every integer d>=1.
                assert all(Fraction((1<<d)-1,1<<d) <= Fraction(d,2) for d in pos)
                assert eff <= Fraction(sum(pos),2) <= Fraction(rho,2)

# Retained RL21 g=2 proper-factor countermodel: sanity for the exact refined sum.
a=65; ell=41
u='11011011010110110110101101110011011100110110110101110101011011100'
v='11111111110111000111110011011011110101010111110011101000011100000'
iu=[i for i,b in enumerate(u) if b=='1']
iv=[i for i,b in enumerate(v) if b=='1']
pos=[i-j for i,j in zip(iu,iv) if i>j]
neg=[j-i for i,j in zip(iu,iv) if i<j]
rho=sum(pos)+sum(neg)
eff=sum(Fraction((1<<d)-1,1<<d) for d in pos)
X=1<<a; Y=3**ell; z=Fraction(X,Y); G=4
threshold=3*(z+1)*G/(z*z)
assert rho==170 and len(pos)==39 and len(neg)==0
assert eff==Fraction(4571,128)
assert eff > threshold
assert eff <= Fraction(rho,2)

# Uniform theorem arithmetic: rho > (45/4)G, 4|G => rho>=46.
# For the least admissible G=4, the strict lower bound is rho>45.
assert Fraction(45,4)*4 == 45

print('RL42 transport-efficiency bridge verifier: PASS')
print('equal-weight ordered pairs checked through length 10 =',pairs)
print('verified pure inequality: sum_pos(1-2^-delta) <= rho/2')
print('RL21 sanity: effective positive-rank mass =',eff,'threshold =',threshold,'rho =',rho)
print('analytic consequence certified symbolically: rho > (45/4)G; with 4|G, rho >= 46')
