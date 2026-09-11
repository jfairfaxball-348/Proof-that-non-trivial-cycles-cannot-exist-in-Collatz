#!/usr/bin/env python3
"""RL295 portable verifier: wall normalization, (4,39) sector cut, Q17 splice."""

def step(d,J,x,allow_depth0=False):
    K=J+2**d-1
    if K%2==0:
        if x:
            d2,K2=d,3*K//2
        else:
            d2,K2=d,(K+3**d-1)//2
    else:
        if x:
            if d<=1 and not allow_depth0:
                return None
            d2,K2=d-1,(K-1)//2
        else:
            d2,K2=d+1,3*(K+3**d)//2
    return d2,K2-2**d2+1,d-1

def replay(d,J,w,allow_depth0=False):
    H=0
    depths=[d]
    for ch in w:
        o=step(d,J,int(ch),allow_depth0)
        assert o is not None, (d,J,ch,w)
        d,J,c=o
        H += c
        depths.append(d)
    return d,J,H,min(depths)

def Kof(d,J): return J+2**d-1
def Jof(d,K): return K-2**d+1

def comp(A,B):
    a,KA=A; b,KB=B
    return (a+b, 3**b*KA+KB)

# 1. Exact wall normalization identities.
wall_checks=0
for a in range(1,7):
    for A in range(-20,21):
        for b in range(1,7):
            for B in range(-20,21):
                for u in range(-5,6):
                    lhs=comp((0,u),(b,B))
                    rhs=(b,B+3**b*u)
                    assert lhs==rhs
                    lhs2=comp((a,A),(0,u))
                    rhs2=(a,A+u)
                    assert lhs2==rhs2
                    wall_checks += 2

# Identity wall and adjacent wall merger.
for u in range(-20,21):
    assert comp((0,0),(0,u))==(0,u)
    assert comp((0,u),(0,0))==(0,u)
    for v in range(-20,21):
        assert comp((0,u),(0,v))==(0,u+v)

# 2. Formal E-wall transducer used by the double-E refactorization.
# E=(d=1,K=1) => J=0; Z=(1,K=0)=>J=-1; P=(2,K=6)=>J=3; I=(0,K=0).
E=(1,Jof(1,1))
Z=(1,Jof(1,0))
for x, expected in [(0,(2,3)), (1,(0,0))]:
    d2,J2,_,=step(*E,x,allow_depth0=True)
    assert (d2,Kof(d2,J2)) == ((2,6) if x==0 else (0,0))

# 3. (4,39) cut.
S=(4,39)
assert replay(*S,"00")[:3] == (5,191,6)
assert replay(*S,"01")[:3] == (3,26,6)  # L_3, K=33
sector_checks=0
for d in range(2,61):
    Cs=(d*d+5*d+2)//2
    for eps in (0,1):
        w="1"+"0"*(d-2)+"1"+str(eps)
        ds,Js,Hs,_=replay(*S,w)
        assert Hs==Cs
        Ks=Kof(ds,Js)
        if d%2==1:
            if eps==0:
                D=d+2
                Kexp=(5*3**D-3)//4
                wp="1"+"0"*(D-2)+"10"
                Hp=(D*D+D-2)//2
            else:
                D=d
                Kexp=(9*3**D-3)//4
                wp="1"+"0"*(D-1)+"11"
                Hp=(D*D+3*D)//2
        else:
            if eps==0:
                D=d+1
                Kexp=(5*3**D-3)//4
                wp="1"+"0"*(D-2)+"10"
                Hp=(D*D+D-2)//2
            else:
                D=d+1
                Kexp=(9*3**D-3)//4
                wp="1"+"0"*(D-1)+"11"
                Hp=(D*D+3*D)//2
        assert (ds,Ks)==(D,Kexp)
        dp,Jp,Hpr,_=replay(2,3,wp)
        assert (dp,Jp)==(ds,Js)
        assert Hpr==Hp
        assert Hpr <= Hs+1
        sector_checks += 1

# 4. Full frozen P -> O_17^(7) -> B_17^(7) -> Q_17 certificate.
P_TO_O17 = (
"1111011010111111011011110111011101111010011101101111110011111010110101011110111101111010110111111011"
"1010011110000010111110110111001101111101001011010111001001111111001111001101010010111100110000111101"
"11011001010111101110101010111111111011001011110111001111001011"
)
assert len(P_TO_O17)==262
d,J,H,_=replay(2,3,P_TO_O17)
assert (d,J,H)==(1,458753,29)

# complementary zero-height exit
d,J,c=step(d,J,1)
assert (d,J,c)==(1,688130,0)

B17_TO_Q17="0010110010010111011101010000000100000000"
assert len(B17_TO_Q17)==40
d2,J2,H2,mindepth=replay(d,J,B17_TO_Q17)
Q17_K=2*3**17
Q17_J=Jof(17,Q17_K)
assert (d2,J2,H2)==(17,Q17_J,154)
# after the forced launch, no intermediate return to d=1:
dd,jj=1,688130
depths=[]
for ch in B17_TO_Q17:
    dd,jj,_=step(dd,jj,int(ch))
    depths.append(dd)
assert depths[0]==2
assert min(depths[:-1])>=2

FULL=P_TO_O17+"1"+B17_TO_Q17
assert len(FULL)==303
d,J,H,_=replay(2,3,FULL)
assert (d,J,H)==(17,Q17_J,183)

# 5. Exact Q_d propagation and constant owner lag versus the (6,807) spine.
spine="1000000101000101"
dS,JS,HS,_=replay(6,807,spine)
assert (dS,Kof(dS,JS),HS)==(17,Q17_K,169)

side_expected=[
(6,736,5),(5,621,10),(6,1462,16),(7,3801,23),
(8,10558,31),(9,30471,40),(10,89737,50),(12,530626,61),
(11,401454,72),(13,1792803,84),(12,1501654,96),
(13,3446175,109),(14,8752393,123),(16,45372670,138),
(15,35839500,153),(17,150532452,169)
]
dd,jj,hh=6,807,0
side=[]
for bit in spine:
    alt=str(1-int(bit))
    oa=step(dd,jj,int(alt))
    assert oa is not None
    da,ja,ca=oa
    side.append((da,ja,hh+ca))
    o=step(dd,jj,int(bit))
    dd,jj,c=o
    hh+=c
assert side==side_expected

tower_checks=0
for D in range(17,81):
    suffix="10"*(D-17)
    do,jo,Ho,_=replay(17,Q17_J,suffix)
    assert do==D and Kof(do,jo)==2*3**D
    owner=183+Ho
    source=169+Ho
    assert owner==D*D-3*D-55
    assert source==D*D-3*D-69
    assert owner-source==14
    assert owner <= source+31
    tower_checks += 1

print("RL295 verifier: PASS")
print("wall_normalization_checks=",wall_checks)
print("4_39_parametric_sector_checks=",sector_checks)
print("P_to_O17_columns=262 cost=29")
print("B17_to_Q17_columns=40 cost=154")
print("P_to_Q17_columns=303 cost=183")
print("Q17_source_6807_cost=169")
print("Q_tail_owner_lag=14")
print("Q_tail_credit=31 spare=17")
print("Q_tail_checks=",tower_checks)
print("pre_Q17_side_sectors=16")
print("gate_A=NOT_CLAIMED")
print("Bcal_P_le_1=NOT_CLAIMED")
