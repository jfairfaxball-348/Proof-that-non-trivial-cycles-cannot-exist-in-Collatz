#!/usr/bin/env python3
from collections import deque
INF=10**18; R=28; PCAP=14

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

def boundary_exits(J):
    assert J>0 and J%2==1;seen=set();cur=J;exits=set()
    while cur not in seen:
        seen.add(cur);n=(cur-1)//2
        if n%2==0:ret=n+1;ex=3*n+2
        else:ret=3*n+2;ex=n+1
        assert ret%2==1 and ex%2==0;exits.add(ex);cur=ret
    return exits

def relaxed_seeds(R):
    seeds={};d=1
    while (d-1)*(d-2)//2<=R:
        eps=1 if d%2==0 else 2;maxJ=3**d-2**d+1;floor=(d-1)*(d-2)//2
        for J in range(1,maxJ+1):
            if J%3 not in (0,eps):continue
            M=J+2**d-2;H=max(floor,v2(M)-d+1,0)
            if not (d==3 and J==2 and H==1):H=max(H,v2(M)-d+2)
            if H<=R:seeds[(d,J)]=min(seeds.get((d,J),INF),H)
        d+=1
    return seeds

def first_even_checkpoint(seeds,R):
    dist={};b=[deque() for _ in range(R+1)];cps={};odd_origins=set()
    def addcp(J,H):cps[J]=min(cps.get(J,INF),H)
    def handle(J,H):
        if J%2==0:addcp(J,H)
        else:
            odd_origins.add(J)
            for e in boundary_exits(J):addcp(e,H)
    for s,H in seeds.items():
        d,J=s
        if d==1:handle(J,H)
        elif H<dist.get(s,INF):dist[s]=H;b[H].append(s)
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
                if d2==1:handle(J2,H2)
                else:
                    s=(d2,J2)
                    if H2<dist.get(s,INF):dist[s]=H2;b[H2].append(s)
    return dist,odd_origins,cps

def positive_closure(start,R):
    dist={start:0};b=[deque() for _ in range(R+1)];b[0].append(start)
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
                assert J2>0;s=(d2,J2)
                if H2<dist.get(s,INF):dist[s]=H2;b[H2].append(s)
    return dist

def genuine_cut(R):
    start=(1,-13);dist={start:0};b=[deque() for _ in range(R+1)];b[0].append(start);cp={}
    for H in range(R+1):
        q=b[H]
        while q:
            d,J=q.popleft()
            if dist.get((d,J))!=H:continue
            if d==1 and J>0 and J%2==0:cp[J]=min(cp.get(J,INF),H);continue
            for x in (0,1):
                o=step(d,J,x)
                if o is None:continue
                d2,J2,c=o;H2=H+c
                if H2>R:continue
                s=(d2,J2)
                if H2<dist.get(s,INF):dist[s]=H2;b[H2].append(s)
    return dist,cp
seeds=relaxed_seeds(R);trans,odd,cps=first_even_checkpoint(seeds,R);pdist=positive_closure((2,3),PCAP)
pcp={J:H for (d,J),H in pdist.items() if d==1 and J%2==0}
assert len(seeds)==19005 and len(trans)==21787 and len(odd)==23 and len(cps)==94 and len(pdist)==2509
exc=[]
for J,H in cps.items():
    mp=pcp.get(J,INF)
    if 1+mp>H:exc.append((J,H,mp))
exc.sort(key=lambda x:(x[1],x[0]));assert exc==[(2,2,2),(8,2,2),(6,5,8)]
small,smallcp=genuine_cut(8);assert smallcp=={2:3,8:3};assert len(small)==227 and len(small)-len(smallcp)==225
print('RL293 first-checkpoint H<=28 splice certificate: PASS')
print('height_cap=',R)
print('relaxed_first_positive_seeds=',len(seeds))
print('positive_transient_states_d_gt_1=',len(trans))
print('positive_odd_boundary_origins=',len(odd))
print('possible_first_positive_even_checkpoints=',len(cps))
print('P_owner_cone_cap=',PCAP)
print('P_owner_cone_physical_states=',len(pdist))
print('immediate_splice_checkpoints=',91)
print('relaxed_exceptions=',exc)
print('fixed_seed_H8_transient_states=',len(small)-len(smallcp))
print('fixed_seed_first_checkpoint_H8=',sorted(smallcp.items()))
print('classification_candidate=FIXED_SEED_FIRST_CHECKPOINT_H28_MINPLUS_SPLICE_TO_2_3')
