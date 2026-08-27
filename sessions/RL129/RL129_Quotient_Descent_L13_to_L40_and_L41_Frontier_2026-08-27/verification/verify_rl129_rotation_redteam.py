#!/usr/bin/env python3
from itertools import product

def Q(bits):
    L=sum(bits)
    seen=0
    out=0
    for p,b in enumerate(bits):
        if b:
            out += (2**p)*(3**(L-1-seen))
            seen += 1
    return out

def D(bits):
    L=sum(bits); A=len(bits)
    return 2**A-3**L

checked=0
bound_checked=0
divisible_checked=0
for A in range(2,13):
    for bits in product((0,1), repeat=A):
        L=sum(bits); Z=A-L
        if L==0 or Z==0: continue
        d=D(bits)
        q=Q(bits)
        b0=bits[0]
        rot=bits[1:]+bits[:1]
        qr=Q(rot)
        if b0==0:
            assert 2*qr==q
        else:
            assert 2*qr==3*q+d
        checked += 1

        if bits[0]==1 and bits[-1]==0:
            assert q <= 2**(Z-1)*(3**L-2**L)
            bound_checked += 1

        if d>0 and q%d==0:
            n=q//d
            nr=qr//d
            if b0==0:
                assert n%2==0 and nr==n//2
            else:
                assert n%2==1 and nr==(3*n+1)//2
            divisible_checked += 1

print('RL129 rotation/bound red-team: PASS')
print(f'rotation_words_checked={checked}')
print(f'transition_root_bounds_checked={bound_checked}')
print(f'exact_divisible_rotation_events_checked={divisible_checked}')
