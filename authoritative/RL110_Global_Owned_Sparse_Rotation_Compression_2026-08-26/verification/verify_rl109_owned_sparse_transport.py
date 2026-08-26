#!/usr/bin/env python3
from itertools import product
from statistics import median_low

RL20_WORD = (
"110110110101101101011011011010110110101101101101011011010110110110101101101011011010"
"110110110101101101011011011010110110101101101101011011010110110110101101101011011010"
"1101101101011010"
)
RL20_REMAINDER = 322171738410077807581692882247758374512983113782519312

def q1(w):
    B = 0
    for i, ch in enumerate(w):
        if ch == '1':
            B = 3 * B + (1 << i)
    return B

def qs(w, s):
    B = 0
    for i, ch in enumerate(w):
        if ch == '1':
            B = 3 * B + s * (1 << i)
    return B

def cyclic_flow_data(a, b):
    n = len(a)
    S=[]
    cur=0
    for i in range(n):
        cur += (1 if a[i]=='1' else 0) - (1 if b[i]=='1' else 0)
        S.append(cur)
    assert cur == 0
    # minimizing integer c for sum_i |c+S_i|: c is a median of -S_i
    vals=sorted(-x for x in S)
    c=vals[(n-1)//2]
    f=[c+x for x in S]
    return sum(abs(x) for x in f), f

def rotate_after_edge(w, edge):
    # edge i is between i and i+1 mod n; cut there, so new index 0=i+1.
    n=len(w); j=(edge+1)%n
    return w[j:]+w[:j]

def linear_distance(a,b):
    cur=0; total=0
    for i in range(len(a)-1):
        cur += (1 if a[i]=='1' else 0) - (1 if b[i]=='1' else 0)
        total += abs(cur)
    return total

# 1. Exhaustive single-swap sparse numerator identity and generalized scaling.
swap_checks=0
scale_checks=0
for n in range(2, 11):
    for bits in product('01', repeat=n):
        w=''.join(bits)
        q=q1(w)
        for s in (1,2,3,5,7,11):
            assert qs(w,s) == s*q
            scale_checks += 1
        for i in range(n-1):
            if w[i:i+2]=='10':
                v=w[:i]+'01'+w[i+2:]
                t=w[i+2:].count('1')
                assert q1(v)-q == (1<<i)*(3**t)
                swap_checks += 1

# 2. Exhaustive cyclic zero-flow cut lemma on small equal-weight pairs.
# If cyclic radius R<n, every chosen minimizing flow with total R has a zero edge;
# cutting a zero-flow edge realizes the same R as a linear earth-mover distance.
cut_checks=0
for n in range(2,9):
    words=[''.join(x) for x in product('01', repeat=n)]
    bywt={}
    for w in words:
        bywt.setdefault(w.count('1'), []).append(w)
    for group in bywt.values():
        for ia,a in enumerate(group):
            for b in group[ia+1:]:
                R,f=cyclic_flow_data(a,b)
                if R < n:
                    zeros=[i for i,x in enumerate(f) if x==0]
                    assert zeros
                    edge=zeros[0]
                    ar=rotate_after_edge(a,edge)
                    br=rotate_after_edge(b,edge)
                    assert linear_distance(ar,br)==R
                    cut_checks += 1


# 2b. Exhaustive one-step rotation radius identity: dist_cyc(w,rot_1(w))=min(L,A-L).
rot1_checks=0
for n in range(2,11):
    for bits in product('01', repeat=n):
        w=''.join(bits)
        L=w.count('1')
        if L in (0,n):
            continue
        v=w[1:]+w[:1]
        R,_=cyclic_flow_data(w,v)
        assert R == min(L,n-L)
        rot1_checks += 1

# 3. RL20 exact radius-4 fake red team: local geometry survives, full-D ownership fails.
assert len(RL20_WORD)==184 and RL20_WORD.count('1')==116
A=len(RL20_WORD); L=RL20_WORD.count('1')
D=(1<<A)-3**L
Q=q1(RL20_WORD)
assert D > 1
assert Q % D == RL20_REMAINDER != 0
minR=None
for i in range(A):
    a=RL20_WORD[i:]+RL20_WORD[:i]
    for j in range(i+1,A):
        b=RL20_WORD[j:]+RL20_WORD[:j]
        R,_=cyclic_flow_data(a,b)
        if minR is None or R<minR:
            minR=R
assert minR==4

print('RL109 owned sparse transport verifier: PASS')
print('single adjacent-swap identities checked =', swap_checks)
print('generalized-increment scaling checks =', scale_checks)
print('zero-flow cut pair checks =', cut_checks)
print('one-step rotation radius checks =', rot1_checks)
print('RL20 fake minimum cyclic radius =', minR)
print('RL20 fake Q mod D =', Q % D)
