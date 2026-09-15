from fractions import Fraction
from functools import lru_cache
from collections import Counter
A=217_976_794_617;E=137_528_045_312;D=A-E
LOW=1<<71;UP=(1<<76)+(1<<36);HC=20_390_252_058
SHAPES=((1,1,1),(1,2,1),(2,1,1),(2,2,1),(3,2,1))
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
 return tuple(o)
def res(g):
 c=0
 for j,x in enumerate(g):c=(1<<x)*c+3**j
 m=3**len(g);return c*pow(1<<sum(g),-1,m)%m,m
def rec(x,g):
 ss=[x]
 for a in g:
  y=(1<<a)*x-1
  if y%3:return None
  x=y//3
  if not x&1:return None
  ss.append(x)
 return ss
def real(g):
 r,m=res(g);x=r+max(0,(LOW-r+m-1)//m)*m
 while x<UP:
  if x&1:
   ss=rec(x,g)
   if ss and DU*min(ss)>=HC:yield x,ss
  x+=m
def nxt(n):
 x=3*n+1;return x>>((x&-x).bit_length()-1)
memo={};maxstep=0;no=[];hitcounts=Counter();rowcounts=Counter()
def hb(start,limit=20000):
 path=[];x=start
 for _ in range(limit):
  if x<LOW:
   d=0
   for s in reversed(path):d+=1;memo[s]=d
   return len(path)
  if x in memo:
   b=memo[x];d=b
   for s in reversed(path):d+=1;memo[s]=d
   return len(path)+b
  path.append(x);x=nxt(x)
 return None
def consume(kind,total,pair,x):
 global maxstep
 rowcounts[(kind,total)]+=1
 h=hb(x)
 if h is None:
  if len(no)<20:no.append((kind,total,pair,x))
 else:
  hitcounts[(kind,total)]+=1;maxstep=max(maxstep,h)
for total in range(44,99):
 for left in range(max(1,total-49),min(49,total-1)+1):
  right=total-left
  for base in fac(total):
   if base[left]!=2:continue
   g=list(base);g[left-1]+=1;g[left]-=1;g=tuple(g)
   for x,ss in real(g):consume('p1',total,(left,right),ss[0])
print('p1 done',sum(v for (k,t),v in rowcounts.items() if k=='p1'),{t:v for (k,t),v in rowcounts.items() if k=='p1'},flush=True)
for total in range(44,99):
 for left in range(max(1,total-49),min(49,total-1)+1):
  right=total-left
  for base in fac(total+1):
   for h in (1,2):
    g=list(base)
    for off,ch in enumerate((h,1-h,-1)):g[left-1+off]+=ch
    if min(g[left-1:left+2])<1:continue
    for x,ss in real(tuple(g)):consume('p2',total,(left,right),ss[0])
print('p2 done',sum(v for (k,t),v in rowcounts.items() if k=='p2'),{t:v for (k,t),v in rowcounts.items() if k=='p2'},flush=True)
for total in range(44,99):
 for left in range(max(1,total-49),min(49,total-1)+1):
  right=total-left
  for base in fac(total+2):
   for shape in SHAPES:
    q=(0,)+shape+(0,);g=list(base);ok=True
    for off in range(4):
     pos=left-1+off;g[pos]+=q[off+1]-q[off]
     if g[pos]<1:ok=False;break
    if not ok:continue
    for x,ss in real(tuple(g)):consume('p3',total,(left,right),ss[0])
print('p3 done',sum(v for (k,t),v in rowcounts.items() if k=='p3'),{t:v for (k,t),v in rowcounts.items() if k=='p3'},flush=True)
print('TOTAL',sum(rowcounts.values()),'HIT',sum(hitcounts.values()),'NO',len(no),'maxstep',maxstep,'examples',no)
assert sum(rowcounts.values())==sum(hitcounts.values()) and not no
