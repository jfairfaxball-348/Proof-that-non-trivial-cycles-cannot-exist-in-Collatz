from collections import deque
import sys,time

def search(A,ELL):
    P=ELL-2; Q=A-ELL; X=1<<A; Y=3**ELL
    def cap_ok(n,pa):
        return (1<<(n+2))*Y*Y <= (3**(pa+2))*X*X
    def lmin(n,pa):
        L=0; left=(1<<(n+2))*Y*Y; right=(3**(pa+2))*X*X
        while left>right:
            L+=1;left*=2;right*=3
        return L
    # state d,T,z,pa,pump,need. pa,z omit virtual neutral 11 loops.
    start=(1,-14,1,0,False,0)
    dq=deque([start]); seen={start}; hits=[]; legal_pump=0; rejected_pump=0
    while dq:
        d,T,z,pa,pump,need=dq.popleft(); n=z+pa
        # beta prefix weight is pa+d (virtual loops would add equally).
        if pa+d>P: continue
        if d==1 and T==-2 and not pump:
            if cap_ok(n,pa):
                legal_pump += 1
                st=(d,T,z,pa,True,0)
                if st not in seen: seen.add(st);dq.append(st)
            else:
                rejected_pump += 1
        # terminal 10 is not inserted into the state graph.
        if d==1 and (T&1):
            gout=(T+1)//2
            if gout>=4 and gout&(gout-1)==0:
                t=gout.bit_length()-3
                if z+t==Q:
                    req=lmin(n,pa)
                    needT=max(need,req) if pump else req
                    p0=pa+1
                    loops=P-p0
                    if loops>=0 and loops>=needT:
                        hits.append((z,t,gout,pa,p0,loops,needT,pump,n,T))
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd<=0: continue
            # omit the only true structural self-loop; virtual flag handles it.
            if d==1 and T==-2 and x==1 and y==1: continue
            num=(3**y)*T+x*3**(d+y-1)-y
            if num&1: continue
            z2=z+1-x; pa2=pa+x
            if z2>Q or pa2>P: continue
            # beta prefix weight monotone; it can never exceed target P.
            if pa2+nd>P: continue
            need2=need
            if x:
                req=lmin(n,pa)
                if pump: need2=max(need2,req)
                elif req: continue
            st=(nd,num//2,z2,pa2,pump,need2)
            if st not in seen:
                seen.add(st);dq.append(st)
    return seen,sorted(set(hits)),legal_pump,rejected_pump

if __name__=='__main__':
    A=int(sys.argv[1]); L=int(sys.argv[2]); t=time.time();seen,h,lp,rp=search(A,L)
    print((A,L,A-L),'states',len(seen),'secs',time.time()-t,'legal_pump_states',lp,'rejected_pump_states',rp)
    print('hits',len(h));print(h[:50])
