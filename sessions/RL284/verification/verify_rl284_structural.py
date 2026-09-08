#!/usr/bin/env python3
"""Portable RL284 structural regression verifier."""

def v2(n):
    n=abs(n)
    assert n != 0
    c=0
    while n%2==0:
        n//=2
        c+=1
    return c

def odd_step(n):
    assert n%2 != 0
    x=3*n+1
    a=v2(x)
    m=x//(2**a)
    assert m%2 != 0
    return m,a

def pred(m,a):
    assert m%2 != 0 and a>=1
    num=(2**a)*m-1
    assert num%3==0
    return num//3

forward=0
for n in range(-3995,3996,2):
    m,a=odd_step(n)
    assert m%3 != 0
    assert m%3 == ((-1)**a)%3
    assert pred(m,a)==n
    forward += 1
assert forward == 3996

converse=0
rays=0
for m in range(-99,100,2):
    if m%3==0:
        continue
    for a in range(1,13):
        if m%3 != ((-1)**a)%3:
            continue
        n=pred(m,a)
        assert odd_step(n)==(m,a)
        converse += 1
        assert pred(m,a+2)==4*n+1
        rays += 1
assert converse == 396
assert rays == 396

witnesses=[(1,1,2),(7,11,1),(5,1,4),(11,17,1)]
for n,m,a in witnesses:
    assert odd_step(n)==(m,a)
assert [(n%3,m%3) for n,m,a in witnesses]==[(1,1),(1,2),(2,1),(2,2)]

cycles=[
    ([1],[2]),
    ([-1],[1]),
    ([-91,-17,-25,-37,-55,-41,-61],[4,1,1,1,2,1,1]),
]
for nodes,vals in cycles:
    n=nodes[0]
    out=[]
    for _ in nodes:
        n,a=odd_step(n)
        out.append(a)
    assert n==nodes[0]
    assert out==vals

print("RL284 portable structural regression: PASS")
print(f"forward_labelled_reconstruction_cases={forward}")
print(f"converse_admissible_pairs={converse}")
print(f"predecessor_ray_cases={rays}")
print("mod3_orientation_witnesses=4")
print("cycle_valuation_words=PASS")
print("prime_branch_indifference=ANALYTIC_FROM_ADMISSIBILITY_CRITERION")
