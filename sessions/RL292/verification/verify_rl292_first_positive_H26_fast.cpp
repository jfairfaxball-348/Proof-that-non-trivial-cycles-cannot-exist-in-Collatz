#include <bits/stdc++.h>
using namespace std;
struct Key{uint64_t J; uint8_t d; bool operator==(Key const&o)const{return J==o.J&&d==o.d;}};
struct Hsh{size_t operator()(Key const&k)const noexcept{return std::hash<uint64_t>{}(k.J ^ (uint64_t(k.d)*0x9e3779b97f4a7c15ULL));}};
static int v2u(uint64_t x){return __builtin_ctzll(x);} 
int main(){
 const int R=26; const uint64_t TARGET=1ULL<<27;
 unordered_map<Key,uint8_t,Hsh> dist; dist.reserve(30000000); dist.max_load_factor(0.72);
 vector<vector<Key>> buckets(R+1);
 auto add=[&](int d,uint64_t J,int H){Key k{J,(uint8_t)d};auto it=dist.find(k); if(it==dist.end()){dist.emplace(k,(uint8_t)H);buckets[H].push_back(k);} else if(H<it->second){it->second=H;buckets[H].push_back(k);} };
 size_t seedcount=0;
 for(int d=1;d<=8;d++){
   int eps=(d%2==0)?1:2; uint64_t p3=1,p2=1;for(int i=0;i<d;i++){p3*=3;p2*=2;} uint64_t maxJ=p3-p2+1;
   int area=(d-1)*(d-2)/2;
   for(uint64_t J=1;J<=maxJ;J++) if(J%3==0||J%3==(uint64_t)eps){
     uint64_t M=J+p2-2; int t=v2u(M); int Hmin=max(area,t-d+1);
     if(!(d==3&&J==2&&Hmin==1)) Hmin=max(Hmin,t-d+2); Hmin=max(Hmin,0);
     if(Hmin<=R){Key k{J,(uint8_t)d}; auto it=dist.find(k); if(it==dist.end()){dist.emplace(k,(uint8_t)Hmin);buckets[Hmin].push_back(k);seedcount++;} else if(Hmin<it->second){it->second=Hmin;buckets[Hmin].push_back(k);} }
   }
 }
 cerr<<"seeds="<<seedcount<<"\n";
 map<int,int> powers; size_t processed=0; uint64_t maxJseen=0; bool overflow=false;
 for(int H=0;H<=R;H++){
   auto &b=buckets[H];
   for(size_t idx=0; idx<b.size(); idx++){
     Key k=b[idx]; auto it=dist.find(k); if(it==dist.end()||it->second!=H) continue; processed++; maxJseen=max(maxJseen,k.J);
     int d=k.d; uint64_t J=k.J;
     if(d==1 && (J&(J-1))==0){int kk=63-__builtin_clzll(J); if(!powers.count(kk)||H<powers[kk]) powers[kk]=H;}
     __int128 p2=(__int128)1<<d, p3=1; for(int i=0;i<d;i++)p3*=3; __int128 K=(__int128)J+p2-1;
     for(int x=0;x<2;x++){
       int d2; __int128 K2;
       if((K&1)==0){d2=d; K2=x?3*K/2:(K+p3-1)/2;}
       else {if(x){if(d<=1)continue; d2=d-1; K2=(K-1)/2;} else {d2=d+1; K2=3*(K+p3)/2;}}
       int H2=H+d-1; if(H2>R) continue; __int128 p22=(__int128)1<<d2; __int128 J2=K2-p22+1;
       if(J2<=0){cerr<<"nonpos!\n";return 2;} if(J2>numeric_limits<uint64_t>::max()){overflow=true;continue;}
       add(d2,(uint64_t)J2,H2);
     }
   }
   cerr<<"H="<<H<<" bucket="<<b.size()<<" dist="<<dist.size()<<" processed="<<processed<<" maxJ="<<maxJseen<<"\n";
 }
 cout<<"states="<<dist.size()<<" processed="<<processed<<" seeds="<<seedcount<<" overflow="<<overflow<<" maxJ="<<maxJseen<<"\n";
 for(auto [k,h]:powers)cout<<"k"<<k<<":H"<<h<<" "; cout<<"\n";
 Key tar{TARGET,1}; cout<<"target="<<(dist.count(tar)?to_string((int)dist[tar]):string("ABSENT"))<<"\n";
}
