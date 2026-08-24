#include <boost/multiprecision/cpp_int.hpp>
#include <atomic>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <omp.h>
using boost::multiprecision::cpp_int; using u128=unsigned __int128;
static std::vector<u128>P3; static int XMAX,YMAX; static std::atomic<bool>BAD(false);
static u128 modcpp(cpp_int a,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;cpp_int r=a%mm;uint64_t lo=(r&((cpp_int(1)<<64)-1)).convert_to<uint64_t>(),hi=(r>>64).convert_to<uint64_t>();return (u128(hi)<<64)|lo;}
static u128 pow2(cpp_int e,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;return modcpp(boost::multiprecision::powm(cpp_int(2),e,mm),m);}
static inline int val3(u128 q,int p){if(!q)return -1;int v=0;while(v<p&&q%3==0){q/=3;++v;}return v==p?-1:v;}
static inline u128 twice1(u128 q,int p){u128 z=2*q+1;if(z>=P3[p])z-=P3[p];return z;}
static inline u128 map00(u128 q,int p,int d){u128 a=2*q;if(a>=P3[p])a-=P3[p];u128 c=P3[d]-1;return a>=c?a-c:a+P3[p]-c;}
static bool amb(u128 q,int p,int x,int y);
// q is known 1 mod 3, hence v3(q)=0 exactly. It is itself nonambiguous.
// Fold the mandatory next zero-event(s) directly to children that may again
// be divisible; stopping after this state is harmless for ambiguity testing.
static inline bool from_unit1(u128 q,int p,int x,int y){
    int d=1+y-x;
    if(y<YMAX){u128 q10=twice1(q,p); if(amb(q10,p,x,y+1))return true;}
    if(x<XMAX && y<YMAX){u128 q00=map00(q,p,d); if(amb(q00,p,x+1,y+1))return true;}
    return false;
}
static bool amb_xfree(u128 q,int p,int yr){int v=val3(q,p);if(v<0)return true;if(yr==0||q%3==2)return false;u128 qr=q;int pr=p;for(int r=0;r<=v;r++){
    if(yr){u128 q1=twice1(qr,pr);if(r<v){ // q1 ==1 mod3; only a second 10 can matter
            if(yr>=2){u128 q2=twice1(q1,pr);if(amb_xfree(q2,pr,yr-2))return true;}
        }else{if(qr%3==1 && amb_xfree(q1,pr,yr-1))return true; /* qr%3==2 -> trap */}}
    if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}}
    return false;}
static bool amb(u128 q,int p,int x,int y){int v=val3(q,p);if(v<0)return true;if(x==XMAX)return amb_xfree(q,p,YMAX-y);if(q%3==2)return false;u128 qr=q;int pr=p;int d=1+y-x;
    for(int r=0;r<=v;r++){
        if(r<v){
            // qr divisible by 3. 10/00 children are exactly 1 mod3, so fold
            // their next zero-event rather than recurse through a v=0 node.
            if(y<YMAX){u128 q1=twice1(qr,pr);if(from_unit1(q1,pr,x,y+1))return true;}
            if(x<XMAX&&y<YMAX){u128 q1=map00(qr,pr,d);if(from_unit1(q1,pr,x+1,y+1))return true;}
        }else{
            // qr is a unit. If it is 2 mod3, both 10 and 00 enter the safe
            // absorbing 2-mod-3 class; only unit 1 can lead to divisibility.
            if(qr%3==1){
                if(y<YMAX){u128 q1=twice1(qr,pr);if(amb(q1,pr,x,y+1))return true;}
                if(x<XMAX&&y<YMAX){u128 q1=map00(qr,pr,d);if(amb(q1,pr,x+1,y+1))return true;}
            }
        }
        if(d>1&&r<v){int np=pr-1;u128 a=2*(qr/3);if(a>=P3[np])a-=P3[np];u128 c=P3[d-1],n=a>=c?a-c:a+P3[np]-c;if(amb(n,np,x+1,y))return true;}
        if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}
    }
    return false;}
struct Task{u128 q;int p,x,y;};
static bool collect(u128 q,int p,int x,int y,int levels,std::vector<Task>&out){int v=val3(q,p);if(v<0)return true;if(x==XMAX)return amb_xfree(q,p,YMAX-y);if(q%3==2)return false;if(levels==0){out.push_back({q,p,x,y});return false;}int d=1+y-x;u128 qr=q;int pr=p;for(int r=0;r<=v;r++){
    if(y<YMAX){u128 nq=twice1(qr,pr);if(collect(nq,pr,x,y+1,levels-1,out))return true;}
    if(x<XMAX&&y<YMAX){u128 nq=map00(qr,pr,d);if(collect(nq,pr,x+1,y+1,levels-1,out))return true;}
    if(d>1&&r<v){int np=pr-1;u128 a=2*(qr/3);if(a>=P3[np])a-=P3[np];u128 c=P3[d-1],n=a>=c?a-c:a+P3[np]-c;if(collect(n,np,x+1,y,levels-1,out))return true;}
    if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}}
    return false;}
int main(int ac,char**av){if(ac<4)return 2;int Z=atoi(av[1]);XMAX=atoi(av[2]);YMAX=atoi(av[3]);int P=ac>4?atoi(av[4]):80,S=ac>5?atoi(av[5]):10;P3.resize(std::max(P+1,YMAX+3));P3[0]=1;for(size_t i=1;i<P3.size();i++)P3[i]=P3[i-1]*3;cpp_int A("123139092617126647266"),E("77692117359936589403"),K=A-E-Z+3;u128 q=pow2(K,P3[P])+1;if(q>=P3[P])q-=P3[P];std::vector<Task>ts;if(collect(q,P,0,0,S,ts)){std::cout<<"AMBIG during collect\n";return 1;}std::cerr<<"tasks="<<ts.size()<<" split="<<S<<"\n";
#pragma omp parallel for schedule(dynamic,1)
for(int i=0;i<(int)ts.size();i++){if(!BAD.load(std::memory_order_relaxed)&&amb(ts[i].q,ts[i].p,ts[i].x,ts[i].y))BAD.store(true,std::memory_order_relaxed);}if(BAD){std::cout<<"AMBIG_FOUND\n";return 1;}std::cout<<"NO_AMBIG_FOLDED Z="<<Z<<" Xcap="<<XMAX<<" Ycap="<<YMAX<<" P="<<P<<" coarse_L_le="<<(P+XMAX+YMAX)<<" tasks="<<ts.size()<<" split="<<S<<"\n";return 0;}
