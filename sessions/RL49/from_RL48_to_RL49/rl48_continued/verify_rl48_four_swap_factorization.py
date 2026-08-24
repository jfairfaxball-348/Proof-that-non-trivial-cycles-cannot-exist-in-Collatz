#!/usr/bin/env python3
from math import gcd


def Q(w):
    rem=sum(w); out=0
    for i,b in enumerate(w):
        if b:
            out += (1<<i)*3**(rem-1)
            rem -= 1
    return out


def build_words(edges,t):
    x=[int(e[0]) for e in edges]
    y=[int(e[1]) for e in edges]
    return [1,1,0]+x+[1]+[0]*t, [1,1,1]+y+[0]*(t+1), x, y


def check_instance(A,L,t,edges,label):
    u,v,x,y=build_words(edges,t)
    assert len(u)==len(v)==A
    assert sum(u)==sum(v)==L
    r=L-3; k=t+3; m=A-k-1
    assert len(x)==len(y)==m and sum(x)==sum(y)==r
    U,V=Q(u),Q(v)
    Qx,Qy=Q(x),Q(y)
    X,Y=1<<A,3**L
    M=X-Y
    # General reconstruction formulae.
    assert U == 15*3**r + 24*Qx + (1<<(A-t-1))
    assert V == 19*3**r + 8*Qy
    # Terminal identity in Q-form, reconstructed from the edge sequence.
    apos=[i for i,e in enumerate(edges) if e[0]=='1']
    bpos=[i for i,e in enumerate(edges) if e[1]=='1']
    assert len(apos)==len(bpos)==r
    T0=-14; Tm=(1<<k)-1
    rhs=(3**r)*T0 + sum(3**(r-j)*(3*(1<<a)-(1<<b))
                            for j,(a,b) in enumerate(zip(apos,bpos),1))
    assert (1<<m)*Tm == rhs
    # Proper-factor relation follows.
    assert U-V == 4*(X+Y)
    # Concatenation identity and exact phase factorization.
    uv=u+v
    assert Q(uv) == Y*U + X*V
    assert Q(uv) == (X+Y)*(V+4*Y)
    # The scalar phase quotient, when integral, is exactly the cycle quotient.
    rem=(V+4*Y)%M
    print(label, 'A,L,t=',(A,L,t),'proper-factor PASS','phase_remainder=',rem)
    if rem==0:
        N=(V+4*Y)//M
        assert N>0
        assert Y*N+U == X*(N+4)
        assert Y*(N+4)+V == X*N
        assert Q(uv)==N*(X*X-Y*Y)
        print(label,'FULL PHASE: N=',N,'mutual 4-swap PASS')
    return rem

# RL47 audited (65,41), t=2 exact structural witness.
EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()
check_instance(65,41,2,EDGES,'RL47 witness')

# RL43/RL45 audited t=0 proper-factor countermodel.  Remove mandatory first 01
# and terminal 10; the remaining columns are precisely the internal x,y block.
path='00 01 10 00 PUMP 00 01 11 10 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 11'.split()
loops=15
pairs=[(0,1)]
for token in path:
    if token=='PUMP': pairs += [(1,1)]*loops
    else: pairs.append((int(token[0]),int(token[1])))
pairs.append((1,0))
assert pairs[0]==(0,1) and pairs[-1]==(1,0)
internal=[str(x)+str(y) for x,y in pairs[1:-1]]
check_instance(65,41,0,internal,'RL45 countermodel')

# Pure word algebra regression: Q(concat)=3^wt(second)Q(first)+2^len(first)Q(second).
for u in ([1],[0,1],[1,0,1],[1,1,0,0,1]):
    for v in ([0],[1,0],[0,1,1]):
        assert Q(list(u)+list(v)) == 3**sum(v)*Q(list(u)) + (1<<len(u))*Q(list(v))
print('RL48 four-swap/factorization verifier: PASS')
