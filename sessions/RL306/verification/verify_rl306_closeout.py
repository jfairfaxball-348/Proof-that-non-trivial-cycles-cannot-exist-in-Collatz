from heapq import heappush, heappop

# RL302/RL306 canonical K coordinate: K = J + 2^d - 1.
def J_of(s):
    d,K=s
    return K - 2**d + 1

def step(s,x):
    d,K=s
    if K % 2 == 0:
        return ((d,3*K//2),d-1) if x else ((d,(K+3**d-1)//2),d-1)
    if x:
        return None if d <= 1 else ((d-1,(K-1)//2),d-1)
    return ((d+1,3*(K+3**d)//2),d-1)

def run(s,w):
    c=0
    for ch in w:
        z=step(s,int(ch))
        if z is None:
            return None
        s,dc=z
        c += dc
    return s,c

def comp(A,B):
    a,ka=A; b,kb=B
    return a+b,3**b*ka+kb

def g(S,u):
    d,K=S
    return 3**d*(u+1)-K-1

def v2(n):
    if n == 0:
        return 10**9
    n=abs(n); c=0
    while n%2==0:
        n//=2; c+=1
    return c

P=(2,6); C8=(1,9); U=(1,6); R3=(3,27); D0=(3,24)
seed=(1,-12) # J=-13
S439=(4,54) # J=39
Sm17=(2,-14) # J=-17
Sm84=(2,-81) # J=-84
Sm28=(3,-21) # J=-28

# 1. Cascade section contravariance.
for a in range(1,6):
    for b in range(1,6):
        for ka in range(-20,21,7):
            for kb in range(-20,21,9):
                A=(a,ka); B=(b,kb)
                for u in range(-11,12):
                    assert g(comp(A,B),u) == g(B,g(A,u))

assert comp(P,C8)==R3
assert comp(P,U)==D0
for u in range(-20,21):
    assert g(seed,u)==g(C8,u+7)

# 2. Seven-source affine atlas.
expected={
    R3:(27,-1), C8:(3,-7), D0:(27,2), S439:(81,26),
    Sm17:(9,22), Sm84:(9,89), Sm28:(27,47)
}
for S,(a,b) in expected.items():
    for u in range(-20,21):
        assert g(S,u)==a*u+b

# 3. Universal gateway theorem on a broad exact range.
gateway=0
for d in range(1,12):
    for K in range(-100,101):
        S=(d,K); O=(d+1,K+3**d)
        s0=step(S,0); o1=step(O,1)
        if s0 and o1:
            assert s0[0]==o1[0]
            gateway += 1
        s1=step(S,1); o0=step(O,0)
        if s1 and o0:
            assert o0[0]==comp(P,s1[0])

# 4. Fixed ingress and immediate scalar partition identities.
assert run(R3,'111')==(C8,3)
assert run(C8,'0')==((2,18),0) # (d,J)=(2,15)
assert run(D0,'011')==((2,18),5)
assert run(S439,'1')==((4,81),3) # J=66
assert run(R3,'0')==((4,81),2)
assert run(S439,'01')==((3,33),6) # J=26
assert run(C8,'000')==((3,33),2)

# 5. Small exact shell closure as regression only.
def shell_min(source, cap):
    dist={source:0}; pq=[(0,source)]
    M={}
    while pq:
        c,s=heappop(pq)
        if c!=dist[s] or c>cap: continue
        d,K=s; J=J_of(s)
        if d==1 and J>0 and J%2==0:
            r=v2(J)
            for k in range(1,r+1):
                M[k]=min(M.get(k,10**9),c)
        for x in (0,1):
            z=step(s,x)
            if not z: continue
            ns,dc=z; nc=c+dc
            if nc<=cap and nc<dist.get(ns,10**9):
                dist[ns]=nc; heappush(pq,(nc,ns))
    return M,len(dist)

M8,n8=shell_min(C8,12)
MR,nr=shell_min(R3,15)
MD,nd=shell_min(D0,17)
MS,ns=shell_min(seed,15)
for k,m in M8.items():
    if k in MR: assert MR[k] >= m
    if k in MD: assert MD[k] >= m
    if k in MS: assert MS[k] >= m+3

print('RL306_CLOSEOUT_VERIFIER_GREEN')
print('gateway_instances',gateway)
print('small_shell_state_counts',n8,nr,nd,ns)
print('M8_small',sorted(M8.items()))
print('MR3_small',sorted(MR.items()))
print('MD0_small',sorted(MD.items()))
print('Mseed_small',sorted(MS.items()))
