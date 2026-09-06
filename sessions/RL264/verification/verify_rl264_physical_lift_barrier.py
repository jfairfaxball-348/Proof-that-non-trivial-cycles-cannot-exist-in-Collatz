#!/usr/bin/env python3
from statistics import median_low

def step(d,J,H,x):
    oldd=d
    if J & 1:
        y=x
        if x==0:
            return d,(J+3**d-2**d)//2,H+oldd-1,y
        return d,(3*J+2**d-1)//2,H+oldd-1,y
    y=1-x
    if x==0:
        return d+1,(3*J+3**(d+1)-2**d-1)//2,H+oldd-1,y
    if d<=1:
        return None
    return d-1,J//2,H+oldd-1,y

def F(n):
    return n//2 if n%2==0 else (3*n+1)//2

def paths(depth):
    states=[(1,-13,0,[],[])]
    for _ in range(depth):
        nxt=[]
        for d,J,H,xs,ys in states:
            for x in (0,1):
                s=step(d,J,H,x)
                if s is not None:
                    d2,J2,H2,y=s
                    nxt.append((d2,J2,H2,xs+[x],ys+[y]))
        states=nxt
    return states

def Q(bits):
    pos=[i for i,b in enumerate(bits) if b]
    r=len(pos)
    return sum(2**a * 3**(r-j-1) for j,a in enumerate(pos))

prefix_checks=0
max_depth=10
for p in range(1,max_depth+1):
    for d,J,H,xs,ys in paths(p):
        hits=[]
        for h in range(2**p):
            A=22+27*h
            bits=[]
            for _ in range(p):
                bits.append(A&1)
                A=F(A)
            if bits==xs:
                hits.append(h)
        assert len(hits)==1
        h=hits[0]

        A=22+27*h
        B=80+81*h
        dd,JJ,HH=1,-13,0
        X=Y=0
        assert 3*A-B == -14
        for x,y in zip(xs,ys):
            assert (A&1)==x and (B&1)==y
            A,B=F(A),F(B)
            s=step(dd,JJ,HH,x)
            assert s is not None
            dd,JJ,HH,y2=s
            assert y2==y
            X+=x; Y+=y
            T=JJ-3**dd+2**dd
            assert 3**dd*A-B==T

        h2=h+2**p
        A2=22+27*h2
        B2=80+81*h2
        for x,y in zip(xs,ys):
            assert (A2&1)==x and (B2&1)==y
            A2,B2=F(A2),F(B2)
        assert A2-A==27*3**X
        assert B2-B==81*3**Y
        assert 3**dd*A2-B2==3**dd*A-B
        prefix_checks+=1

terminal_checks=0
profile_checks=0
self_rotation_checks=0
for p in range(1,15):
    for d,J,H,xs,ys in paths(p):
        if not (d==1 and J>0 and J&(J-1)==0):
            continue
        k=J.bit_length()-1
        if k<3:
            continue
        m=p
        r=sum(xs)
        ell=r+3
        a=m+k+1
        qx,qy=Q(xs),Q(ys)

        assert 3*qx-qy == 14*3**r + 2**(a-1)-2**(a-k-1)
        defect=qx-qy
        physical = 69*3**r + 24*qx - 6*2**a + 8*2**(a-k-1)
        phase = 237*3**r - 12*defect - 2**(a-k+1)
        assert physical==phase
        terminal_checks+=1

        t=k-3
        u=[1,1,0]+xs+[1]+[0]*t
        v=[1,1,1]+ys+[0]*(t+1)
        assert len(u)==a and len(v)==a and sum(u)==sum(v)==ell
        s=0
        prof=[]
        for vb,ub in zip(v,u):
            s+=vb-ub
            prof.append(s)
        assert s==0
        assert min(prof)>=0
        assert prof.count(0)==k
        assert sum(max(0,z-1) for z in prof)==H
        assert sum(prof)==a-k+H
        profile_checks+=1

        doubled=prof+[-z for z in prof]
        c=median_low(sorted(doubled))
        dist=sum(abs(z-c) for z in doubled)
        assert dist==2*(a-k+H)
        self_rotation_checks+=1

print("PASS RL264 physical-lift barrier")
print(f"finite legal prefix affine-ray checks={prefix_checks}; max depth={max_depth}")
print(f"terminal rank/ownership equivalence checks={terminal_checks}")
print(f"terminal transport-profile checks={profile_checks}")
print(f"natural self-rotation distance checks={self_rotation_checks}")
print("verified: terminal physical scalar equation is algebraically identical to RL65 phase quotient")
print("verified: dist_cyc(uv,vu)=2(a-k+H) on bounded terminal audit")
print("FAST_RL264_VERIFIERS_PASS")
