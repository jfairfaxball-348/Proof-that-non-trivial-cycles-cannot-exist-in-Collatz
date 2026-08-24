#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>
#include <chrono>
using boost::multiprecision::cpp_int;
struct Key{uint64_t q;uint16_t x,y,d;bool operator==(Key const&o)const{return q==o.q&&x==o.x&&y==o.y&&d==o.d;}};struct H{size_t operator()(Key const&k)const noexcept{uint64_t h=k.q*0x9e3779b97f4a7c15ULL;h^=((uint64_t)k.x<<48)^((uint64_t)k.y<<32)^k.d;h^=h>>33;h*=0xff51afd7ed558ccdULL;h^=h>>33;return(size_t)h;}};
static int XMAX,YMAX;static std::unordered_set<Key,H> dead;static std::string revpath;static uint64_t calls;
static uint64_t p3(int d){uint64_t x=1;for(int i=0;i<d;i++){if(x>UINT64_MAX/3)return UINT64_MAX;x*=3;}return x;}
static bool dfs(uint64_t q,int d,int x,int y){++calls;if(q==18&&d==2){std::cout<<"HIT x="<<x<<" y="<<y<<" reverse_edges="<<revpath<<"\n";return true;}if(x>XMAX||y>YMAX||d<1||d>25||q==0)return false;Key key{q,(uint16_t)x,(uint16_t)y,(uint16_t)d};if(dead.count(key))return false;
 int v=0;uint64_t t=q;while(t%3==0){t/=3;v++;if(v>30)break;}
 uint64_t qr=q;
 for(int r=0;r<=v;r++){
   // target after r backward 11s
   if(qr==18&&d==2){revpath.append(r,'1');std::cout<<"HIT x="<<x<<" y="<<y<<" reverse_edges="<<revpath<<"\n";revpath.resize(revpath.size()-r);return true;}
   size_t old=revpath.size();revpath.append(r,'1');
   if(y<YMAX && qr <= (UINT64_MAX-1)/2){revpath.push_back('A'); if(dfs(2*qr+1,d+1,x,y+1))return true; revpath.resize(old+r);} // A=backward10, forward x=1
   if(x<XMAX&&y<YMAX){uint64_t c=p3(d);if(c!=UINT64_MAX){c-=1;if(qr<=UINT64_MAX/2){__int128 nq=(__int128)2*qr-c;if(nq>0&&nq<=UINT64_MAX){revpath.push_back('B');if(dfs((uint64_t)nq,d,x+1,y+1))return true;revpath.resize(old+r);}}}} // B=backward00
   if(x<XMAX&&d>1&&r<v){ // current qr divisible by3
      uint64_t c=p3(d-1);if(c!=UINT64_MAX){__int128 nq=(__int128)2*(qr/3)-c;if(nq>0&&nq<=UINT64_MAX){revpath.push_back('C');if(dfs((uint64_t)nq,d-1,x+1,y))return true;revpath.resize(old+r);}}
   }
   revpath.resize(old);
   if(r<v){qr=2*(qr/3);} // one backward 11
 }
 dead.insert(key);return false;}
int main(){uint64_t q0=(1ULL<<25)+1;for(int xm=0;xm<=10;xm++){XMAX=xm;YMAX=xm+1;dead.clear();dead.reserve(1000000);revpath.clear();calls=0;auto t=std::chrono::steady_clock::now();bool h=dfs(q0,1,0,0);double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t).count();std::cerr<<"xm="<<xm<<" hit="<<h<<" calls="<<calls<<" dead="<<dead.size()<<" sec="<<sec<<"\n";if(h)return 0;}return 1;}
