#include <bits/stdc++.h>
using namespace std;
struct S{int d; long long J; bool operator==(S const&o)const{return d==o.d&&J==o.J;}};
struct Hsh{size_t operator()(S const&s)const noexcept{uint64_t x=(uint64_t)s.J; x^=x>>33; x*=0xff51afd7ed558ccdULL; x^=x>>33; x*=0xc4ceb9fe1a85ec53ULL; x^=x>>33; return x ^ (uint64_t)s.d*0x9e3779b97f4a7c15ULL;}};
int v2ll(long long x){return __builtin_ctzll((unsigned long long)x);} 
int main(){int HMAX=24; vector<unordered_set<S,Hsh>> seen(HMAX+1); vector<vector<S>> q(HMAX+1); seen[0].reserve(100); seen[0].insert({1,-13}); q[0].push_back({1,-13});
 for(int H=0;H<=HMAX;H++){
   if(H>=18) seen[H].reserve((size_t)(1ull<<min(25,H-1)));
   size_t idx=0; long long maxabs=0; int maxd=0, maxmargin=-999; vector<array<long long,5>> viol;
   while(idx<q[H].size()){
     S s=q[H][idx++]; int d=s.d; long long J=s.J; maxabs=max(maxabs,llabs(J)); maxd=max(maxd,d);
     int K=H+d*(d+1)/2-1;
     if(J>0){int vv=v2ll(J); maxmargin=max(maxmargin,vv-K); if(vv>K){viol.push_back({H,d,J,vv,K}); if(viol.size()>=10) break;}}
     __int128 p3=1,p2=1; for(int i=0;i<d;i++){p3*=3;p2*=2;}
     __int128 A=p3-p2, B=p2-1, C=3*p3-p2-1;
     vector<S> nxt;
     if(J&1){
       __int128 j0=((__int128)J+A)/2; __int128 j1=(3*(__int128)J+B)/2;
       if(j0<LLONG_MIN||j0>LLONG_MAX||j1<LLONG_MIN||j1>LLONG_MAX){cerr<<"overflow\n";return 2;}
       nxt.push_back({d,(long long)j0}); nxt.push_back({d,(long long)j1});
     } else {
       __int128 ju=(3*(__int128)J+C)/2; if(ju<LLONG_MIN||ju>LLONG_MAX){cerr<<"overflow\n";return 2;}
       nxt.push_back({d+1,(long long)ju}); if(d>1)nxt.push_back({d-1,J/2});
     }
     int Hn=H+d-1; if(Hn<=HMAX){
       for(auto st:nxt){auto [it,ins]=seen[Hn].insert(st); if(ins)q[Hn].push_back(st);} }
   }
   cout<<"H "<<H<<" count "<<seen[H].size()<<" processed "<<idx<<" maxd "<<maxd<<" maxabs "<<maxabs<<" margin "<<maxmargin;
   if(!viol.empty()){cout<<" VIOL"; for(auto a:viol)cout<<" (d="<<a[1]<<",J="<<a[2]<<",v="<<a[3]<<",K="<<a[4]<<")"; cout<<"\n"; break;} cout<<"\n";
 }
}
