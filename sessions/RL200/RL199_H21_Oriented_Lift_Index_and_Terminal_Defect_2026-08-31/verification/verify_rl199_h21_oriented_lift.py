#!/usr/bin/env python3

C34=21*(2**34)
CPRE=14*(3**34)
T=7*(3**35)
MOD22=2**22
M=9*MOD22

def v2(n):
    assert n>0
    return (n & -n).bit_length()-1

def y34(q):
    return (2**34)*q-1

def tail(q,t):
    return (2**(34-t))*(3**t)*q-1

# Fixed constants and affine tail.
assert C34==360_777_252_864
assert CPRE==233_480_543_795_331_966
assert T==350_220_815_692_997_949
for q in (2,8,9,17,18,35,72,89):
    lo=y34(q)
    hi=y34(q+21)
    assert hi-lo==C34
    y,z=lo,hi
    for t in range(33):
        assert v2(3*y+1)==1 and v2(3*z+1)==1
        y=(3*y+1)//2
        z=(3*z+1)//2
        assert y==tail(q,t+1)
        assert z==tail(q+21,t+1)
    assert z-y==CPRE

# tau35 inverse + unit-mod-3 prehistory, state selector, terminal orientation.
rows={}
for r in range(18):
    q=r if r else 18
    lo=y34(q); hi=y34(q+21)
    candidates=[]
    # 011: leading exponent 1
    nlo=2*lo-1; nhi=2*hi-1
    if nlo%3==0 and nhi%3==0:
        zlo,zhi=nlo//3,nhi//3
        if zlo%3 and zhi%3:
            candidates.append("011")
    # 111: leading exponent 2
    nlo=4*lo-1; nhi=4*hi-1
    if nlo%3==0 and nhi%3==0:
        zlo,zhi=nlo//3,nhi//3
        if zlo%3 and zhi%3:
            candidates.append("111")
    if candidates:
        assert len(candidates)==1
        state=candidates[0]
        prelo=tail(q,33); prehi=tail(q+21,33)
        klo=v2(3*prelo+1); khi=v2(3*prehi+1)
        assert (klo==1) ^ (khi==1)
        orientation="lower" if klo==1 else "upper"
        sign="+" if orientation=="lower" else "-"
        rows[r]=(state,orientation,sign)

assert rows=={
    0:("011","lower","+"),
    8:("111","lower","+"),
    9:("011","upper","-"),
    17:("111","upper","-"),
}

# Exact terminal defect and numerator invariance on representative classes.
for r,(state,orientation,sign) in rows.items():
    q=r if r else 18
    sodd=q+21 if q%2==0 else q
    nu=v2((3**34)*sodd-1)
    assert nu>=1
    prelo=tail(q,33); prehi=tail(q+21,33)
    klo=v2(3*prelo+1); khi=v2(3*prehi+1)
    hlo=22-klo; hhi=22-khi
    if q%2==0:
        assert hlo==21 and hhi==21-nu and hlo-hhi==nu
        outlo=(3*prelo+1)//(2**klo)
        outhi=(3*prehi+1)//(2**khi)
        cterm=(2**nu)*outhi-outlo
    else:
        assert hhi==21 and hlo==21-nu and hlo-hhi==-nu
        outlo=(3*prelo+1)//(2**klo)
        outhi=(3*prehi+1)//(2**khi)
        cterm=outhi-(2**nu)*outlo
    assert cterm==T

# Hensel inverse and CRT forbidden residues.
rinv=pow(pow(3,34,MOD22),-1,MOD22)
assert rinv==1_893_305
assert (pow(3,34,MOD22)*rinv)%MOD22==1

def crt9_2(a,b):
    # x=a mod9, x=b mod2^22
    return (a + 9*(((b-a)*pow(9,-1,MOD22))%MOD22))%M

forbidden={
    0:crt9_2(0,(rinv-21)%MOD22),
    8:crt9_2(8,(rinv-21)%MOD22),
    9:crt9_2(0,rinv),
    17:crt9_2(8,rinv),
}
assert forbidden=={
    0:18_670_500,
    8:1_893_284,
    9:6_087_609,
    17:27_059_129,
}
assert M==37_748_736 and M//18==2_097_152
for r,f in forbidden.items():
    assert f%18==r
    s=f+21 if f%2==0 else f
    assert v2((3**34)*s-1)>=22

# eta-independent common difference formula.
for t in range(34):
    diff=tail(123+21,t)-tail(123,t)
    assert diff==21*(2**(34-t))*(3**t)
assert 3*CPRE==2*T

print("PASS RL199 exact H21 oriented lift-index certificate")
print("allowed_eta_mod18=0,8,9,17")
print("state_selector=011:eta_mod9_0 111:eta_mod9_8")
print("terminal_sign=positive_if_eta_even negative_if_eta_odd")
print("terminal_defect_magnitude=nu_1_to_21_physical")
print("hensel_inverse_mod_2^22=1893305")
print("hensel_modulus=37748736")
print("forbidden_eta=0:18670500,8:1893284,9:6087609,17:27059129")
print("common_pair_suffix_eta_blind=yes")
