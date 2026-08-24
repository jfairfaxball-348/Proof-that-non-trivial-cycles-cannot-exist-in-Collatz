#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <omp.h>
using boost::multiprecision::cpp_int; using u128=unsigned __int128;
static std::vector<u128>P3; static int XMAX,YMAX; static bool collect_amb=false; static int collected_done=-1000000;
static u128 modcpp(cpp_int a,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;cpp_int r=a%mm;uint64_t lo=(r&((cpp_int(1)<<64)-1)).convert_to<uint64_t>(),hi=(r>>64).convert_to<uint64_t>();return (u128(hi)<<64)|lo;}
static u128 pow2(cpp_int e,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;return modcpp(boost::multiprecision::powm(cpp_int(2),e,mm),m);}
static inline int val3(u128 q,int p){if(!q)return -1;int v=0;while(v<p&&q%3==0){q/=3;++v;}return v==p?-1:v;}
static int xfree(u128 q,int p,int yr){int v=val3(q,p);if(v<0)return 1000000;int best=v;u128 qr=q;int pr=p;for(int r=0;r<=v;r++){if(yr){u128 nq=2*qr+1;if(nq>=P3[pr])nq-=P3[pr];if(r==v)best=std::max(best,r+1+xfree(nq,pr,yr-1));else{best=std::max(best,r+1);if(yr>=2){u128 nq2=2*nq+1;if(nq2>=P3[pr])nq2-=P3[pr];best=std::max(best,r+2+xfree(nq2,pr,yr-2));}}}if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}}return best;}
static int dfs(u128 q,int p,int x,int y){int v=val3(q,p);if(v<0)return 1000000;if(x==XMAX)return xfree(q,p,YMAX-y);if(q%3==2){int xr=XMAX-x,yr=YMAX-y;return xr<=yr?yr:-1000000;}int best=-1000000;u128 qr=q;int pr=p;int d=1+y-x;for(int r=0;r<=v;r++){if(y<YMAX){u128 nq=2*qr+1;if(nq>=P3[pr])nq-=P3[pr];int t=dfs(nq,pr,x,y+1);if(t<900000)best=std::max(best,r+1+t);u128 c=P3[d]-1,a=2*qr;if(a>=P3[pr])a-=P3[pr];u128 n2=(a>=c)?a-c:a+P3[pr]-c;t=dfs(n2,pr,x+1,y+1);if(t<900000)best=std::max(best,r+1+t);}if(d>1&&r<v){int np=pr-1;u128 a=2*(qr/3);if(a>=P3[np])a-=P3[np];u128 c=P3[d-1],n=(a>=c)?a-c:a+P3[np]-c;int t=dfs(n,np,x+1,y);if(t<900000)best=std::max(best,r+1+t);}if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}}return best;}
struct Task{u128 q;int p,x,y,prefix;};
static void collect(u128 q,int p,int x,int y,int prefix,int levels,std::vector<Task>&out){int v=val3(q,p);if(v<0){collect_amb=true;return;}if(x==XMAX){int t=xfree(q,p,YMAX-y);if(t>=900000)collect_amb=true;else collected_done=std::max(collected_done,prefix+t);return;}if(q%3==2){int xr=XMAX-x,yr=YMAX-y;if(xr<=yr)collected_done=std::max(collected_done,prefix+yr);return;}if(levels==0){out.push_back({q,p,x,y,prefix});return;}int d=1+y-x;u128 qr=q;int pr=p;for(int r=0;r<=v;r++){if(y<YMAX){u128 nq=2*qr+1;if(nq>=P3[pr])nq-=P3[pr];collect(nq,pr,x,y+1,prefix+r+1,levels-1,out);u128 c=P3[d]-1,a=2*qr;if(a>=P3[pr])a-=P3[pr];u128 n2=(a>=c)?a-c:a+P3[pr]-c;collect(n2,pr,x+1,y+1,prefix+r+1,levels-1,out);}if(d>1&&r<v){int np=pr-1;u128 a=2*(qr/3);if(a>=P3[np])a-=P3[np];u128 c=P3[d-1],n=(a>=c)?a-c:a+P3[np]-c;collect(n,np,x+1,y,prefix+r+1,levels-1,out);}if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}}
}
int main(int ac,char**av){if(ac<4)return 2;int Z=atoi(av[1]);XMAX=atoi(av[2]);YMAX=atoi(av[3]);int P=ac>4?atoi(av[4]):80;int SPLIT=ac>5?atoi(av[5]):2;P3.resize(std::max(P+1,YMAX+3));P3[0]=1;for(size_t i=1;i<P3.size();i++)P3[i]=P3[i-1]*3;cpp_int A("123139092617126647266"),E("77692117359936589403"),K=A-E-Z+3;u128 q=pow2(K,P3[P])+1;if(q>=P3[P])q-=P3[P];std::vector<Task>ts;collect(q,P,0,0,0,SPLIT,ts);if(collect_amb){std::cerr<<"ambiguity in collector\n";return 1;}
auto less_state=[](const Task&a,const Task&b){if(a.p!=b.p)return a.p<b.p;if(a.x!=b.x)return a.x<b.x;if(a.y!=b.y)return a.y<b.y;return a.q<b.q;};
auto same_state=[](const Task&a,const Task&b){return a.p==b.p&&a.x==b.x&&a.y==b.y&&a.q==b.q;};
size_t raw=ts.size(); std::sort(ts.begin(),ts.end(),less_state); size_t w=0;
for(size_t i=0;i<ts.size();){size_t j=i+1; Task t=ts[i]; while(j<ts.size()&&same_state(ts[i],ts[j])){if(ts[j].prefix>t.prefix)t.prefix=ts[j].prefix; ++j;} ts[w++]=t; i=j;} ts.resize(w);
auto t0=std::chrono::steady_clock::now();int best=collected_done;
#pragma omp parallel for schedule(dynamic,16) reduction(max:best)
for(int i=0;i<(int)ts.size();++i){int z=dfs(ts[i].q,ts[i].p,ts[i].x,ts[i].y);if(z>=900000)best=1000000;else best=std::max(best,ts[i].prefix+z);}double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count();std::cout<<"exactX_dedup Z="<<Z<<" X="<<XMAX<<" Y="<<YMAX<<" max="<<best<<" raw_tasks="<<raw<<" unique_tasks="<<ts.size()<<" split="<<SPLIT<<" threads="<<omp_get_max_threads()<<" sec="<<sec<<"\n";return best>=900000?1:0;}
