#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using boost::multiprecision::cpp_int; using u128=unsigned __int128;
static std::vector<u128>P3; static int XMAX,YMAX,TARGET; static std::string path;
static u128 modcpp(cpp_int a,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;cpp_int r=a%mm;uint64_t lo=(r&((cpp_int(1)<<64)-1)).convert_to<uint64_t>(),hi=(r>>64).convert_to<uint64_t>();return (u128(hi)<<64)|lo;} static u128 pow2(cpp_int e,u128 m){cpp_int mm=(cpp_int((uint64_t)(m>>64))<<64)+(uint64_t)m;return modcpp(boost::multiprecision::powm(cpp_int(2),e,mm),m);} static int val3(u128 q,int p){if(!q)return -1;int v=0;while(v<p&&q%3==0){q/=3;++v;}return v==p?-1:v;}
static bool dfs(u128 q,int p,int x,int y,int len){if(len>=TARGET)return true;int v=val3(q,p);if(v<0)return false;if(len+v>=TARGET){path.append(TARGET-len,'1');return true;}int d=1+y-x;u128 qr=q;int pr=p;for(int r=0;r<=v;r++){size_t old=path.size();path.append(r,'1');int nl=len+r;
 if(y<YMAX){u128 nq=2*qr+1;if(nq>=P3[pr])nq-=P3[pr];path.push_back('A');if(dfs(nq,pr,x,y+1,nl+1))return true;path.resize(old+r);
 if(x<XMAX){u128 c=P3[d]-1,a=2*qr;if(a>=P3[pr])a-=P3[pr];u128 n2=(a>=c)?a-c:a+P3[pr]-c;path.push_back('B');if(dfs(n2,pr,x+1,y+1,nl+1))return true;path.resize(old+r);}}
 if(x<XMAX&&d>1&&r<v){int np=pr-1;u128 a=2*(qr/3);if(a>=P3[np])a-=P3[np];u128 c=P3[d-1],n=(a>=c)?a-c:a+P3[np]-c;path.push_back('C');if(dfs(n,np,x+1,y,nl+1))return true;path.resize(old+r);}path.resize(old);if(r<v){--pr;qr=2*(qr/3);if(qr>=P3[pr])qr-=P3[pr];}}
 return false;}
int main(int ac,char**av){if(ac<5)return 2;int Z=atoi(av[1]);XMAX=atoi(av[2]);YMAX=atoi(av[3]);TARGET=atoi(av[4]);int P=std::min(120,std::max(TARGET+10,80));P3.resize(std::max(P+1,YMAX+3));P3[0]=1;for(size_t i=1;i<P3.size();i++)P3[i]=P3[i-1]*3;cpp_int A("123139092617126647266"),E("77692117359936589403"),K=A-E-Z+3;u128 q=pow2(K,P3[P])+1;if(q>=P3[P])q-=P3[P];bool h=dfs(q,P,0,0,0);std::cout<<"Z="<<Z<<" X="<<XMAX<<" Y="<<YMAX<<" target="<<TARGET<<" hit="<<h<<" path="<<path<<"\n";return h?0:1;}
