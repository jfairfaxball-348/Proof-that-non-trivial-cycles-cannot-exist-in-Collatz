#!/usr/bin/env python3
from collections import deque
INF=10**18; CAP=7

def v2(n):n=abs(n);return (n & -n).bit_length()-1

def step(d,J,x):
    K=J+2**d-1
    if K%2==0:
        if x:d2,K2=d,3*K//2
        else:d2,K2=d,(K+3**d-1)//2
    else:
        if x:
            if d<=1:return None
            d2,K2=d-1,(K-1)//2
        else:d2,K2=d+1,3*(K+3**d)//2
    return d2,K2-2**d2+1,d-1

def closure(start,R):
    dist={start:0}; b=[deque() for _ in range(R+1)];b[0].append(start)
    for H in range(R+1):
        q=b[H]
        while q:
            d,J=q.popleft()
            if dist.get((d,J))!=H:continue
            for x in (0,1):
                o=step(d,J,x)
                if o is None:continue
                d2,J2,c=o;H2=H+c
                if H2>R:continue
                assert J2>0
                s=(d2,J2)
                if H2<dist.get(s,INF):dist[s]=H2;b[H2].append(s)
    return dist

def first_returns(limit):
    launch=step(1,8,0);assert launch and launch[0]==2 and launch[2]==0
    stack=[(launch[0],launch[1],0,'0')]; seen=set(); out=set()
    while stack:
        d,J,A,w=stack.pop(); key=(d,J,A,w)
        if key in seen:continue
        seen.add(key)
        for x in (0,1):
            o=step(d,J,x)
            if o is None:continue
            d2,J2,c=o;A2=A+c;w2=w+str(x)
            if A2>=limit:continue
            if d2==1:out.add((J2,A2,w2))
            else:stack.append((d2,J2,A2,w2))
    return sorted(out,key=lambda t:(t[1],t[0],t[2]))
dist=closure((1,8),CAP)
cp={J:A for (d,J),A in dist.items() if d==1 and J%2==0}
by={}
for J,A in cp.items():
    if J==8:continue
    by.setdefault(A,[]).append(J)
for A in by:by[A].sort()
expected={2:[2,12],6:[6,14,18,20,26,30,32,62,68,80,134],7:[24,48,102]}
assert by==expected
rets=first_returns(8);assert rets==[(5,2,'001'),(12,2,'011')]
for A,Js in expected.items():
    for J in Js:assert v2(J)<=A+1
assert v2(8)==3==2+1
print('RL293 checkpoint-8 complete low-area A<=7 closure: PASS')
print('first_returns_below_8=',rets)
for A in sorted(expected):print(f'checkpoint_frontier_A{A}='+','.join(map(str,expected[A])))
print('nonempty_return_8_cost=2_sharp_v2=3')
print('all_nonempty_balanced_checkpoint_futures_A<=7_satisfy_v2(J)<=A+1')
print('classification_candidates=CHECKPOINT8_AREA_TWO_RENEWAL_EQUALITY_RIGIDITY;CHECKPOINT8_FULL_LOWAREA_A_LE_7_EXCESS_ONE_CLOSURE')
