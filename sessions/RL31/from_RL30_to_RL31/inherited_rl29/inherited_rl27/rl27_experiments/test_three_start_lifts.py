from fractions import Fraction
from math import gcd

RMIN=1<<71

# affine trajectory under full Collatz T: state=(A*R+C)/2^j

def parity_and_affine(r,c,k):
    # r is representative mod 2^k, enough to determine first k parity bits
    x=r+c
    A=1; C=c; den=1
    out=[]
    for j in range(k):
        bit=x&1
        out.append((bit,A,C,den)) # state before step j
        if bit:
            x=(3*x+1)//2
            C=3*C+den
            A=3*A
        else:
            x//=2
        den*=2
    out.append((None,A,C,den))
    return out

def interval_constraints(r,k):
    # all states after 0..k for starts c in {0,12,4} are >= R.
    # return integer interval [lo, hi] on R (not enforcing residue/mod9 yet)
    lo=RMIN
    hi=None
    for c in (0,12,4):
        arr=parity_and_affine(r,c,k)
        for j,(bit,A,C,den) in enumerate(arr):
            # (A-den)R + C >=0
            q=A-den
            if q==0:
                if C<0:
                    return None
            elif q>0:
                # R >= ceil(-C/q)
                if C<0:
                    need=(-C + q-1)//q
                    if need>lo: lo=need
            else:
                # R <= floor(C/(-q))
                cap=C//(-q)
                if hi is None or cap<hi: hi=cap
                if hi<lo: return None
    return lo,hi

def first_in_progression(r,k,lo):
    # R == r mod 2^k and R == 1 mod9.
    M=1<<k
    # r + M t == 1 mod9
    inv=pow(M,-1,9)
    t0=((1-r)%9)*inv%9
    base=r+M*t0
    step=9*M
    if base<lo:
        n=(lo-base+step-1)//step
        base += n*step
    return base

def viable(r,k):
    iv=interval_constraints(r,k)
    if iv is None: return False,None
    lo,hi=iv
    R0=first_in_progression(r,k,lo)
    if hi is not None and R0>hi:
        return False,(lo,hi,R0)
    return True,(lo,hi,R0)

surv=[27]
print('depth 5 survivors',len(surv),surv)
for k in range(6,121):
    oldmod=1<<(k-1)
    cand=[]
    for r in surv:
        for rr in (r,r+oldmod):
            ok,meta=viable(rr,k)
            if ok: cand.append(rr)
    surv=cand
    if k<=20 or k%5==0 or not surv:
        print('depth',k,'survivors',len(surv))
        if len(surv)<=12:
            print(' residues',surv)
    if not surv:
        break
