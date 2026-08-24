#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>
using boost::multiprecision::cpp_int; using u128=unsigned __int128;
static std::vector<u128>P3;
static u128 modcpp(cpp_int a,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;cpp_int r=a%mm;uint64_t lo=(r&((cpp_int(1)<<64)-1)).convert_to<uint64_t>(),hi=(r>>64).convert_to<uint64_t>();return (u128(hi)<<64)|lo;}
static u128 pow2(cpp_int e,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;return modcpp(boost::multiprecision::powm(cpp_int(2),e,mm),m);}
static inline int val3(u128 q,int p){if(!q)return -1;int v=0;while(v<p&&q%3==0){q/=3;++v;}return v==p?-1:v;}
struct Key{uint64_t lo,hi;uint16_t p;bool operator==(Key const&o)const{return lo==o.lo&&hi==o.hi&&p==o.p;}};
struct Hash{size_t operator()(Key const&k)const{uint64_t h=k.lo^(k.hi+0x9e3779b97f4a7c15ULL+(k.lo<<6)+(k.lo>>2));h^=(uint64_t)k.p*0xbf58476d1ce4e5b9ULL;h^=h>>30;h*=0xbf58476d1ce4e5b9ULL;h^=h>>27;h*=0x94d049bb133111ebULL;h^=h>>31;return (size_t)h;}};
static inline Key key(u128 q,int p){return {(uint64_t)q,(uint64_t)(q>>64),(uint16_t)p};}
static inline u128 qfrom(Key const&k){return (u128(k.hi)<<64)|k.lo;}
static inline void put(std::unordered_map<Key,int,Hash>&m,u128 q,int p,int pref){Key k=key(q,p);auto it=m.find(k);if(it==m.end())m.emplace(k,pref);else if(pref>it->second)it->second=pref;}
int main(int ac,char**av){if(ac<4)return 2;int Z=atoi(av[1]),X=atoi(av[2]),Y=atoi(av[3]),P=ac>4?atoi(av[4]):80;P3.resize(std::max(P+1,Y+3));P3[0]=1;for(size_t i=1;i<P3.size();i++)P3[i]=P3[i-1]*3;cpp_int A("123139092617126647266"),E("77692117359936589403"),K=A-E-Z+3;u128 q0=pow2(K,P3[P])+1;if(q0>=P3[P])q0-=P3[P];using Map=std::unordered_map<Key,int,Hash>;std::vector<std::vector<Map>> dp(X+1);for(auto &r:dp)r.resize(Y+1);dp[0][0].reserve(1024);put(dp[0][0],q0,P,0);int best=0;size_t total=0,peak=1;auto t0=std::chrono::steady_clock::now();for(int s=0;s<=X+Y;s++){for(int x=0;x<=X;x++){int y=s-x;if(y<0||y>Y)continue;auto &cur=dp[x][y];if(cur.empty())continue;peak=std::max(peak,cur.size());total+=cur.size();int d=1+y-x;if(d<1){std::cerr<<"bad height\n";return 3;}for(auto const&kv:cur){u128 q=qfrom(kv.first);int p=kv.first.p,pref=kv.second;int v=val3(q,p);if(v<0){std::cerr<<"AMBIG x="<<x<<" y="<<y<<" p="<<p<<" pref="<<pref<<"\n";return 1;}best=std::max(best,pref+v);u128 qr=q;int pr=p;for(int r=0;r<=v;r++){int npref=pref+r+1;if(y<Y){u128 nq=2*qr+1;if(nq>=P3[pr])nq-=P3[pr];put(dp[x][y+1],nq,pr,npref);}if(x<X&&y<Y){u128 c=P3[d]-1,a=2*qr;if(a>=P3[pr])a-=P3[pr];u128 nq=a>=c?a-c:a+P3[pr]-c;put(dp[x+1][y+1],nq,pr,npref);}if(x<X&&d>1&&r<v){int np=pr-1;u128 a=2*(qr/3);if(a>=P3[np])a-=P3[np];u128 c=P3[d-1],nq=a>=c?a-c:a+P3[np]-c;put(dp[x+1][y],nq,np,npref);}if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}}
} Map().swap(cur);}std::cerr<<"s="<<s<<" total_processed="<<total<<" peak_cell="<<peak<<" best="<<best<<"\n";}
double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count();std::cout<<"EVENT_DP_CERT Z="<<Z<<" Xcap="<<X<<" Ycap="<<Y<<" max="<<best<<" P="<<P<<" states_processed="<<total<<" peak_cell="<<peak<<" sec="<<sec<<"\n";return 0;}
