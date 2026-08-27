#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using u64 = std::uint64_t;
constexpr int L=11, MAX_Z=33;
constexpr u64 THREE_L=177147;
static const u64 p3[]={1,3,9,27,81,243,729,2187,6561,19683,59049,177147};

static void comps(int n,int parts,std::vector<int>& cur,std::vector<std::vector<int>>& out){
  if(parts==1){cur.push_back(n);out.push_back(cur);cur.pop_back();return;}
  for(int a=1;a<=n-parts+1;++a){cur.push_back(a);comps(n-a,parts-1,cur,out);cur.pop_back();}
}
static bool primitive(const std::vector<int>& o,const std::vector<int>& z){
  std::vector<int>b; for(size_t i=0;i<o.size();++i){b.insert(b.end(),o[i],1);b.insert(b.end(),z[i],0);}
  for(int d=1;d<(int)b.size();++d)if((int)b.size()%d==0){bool same=true;for(size_t i=0;i<b.size();++i)if(b[i]!=b[i%d]){same=false;break;}if(same)return false;}
  return true;
}
static bool canonical_pairs(const std::vector<int>& o,const std::vector<int>& z){
  const int t=(int)o.size();
  for(int s=1;s<t;++s)for(int q=0;q<t;++q){
    const int a=(q+s)%t;
    if(o[a]!=o[q]) { if(o[q]>o[a]) return false; break; }
    if(z[a]!=z[q]) { if(z[q]>z[a]) return false; break; }
  }
  return true;
}
static u64 qnum(const std::vector<int>& bits,int shift){
  const int A=(int)bits.size(); int seen=0; u64 q=0;
  for(int p=0;p<A;++p)if(bits[(shift+p)%A])q+=(u64(1)<<p)*p3[L-1-seen++];
  return q;
}
static std::string word(const std::vector<int>& bits,int shift){std::string s;for(size_t p=0;p<bits.size();++p)s+=bits[(shift+p)%bits.size()]?'1':'0';return s;}

struct Search {
  int Z,t;u64 U,D;const std::vector<int>&o;
  std::array<u64,MAX_Z+1> zw{};
  std::array<std::array<int,MAX_Z+1>,L+1> cc{};
  std::array<u64,MAX_Z+1> zcap{};
  std::array<std::array<int,MAX_Z+1>,L+1> ccap{};
  std::vector<int>z;
  u64 profiles=0,periodic=0,canonical=0,orbit_weight=0,roots=0,hits=0;
  Search(int Z_,u64 U_,u64 D_,const std::vector<int>&o_):Z(Z_),t((int)o_.size()),U(U_),D(D_),o(o_){
    for(int k=1;k<=Z;++k)zcap[k]=(U-1)/(u64(1)<<k)+1;
    for(int j=1;j<=L;++j)for(int k=1;k<=Z;++k)ccap[j][k]=(int)(U/(p3[j]*(u64(1)<<k)))+1;
  }
  bool add(int i,int v){
    for(int k=1;k<=v;++k){zw[k]+=v-k+1;for(int j=1;j<=o[i];++j)++cc[j][k];}
    for(int k=1;k<=v;++k){if(zw[k]>zcap[k]){undo(i,v);return false;}for(int j=1;j<=o[i];++j)if(cc[j][k]>ccap[j][k]){undo(i,v);return false;}}
    return true;
  }
  void undo(int i,int v){for(int k=1;k<=v;++k){zw[k]-=v-k+1;for(int j=1;j<=o[i];++j)--cc[j][k];}}
  void owned(){
    std::vector<int>bits;for(size_t i=0;i<o.size();++i){bits.insert(bits.end(),o[i],1);bits.insert(bits.end(),z[i],0);}
    ++canonical; orbit_weight+=t; for(int s=0;s<(int)bits.size();++s){++roots;u64 q=qnum(bits,s);if(q%D==0){++hits;std::cout<<"HIT Z="<<Z<<" word="<<word(bits,s)<<" x="<<(q/D)<<'\n';}}
  }
  void dfs(int i,int rem){
    if(i==t){if(rem==0){++profiles;if(!primitive(o,z)){++periodic;return;}if(canonical_pairs(o,z))owned();}return;}
    const int slots=t-i-1;for(int v=1;v<=rem-slots;++v)if(add(i,v)){z.push_back(v);dfs(i+1,rem-v);z.pop_back();undo(i,v);}
  }
};
static u64 one_floor(const std::vector<int>&o){u64 out=0;for(int j=1;j<=L;++j){u64 c=0;for(int x:o)if(x>=j)c+=x-j+1;if(c)out=std::max(out,(c-1)*p3[j]);}return out;}
int main(){
  std::cout<<"# L=11 canonical constrained ownership certificate\n";
  u64 totalP=0,totalPer=0,totalCan=0,totalWeight=0,totalRoots=0,totalHits=0;
  for(int Z=7;Z<=33;++Z){const u64 D=(u64(1)<<(L+Z))-THREE_L,B=((u64(1)<<Z)-1)*(THREE_L-(u64(1)<<L)),U=B/D;u64 P=0,Per=0,Can=0,Roots=0,Hits=0;
    u64 Weight=0; for(int t=1;t<=std::min(L,Z);++t){if(6*(t-1)>U)continue;std::vector<std::vector<int>>os;std::vector<int>cur;comps(L,t,cur,os);for(const auto&o:os){if(one_floor(o)>U)continue;Search s(Z,U,D,o);s.dfs(0,Z);P+=s.profiles;Per+=s.periodic;Can+=s.canonical;Weight+=s.orbit_weight;Roots+=s.roots;Hits+=s.hits;}}
    if(Weight!=P-Per){std::cerr<<"orbit-weight mismatch at Z="<<Z<<" profiles="<<P<<" periodic="<<Per<<" weight="<<Weight<<" canonical="<<Can<<'\n';return 2;}
    totalP+=P;totalPer+=Per;totalCan+=Can;totalWeight+=Weight;totalRoots+=Roots;totalHits+=Hits;
    std::cout<<"Z="<<Z<<" U="<<U<<" capacity_profiles="<<P<<" periodic="<<Per<<" canonical_primitive_profiles="<<Can<<" orbit_weight="<<Weight<<" roots_tested="<<Roots<<" divisibility_hits="<<Hits<<'\n';
  }
  if(totalWeight!=totalP-totalPer){std::cerr<<"total orbit-weight mismatch\n";return 2;}
  std::cout<<"TOTAL capacity_profiles="<<totalP<<" periodic="<<totalPer<<" canonical_primitive_profiles="<<totalCan<<" orbit_weight="<<totalWeight<<" roots_tested="<<totalRoots<<" divisibility_hits="<<totalHits<<'\n';
}
