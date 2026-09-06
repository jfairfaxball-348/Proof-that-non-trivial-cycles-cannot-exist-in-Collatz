\
#!/usr/bin/env python3
from collections import Counter
from math import gcd

def Q(bits):
    L=sum(bits); q=0; r=0
    for i,b in enumerate(bits):
        if b:
            r += 1
            q += (1<<i) * (3**(L-r))
    return q

def rot(bits,m):
    m %= len(bits)
    return bits[m:]+bits[:m]

def flow(bits,m):
    y=rot(bits,m); c=0; vals=[]
    for a,b in zip(bits,y):
        c += a-b
        vals.append(c)
    med=sorted(vals)[(len(vals)-1)//2]
    return [v-med for v in vals]

def dist(bits,m):
    return sum(abs(v) for v in flow(bits,m))

def primitive(bits):
    A=len(bits)
    for p in range(1,A):
        if A%p==0 and bits == bits[:p]*(A//p):
            return False
    return True

def runs(g):
    if not any(g): return []
    if 0 in g:
        k=g.index(0); z=g[k:]+g[:k]
    else:
        z=g
    out=[]; cur=[]
    for v in z:
        if v==0:
            if cur: out.append(cur); cur=[]
        else:
            cur.append(v)
    if cur: out.append(cur)
    return out

def topology(g):
    assert sum(abs(v) for v in g)==5
    rr=runs(g)
    if max(abs(v) for v in g)<=1:
        ll=sorted((len(r) for r in rr), reverse=True)
        return "["+",".join(map(str,ll))+"]"
    masses=sorted((sum(abs(v) for v in r) for r in rr), reverse=True)
    if masses==[5]: return "height2-connected-5"
    if masses==[4,1]: return "height2-4+1"
    raise AssertionError((g,masses))

expected_top={
    "[5]":2070,"[4,1]":10798,"[3,2]":10382,"[3,1,1]":34684,
    "[2,2,1]":30830,"[2,1,1,1]":67150,"[1,1,1,1,1]":23326,
    "height2-connected-5":696,"height2-4+1":1606,
}
expected_skew={1:50802,3:48254,5:82486}

raw=0; top=Counter(); skew=Counter(); full=[]; proper=set(); checks=0
for A in range(1,19):
    for mask in range(1<<A):
        b=[(mask>>i)&1 for i in range(A)]
        L=sum(b); D=(1<<A)-3**L
        if D<=1: continue
        q0=Q(b); has5=False
        for m in range(1,A):
            g=flow(b,m)
            if sum(abs(v) for v in g)!=5: continue
            has5=True; raw += 1
            top[topology(g)] += 1
            k=sum(g); skew[abs(k)] += 1
            assert abs(k) in (1,3,5) and k != 0
            assert (m*L+k)%A==0
            qq=(m*L+k)//A
            assert qq*A-m*L==k
            assert k % gcd(A,L)==0
            checks += 1
            if q0%D==0:
                full.append((A,L,D,q0,mask,m))
        if has5 and q0%D!=0 and gcd(q0,D)>1:
            proper.add((A,L,D,q0,gcd(q0,D),mask))

assert raw==181542
assert dict(top)==expected_top
assert dict(skew)==expected_skew
assert checks==181542
assert len(full)==10
for A,L,D,q0,mask,m in full:
    b=[(mask>>i)&1 for i in range(A)]
    assert (A,L,D)==(10,5,781)
    assert not primitive(b)
    assert b in ([1,0]*5,[0,1]*5)
assert len(proper)==4590

w={
"[5]":(10,"1111100000",1),
"[4,1]":(10,"1111010000",1),
"[3,2]":(10,"1110110000",9),
"[3,1,1]":(10,"1101010100",3),
"[2,2,1]":(11,"11011010000",1),
"[2,1,1,1]":(10,"1101010100",1),
"[1,1,1,1,1]":(13,"1101100100100",2),
"height2-connected-5":(13,"1101101101000",3),
"height2-4+1":(12,"111001001000",3),
}
for t,(A,s,m) in w.items():
    b=list(map(int,s)); L=sum(b); D=(1<<A)-3**L
    ds=[dist(b,j) for j in range(1,A)]
    assert primitive(b) and D>1
    assert dist(b,m)==5 and topology(flow(b,m))==t
    assert 3 not in ds and 4 not in ds

neg=list(map(int,"00011110111"))
A=len(neg); L=sum(neg); D=(1<<A)-3**L; q0=Q(neg)
assert (A,L,D,q0,q0//D)==(11,7,-139,18904,-136)
assert [dist(neg,m) for m in range(1,A)]==[4,7,7,7,8,8,7,7,7,4]

print("PASS RL265 Radius-5 structural reconstruction")
print("raw_distance5_A_le_18=181542")
print("topologies="+repr(dict(sorted(top.items()))))
print("skew_abs_counts="+repr(dict(sorted(skew.items()))))
print("determinant_checks=181542")
print("full_D_hits=10 all_nonprimitive_alternating_A10_D781")
print("proper_factor_only_words=4590")
print("irreducible_topology_witnesses=9 all_primitive_D_gt_1_no_distance_3_or_4_rotations")
print("RL247_negative_regression=PASS D=-139 Q=18904 n=-136")
print("FAST_RL265_VERIFIERS_PASS")
