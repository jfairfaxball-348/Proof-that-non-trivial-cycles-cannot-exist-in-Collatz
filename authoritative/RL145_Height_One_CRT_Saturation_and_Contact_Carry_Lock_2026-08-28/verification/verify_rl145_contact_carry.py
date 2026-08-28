#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
P=A-L
K=2*L-A
SINGLE=5*L-3*A
DOUBLE=2*A-3*L

assert P==80_448_749_305
assert K==57_079_296_007
assert SINGLE==33_709_842_709
assert DOUBLE==23_369_453_298
assert 2*A>3*L
assert 3*A<5*L
assert SINGLE+DOUBLE==K
assert SINGLE+2*DOUBLE==P

# RL145.1 symbolic count identity check.
# n1+n2+n3=gL and n2+2n3=gP imply n1=gK+n3.
for g in (1,2,13,101):
    for n3 in (0,1,7):
        if 2*n3<=g*P:
            n2=g*P-2*n3
            n1=g*L-n2-n3
            assert n1==g*K+n3

# RL145.3 exact g=13 equalizer population.
g=13
q=K
O2=g*K
t=g*P
C2=9*q
C3=3*q
C4=q
e1=C2-C3
e2=C3-C4
e3=C4
odd1=t-C2
assert O2==13*q
assert odd1>0
assert odd1+2*e1+3*e2+4*e3==g*L
assert 13*SINGLE>5*q

floors={
    "O1_mod3":3*(g*L-1),
    "O2_mod9":9*(O2-1),
    "terminal_mod18":18*(C2-1),
    "continuing_mod18":18*(C3+C4-1),
    "O3_mod27":27*(C3+C4-1),
    "C3_boundary_mod54":54*(C3-1),
    "O4_mod81":81*(C4-1),
    "C4_boundary_mod162":162*(C4-1),
    "all_boundaries_mod6":6*(t-1),
    "zero_depth1_mod2":2*(g*P-1)+1,
}
assert max(floors.values())==18*(C2-1)==162*q-18
assert Fraction(max(floors.values()),O2) < Fraction(162,13)

# Small-carry endpoint thresholds.
assert 2**35 < Fraction(L,3) < 2**36
assert 3**22 < Fraction(L,3) < 3**23
assert (A*22)//L==34
assert (A*23)//L==36

frontier=[]
for r in range(23):
    b=(A*r)//L
    max_k=-1
    for k in range(23):
        if 3*(2**b)*(3**k) < L:
            max_k=k
    frontier.append((r,b,max_k))

expected=[
(0,0,22),(1,1,21),(2,3,20),(3,4,19),(4,6,18),(5,7,17),
(6,9,16),(7,11,15),(8,12,14),(9,14,13),(10,15,12),
(11,17,11),(12,19,10),(13,20,9),(14,22,8),(15,23,7),
(16,25,6),(17,26,5),(18,28,4),(19,30,3),(20,31,2),
(21,33,1),(22,34,0)]
assert frontier==expected

# Algebraic cross-check of the rotated carry recurrence on toy coprime X,Y.
for X,Y,g in ((32,27,5),(256,243,4),(16,9,7)):
    F=sum(X**i*Y**(g-1-i) for i in range(g))
    # Constant contact sequence is an owning contact-polynomial model.
    cs=[7]*g
    Ss=[]
    for t in range(g):
        S=sum(X**i*Y**(g-1-i)*cs[(t+i)%g] for i in range(g))
        assert S%F==0
        Ss.append(S)
    ns=[S//F for S in Ss]
    for t in range(g):
        lhs=X*ns[(t+1)%g]-Y*ns[t]
        rhs=(X-Y)*cs[t]
        assert lhs==rhs

print("RL145 fast verifier: PASS")
print("A,L =",A,L)
print("P,K =",P,K)
print("single/double mechanical one-gaps =",SINGLE,DOUBLE)
print("g=13 C2,C3,C4 =",C2,C3,C4)
print("max saturation floor =",max(floors.values()))
print("endpoint frontier =",frontier)
