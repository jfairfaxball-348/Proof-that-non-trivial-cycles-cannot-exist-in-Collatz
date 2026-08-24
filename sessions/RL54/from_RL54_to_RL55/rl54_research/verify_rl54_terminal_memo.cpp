#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>
using boost::multiprecision::cpp_int; using u128=unsigned __int128;
static std::vector<u128>P3; static int XMAX,YMAX;
static u128 modcpp(cpp_int a,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;cpp_int r=a%mm;uint64_t lo=(r&((cpp_int(1)<<64)-1)).convert_to<uint64_t>(),hi=(r>>64).convert_to<uint64_t>();return (u128(hi)<<64)|lo;}
static u128 pow2(cpp_int e,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;return modcpp(boost::multiprecision::powm(cpp_int(2),e,mm),m);}
static inline int val3(u128 q,int p){if(!q)return -1;int v=0;while(v<p&&q%3==0){q/=3;++v;}return v==p?-1:v;}
struct Key{uint64_t lo,hi;uint16_t p;uint8_t x,y; bool operator==(Key const&o)const{return lo==o.lo&&hi==o.hi&&p==o.p&&x==o.x&&y==o.y;}};
struct Hash{size_t operator()(Key const&k)const{uint64_t h=k.lo^(k.hi+0x9e3779b97f4a7c15ULL+(k.lo<<6)+(k.lo>>2)); h^=((uint64_t)k.p<<32)|((uint64_t)k.x<<16)|k.y; h^=h>>30;h*=0xbf58476d1ce4e5b9ULL;h^=h>>27;h*=0x94d049bb133111ebULL;h^=h>>31;return (size_t)h;}};
static inline Key key(u128 q,int p,int x,int y){return {(uint64_t)q,(uint64_t)(q>>64),(uint16_t)p,(uint8_t)x,(uint8_t)y};}
static std::unordered_map<Key,int,Hash> memo, memox;
static int xfree(u128 q,int p,int yr){Key k=key(q,p,0,yr); auto it=memox.find(k); if(it!=memox.end())return it->second; int v=val3(q,p);if(v<0)return 1000000;int best=v;u128 qr=q;int pr=p;for(int r=0;r<=v;r++){if(yr){u128 nq=2*qr+1;if(nq>=P3[pr])nq-=P3[pr];if(r==v)best=std::max(best,r+1+xfree(nq,pr,yr-1));else{best=std::max(best,r+1);if(yr>=2){u128 nq2=2*nq+1;if(nq2>=P3[pr])nq2-=P3[pr];best=std::max(best,r+2+xfree(nq2,pr,yr-2));}}}if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}} memox.emplace(k,best); return best;}
static int dfs(u128 q,int p,int x,int y){Key k=key(q,p,x,y);auto it=memo.find(k);if(it!=memo.end())return it->second;int v=val3(q,p);if(v<0)return 1000000;int ans;if(x==XMAX)ans=xfree(q,p,YMAX-y);else if(q%3==2){int xr=XMAX-x,yr=YMAX-y;ans=xr<=yr?yr:-1000000;}else{int best=-1000000;u128 qr=q;int pr=p;int d=1+y-x;for(int r=0;r<=v;r++){if(y<YMAX){u128 nq=2*qr+1;if(nq>=P3[pr])nq-=P3[pr];int t=dfs(nq,pr,x,y+1);if(t<900000)best=std::max(best,r+1+t);u128 c=P3[d]-1,a=2*qr;if(a>=P3[pr])a-=P3[pr];u128 n2=(a>=c)?a-c:a+P3[pr]-c;t=dfs(n2,pr,x+1,y+1);if(t<900000)best=std::max(best,r+1+t);}if(d>1&&r<v){int np=pr-1;u128 a=2*(qr/3);if(a>=P3[np])a-=P3[np];u128 c=P3[d-1],n=(a>=c)?a-c:a+P3[np]-c;int t=dfs(n,np,x+1,y);if(t<900000)best=std::max(best,r+1+t);}if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}}ans=best;} memo.emplace(k,ans);return ans;}
int main(int ac,char**av){if(ac<4)return 2;int Z=atoi(av[1]);XMAX=atoi(av[2]);YMAX=atoi(av[3]);int P=ac>4?atoi(av[4]):80;P3.resize(std::max(P+1,YMAX+3));P3[0]=1;for(size_t i=1;i<P3.size();i++)P3[i]=P3[i-1]*3; memo.reserve(1<<22);memox.reserve(1<<20);cpp_int A("123139092617126647266"),E("77692117359936589403"),K=A-E-Z+3;u128 q=pow2(K,P3[P])+1;if(q>=P3[P])q-=P3[P];auto t0=std::chrono::steady_clock::now();int best=dfs(q,P,0,0);double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count();std::cout<<"memo_exact Z="<<Z<<" X="<<XMAX<<" Y="<<YMAX<<" max="<<best<<" states="<<memo.size()<<" xfree_states="<<memox.size()<<" sec="<<sec<<"\n";return best>=900000?1:0;}
