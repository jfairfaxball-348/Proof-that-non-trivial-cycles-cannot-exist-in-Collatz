#include <bits/stdc++.h>
using namespace std; using i128=__int128_t; using u128=__uint128_t; using u64=unsigned long long;
struct Rat{ i128 n=0,d=1; } E[26],C[26];
u64 p3[32]; u64 inv3pow[32][32]; unsigned long long cnt[26]={},ccnt[26]={};
ofstream smallf("/mnt/data/rl41_work/small_types_18_fast_raw.tsv"), crossf("/mnt/data/rl41_work/cross_types_25_fast_raw.tsv");
string s128(i128 x){ if(x==0)return"0"; bool neg=x<0;if(neg)x=-x;string s;while(x){s.push_back('0'+x%10);x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
bool gt(Rat a,Rat b){return a.n*b.d>b.n*a.d;}
// M suffix peak as mn/md, exact powers of 3/2, always >=1.
inline void appendM(u64 &mn,u64 &md,int bit){
    if(bit){ mn*=3; md*=2; } // (3/2)M >=1
    else { // max(1,M/2)
        if(mn>2*md) md*=2; else {mn=1;md=1;}
    }
}
inline Rat strong_unred(i128 D,int h,u64 mn,u64 md){
    // D/2^h * min(1,16 md/(15 mn))
    i128 n=D, d=((i128)1<<h);
    if((i128)15*mn>(i128)16*md){ n*= (i128)16*md; d*= (i128)15*mn; }
    return {n,d};
}
inline pair<i128,i128> reduceRat(Rat r){
    // values for outputs in our small range fit u64 after reduction; generic Euclid i128
    i128 a=r.n,b=r.d; while(b){i128 t=a%b;a=b;b=t;} return {r.n/a,r.d/a};
}
inline u64 maskmod(i128 x,u64 mod){ return (u64)(x & (i128)(mod-1)); }
void rec(int h,int d,int area,int pa,i128 Qa,i128 Qb,u64 Mbn,u64 Mbd){
    int area2=area+d; if(area2>25)return;
    if(d==1){
        int hh=h+1,p=pa+1,r=area2;
        i128 qa=3*Qa + ((i128)1<<h), qb=Qb, D=qa-qb;
        // beta appends 0
        u64 mn=Mbn,md=Mbd; appendM(mn,md,0);
        Rat S=strong_unred(D,hh,mn,md); cnt[r]++;
        if(gt(S,E[r]))E[r]=S;
        if(r<=18){auto rr=reduceRat(S);smallf<<r<<'\t'<<s128(D)<<'\t'<<hh<<'\t'<<p<<'\t'<<s128(rr.first)<<'\t'<<s128(rr.second)<<'\n';}
        u64 mod=1ULL<<hh; u64 Dm=maskmod(D,mod); u64 g=(u128)Dm*inv3pow[p][hh] & (mod-1); if(g==0)g=mod;
        i128 maxg=(D-1)/p3[p];
        if((i128)g<=maxg && (g&1)){
            ccnt[r]++; if(gt(S,C[r]))C[r]=S;
            i128 om=(D-(i128)p3[p]*g)/mod; auto rr=reduceRat(S);
            crossf<<r<<'\t'<<s128(D)<<'\t'<<hh<<'\t'<<p<<'\t'<<s128(rr.first)<<'\t'<<s128(rr.second)<<'\t'<<g<<'\t'<<s128(om)<<'\n';
        }
    }
    static int pp[4][2]={{0,0},{1,1},{0,1},{1,0}};
    for(auto &xy:pp){int x=xy[0],y=xy[1],nd=d+y-x;if(nd<=0)continue;
        i128 qa=Qa,qb=Qb;u64 mn=Mbn,md=Mbd;
        if(x)qa=3*qa+((i128)1<<h);
        if(y){qb=3*qb+((i128)1<<h);appendM(mn,md,1);} else appendM(mn,md,0);
        rec(h+1,nd,area2,pa+x,qa,qb,mn,md);
    }
}
int main(){
    p3[0]=1;for(int i=1;i<32;i++)p3[i]=p3[i-1]*3ULL;
    for(int p=0;p<32;p++)for(int h=1;h<32;h++){u64 mod=1ULL<<h,a=p3[p]& (mod-1),inv=1;for(int k=0;k<6;k++)inv*=2-a*inv;inv3pow[p][h]=inv&(mod-1);}
    smallf<<"r\tD\th\tp\tsn\tsd\n";crossf<<"r\tD\th\tp\tsn\tsd\tg\toutmag\n";
    // initial alpha=0,beta=1 at h=1,d=1, area=0, pa=0. Qa=0,Qb=1,M(beta)=3/2.
    rec(1,1,0,0,0,1,3,2);
    for(int r=1;r<=25;r++){auto er=reduceRat(E[r]),cr=reduceRat(C[r]);cout<<r<<" cnt "<<cnt[r]<<" E "<<s128(er.first)<<"/"<<s128(er.second)<<" cross "<<ccnt[r]<<" C "<<s128(cr.first)<<"/"<<s128(cr.second)<<"\n";}
}
