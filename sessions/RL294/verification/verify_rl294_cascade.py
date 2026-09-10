#!/usr/bin/env python3
"""Portable RL294 regression verifier.

Checks only promoted algebraic identities and explicit all-depth constructions.
It does not claim Gate A, the all-depth first-d=1 owner theorem, or the
unpromoted (4,39) cascade-wall reduction.
"""

def step_k(d, K, x, allow_depth0=False):
    assert x in (0,1)
    if K % 2 == 0:
        y = x
        if x:
            d2, K2 = d, 3*K//2
        else:
            d2, K2 = d, (K + 3**d - 1)//2
    else:
        y = 1-x
        if x:
            d2, K2 = d-1, (K-1)//2
        else:
            d2, K2 = d+1, 3*(K + 3**d)//2
    if d2 < 1 and not allow_depth0:
        return None
    return d2, K2, y, d-1

def to_J(d,K):
    return K - 2**d + 1

def compose(A,B):
    da,Ka=A; db,Kb=B
    return da+db, (3**db)*Ka + Kb

def replay(d,K,word):
    cost=0
    for ch in word:
        st=step_k(d,K,int(ch))
        assert st is not None
        d,K,y,c=st
        cost += c
    return d,K,cost

def G(z):
    return z//2 if z%2==0 else (3*z-1)//2

edge_checks=0
g_checks=0
for d in range(1,9):
    for K in range(-120,301):
        for x in (0,1):
            st=step_k(d,K,x)
            if st is None:
                continue
            d2,K2,y,c=st
            rhs = 3**y*K + (1-x)*3**(d+y) - (1-y)
            assert 2*K2 == rhs
            assert d2 == d + y - x
            N, N2 = K+1, K2+1
            T, T2 = K+1-3**d, K2+1-3**d2
            if x == 1:
                assert N2 == G(N)
                g_checks += 1
            if x == 0:
                assert T2 == G(T)
                g_checks += 1
            edge_checks += 1

composition_checks=0
for da in range(1,5):
  for db in range(1,5):
    for Ka in range(-16,25):
      for Kb in range(-16,25):
        A=(da,Ka); B=(db,Kb)
        C=compose(A,B)
        for x in (0,1):
            sa=step_k(da,Ka,x)
            if sa is None:
                continue
            da2,Ka2,y,_=sa
            sb=step_k(db,Kb,y)
            if sb is None:
                continue
            db2,Kb2,z,_=sb
            sc=step_k(C[0],C[1],x)
            assert sc is not None
            dc2,Kc2,z2,_=sc
            assert z2 == z
            assert (dc2,Kc2) == compose((da2,Ka2),(db2,Kb2))
            assert C[0]-1 == (da-1)+(db-1)+1
            composition_checks += 1

assoc_checks=0
states=[(d,K) for d in range(1,4) for K in (-7,-3,0,1,3,6,9,14)]
for A in states:
  for B in states:
    for C in states:
        assert compose(compose(A,B),C)==compose(A,compose(B,C))
        assoc_checks += 1

P=(2,6)
R3=(2,0)
R6=(2,-3)
Z=(1,0)
E=(1,1)
I=(0,0)
def BJ(J): return (1,J+1)

assert compose(P,R3)==(4,54) and to_J(4,54)==39
assert compose(Z,Z)==R3
assert compose(BJ(-4),BJ(-6)) == (2,-14) and to_J(2,-14)==-17
assert compose(BJ(-19),BJ(-28)) == (2,-81) and to_J(2,-81)==-84
assert compose(BJ(-4),P) == (3,-21) and to_J(3,-21)==-28
assert compose(R6,BJ(-13)) == (3,-21)

assert step_k(*Z,1,allow_depth0=True)[:2] == Z
assert step_k(*Z,0,allow_depth0=True)[:2] == E
assert step_k(*E,1,allow_depth0=True)[:2] == I
assert step_k(*E,0,allow_depth0=True)[:2] == P

tower_checks=0
for D in range(2,61):
    w2 = "0" + "0"*(D-2) + "1"
    d2,K2,c2 = replay(1,3,w2)
    Sd=(D-1,(3**D-1)//2)
    assert (d2,K2)==Sd
    assert c2 == D*(D-1)//2

    wp = "1" + "0"*(D-2) + "1"
    dp,Kp,cp = replay(*P,wp)
    assert (dp,Kp)==Sd
    assert cp == c2+1
    tower_checks += 1

# P reaches checkpoint J=8 at added cost 2.
d8,K8,c8=replay(*P,"1111")
assert d8==1 and to_J(d8,K8)==8 and c8==2

cp8_checks=0
for D in range(3,41):
    w="0"+"10"*(D-3)+"0"
    dd,KK,cc=replay(1,9,w)
    Sd=(D-1,(3**D-1)//2)
    assert (dd,KK)==Sd
    assert cc==(D-2)**2
    cp8_checks += 1

R=list(range(0,18,2))
carry_checks=0
trans={}
for r in R:
    for y in (0,1):
        s=(r+8)//2 if y==0 else 3*r//2
        candidates=[]
        for rp in R:
            num=s-rp
            if num%9==0:
                c=num//9
                candidates.append((rp,c))
        assert len(candidates)==1
        rp,c=candidates[0]
        trans[(r,y)]=(rp,c)
        assert s==rp+9*c
        carry_checks += 1

assert trans[(0,1)]==(0,0)
assert trans[(0,0)]==(4,0)
assert trans[(4,1)]==(6,0)
assert trans[(6,1)]==(0,1)

g0=0
g4=g0/2
g6=3*g4/2
assert 1+g0 != 3*g6/2

print("RL294 cascade verifier: PASS")
print(f"unified_edge_checks={edge_checks}")
print(f"dual_G_checks={g_checks}")
print(f"composition_checks={composition_checks}")
print(f"associativity_checks={assoc_checks}")
print(f"checkpoint2_P_tower_checks={tower_checks}")
print(f"checkpoint8_tower_checks={cp8_checks}")
print(f"base9_carry_checks={carry_checks}")
print("front_door_factorizations=PASS")
print("Z_E_formal_wall_transducer=PASS")
print("base9_scalar_correction=IMPOSSIBLE_BY_4_EDGE_CONTRADICTION")
print("gate_A=NOT_CLAIMED")
print("all_depth_first_d1_owner=NOT_CLAIMED")
