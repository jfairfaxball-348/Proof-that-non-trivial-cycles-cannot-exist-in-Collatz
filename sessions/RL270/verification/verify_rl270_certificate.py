#!/usr/bin/env python3
from math import comb, gcd

NONBRACKET_CUTOFF=1713
BRACKET_CUTOFF=690205
EXPECTED_PAIRS=2234
EXPECTED_MAX_A=690
EXPECTED_RAW=618_391_058_390
EXPECTED_FAMILY={
'antipodal':7_097_775_603,
'long':3_117_265_503,
'short':6_563_699,
'interlaced':538_629_405,
}
EXPECTED_OPS={
'antipodal':(4_489_399,4_489_399),
'long':(2_798_156,1_107_046),
'short':(72_715,150_525),
'interlaced':(53_541,1_378_850),
}
EXPECTED_TOTAL=10_760_234_210
EXPECTED_RESIDUES=14_539_631
EXPECTED_COARSE=[
(5,3,3,2),(8,5,3,2),(27,17,19,12),(46,29,19,12),
(65,41,19,12),(149,94,84,53),(233,147,84,53)]

def positive_D(A,L): return (1<<A)-3**L

def mixed_bound(A,L,m,q):
    U5=(4*A)//5
    r=q if m<=A-m else L-q
    return 5*3**(7+r)*2**(U5-r)

def determinant_pair(A,L):
    if L<=1 or gcd(A,L)!=1:return None
    q=pow(A,-1,L)
    num=q*A-1
    if num%L:return None
    m=num//L
    if not(0<m<A and 0<q<L):return None
    assert q*A-m*L==1
    return m,q

def stern_brocot_rows_exact(cutoff):
    ln,ld=1,1; un,ud=2,1
    l2,l3=2,3; u2,u3=4,3
    rows=[]
    while True:
        mn,md=ln+un,ld+ud
        if un>cutoff and mn>cutoff:break
        m2,m3=l2*u2,l3*u3
        if m2>m3:
            un,ud=mn,md; u2,u3=m2,m3
        else:
            ln,ld=mn,md; l2,l3=m2,m3
        A,L,m,q=un,ud,ln,ld
        if A<=cutoff and 0<m<A and 0<q<L:
            assert q*A-m*L==1 and (1<<A)>3**L and (1<<m)<3**q
            row=(A,L,m,q)
            if not rows or rows[-1]!=row: rows.append(row)
    return rows

def complete_survivors():
    out=set()
    for A in range(2,NONBRACKET_CUTOFF):
        for L in range(2,A):
            D=positive_D(A,L)
            if D<=1:continue
            p=determinant_pair(A,L)
            if not p:continue
            m,q=p
            if D<=mixed_bound(A,L,m,q):out.add((A,L,m,q))
    rows=stern_brocot_rows_exact(BRACKET_CUTOFF)
    assert len(rows)==36
    coarse=[]
    for row in rows:
        A,L,m,q=row
        if positive_D(A,L)<=mixed_bound(A,L,m,q):
            coarse.append(row);out.add(row)
    assert coarse==EXPECTED_COARSE
    return sorted(out)

def antipodal_count(A,L):
    dmin=max(1,2*L-A+1); B=L-1
    M=B-dmin+1
    return comb(M,4) if M>=4 else 0

def short_count(A,L):
    K=A-2*L-1; U=min(K,L-2)
    if U<3:return 0
    return (L-1)*comb(U,3)-3*comb(U+1,4)

def inter_count(A,L):
    amin=max(1,2*L-A+1); cmin=max(1,A-2*L+1)
    M0=2*amin+cmin+1; N=(L-1)-M0
    return comb(N+4,4) if N>=0 else 0

def sum_min_sminus1(lo,hi,cap):
    if lo>hi or cap<1:return 0
    split=min(hi,cap+1); total=0
    if lo<=split:
        n=split-lo+1
        total += n*((lo-1)+(split-1))//2
    lo2=max(lo,cap+2)
    if lo2<=hi: total += (hi-lo2+1)*cap
    return total

def long_count(A,L):
    K=2*L-A-1; H=A-L-1
    if K<3:return 0
    total=0
    for a in range(1,K-1):
        bmax=H-1
        for b in range(1,bmax+1):
            lo=max(2,K+2-b); hi=K-a; cap=H-b
            total += sum_min_sminus1(lo,hi,cap)
    return total

def zpowers(z,D,n):
    pos=[1]*(n+1)
    for k in range(1,n+1):pos[k]=pos[k-1]*z%D
    zi=pow(z,-1,D); neg=[1]*(n+1)
    for k in range(1,n+1):neg[k]=neg[k-1]*zi%D
    return pos,neg

def anti_check(p):
    A,L,m,q=p; D=positive_D(A,L)
    z=pow(2,m,D)*pow(pow(3,q,D),-1,D)%D
    B=L-1; dmin=max(1,2*L-A+1); pos,neg=zpowers(z,D,B)
    right={}; rn=0
    for c in range(1,B+1):
        md=B-2-c
        if md<dmin:continue
        for d in range(dmin,md+1):
            rn+=1; res=(pos[c]+2*pos[c+d])%D; sd=c+d
            old=right.get(res)
            if old is None or sd<old[0]:right[res]=(sd,c,d)
    ln=0
    for a in range(1,B+1):
        for b in range(1,B-a+1):
            budget=B-a-b
            if budget<1+dmin:continue
            ln+=1; res=(1+neg[a+b]-neg[b])%D
            rr=right.get(res)
            if rr and rr[0]<=budget:
                sd,c,d=rr
                F=(2*pos[a+b+c+d]-1+pos[a]-pos[a+b]+pos[a+b+c])%D
                assert F==0
                return True,ln,rn
    return False,ln,rn

def long_check(p):
    A,L,m,q=p; K=2*L-A-1
    if K<3:return False,0,0
    D=positive_D(A,L); z=pow(2,m,D)*pow(pow(3,q,D),-1,D)%D
    pos,neg=zpowers(z,D,A)
    right={};rn=0
    cmax=min(K-2,A-L-2)
    for c in range(1,cmax+1):
        for d in range(1,K-c):
            rn+=1;res=(2*pos[c]+4*pos[c+d])%D
            right.setdefault(res,[]).append((c,d,c+d))
    ln=0
    for a in range(1,K-1):
        bmax=min(A-L+a-1,A-L-2)
        for b in range(1,bmax+1):
            lo=K+2-b; hi=K-a; cup=A-L-1-b
            if lo>hi or hi<2 or cup<1:continue
            ln+=1;res=(3*neg[a]-2*neg[b]+2)%D
            for c,d,s in right.get(res,[]):
                if lo<=s<=hi and c<=cup:
                    F=(4*pos[a+b+c+d]-3*pos[b]+2*pos[a]-2*pos[a+b]+2*pos[a+b+c])%D
                    assert F==0
                    return True,ln,rn
    return False,ln,rn

def short_check(p):
    A,L,m,q=p; K=A-2*L-1
    if K<3:return False,0,0
    D=positive_D(A,L); z=pow(2,m,D)*pow(pow(3,q,D),-1,D)%D
    pos,neg=zpowers(z,D,max(L,K)+2)
    right={};rn=0
    cmax=min(K-2,L-4)
    for c in range(1,cmax+1):
        md=L-3-c
        for d in range(1,md+1):
            rn+=1;res=(pos[c]+2*pos[c+d])%D
            right.setdefault(res,[]).append((c,d,c+d))
    ln=0;maxab=min(K-1,L-3)
    for a in range(1,maxab):
        for b in range(1,maxab-a+1):
            ab=a+b;cmax0=K-ab;smax=L-1-ab
            if cmax0<1 or smax<2:continue
            ln+=1;res=(1+2*neg[b]-2*neg[ab])%D
            for c,d,sd in right.get(res,[]):
                if c<=cmax0 and sd<=smax:
                    F=(2*pos[a+b+c+d]-pos[a+b]+pos[a+b+c]+2-2*pos[a])%D
                    assert F==0
                    return True,ln,rn
    return False,ln,rn

def inter_check(p):
    A,L,m,q=p
    amin=max(1,2*L-A+1);dmin=amin;cmin=max(1,A-2*L+1);B=L-1-cmin
    if amin+1+dmin>B:return False,0,0
    D=positive_D(A,L);z=pow(2,m,D)*pow(pow(3,q,D),-1,D)%D
    pos,neg=zpowers(z,D,B+2)
    right={};rn=0
    for b in range(1,B+1):
        md=B-amin-b
        if md<dmin:continue
        for d in range(dmin,md+1):
            rn+=1;res=pos[b]*(5+6*pos[d])%D;sd=b+d
            old=right.get(res)
            if old is None or sd<old[0]:right[res]=(sd,b,d)
    ln=0
    for a in range(amin,B+1):
        budget=B-a
        if budget<1+dmin:continue
        ln+=1;res=(3*neg[a]+2)%D
        rr=right.get(res)
        if rr and rr[0]<=budget:
            sd,b,d=rr;c=cmin
            F=(6*pos[a+b+d]-3-2*pos[a]+5*pos[a+b])%D
            assert F==0
            return True,ln,rn
    return False,ln,rn

def main():
    pairs=complete_survivors()
    assert len(pairs)==EXPECTED_PAIRS and max(p[0] for p in pairs)==EXPECTED_MAX_A
    raw=sum(2*comb(A-6,4) for A,_,_,_ in pairs if A>=10)
    assert raw==EXPECTED_RAW
    totals={
      'antipodal':sum(antipodal_count(A,L) for A,L,_,_ in pairs),
      'long':sum(long_count(A,L) for A,L,_,_ in pairs),
      'short':sum(short_count(A,L) for A,L,_,_ in pairs),
      'interlaced':sum(inter_count(A,L) for A,L,_,_ in pairs),
    }
    assert totals==EXPECTED_FAMILY and sum(totals.values())==EXPECTED_TOTAL
    funcs={'antipodal':anti_check,'long':long_check,'short':short_check,'interlaced':inter_check}
    ops={}
    for name,fn in funcs.items():
        ltot=rtot=0;hits=[]
        for p in pairs:
            hit,l,r=fn(p);ltot+=l;rtot+=r
            if hit:hits.append(p)
        assert not hits,(name,hits[:3])
        ops[name]=(ltot,rtot)
    assert ops==EXPECTED_OPS,(ops,EXPECTED_OPS)
    assert sum(a+b for a,b in ops.values())==EXPECTED_RESIDUES
    for A,L,m,q in pairs:
        D=positive_D(A,L)
        assert gcd(D,3**q-2**m)==1
    print('RL270 certificate: PASS')
    print('pairs =',len(pairs),'max_A =',max(p[0] for p in pairs))
    print('raw_gap_states =',raw)
    print('structural_states =',sum(totals.values()),totals)
    print('mitm_residues =',sum(a+b for a,b in ops.values()),ops)
    print('full_D_hits = 0')
    print('RL270_CERTIFICATE_PASS')

if __name__=='__main__':main()
