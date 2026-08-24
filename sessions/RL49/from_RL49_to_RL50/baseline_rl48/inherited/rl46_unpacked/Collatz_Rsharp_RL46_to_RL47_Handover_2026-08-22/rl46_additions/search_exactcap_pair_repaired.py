from collections import deque
import sys,time

def search(A,ELL,Emax):
 P=ELL-2;Q=A-ELL;X=1<<A;Y=3**ELL
 def cap_ok(n,pa):
  return (1<<(n+2))*Y*Y <= (3**(pa+2))*X*X
 def lmin_exact(n,pa):
  L=0;left=(1<<(n+2))*Y*Y;right=(3**(pa+2))*X*X
  while left>right:
   L+=1;left*=2;right*=3
  return L
 start=(1,0,-14,1,0,False,0)
 dq=deque([start]);seen={start};hits=set();pump_reject=0
 while dq:
  d,e,T,z,pa,pump,need=dq.popleft();n=z+pa
  # A virtual neutral 11 pump can only start if its FIRST actual 11 column
  # already obeys the prefix cap. Once legal, each further pump multiplies
  # the cap ratio by 2/3 and remains legal.
  if d==1 and T==-2 and not pump:
   if cap_ok(n,pa):
    st=(d,e,T,z,pa,True,0)
    if st not in seen:seen.add(st);dq.append(st)
   else:
    pump_reject += 1
  if d==1 and T&1:
   gout=(T+1)//2
   if gout>=4 and gout&(gout-1)==0:
    t=gout.bit_length()-3
    if z+t==Q:
     req=lmin_exact(n,pa)
     if pump:
      loops=P-(pa+1)
      if loops>=max(need,req):hits.add((e,z,t,pa+1,loops,max(need,req),gout))
     elif pa+1==P and req==0:
      hits.add((e,z,t,pa+1,0,0,gout))
  for x,y in ((0,0),(1,1),(0,1),(1,0)):
   nd=d+y-x
   if nd<=0:continue
   ne=e+d-x
   if ne>Emax:continue
   if d==1 and T==-2 and x==1 and y==1:continue
   num=3**y*T+x*3**(d+y-1)-y
   if num&1:continue
   need2=need
   if x:
    req=lmin_exact(n,pa)
    if pump:need2=max(need2,req)
    elif req:continue
   pa2=pa+x;z2=z+1-x
   if pa2>P or z2>Q:continue
   st=(nd,ne,num//2,z2,pa2,pump,need2)
   if st not in seen:seen.add(st);dq.append(st)
 return seen,sorted(hits),pump_reject

if __name__=='__main__':
 A=int(sys.argv[1]);L=int(sys.argv[2]);E=int(sys.argv[3]);t=time.time();seen,h,r=search(A,L,E)
 print((A,L,A-L),'E',E,'states',len(seen),'secs',time.time()-t,'pump_reject',r,'hits',len(h),'min',min((x[0] for x in h),default=None))
 print(h[:30])
