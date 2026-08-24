from math import gcd
RMIN=1<<71

def parity_and_affine(r,c,k):
    x=r+c; A=1; C=c; den=1
    out=[]
    for j in range(k):
        bit=x&1
        out.append((bit,A,C,den))
        if bit:
            x=(3*x+1)//2; C=3*C+den; A=3*A
        else:
            x//=2
        den*=2
    out.append((None,A,C,den))
    return out

def interval_constraints(r,k):
    lo=RMIN; hi=None
    for c in (0,12,4):
        for bit,A,C,den in parity_and_affine(r,c,k):
            q=A-den
            if q==0:
                if C<0:return None
            elif q>0:
                if C<0: lo=max(lo,(-C+q-1)//q)
            else:
                cap=C//(-q); hi=cap if hi is None else min(hi,cap)
                if hi<lo:return None
    return lo,hi

def first_prog(r,k,lo):
    M=1<<k
    t0=((1-r)%9)*pow(M,-1,9)%9
    base=r+M*t0; step=9*M
    if base<lo:base+=((lo-base+step-1)//step)*step
    return base

def viable(r,k):
    iv=interval_constraints(r,k)
    if iv is None:return False
    lo,hi=iv; x=first_prog(r,k,lo)
    return hi is None or x<=hi

def T(n):return (3*n+1)//2 if n&1 else n//2

def metrics(r,K):
    xs=[r,r+12,r+4]; ps=[0,0,0]
    uns=0; maxv=0; maxrun=0; run=0
    for j in range(K):
        sync=(ps[0]==ps[1]==ps[2])
        if sync:
            run+=1; maxrun=max(maxrun,run)
            g=abs(xs[1]-xs[0]);h=abs(xs[2]-xs[0]);d=gcd(g,h)
            vv=0
            if d:
                while d%2==0:vv+=1;d//=2
            maxv=max(maxv,vv)
        else:
            uns+=1;run=0
        for i in range(3):
            ps[i]+=xs[i]&1; xs[i]=T(xs[i])
    return uns,maxv,maxrun

surv=[27]
for k in range(6,36):
    old=1<<(k-1); ns=[]
    for r in surv:
        if viable(r,k):
            ns.append(r)
        rr=r+old
        if viable(rr,k):
            ns.append(rr)
    surv=ns
    if k in (20,25,30,35):
        vals=[metrics(r,k) for r in surv]
        print('depth',k,'survivors',len(surv),'min_unsync',min(x[0] for x in vals),'max_v2',max(x[1] for x in vals),'max_sync_run_levels',max(x[2] for x in vals))
