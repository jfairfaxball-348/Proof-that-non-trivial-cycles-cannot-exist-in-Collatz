from functools import lru_cache
A=217_976_794_617;E=137_528_045_312;D=A-E
LOW=1<<71;UP=(1<<76)+(1<<36); MIN_OWNED=22689747442693040208618
@lru_cache(None)
def fac(n):
 cuts=sorted({0,E,*(((-D*j)%E) for j in range(n+1))});o=set()
 for a,b in zip(cuts,cuts[1:]):
  for r in (a,min(a+1,b-1)):
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
def reconstruct_min(x,g):
 mn=x
 for a in g:
  x=((1<<a)*x-1)//3
  if x<mn:mn=x
 return mn
def nxt(n):
 x=3*n+1;return x>>((x&-x).bit_length()-1)
memo={}
def escape(x):
 path=[]
 while x>=LOW and x not in memo:
  path.append(x);x=nxt(x)
 b=0 if x<LOW else memo[x]
 for y in reversed(path):
  b+=1;memo[y]=b
 return memo[path[0]] if path else b
count=0;maxesc=0;per=[]
for g in fac(37):
 r,m=res(g);x=r+max(0,(LOW-r+m-1)//m)*m;c=0
 while x<UP:
  if x&1 and reconstruct_min(x,g)>=MIN_OWNED:
   c+=1;count+=1;e=escape(x)
   if e>maxesc:maxesc=e
  x+=m
 per.append(c)
print('RL334_ZERO38_GREEN')
print('factors',len(fac(37)))
print('candidates',count)
print('max_escape_odd_steps',maxesc)
print('per_factor_minmax',min(per),max(per))
assert len(fac(37))==38
assert count==1_825_797
assert maxesc==213
