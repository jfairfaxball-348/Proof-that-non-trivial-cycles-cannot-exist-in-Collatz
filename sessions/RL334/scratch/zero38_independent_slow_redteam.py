from fractions import Fraction
from functools import lru_cache
A=217_976_794_617;E=137_528_045_312;D=A-E
LOW=1<<71;UP=(1<<76)+(1<<36);HC=20_390_252_058
def li(x,n=280):
 x2=x*x;t=x;s=Fraction(0)
 for i in range(n):s+=t/(2*i+1);t*=x2
 lo=2*s;return lo,lo+2*t/(2*n+1)/(1-x2)
_,u2=li(Fraction(1,3));l3,_=li(Fraction(1,2));DU=A*u2-E*l3
@lru_cache(None)
def fac(n):
 cuts=sorted({0,E,*(((-D*j)%E) for j in range(n+1))});o=set()
 for a,b in zip(cuts,cuts[1:]):
  for r in {a,min(a+1,b-1)}:
   p=(r+E-1)//E;g=[]
   for j in range(1,n+1):
    q=(r+D*j+E-1)//E;g.append(1+q-p);p=q
   o.add(tuple(g))
 assert len(o)==n+1
 return tuple(o)
def res(g):
 c=0
 for j,x in enumerate(g):c=(1<<x)*c+3**j
 m=3**len(g);return c*pow(1<<sum(g),-1,m)%m,m
def rec(x,g):
 ss=[x]
 for a in g:
  y=(1<<a)*x-1;assert y%3==0;x=y//3;assert x&1;ss.append(x)
 return ss
def nxt(n):
 x=3*n+1;return x>>((x&-x).bit_length()-1)
def escape(x,lim=1000):
 for s in range(lim+1):
  if x<LOW:return s
  x=nxt(x)
 raise AssertionError((x,lim))
count=0;maxesc=0;per=[]
for g in fac(37):
 r,m=res(g);x=r+max(0,(LOW-r+m-1)//m)*m;c=0
 while x<UP:
  if x&1:
   ss=rec(x,g)
   if DU*min(ss)>=HC:c+=1;count+=1;maxesc=max(maxesc,escape(ss[0]))
  x+=m
 per.append(c)
print('factors',len(fac(37)),'count',count,'maxescape',maxesc,'per_minmax',min(per),max(per))
assert len(fac(37))==38 and count==1825797 and maxesc==213
