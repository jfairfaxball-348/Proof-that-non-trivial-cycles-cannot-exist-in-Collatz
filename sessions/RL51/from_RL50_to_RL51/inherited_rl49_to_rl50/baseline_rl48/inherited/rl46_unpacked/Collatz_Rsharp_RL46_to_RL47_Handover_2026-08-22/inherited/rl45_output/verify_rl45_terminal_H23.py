#!/usr/bin/env python3
from collections import deque

HMAX=23
EXPECTED=[9,10,9,32,26,49,90,105,172,270,549,859,1768,3578,6906,13642,26624,53758,109744,222460,458460,950914,1987355,4152245]

def v2(n):
    assert n>0
    s=0
    while n%2==0:
        n//=2; s+=1
    return s

# Exact quotient state after the mandatory first local column (alpha,beta)=(0,1)
# for incoming physical gap 9.  T=-14 and J=T+3^d-2^d=-13.
seen=[set() for _ in range(HMAX+1)]
queues=[deque() for _ in range(HMAX+1)]
seen[0].add((1,-13)); queues[0].append((1,-13))
positive_equal=[]
max_d=[]

for H in range(HMAX+1):
    q=queues[H]
    while q:
        d,J=q.popleft()
        K=H+d*(d+1)//2-1
        if J>0:
            vv=v2(J)
            # Stronger statewise valuation form.  At d=1 this is exactly
            # v2(T+1)<=H; a violation at d>1 descends through compatible 10s.
            assert vv<=K, (H,d,J,vv,K)
            if vv==K:
                positive_equal.append((H,d,J,K))

        A=3**d-2**d
        B=2**d-1
        C=3**(d+1)-2**d-1

        # Because A is odd, J and T have opposite parity.  Exact compatibility
        # therefore leaves precisely the same-bit edges when J is odd and the
        # skew edges when J is even.
        if J&1:
            nxt=((d,(J+A)//2),(d,(3*J+B)//2))       # 00, 11
        else:
            tmp=[(d+1,(3*J+C)//2)]                  # 01
            if d>1:
                tmp.append((d-1,J//2))              # 10 internal descent
            nxt=tuple(tmp)

        Hn=H+d-1
        if Hn>HMAX:
            continue
        for st in nxt:
            if st not in seen[Hn]:
                seen[Hn].add(st); queues[Hn].append(st)

    assert len(seen[H])==EXPECTED[H], (H,len(seen[H]),EXPECTED[H])
    max_d.append(max(d for d,J in seen[H]))

assert set(positive_equal)=={(3,1,8,3)}

print('RL45 terminal H<=23 quotient verifier: PASS')
print('state counts H=0..23 =',EXPECTED)
print('max d by H =',max_d)
print('positive equality states =',sorted(set(positive_equal)))
print('no positive reachable state with v2(J)>K through H=23')
print('certificate is independent of excursion e, p, and length once (d,H,J) is fixed')
