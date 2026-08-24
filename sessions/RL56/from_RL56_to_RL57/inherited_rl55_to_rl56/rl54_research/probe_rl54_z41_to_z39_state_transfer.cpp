#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_set>
#include <vector>
using boost::multiprecision::cpp_int; using u128=unsigned __int128;
static std::vector<u128>P3;
static u128 modcpp(cpp_int a,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;cpp_int r=a%mm;uint64_t lo=(r&((cpp_int(1)<<64)-1)).convert_to<uint64_t>(),hi=(r>>64).convert_to<uint64_t>();return (u128(hi)<<64)|lo;}
static u128 pow2(cpp_int e,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;return modcpp(boost::multiprecision::powm(cpp_int(2),e,mm),m);}
static int v3(u128 q,int p){if(!q)return -1;int v=0;while(v<p&&q%3==0){q/=3;v++;}return v==p?-1:v;}
struct K{uint64_t lo,hi;uint16_t p;bool operator==(K const&o)const{return lo==o.lo&&hi==o.hi&&p==o.p;}};
struct H{size_t operator()(K const&k)const{uint64_t h=k.lo^(k.hi+0x9e3779b97f4a7c15ULL+(k.lo<<6)+(k.lo>>2));h^=(uint64_t)k.p*0xbf58476d1ce4e5b9ULL;return (size_t)(h^(h>>31));}};
static K key(u128 q,int p){return {(uint64_t)q,(uint64_t)(q>>64),(uint16_t)p};}
using Set=std::unordered_set<K,H>;
static std::vector<std::vector<Set>> build(int Z,int X,int Y,int P,int Smax){std::vector<std::vector<Set>> a(X+1);for(auto&r:a)r.resize(Y+1);cpp_int A("123139092617126647266"),E("77692117359936589403"),kk=A-E-Z+3;u128 q=pow2(kk,P3[P])+1;if(q>=P3[P])q-=P3[P];a[0][0].insert(key(q,P));for(int s=0;s<=Smax;s++){for(int x=0;x<=X;x++){int y=s-x;if(y<0||y>Y)continue;std::vector<K> cur(a[x][y].begin(),a[x][y].end());for(auto const&z:cur){u128 q=(u128(z.hi)<<64)|z.lo;int p=z.p;if(q%3==2)continue;int v=v3(q,p);if(v<0){std::cerr<<"amb\n";exit(2);}int d=1+y-x;u128 qr=q;int pr=p;for(int r=0;r<=v;r++){if(y<Y&&s+1<=Smax){u128 nq=2*qr+1;if(nq>=P3[pr])nq-=P3[pr];a[x][y+1].insert(key(nq,pr));}if(x<X&&y<Y&&s+2<=Smax){u128 c=P3[d]-1,aa=2*qr;if(aa>=P3[pr])aa-=P3[pr];u128 nq=aa>=c?aa-c:aa+P3[pr]-c;a[x+1][y+1].insert(key(nq,pr));}if(x<X&&d>1&&r<v&&s+1<=Smax){int np=pr-1;u128 aa=2*(qr/3);if(aa>=P3[np])aa-=P3[np];u128 c=P3[d-1],nq=aa>=c?aa-c:aa+P3[np]-c;a[x+1][y].insert(key(nq,np));}if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}}
}}}return a;}
int main(int ac,char**av){int S=ac>1?atoi(av[1]):12,P=80;P3.resize(P+20);P3[0]=1;for(size_t i=1;i<P3.size();i++)P3[i]=P3[i-1]*3;auto z39=build(39,12,16,P,S);auto z41=build(41,14,18,P,S+4);size_t tot=0,match=0;for(int x=2;x<=14;x++)for(int y=2;y<=18;y++){if(x+y>S+4)continue;auto &u=z41[x][y];auto &v=z39[x-2][y-2];size_t m=0;for(auto const&k:u)if(v.count(k))m++;if(!u.empty()){std::cout<<"cell41("<<x<<","<<y<<")="<<u.size()<<" vs39("<<x-2<<","<<y-2<<")="<<v.size()<<" exact_matches="<<m<<"\n";tot+=u.size();match+=m;}}
std::cout<<"TOTAL eligible z41 states="<<tot<<" matches="<<match<<" fraction="<<(tot?double(match)/tot:0)<<"\n";}
