#include <bits/stdc++.h>
using namespace std; using u64=uint64_t; using u128=__uint128_t;
string s128(u128 x){if(!x)return"0";string s;while(x){s.push_back('0'+x%10);x/=10;}reverse(s.begin(),s.end());return s;}
struct Target{u128 t; int K;};
struct Node{int j;u64 r,A,C;};
struct Stats{u64 nodes=0,drop=0,leaf=0,exacts=0;int maxj=0,maxsteps=0;u128 peak=0;u64 hs=0;u128 hn=0;int hk=0;};
vector<Target> targets;
void init_targets(int KMIN){
  for(int K=(KMIN|1);K<127;K+=2){u128 P=(u128)1<<K; targets.push_back({(P-2)/3,K}); targets.push_back({P-1,K});}
  sort(targets.begin(),targets.end(),[](auto&a,auto&b){return a.t<b.t;});
}
bool is_target(u128 n,int &K){
  auto it=lower_bound(targets.begin(),targets.end(),n,[](const Target&a,u128 x){return a.t<x;});
  if(it!=targets.end()&&it->t==n){K=it->K; return true;} return false;
}
bool range_class(u64 L,u64 U,int j,u64 r,u64&mn,u64&mx){
  u64 M=1ULL<<j, rem=L&(M-1), add=(r>=rem?r-rem:M-(rem-r));
  if(add>U-L)return false; mn=L+add;
  u64 remU=U&(M-1), sub=(remU>=r?remU-r:M-(r-remU)); mx=U-sub; return mn<=mx;
}
bool exact_from(u64 s,u128 n,int steps0,Stats&st){
  int steps=steps0; const u128 MAX=~(u128)0;
  while(n>=s){ st.peak=max(st.peak,n); int K; if(is_target(n,K)){st.hs=s;st.hn=n;st.hk=K;return false;}
    if(n&1){if(n>(MAX-1)/3){cerr<<"overflow\n";exit(4);} n=(3*n+1)/2;} else n/=2;
    if(++steps>10000){cerr<<"pathlong\n";exit(5);} }
  st.maxsteps=max(st.maxsteps,steps); return true;
}
bool cert(u64 L,u64 U,Stats&st){
  vector<Node> S{{0,0,1,0}};
  while(!S.empty()){
    Node d=S.back();S.pop_back(); st.nodes++; st.maxj=max(st.maxj,d.j);
    u64 mn,mx; if(!range_class(L,U,d.j,d.r,mn,mx)) continue;
    u128 den=(u128)1<<d.j;
    u128 y0=((u128)d.A*mn+d.C)/den, y1=((u128)d.A*mx+d.C)/den;
    auto lo=lower_bound(targets.begin(),targets.end(),y0,[](const Target&a,u128 x){return a.t<x;});
    for(auto it=lo; it!=targets.end() && it->t<=y1; ++it){
      u128 rhs=den*it->t; if(rhs<d.C)continue; rhs-=d.C; if(rhs%d.A)continue;
      u128 nn=rhs/d.A; if(nn<mn||nn>mx||nn>numeric_limits<u64>::max())continue;
      u64 s=(u64)nn, M=1ULL<<d.j; if((s&(M-1))!=d.r)continue;
      st.hs=s;st.hn=it->t;st.hk=it->K;return false;
    }
    if(den>d.A && (den-d.A)*(u128)mn>d.C){st.drop++;continue;}
    if(mn==mx || d.j>=36){
      st.leaf++; u64 M=1ULL<<d.j;
      for(u64 s=mn;;){ st.exacts++; u128 y=((u128)d.A*s+d.C)/den; if(!exact_from(s,y,d.j,st))return false; if(mx-s<M)break; s+=M; }
      continue;
    }
    u64 M=1ULL<<d.j;
    for(int b=0;b<2;b++){
      u64 rr=d.r+(b?M:0); u128 num=(u128)d.A*rr+d.C; bool odd=(num>>d.j)&1;
      u64 A=d.A,C=d.C; if(odd){A*=3;C=3*C+M;} S.push_back({d.j+1,rr,A,C});
    }
  }
  return true;
}
int main(int ac,char**av){if(ac!=4){cerr<<"usage L U KMIN\n";return 2;}u64 L=stoull(av[1]),U=stoull(av[2]);int KMIN=stoi(av[3]);init_targets(KMIN);Stats st;bool ok=cert(L,U,st);cout<<"ok="<<ok<<" interval=["<<L<<","<<U<<"] KMIN="<<KMIN<<" nodes="<<st.nodes<<" drop="<<st.drop<<" leaf="<<st.leaf<<" exacts="<<st.exacts<<" maxj="<<st.maxj<<" maxsteps="<<st.maxsteps<<" peak="<<s128(st.peak);if(!ok)cout<<" hit_start="<<st.hs<<" hit_state="<<s128(st.hn)<<" K="<<st.hk;cout<<"\n";return ok?0:1;}
