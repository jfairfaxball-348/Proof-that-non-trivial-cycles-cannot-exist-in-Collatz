#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <cstdint>
#include <limits>
#include <chrono>
#include <algorithm>
using boost::multiprecision::cpp_int;
using std::uint64_t;

static std::vector<cpp_int> P2{cpp_int(1)}, P3{cpp_int(1)};
static inline void ensure2(int n){ while((int)P2.size()<=n) P2.push_back(P2.back()*2); }
static inline void ensure3(int n){ while((int)P3.size()<=n) P3.push_back(P3.back()*3); }

struct Key {
    int i,p,rem,d;
    long long J;
    bool operator==(Key const& o) const { return i==o.i&&p==o.p&&rem==o.rem&&d==o.d&&J==o.J; }
};
struct KeyHash {
    size_t operator()(Key const& k) const noexcept {
        uint64_t h=1469598103934665603ULL;
        auto mix=[&](uint64_t x){ h^=x; h*=1099511628211ULL; };
        mix((uint64_t)k.i); mix((uint64_t)k.p); mix((uint64_t)k.rem); mix((uint64_t)k.d); mix((uint64_t)k.J);
        return (size_t)h;
    }
};

const int N=26, KMIN=25;
const long long TA=33, TB=4;
const long long REQA=143, REQB=12;
const cpp_int AA = cpp_int(27)*cpp_int(1000000000000000000LL)+2; // 13.5 + 1e-18 times AB
const cpp_int AB = cpp_int(2)*cpp_int(1000000000000000000LL);

struct Pots { cpp_int nxi,Dxi,npsi,D; };
static Pots pots(int i,int p,int d,long long J){
    ensure2(std::max(i,d)+2); ensure3(p+d+2);
    cpp_int T = cpp_int(J)-P3[d]+P2[d];
    cpp_int Dxi=P3[p+d-1]*P2[d-1];
    cpp_int nxi=P2[i]*((T-1)*P2[d-1]+P3[d-1]);
    cpp_int D=2*Dxi;
    cpp_int npsi=P2[i]*(P3[d-1]*P2[d]+(T-1)*P2[d-1]+P3[d-1]);
    return {nxi,Dxi,npsi,D};
}

static bool checked_ll(__int128 x,long long &out){
    if(x < (__int128)std::numeric_limits<long long>::min() || x > (__int128)std::numeric_limits<long long>::max()) return false;
    out=(long long)x; return true;
}
struct Step { bool ok; int d; long long J; };
static Step step(int d,long long J,int x){
    ensure2(d+2); ensure3(d+2);
    bool odd=(J&1LL)!=0;
    int y;
    if(x==0) y=odd?0:1;
    else { if(odd) y=1; else if(d>1) y=0; else return {false,0,0}; }
    cpp_int jj;
    int nd=d;
    if(x==0&&y==0) jj=(cpp_int(J)+P3[d]-P2[d])/2;
    else if(x==1&&y==1) jj=(cpp_int(3)*J+P2[d]-1)/2;
    else if(x==0&&y==1){ nd=d+1; jj=(cpp_int(3)*J+P3[d+1]-P2[d]-1)/2; }
    else { nd=d-1; jj=cpp_int(J)/2; }
    if(jj < std::numeric_limits<long long>::min() || jj > std::numeric_limits<long long>::max()){
        std::cerr << "J overflow: independent run needs wider key representation\n"; std::exit(3);
    }
    return {true,nd,jj.convert_to<long long>()};
}

struct KSel { bool ok; int K; cpp_int pcn,pcd; };
static KSel kselect(Pots const& q){
    cpp_int diff=AA*q.Dxi-q.nxi*AB;
    if(diff<=0) return {false,0,0,0};
    cpp_int rhs=AA*q.Dxi;
    int K=KMIN;
    // Find the smallest admissible odd K satisfying Xi_cut < A(1-2^-K).
    while((diff<<K)<=rhs) K+=2;
    cpp_int two=cpp_int(1)<<K;
    if(!(q.nxi*AB*two < AA*(two-1)*q.Dxi)) { std::cerr<<"internal K selector inconsistency\n"; std::exit(4); }
    cpp_int pcn=AA*(two+1), pcd=cpp_int(2)*AB*two;
    if(q.npsi*pcd >= pcn*q.D) return {false,0,0,0};
    return {true,K,pcn,pcd};
}

static std::unordered_map<Key,cpp_int,KeyHash> seen;
static uint64_t nodes=0, pr[5]={0,0,0,0,0};
static int kmax_seen=0, max_i=0, max_p=0, max_d=0;
static long long max_abs_J=0;

static bool rec(int i,int p,int rem,cpp_int const& Znum,int d,long long J){
    ++nodes; max_i=std::max(max_i,i); max_p=std::max(max_p,p); max_d=std::max(max_d,d); max_abs_J=std::max(max_abs_J,(long long)std::llabs(J));
    ensure2(i+rem+3); ensure3(p+d+3);
    Pots q=pots(i,p,d,J);
    KSel ks=kselect(q);
    if(!ks.ok){ ++pr[0]; return false; }
    kmax_seen=std::max(kmax_seen,ks.K);

    // W = 2^i J / 3^(p+d), with -13/3 <= W < A/3.
    if(cpp_int(3)*AB*P2[i]*J >= AA*P3[p+d] || cpp_int(3)*P2[i]*J < cpp_int(-13)*P3[p+d]){ ++pr[1]; return false; }

    cpp_int den=P3[p];
    // Necessary total viability: prefix mass + terminal Psi room > 143/12.
    cpp_int lhs=(Znum*q.D*ks.pcd + ks.pcn*den*q.D - q.npsi*den*ks.pcd)*REQB;
    cpp_int rhs=cpp_int(REQA)*den*q.D*ks.pcd;
    if(lhs<=rhs){ ++pr[2]; return false; }

    // Three independent upper bounds on possible mass by the 26th x-zero.
    if(cpp_int(TB)*(cpp_int(30)*Znum + cpp_int(17)*rem*den) <= cpp_int(TA)*30*den){ ++pr[3]; return false; }
    if(cpp_int(TB)*(Znum + (P2[rem]-1)*P2[i]) <= cpp_int(TA)*den){ ++pr[3]; return false; }
    cpp_int lhs2=(Znum*q.D*ks.pcd + ks.pcn*den*q.D - q.npsi*den*ks.pcd)*TB;
    cpp_int rhs2=cpp_int(TA)*den*q.D*ks.pcd;
    if(lhs2<=rhs2){ ++pr[3]; return false; }

    Key key{i,p,rem,d,J};
    auto it=seen.find(key);
    if(it!=seen.end() && Znum<=it->second){ ++pr[4]; return false; }
    if(it==seen.end()) seen.emplace(key,Znum); else it->second=Znum;

    if(rem==0){
        std::cout << "COUNTEREXAMPLE PREFIX FOUND i="<<i<<" p="<<p<<" d="<<d<<" J="<<J<<" K="<<ks.K<<"\n";
        return true;
    }

    // x=0 branch: exact relaxed sequential cap g <= 17/30.
    if(cpp_int(30)*P2[i] <= cpp_int(17)*den){
        Step s=step(d,J,0);
        if(s.ok && rec(i+1,p,rem-1,Znum+P2[i],s.d,s.J)) return true;
    }
    // x=1 branch.
    Step s=step(d,J,1);
    if(s.ok && rec(i+1,p+1,rem,cpp_int(3)*Znum,s.d,s.J)) return true;
    return false;
}

int main(){
    seen.reserve(900000);
    auto t0=std::chrono::steady_clock::now();
    bool hit=rec(0,0,N,cpp_int(0),1,-13);
    double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count();
    std::cout << "INDEPENDENT_CPP TARGET 33/4 hit "<<(hit?"True":"False")
              <<" nodes "<<nodes<<" states "<<seen.size()<<" sec "<<sec
              <<" pr ["<<pr[0]<<","<<pr[1]<<","<<pr[2]<<","<<pr[3]<<","<<pr[4]<<"]"
              <<" kmax "<<kmax_seen<<" max_i "<<max_i<<" max_p "<<max_p<<" max_d "<<max_d<<" max_abs_J "<<max_abs_J<<"\n";
    return hit?2:0;
}
