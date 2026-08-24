#!/usr/bin/env python3
import sys,time
N=26; KMIN=25
s=sys.argv[1] if len(sys.argv)>1 else '9'
if '/' in s: TA,TB=map(int,s.split('/'))
else:
 from fractions import Fraction
 f=Fraction(s);TA,TB=f.numerator,f.denominator
# A=27 zeta/2 < 13.5+1e-18
AA=27*10**18+2; AB=2*10**18
# W_end=A/3
# compare W <= AA/(3AB)
REQA,REQB=143,12
p2=[1];p3=[1]
def e2(n):
 while len(p2)<=n:p2.append(p2[-1]*2)
def e3(n):
 while len(p3)<=n:p3.append(p3[-1]*3)
def potnums(i,p,d,J):
 e2(max(i,d));e3(p+d+2);T=J-p3[d]+p2[d]
 Dxi=p3[p+d-1]*p2[d-1]; nxi=p2[i]*((T-1)*p2[d-1]+p3[d-1]); D=2*Dxi
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
# smallest odd K>=25 satisfying Xi < A(1-2^-K); return max compatible Psi cap=A/2(1+2^-K)
def kselect(nxi,Dxi,npsi,D):
 diff=AA*Dxi-nxi*AB
 if diff<=0:return None
 rhs=AA*Dxi
 # Need diff*2^K > rhs
 K=max(KMIN, rhs.bit_length()-diff.bit_length())
 if K%2==0:K+=1
 while (diff<<K)<=rhs:K+=2
 # exact xi check
 two=1<<K
 if not(nxi*AB*two < AA*(two-1)*Dxi):
  K+=2;two<<=2
 # current psi must fit same K; larger K only decreases cap
 pcn=AA*(two+1); pcd=2*AB*two
 if npsi*pcd >= pcn*D:return None
 return K,pcn,pcd
seen={};nodes=0;hitstate=None;pr=[0]*6;kmax=0
def rec(i,p,rem,Znum,d,J):
 global nodes,hitstate,kmax
 nodes+=1;e2(i+rem+2);e3(p+d+2)
 nxi,Dxi,npsi,D=potnums(i,p,d,J)
 ks=kselect(nxi,Dxi,npsi,D)
 if ks is None:pr[0]+=1;return False
 K,pcn,pcd=ks;kmax=max(kmax,K)
 # W bounds: W=2^i J/3^(p+d), end A/3
 if 3*AB*p2[i]*J >= AA*p3[p+d] or 3*p2[i]*J < -13*p3[p+d]:pr[1]+=1;return False
 den=p3[p]
 # full total viability using same-K maximal psi endpoint
 lhs=(Znum*D*pcd + pcn*den*D - npsi*den*pcd)*REQB
 rhs=REQA*den*D*pcd
 if lhs<=rhs:pr[2]+=1;return False
 # target first26 mass bounds
 if TB*(30*Znum+17*rem*den)<=TA*30*den:pr[3]+=1;return False
 if TB*(Znum+(p2[rem]-1)*p2[i])<=TA*den:pr[3]+=1;return False
 # same-K potential room bounds all remaining zeros
 lhs2=(Znum*D*pcd + pcn*den*D - npsi*den*pcd)*TB
 rhs2=TA*den*D*pcd
 if lhs2<=rhs2:pr[3]+=1;return False
 key=(i,p,rem,d,J);old=seen.get(key)
 if old is not None and Znum<=old:pr[4]+=1;return False
 seen[key]=Znum
 if rem==0:
  hitstate=(i,p,d,J,Znum,den,npsi,D,nxi,Dxi,K,pcn,pcd);return True
 if 30*p2[i]<=17*den:
  st=step(d,J,0)
  if st and rec(i+1,p,rem-1,Znum+p2[i],*st):return True
 st=step(d,J,1)
 if st and rec(i+1,p+1,rem,3*Znum,*st):return True
 return False
st=time.time();hit=rec(0,0,N,0,1,-13)
print('TARGET',TA,TB,TA/TB,'hit',hit,'nodes',nodes,'states',len(seen),'sec',time.time()-st,'pr',pr,'kmax',kmax)
if hitstate:
 i,p,d,J,zn,de,np,dd,nx,dx,K,pcn,pcd=hitstate
 print('hit',i,p,d,J,'Kmin',K,'Z',zn/de,'psi',np/dd,'xi',nx/dx,'totalUB',zn/de+pcn/pcd-np/dd)
