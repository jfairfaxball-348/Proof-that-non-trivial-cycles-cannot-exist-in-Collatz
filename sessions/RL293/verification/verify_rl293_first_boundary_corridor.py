#!/usr/bin/env python3
from fractions import Fraction
from math import log

def v2(n):n=abs(n);return (n & -n).bit_length()-1

def stepK(d,K,x):
    if K%2==0:return (d,3*K//2) if x else (d,(K+3**d-1)//2)
    if x:
        if d<=1:return None
        return d-1,(K-1)//2
    return d+1,3*(K+3**d)//2
checks=0
for d in range(2,10):
  for K in range(2,500):
    for x in (0,1):
      o=stepK(d,K,x)
      if o is None:continue
      d2,K2=o;q=Fraction(K,3**d);q2=Fraction(K2,3**d2)
      if x==1:assert q2<=Fraction(3,2)*q
      else:assert q2<=max(Fraction(1),q)
      checks+=1
for R in range(3,40,2):
    n=(2**R-2)//3;J=2*n+1;H=R-1
    assert 3*n+2==2**R and v2(3*n+2)==R==H+1 and J<2**(H+1)
    assert (J%3 in (0,2))==(R%6 in (3,5))
    if R>=5:assert Fraction(J+1,1)>3*Fraction(3,2)**H
lam=log(4/3)/log(3/2)
print('RL293 first-boundary normalized-K corridor regression: PASS')
print('sampled_normalized_K_transition_checks=',checks)
print('lambda=',repr(lam))
print('immediate_danger_family_checked_R=3..39_odd')
print('mod3_allowed_classes=R mod 6 in {3,5}')
print('new_corridor_excludes_all_immediate_family_members_R>=5_at_H=R-1')
print('classification_candidate=FIRST_BOUNDARY_NORMALIZED_K_CORRIDOR_AND_HIGH_WEIGHT_DANGER_REDUCTION')
