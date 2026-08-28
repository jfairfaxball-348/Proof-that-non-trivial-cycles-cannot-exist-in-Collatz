#!/usr/bin/env python3
for A,L in ((5,3),(7,4),(11,7)):
  N=4*L; b=[A*i//L for i in range(N+1)]; c=[b[i+1]-b[i] for i in range(N)]
  choices=[i for i,x in enumerate(c) if x==2 and 0<i<N-1]
  for j in choices:
    for k in choices:
      if k<=j+1: continue
      h=[0]*N; h[j]=h[k]=-1
      a=[c[i]+h[i]-h[(i+1)%N] for i in range(N)]
      assert min(a)>=1 and a[j]==a[k]==1
print('RL150 fast verifier: PASS')
