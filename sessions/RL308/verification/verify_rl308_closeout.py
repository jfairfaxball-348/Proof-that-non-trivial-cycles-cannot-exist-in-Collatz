#!/usr/bin/env python3
from fractions import Fraction

def st(s,x):
    d,J=s
    K=J+2**d-1
    if K%2==0:
        d2,K2=(d,3*K//2) if x else (d,(K+3**d-1)//2)
    elif x:
        if d<=1:
            return None
        d2,K2=d-1,(K-1)//2
    else:
        d2,K2=d+1,3*(K+3**d)//2
    return (d2,K2-2**d2+1),d-1

def rp(s,w):
    c=0
    for q in w:
        o=st(s,int(q))
        assert o is not None, (s,w,q)
        s,z=o
        c+=z
    return s,c

X=(4,43)
Y=(6,504)
M17=(2,-17)
C8=(1,8)

safe_data = [
    ("010",(3,23),8,"01000111100000100",18,11),
    ("011",(3,44),8,"010001111011011111001000",13,6),
    ("100",(5,216),10,"010000010000",17,8),
    ("101",(5,347),10,"010000010001",17,8),
    ("110",(4,90),8,"0100011110100100",14,7),
    ("111",(2,18),8,"01000111101011100",13,6),
    ("0010",(4,81),13,"0100011110110101111110000000",20,8),
    ("0011",(4,153),13,"01000111101101011111101101100000",17,5),
    ("00001",(5,326),20,"010001111011010111111011011110111011101111010011101101111110011110001010100100000000",27,8),
    ("00011",(5,495),20,"01000111101101011111101101111011101110111101001110110111111001111000001101110111111011010110111010001101110000000000",26,7),
]
residuals = {
    "00000": ((7,2039),20),
    "00010": ((7,2546),20),
}

for w,s,c,ow,oc,bnd in safe_data:
    assert rp(X,w)==(s,c), (w,rp(X,w),(s,c))
    assert rp(M17,ow)==(s,oc), (w,rp(M17,ow),(s,oc))
    assert 1+oc-c==bnd, (w,1+oc-c,bnd)

for w,v in residuals.items():
    assert rp(X,w)==v, (w,rp(X,w),v)

leaves=[x[0] for x in safe_data]+list(residuals)
assert len(leaves)==12 and len(set(leaves))==12
for i,a in enumerate(leaves):
    for j,b in enumerate(leaves):
        if i!=j:
            assert not b.startswith(a), (a,b)

kraft=sum(Fraction(1,2**len(w)) for w in leaves)
assert kraft==1, kraft

proper={""}
for w in leaves:
    for i in range(1,len(w)):
        proper.add(w[:i])
for w in proper:
    s,c=rp(X,w)
    d,J=s
    assert not (d==1 and J>0 and J%2==0), (w,s,c)

assert max(x[5] for x in safe_data)==11
assert set(residuals.values())=={((7,2039),20),((7,2546),20)}

# Frozen supporting common-state identities.
assert rp(C8,"011010")==((2,19),4)
assert rp(X,"11101")==((2,19),11)
assert rp(X,"1110111")==((1,15),13)
assert rp(Y,"1111111100")==((1,15),19)

print("RL308_CLOSEOUT_VERIFIER_GREEN")
print("cut_leaves",len(leaves))
print("owned_leaves",len(safe_data))
print("kraft",kraft)
print("max_owned_branch_bound",max(x[5] for x in safe_data))
print("residual_1",(7,2039),20,31)
print("residual_2",(7,2546),20,31)
print("supporting_common_state_X_8",(2,19),"costs",11,4)
print("supporting_common_state_Y_X",(1,15),"costs",19,13)
