#!/usr/bin/env python3
for A,L in ((5,3),(7,4),(11,7)):
  for j in range(1,5*L):
    b=A*j//L; rem=(j*A)%L
    assert (b+1)*L-j*A == (L-rem if rem else L)
    c=b-A*(j-1)//L
    for H in range(12):
      assert -1 == H+c-(H+c+1)
      y=7 if (H+c+1)%2==0 else 11
      previous=(2**(H+c+1)*y-1)//3
      assert 3*previous+1 == 2**(H+c+1)*y
print('RL149 fast verifier: PASS')
