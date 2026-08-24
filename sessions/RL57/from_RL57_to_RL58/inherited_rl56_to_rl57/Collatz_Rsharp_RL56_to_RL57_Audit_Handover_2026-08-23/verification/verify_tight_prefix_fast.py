#!/usr/bin/env python3
import sys,time
# Exact conservative caps using inherited zeta-1 < 398/(45*2^71).
# Since 398/(45*2^71) < 1/10^20, use clean rational overcaps:
# Xi_end < 27/2 + 1/10^18; Psi_end(K>=3) < 243/32 +1/10^18.
N=26
KMIN=int(sys.argv[1]) if len(sys.argv)>1 else 3
# target a/b
s=sys.argv[2] if len(sys.argv)>2 else '107/10'
if '/' in s: TA,TB=map(int,s.split('/'))
else:
 from fractions import Fraction
 f=Fraction(s);TA,TB=f.numerator,f.denominator
CAPA,CAPB=17,30
# Xi cap fixed: 27/2 + 1e-18
XIA=27*10**18+2; XIB=2*10**18
# Psi cap depending Kmin, overcap exact factor plus 1e-18
# 27/4*(1+2^-K) = 27*(2^K+1)/(4*2^K)
base_num=27*((1<<KMIN)+1); base_den=4*(1<<KMIN)
PSIA=base_num*10**18+base_den; PSIB=base_den*10**18
p2=[1];p3=[1]
def e2(n):
 while len(p2)<=n:p2.append(p2[-1]*2)
def e3(n):
 while len(p3)<=n:p3.append(p3[-1]*3)
def potnums(i,p,d,J):
 e2(max(i,d));e3(p+d+2)
 T=J-p3[d]+p2[d]
 Dxi=p3[p+d-1]*p2[d-1]
 nxi=p2[i]*((T-1)*p2[d-1]+p3[d-1])
 D=2*Dxi
 npsi=p2[i]*(p3[d-1]*p2[d]+(T-1)*p2[d-1]+p3[d-1])
 return nxi,Dxi,npsi,D
def step(d,J,x):
 e2(d+1);e3(d+1)
 if x==0:y=0 if J&1 else 1
 else:
  if J&1:y=1
  elif d>1:y=0
  else:return None
 if x==0 and y==0:return d,(J+p3[d]-p2[d])//2
 if x==1 and y==1:return d,(3*J+p2[d]-1)//2
 if x==0 and y==1:return d+1,(3*J+p3[d+1]-p2[d]-1)//2
 return d-1,J//2
seen={};nodes=0;pr=[0,0,0,0];hitstate=None
def rec(i,p,rem,Znum,d,J):
 global nodes,hitstate
 nodes+=1;e2(i+rem+2);e3(p+d+2)
 nxi,Dxi,npsi,D=potnums(i,p,d,J)
 if nxi*XIB>=XIA*Dxi:pr[0]+=1;return False
 if npsi*PSIB>=PSIA*D:pr[1]+=1;return False
 den=p3[p]
 # UB cap: Z + rem*17/30 <= target
 if TB*(30*Znum+17*rem*den)<=TA*30*den:pr[2]+=1;return False
 # UB geom
 if TB*(Znum+(p2[rem]-1)*p2[i])<=TA*den:pr[2]+=1;return False
 # UB potential: Z + PsiCap - psi <= target
 # (Znum/den - npsi/D) <= target-PsiCap
 # directly compare Z* + cap <= target
 # (Znum*D + PSIA/PSIB*den*D - npsi*den)/(den*D) <= TA/TB
 lhs=(Znum*D*PSIB + PSIA*den*D - npsi*den*PSIB)*TB
 rhs=TA*den*D*PSIB
 if lhs<=rhs:pr[3]+=1;return False
 key=(i,p,rem,d,J);old=seen.get(key)
 if old is not None and Znum<=old:return False
 seen[key]=Znum
 if rem==0:
  hitstate=(i,p,d,J,Znum,den,npsi,D,nxi,Dxi);return True
 if 30*p2[i]<=17*den:
  st=step(d,J,0)
  if st and rec(i+1,p,rem-1,Znum+p2[i],*st):return True
 st=step(d,J,1)
 if st and rec(i+1,p+1,rem,3*Znum,*st):return True
 return False
st=time.time();hit=rec(0,0,N,0,1,-13)
print('KMIN',KMIN,'TARGET',TA,TB,TA/TB,'hit',hit,'nodes',nodes,'states',len(seen),'sec',time.time()-st)
print('caps xi',XIA/XIB,'psi',PSIA/PSIB,'pr',pr)
if hitstate:
 i,p,d,J,zn,de,np,dd,nx,dx=hitstate
 print('hitstate i p d J',i,p,d,J,'Z',zn/de,'psi',np/dd,'xi',nx/dx)
