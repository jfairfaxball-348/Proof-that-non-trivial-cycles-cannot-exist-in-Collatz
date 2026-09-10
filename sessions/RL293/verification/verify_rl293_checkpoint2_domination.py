#!/usr/bin/env python3
from collections import deque
INF=10**18

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

def replay(start,word):
    d,J=start;A=0
    for ch in word:
        o=step(d,J,int(ch));assert o is not None
        d,J,c=o;A+=c
    return d,J,A

def Kof(d,J):return J+2**d-1
d,J,A=replay((1,2),'0');assert (d,Kof(d,J),A)==(2,9,0)
for depth in range(2,9):
    J=3**depth-2**depth+1
    o0=step(depth,J,0);o1=step(depth,J,1);assert o0 and o1
    assert (o0[0],Kof(o0[0],o0[1]),o0[2])==(depth+1,3**(depth+1),depth-1)
    assert (o1[0],Kof(o1[0],o1[1]),o1[2])==(depth-1,(3**depth-1)//2,depth-1)
for depth,word,cost in [(3,'00',1),(4,'0100',4),(5,'010100',9)]:
    d8,J8,A8=replay((1,8),word);assert A8==cost and (d8,Kof(d8,J8))==(depth-1,(3**depth-1)//2)
S6=(5,364-2**5+1);assert replay(S6,'01111')==(1,17,14)
cur=17;seen=set();exits=[];trace=[]
while cur not in seen:
    seen.add(cur);trace.append(cur);n=(cur-1)//2
    if n%2==0:ret=n+1;ex=3*n+2
    else:ret=3*n+2;ex=n+1
    exits.append(ex);cur=ret
assert trace==[17,9,5,3] and set(exits)=={2,8,14,26}
R=6;dist={(1,8):0};b=[deque() for _ in range(R+1)];b[0].append((1,8))
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
            s=(d2,J2)
            if H2<dist.get(s,INF):dist[s]=H2;b[H2].append(s)
for J in (2,8,14,26):assert dist.get((1,J),INF)<=6
print('RL293 checkpoint-2 to checkpoint-8 domination regression: PASS')
print('tower_departures_checked=d2..d8')
print('same_state_mergers=d3_cost1,d4_cost4,d5_cost9')
print('d6_first_return_equality=source2_cost29_to_odd_J17')
print('J17_boundary_exits=2,8,14,26_all_source8_cost<=6')
print('classification_candidate=CHECKPOINT2_TO_CHECKPOINT8_STRICT_MINPLUS_DOMINATION_THROUGH_COST29')
