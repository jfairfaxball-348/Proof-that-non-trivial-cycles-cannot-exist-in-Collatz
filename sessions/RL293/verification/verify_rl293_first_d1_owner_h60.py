#!/usr/bin/env python3
"""RL293 compact first-d=1 owner certificate through historical H<=60."""
from collections import deque
INF=10**18; HMAX=60; PCAP=22

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

def boundary_trace(J,limit=100000):
    assert J>0 and J&1;seen=set();cur=J;out=[]
    for _ in range(limit):
        if cur in seen:return out
        seen.add(cur);n=(cur-1)//2
        if n%2==0:ret=n+1;ex=3*n+2
        else:ret=3*n+2;ex=n+1
        assert ret&1 and ex%2==0;out.append((cur,ex));cur=ret
    raise AssertionError(('boundary trace cap',J))

def relaxed_seeds(R):
    seeds=[];d=1
    while (d-1)*(d-2)//2<=R:
        eps=1 if d%2==0 else 2;maxJ=3**d-2**d+1;floor=(d-1)*(d-2)//2
        for J in range(1,maxJ+1):
            if J%3 not in (0,eps):continue
            M=J+2**d-2;H=max(floor,v2(M)-d+1,0)
            if not (d==3 and J==2 and H==1):H=max(H,v2(M)-d+2)
            if H<=R:seeds.append(((d,J),H))
        d+=1
    return seeds

def first_d1_relaxed(seeds,R):
    dist={};b=[deque() for _ in range(R+1)]
    for s,H in seeds:
        if H<dist.get(s,INF):dist[s]=H;b[H].append(s)
    arrivals={}
    for H in range(R+1):
        q=b[H]
        while q:
            d,J=q.popleft()
            if dist.get((d,J))!=H:continue
            if d==1:arrivals[J]=min(arrivals.get(J,INF),H);continue
            for x in (0,1):
                o=step(d,J,x)
                if o is None:continue
                d2,J2,c=o;H2=H+c
                if H2>R:continue
                assert J2>0
                if d2==1:arrivals[J2]=min(arrivals.get(J2,INF),H2)
                else:
                    s=(d2,J2)
                    if H2<dist.get(s,INF):dist[s]=H2;b[H2].append(s)
    return dist,arrivals

def p_owner_cone(R):
    start=(2,3);hi={start:0};d1={};b=[deque() for _ in range(R+1)];b[0].append(start);odd_cache={}
    def launch_even(J,H):
        la=step(1,J,0);assert la and la[0]==2 and la[2]==0
        s=(la[0],la[1])
        if H<hi.get(s,INF):hi[s]=H;b[H].append(s)
    for H in range(R+1):
        q=b[H]
        while q:
            d,J=q.popleft()
            if hi.get((d,J))!=H:continue
            for x in (0,1):
                o=step(d,J,x)
                if o is None:continue
                d2,J2,c=o;H2=H+c
                if H2>R:continue
                assert J2>0
                if d2==1:
                    if J2%2==0:
                        d1[J2]=min(d1.get(J2,INF),H2);launch_even(J2,H2)
                    else:
                        if J2 not in odd_cache:odd_cache[J2]=boundary_trace(J2)
                        for Jo,Ex in odd_cache[J2]:
                            d1[Jo]=min(d1.get(Jo,INF),H2);d1[Ex]=min(d1.get(Ex,INF),H2);launch_even(Ex,H2)
                else:
                    s=(d2,J2)
                    if H2<hi.get(s,INF):hi[s]=H2;b[H2].append(s)
    return hi,d1

def genuine_first_checkpoint_through_8():
    R=8;start=(1,-13);dist={start:0};b=[deque() for _ in range(R+1)];b[0].append(start);cp={}
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
seeds=relaxed_seeds(HMAX);transient,arrivals=first_d1_relaxed(seeds,HMAX);phi,pd1=p_owner_cone(PCAP)
exceptions=[]
for J,H in arrivals.items():
    mp=pd1.get(J,INF)
    if 1+mp>H:exceptions.append((J,H,mp))
exceptions.sort(key=lambda x:(x[1],x[0]))
assert len(seeds)==525986,len(seeds)
assert len(transient)==608084,len(transient)
assert len(arrivals)==865,len(arrivals)
assert len(phi)+len(pd1)==619141,(len(phi),len(pd1))
assert exceptions==[(2,2,2),(3,2,2),(6,5,8)],exceptions
small_states,small_cp=genuine_first_checkpoint_through_8()
assert small_cp=={2:3,8:3},small_cp
# Mechanical closeout repair: total map includes the two terminal checkpoint states.
assert len(small_states)==227,len(small_states)
assert len(small_states)-len(small_cp)==225,(len(small_states),len(small_cp))
print('RL293 compact first-d1 owner H<=60 certificate: PASS')
print('height_cap=',HMAX)
print('relaxed_first_positive_seeds=',len(seeds))
print('positive_transient_states_before_first_d1=',len(transient))
print('possible_first_positive_d1_states=',len(arrivals))
print('P_owner_cone_cap=',PCAP)
print('P_owner_cone_physical_states=',len(phi)+len(pd1))
print('relaxed_owner_exceptions=',exceptions)
print('genuine_fixed_seed_H8_total_stored_states=',len(small_states))
print('genuine_fixed_seed_H8_transient_states=',len(small_states)-len(small_cp))
print('genuine_fixed_seed_first_checkpoint_H<=8=',sorted(small_cp.items()))
print('genuine_exception_repairs=J2,J3 use promoted positive-d1 H>=3; J6 has first-checkpoint H>=9')
print('classification_candidate=FIXED_SEED_FIRST_D1_MINIMUM_OWNER_H60_CERTIFICATE')
