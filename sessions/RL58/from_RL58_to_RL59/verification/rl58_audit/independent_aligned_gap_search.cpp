#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>

using boost::multiprecision::cpp_int;
using boost::multiprecision::cpp_rational;

static const int N = 26;
static const int KMIN = 25;
static const cpp_rational CAP = cpp_rational(17)/30;
static const cpp_rational DEFECT_MAX = cpp_rational(5)/3;
static const cpp_rational TOTAL_REQ = cpp_rational(143)/12;
static const cpp_rational TARGET = cpp_rational(17)/3;
// Safe inherited over-cap: 27*zeta/2 < 27/2 + 10^-18.
static const cpp_rational ALPHA = cpp_rational(cpp_int(27)*cpp_int(1000000000000000000LL)+2,
                                                cpp_int(2)*cpp_int(1000000000000000000LL));

static std::vector<cpp_int> P2{cpp_int(1)}, P3{cpp_int(1)};
static void need2(int n){ while((int)P2.size()<=n) P2.push_back(P2.back()*2); }
static void need3(int n){ while((int)P3.size()<=n) P3.push_back(P3.back()*3); }

struct Dyn {
    int i=0, p=0, d=1;
    long long J=-13;
};
struct State {
    Dyn q;
    int rem=N;
    cpp_rational Z=0;   // accumulated x-zero mass
    cpp_rational Y=0;   // accumulated y-zero mass
    cpp_rational A=0;   // aligned (r=0) x-zero mass
};

struct StepInfo { bool ok=false; int y=0; Dyn q; };

static StepInfo advance(Dyn const& s, int x){
    need2(s.d+2); need3(s.d+2);
    int y;
    if(x==0) y = (s.J & 1LL) ? 0 : 1;
    else {
        if(s.J & 1LL) y=1;
        else if(s.d>1) y=0;
        else return {};
    }
    cpp_int jn;
    int dn=s.d;
    if(x==0 && y==0) jn=(cpp_int(s.J)+P3[s.d]-P2[s.d])/2;
    else if(x==1 && y==1) jn=(cpp_int(3)*s.J+P2[s.d]-1)/2;
    else if(x==0 && y==1){ dn=s.d+1; jn=(cpp_int(3)*s.J+P3[s.d+1]-P2[s.d]-1)/2; }
    else { dn=s.d-1; jn=cpp_int(s.J)/2; }
    if(jn < std::numeric_limits<long long>::min() || jn > std::numeric_limits<long long>::max()){
        std::cerr << "J overflow\n"; std::exit(3);
    }
    Dyn t{s.i+1, s.p+x, dn, jn.convert_to<long long>()};
    return {true,y,t};
}

static cpp_rational g_of(Dyn const& s){ need2(s.i); need3(s.p); return cpp_rational(P2[s.i],P3[s.p]); }
static cpp_rational yweight_of(Dyn const& s){ need2(s.i); need3(s.p+s.d-1); return cpp_rational(P2[s.i],P3[s.p+s.d-1]); }

struct Pot { cpp_rational xi, psi; };
static Pot potentials(Dyn const& s){
    need2(s.d); need3(s.d);
    cpp_rational g=g_of(s);
    cpp_int T=cpp_int(s.J)-P3[s.d]+P2[s.d];
    cpp_rational xi = g * ( cpp_rational(T-1,P3[s.d-1]) + cpp_rational(1,P2[s.d-1]) );
    cpp_rational psi = g + xi/2;
    return {xi,psi};
}

struct TermCap { bool ok=false; int K=0; cpp_rational psi_end=0; };
static TermCap terminal_cap(Pot const& pot){
    if(pot.xi >= ALPHA) return {};
    int K=KMIN;
    for(;; K+=2){
        need2(K);
        cpp_rational xi_end = ALPHA * (cpp_rational(1) - cpp_rational(1,P2[K]));
        if(pot.xi < xi_end){
            cpp_rational psi_end = (ALPHA/2) * (cpp_rational(1) + cpp_rational(1,P2[K]));
            if(pot.psi >= psi_end) return {};
            return {true,K,psi_end};
        }
        if(K>999){ std::cerr << "unexpected K loop\n"; std::exit(4); }
    }
}

struct Key {
    int i,p,rem,d; long long J;
    bool operator==(Key const&o) const { return i==o.i&&p==o.p&&rem==o.rem&&d==o.d&&J==o.J; }
};
struct Hash {
    size_t operator()(Key const& k) const noexcept {
        std::uint64_t h=0x9e3779b97f4a7c15ULL;
        auto mix=[&](std::uint64_t x){ x += 0x9e3779b97f4a7c15ULL; x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL; x=(x^(x>>27))*0x94d049bb133111ebULL; x^=x>>31; h ^= x + (h<<6)+(h>>2); };
        mix(k.i);mix(k.p);mix(k.rem);mix(k.d);mix((std::uint64_t)k.J);return (size_t)h;
    }
};
struct Pt { cpp_rational A,Z,D; };
static std::unordered_map<Key,std::vector<Pt>,Hash> memo;

static std::uint64_t calls=0,gapsteps=0,zeroBranches=0,prDef=0,prK=0,prW=0,prTotal=0,prTarget=0,prMemo=0;
static size_t maxFront=0;
static std::string zero_positions;

static bool viable(State const& s, TermCap *tc_out=nullptr){
    ++gapsteps;
    cpp_rational g=g_of(s.q);
    cpp_rational D=s.Z-s.Y;
    cpp_rational defect_lb = D - cpp_rational(s.q.d-1)*cpp_rational(17,45);
    if(defect_lb >= DEFECT_MAX){ ++prDef; return false; }

    Pot pot=potentials(s.q);
    TermCap tc=terminal_cap(pot);
    if(!tc.ok){ ++prK; return false; }

    cpp_rational W = g * cpp_rational(s.q.J,P3[s.q.d]);
    if(W < cpp_rational(-13,3) || W >= ALPHA/3){ ++prW; return false; }

    cpp_rational psi_room = tc.psi_end - pot.psi;
    if(s.Z + psi_room <= TOTAL_REQ){ ++prTotal; return false; }

    if(s.A + cpp_rational(s.rem)*CAP <= TARGET){ ++prTarget; return false; }
    need2(s.rem);
    if(s.A + cpp_rational(P2[s.rem]-1)*g <= TARGET){ ++prTarget; return false; }
    if(s.A + psi_room <= TARGET){ ++prTarget; return false; }

    if(tc_out) *tc_out=tc;
    return true;
}

static bool dominated_or_insert(State const& s){
    Key k{s.q.i,s.q.p,s.rem,s.q.d,s.q.J};
    cpp_rational D=s.Z-s.Y;
    auto &v=memo[k];
    for(auto const& t:v){
        if(t.A>=s.A && t.Z>=s.Z && t.D<=D){ ++prMemo; return true; }
    }
    v.erase(std::remove_if(v.begin(),v.end(),[&](Pt const&t){
        return t.A<=s.A && t.Z<=s.Z && t.D>=D;
    }),v.end());
    v.push_back({s.A,s.Z,D});
    if(v.size()>maxFront) maxFront=v.size();
    return false;
}

static State do_step(State const& s,int x,StepInfo const& st){
    State t=s;
    cpp_rational g=g_of(s.q);
    cpp_rational yw=yweight_of(s.q);
    if(x==0){
        t.Z += g;
        if(s.q.d==1 && st.y==0) t.A += g;
        --t.rem;
    }
    if(st.y==0) t.Y += yw;
    t.q=st.q;
    return t;
}

// Independent organization: recurse only at x-zero events.  Between two x-zeros,
// scan the unique x=1 continuation and branch only on the choice to place the next zero now.
static bool dfs_after_zero(State const& start){
    ++calls;
    if(dominated_or_insert(start)) return false;
    State cur=start;
    for(;;){
        if(!viable(cur)) return false;
        if(cur.rem==0){
            std::cout << "HIT aligned=" << cur.A << " totalZ=" << cur.Z
                      << " i="<<cur.q.i<<" p="<<cur.q.p<<" d="<<cur.q.d<<" J="<<cur.q.J
                      << " zeros="<<zero_positions<<"\n";
            return true;
        }

        cpp_rational g=g_of(cur.q);
        if(g <= CAP){
            StepInfo z=advance(cur.q,0);
            if(z.ok){
                ++zeroBranches;
                State child=do_step(cur,0,z);
                size_t old=zero_positions.size();
                if(!zero_positions.empty()) zero_positions.push_back(',');
                zero_positions += std::to_string(cur.q.i);
                if(dfs_after_zero(child)) return true;
                zero_positions.resize(old);
            }
        }

        StepInfo one=advance(cur.q,1);
        if(!one.ok) return false;
        cur=do_step(cur,1,one);
    }
}

int main(){
    memo.reserve(600000);
    auto t0=std::chrono::steady_clock::now();
    State s;
    bool hit=dfs_after_zero(s);
    double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-t0).count();
    std::cout << "RL58_GAP_AUDIT target=17/3 hit="<<(hit?1:0)
              << " calls="<<calls<<" gapsteps="<<gapsteps<<" zeroBranches="<<zeroBranches
              << " memoKeys="<<memo.size()<<" maxFront="<<maxFront
              << " prDef="<<prDef<<" prK="<<prK<<" prW="<<prW<<" prTotal="<<prTotal
              << " prTarget="<<prTarget<<" prMemo="<<prMemo<<" sec="<<sec<<"\n";
    return hit?2:0;
}
