#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_set>
#include <vector>
using boost::multiprecision::cpp_int;
using boost::multiprecision::uint256_t;
struct State { uint256_t q; uint16_t p; uint8_t x,y; bool operator==(State const&o)const{return q==o.q&&p==o.p&&x==o.x&&y==o.y;} };
struct Hash { size_t operator()(State const&s)const { uint64_t a[4]; uint256_t z=s.q; for(int i=0;i<4;i++){a[i]=(uint64_t)(z & uint256_t(0xffffffffffffffffULL)); z >>=64;} uint64_t h=0x9e3779b97f4a7c15ULL; for(int i=0;i<4;i++){uint64_t v=a[i]+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);h^=v;} h^=((uint64_t)s.p<<32)|((uint64_t)s.x<<16)|s.y; h^=h>>30;h*=0xbf58476d1ce4e5b9ULL;h^=h>>27;h*=0x94d049bb133111ebULL;h^=h>>31; return (size_t)h; } };
static uint256_t modpow2(cpp_int e, cpp_int const&m){ cpp_int r=boost::multiprecision::powm(cpp_int(2),e,m); return uint256_t(r); }
static inline uint256_t modsub(uint256_t a,uint256_t b,uint256_t m){return a>=b?a-b:a+m-b;}
int main(int ac,char**av){ if(ac<5){std::cerr<<"usage Z Xcap Ycap target_depth [P]\n"; return 2;} int Z=atoi(av[1]), X=atoi(av[2]), Y=atoi(av[3]), T=atoi(av[4]); int P=(ac>5?atoi(av[5]):T+2); if(P<=T){std::cerr<<"need P>T\n";return 2;} if(P>150){std::cerr<<"P too large for uint256_t\n";return 2;} std::vector<uint256_t> p3(P+1); p3[0]=1; for(int i=1;i<=P;i++)p3[i]=p3[i-1]*3; cpp_int A("123139092617126647266"),ELL("77692117359936589403"),K=A-ELL-Z+3; cpp_int mod=1; for(int i=0;i<P;i++)mod*=3; uint256_t q0=modpow2(K,mod)+1; if(q0>=p3[P])q0-=p3[P]; std::unordered_set<State,Hash> cur,nxt; cur.reserve(1<<20); nxt.reserve(1<<20); cur.insert({q0,(uint16_t)P,0,0}); auto t0=std::chrono::steady_clock::now(); size_t peak=1; int last=0; for(int depth=0; depth<T; ++depth){ nxt.clear(); for(auto const&s:cur){ int d=1+(int)s.y-(int)s.x; uint256_t m=p3[s.p]; // 10
      if(s.y<Y){ uint256_t q=s.q*2+1; if(q>=m)q-=m; nxt.insert({q,s.p,s.x,(uint8_t)(s.y+1)}); }
      // 00
      if(s.x<X && s.y<Y){ uint256_t c=p3[d]-1; uint256_t a=s.q*2; if(a>=m)a-=m; uint256_t q=modsub(a,c,m); nxt.insert({q,s.p,(uint8_t)(s.x+1),(uint8_t)(s.y+1)}); }
      if(s.q%3==0 && s.p>1){ uint16_t np=s.p-1; uint256_t nm=p3[np]; uint256_t a=2*(s.q/3); if(a>=nm)a-=nm; // 11
        nxt.insert({a,np,s.x,s.y});
        if(s.x<X && d>1){ uint256_t c=p3[d-1]; uint256_t q=modsub(a,c,nm); nxt.insert({q,np,(uint8_t)(s.x+1),s.y}); }
      }
    }
    cur.swap(nxt); last=depth+1; peak=std::max(peak,cur.size()); if((last%10)==0 || cur.empty()) std::cerr<<"depth="<<last<<" states="<<cur.size()<<" peak="<<peak<<"\n"; if(cur.empty())break; }
 double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count(); if(cur.empty()){std::cout<<"BFS_CERT Z="<<Z<<" Xcap="<<X<<" Ycap="<<Y<<" extinct_at="<<last<<" max_length<="<<last-1<<" P="<<P<<" peak_states="<<peak<<" sec="<<sec<<"\n"; return 0;} else {std::cout<<"BFS_SURVIVES Z="<<Z<<" Xcap="<<X<<" Ycap="<<Y<<" depth="<<T<<" states="<<cur.size()<<" P="<<P<<" peak_states="<<peak<<" sec="<<sec<<"\n"; return 1;} }
