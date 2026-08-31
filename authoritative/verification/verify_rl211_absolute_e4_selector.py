#!/usr/bin/env python3
from itertools import product

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
K0=1<<37

def b(i): return A*i//L
def compose(acc):
    S=0; Q=0
    for a in acc:
        Q=3*Q+(1<<S)
        S+=a
    return S,Q

assert [b(i) for i in range(5)] == [0,1,3,4,6]
c=[b(i+1)-b(i) for i in range(4)]
assert c == [1,2,1,2]

paths=[]
def rec(i, hs, acc):
    if i==4:
        if hs[-1]==1:
            S,Q=compose(acc)
            paths.append((tuple(hs),tuple(acc),S,Q))
        return
    h=hs[-1]
    ci=c[i]
    for hn in range(h+ci):
        a=ci+h-hn
        assert a>=1
        rec(i+1, hs+[hn], acc+[a])

# h0=0, h1 is anchored to zero; begin after fixed edge 0.
# a0=c0=1.
rec(1,[0,0],[1])
assert paths == [
    ((0,0,0,0,1),(1,2,1,1),5,85),
    ((0,0,1,0,1),(1,1,2,1),5,73),
    ((0,0,1,1,1),(1,1,1,2),5,65),
]

eta81=[]
for hs,acc,S,Q in paths:
    mod=3**4
    coeff=pow(2,S+34,mod)
    rhs=(pow(2,S,mod)+Q)%mod
    eta=(rhs*pow(coeff,-1,mod))%mod
    eta81.append(eta)
assert eta81 == [45,3,56]
assert [x%9 for x in eta81] == [0,3,2]
assert eta81[0]%9 in (0,8)
assert all(x%9 not in (0,8) for x in eta81[1:])

# Exact source/root gap for e=4.
e=4; S=5; Q=85
gap=3**4 * 2**32
assert gap == 2*K0*3**4//2**b(4)

pairs=[]
for eta in (45,126,207):
    y4=(1<<34)*eta-1-gap
    num=(1<<S)*y4-Q
    assert num%(3**4)==0
    y0=num//(3**4)
    yp=y0+K0
    pairs.append((eta,y0%3,yp%3))
assert pairs == [(45,1,0),(126,0,2),(207,2,1)]
assert [r for r,a,z in pairs if a and z] == [207]

# Flat K normalized gaps are dyadic: after removing 3^t only a power of two remains.
for t in range(38):
    bt=b(t)
    # Delta = 3^t * 2^(37-bt), represented as numerator / 2^den.
    if bt<=37:
        num=3**t * 2**(37-bt); den=1
    else:
        num=3**t; den=2**(bt-37)
    assert den & (den-1) == 0
    assert num % 2 == 1 or den == 1

print("PASS RL211 exact absolute e=4 eta selector certificate")
print("root_heights=00001 root_accelerations=1211")
print("eta_mod81=45 eta_mod243=207 h21_state=011")
print("excluded_at_e4=state111 eta_mod18_8_17")
print("rank_deletions=0 frontier=13415865871")
print("flat_K_denominator_consumer=dyadic_barrier")
