#include <bits/stdc++.h>
using namespace std;
int main(){
 const long double CAP=17.0L/30.0L;
 long double best=-1; unsigned long long bestJs=0,bJ=0,bJe=0; int bst=0,beb=0; long double bg=0,bge=0,bM=0,bMe=0,bmz=0,blt=0,blc=0,bl=0;
 for(unsigned long long Js=1;Js<20000000ULL;Js+=2){
   __uint128_t J=Js; long double g=1,M=0,maxz=0;
   for(int step=0;step<160;step++){
     int cb=((unsigned long long)(J&3)==1)?0:1, eb=1-cb;
     __uint128_t Je; long double ge,Me,mz;
     if(eb==0){Je=(J+1)/2; ge=2*g; Me=M+g; mz=max(maxz,g);} else {Je=(3*J+1)/2; ge=(2.0L/3)*g; Me=M; mz=maxz;}
     long double JeD=(long double)Je;
     long double lt=1.5L/(ge*(JeD+2));
     long double lc=(mz==0)?1e300L:CAP/mz;
     long double lam=min(lt,lc), val=lam*Me;
     if(val>best){best=val;bestJs=Js;bst=step;bJ=(unsigned long long)J;beb=eb;bJe=(unsigned long long)Je;bg=g;bge=ge;bM=M;bMe=Me;bmz=mz;blt=lt;blc=lc;bl=lam;}
     if(cb==0){maxz=max(maxz,g);M+=g;g*=2;J=(J+1)/2;}else{g*=2.0L/3;J=(3*J+1)/2;}
     if(J>((__uint128_t)1<<120)) break;
   }
 }
 cout<<setprecision(18)<<"best="<<(double)best<<" Js="<<bestJs<<" step="<<bst<<" J="<<bJ<<" exitbit="<<beb<<" Je="<<bJe<<" g="<<(double)bg<<" ge="<<(double)bge<<" M="<<(double)bM<<" Me="<<(double)bMe<<" mz="<<(double)bmz<<" lt="<<(double)blt<<" lc="<<(double)blc<<" lam="<<(double)bl<<"\n";
}
