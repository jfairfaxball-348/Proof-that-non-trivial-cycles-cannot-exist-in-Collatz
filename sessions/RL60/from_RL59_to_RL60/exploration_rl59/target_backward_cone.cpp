#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <unordered_set>
#include <limits>
using boost::multiprecision::cpp_int;
static std::vector<cpp_int>P2{cpp_int(1)},P3{cpp_int(1)};
static inline void e2(int n){while((int)P2.size()<=n)P2.push_back(P2.back()*2);}
static inline void e3(int n){while((int)P3.size()<=n)P3.push_back(P3.back()*3);}
const int IT=73,PT=47,ZT=26,KMIN=25; const cpp_int AA=cpp_int(27)*cpp_int(1000000000000000000LL)+2,AB=cpp_int(2)*cpp_int(1000000000000000000LL);
struct Key{int p,d;long long J;bool operator==(Key const&o)const{return p==o.p&&d==o.d&&J==o.J;}};struct KH{size_t operator()(Key const&k)const noexcept{uint64_t h=1469598103934665603ULL;auto m=[&](uint64_t x){h^=x;h*=1099511628211ULL;};m(k.p);m(k.d);m((uint64_t)k.J);return(size_t)h;}};
static bool viable(int i,int p,int d,long long J){if(d<1||p<0)return false;e2(i+2);e3(p+d+3);cpp_int T=cpp_int(J)-P3[d]+P2[d];cpp_int dx=P3[p+d-1]*P2[d-1],nx=P2[i]*((T-1)*P2[d-1]+P3[d-1]);cpp_int dp=2*dx,np=P2[i]*(P3[d-1]*P2[d]+(T-1)*P2[d-1]+P3[d-1]);cpp_int diff=AA*dx-nx*AB;if(diff<=0)return false;cpp_int rhs=AA*dx;int K=KMIN;while((diff<<K)<=rhs)K+=2;cpp_int two=cpp_int(1)<<K,pcn=AA*(two+1),pcd=cpp_int(2)*AB*two;if(np*pcd>=pcn*dp)return false;if(cpp_int(3)*AB*P2[i]*J>=AA*P3[p+d]||cpp_int(3)*P2[i]*J<cpp_int(-13)*P3[p+d])return false;return true;}
static void add(std::unordered_set<Key,KH>&nxt,int iprev,int p,int d,cpp_int const&Jbig,int x){if(p<0||d<1||Jbig<std::numeric_limits<long long>::min()||Jbig>std::numeric_limits<long long>::max())return;long long J=Jbig.convert_to<long long>();int z=iprev-p;if(z<0||z>ZT||p>PT)return; // predecessor count bounds
 if(x==0){e2(iprev+1);e3(p+1); if(cpp_int(30)*P2[iprev]>cpp_int(17)*P3[p])return;}
 if(!viable(iprev,p,d,J))return;nxt.insert(Key{p,d,J});}
int main(){e2(IT+3);e3(IT+10);std::unordered_set<Key,KH>cur,nxt;cur.reserve(1000000);nxt.reserve(1000000);cur.insert(Key{PT,1,3});
 for(int i=IT;i>55;i--){nxt.clear();int ip=i-1;for(auto const&k:cur){int p=k.p,d=k.d;cpp_int Jp=k.J;
   // inverse 00: predecessor d, p unchanged, x=0; legal J odd checked by parity
   cpp_int J00=2*Jp-P3[d]+P2[d]; if((J00&1)!=0) add(nxt,ip,p,d,J00,0);
   // inverse 11: predecessor d, p-1, x=1; exact divisibility and odd predecessor
   cpp_int num11=2*Jp-P2[d]+1;if(num11%3==0){cpp_int J11=num11/3;if((J11&1)!=0)add(nxt,ip,p-1,d,J11,1);}
   // inverse 01: predecessor d-1,p unchanged,x=0, requires target d>=2 and even predecessor
   if(d>=2){cpp_int num01=2*Jp-P3[d]+P2[d-1]+1;if(num01%3==0){cpp_int J01=num01/3;if((J01&1)==0)add(nxt,ip,p,d-1,J01,0);}}
   // inverse 10: predecessor d+1,p-1,x=1, J=2Jp even
   add(nxt,ip,p-1,d+1,2*Jp,1);
 }
 cur.swap(nxt);std::cerr<<"layer="<<ip<<" states="<<cur.size()<<"\n";if(cur.empty())break;}
 Key start{0,1,-13};std::cout<<"start_reachable="<<(cur.count(start)?1:0)<<" final_states="<<cur.size()<<"\n";
}
