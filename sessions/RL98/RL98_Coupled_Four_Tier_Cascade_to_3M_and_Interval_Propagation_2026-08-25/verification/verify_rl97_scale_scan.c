#include <gmp.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
int main(int argc,char**argv){
 if(argc<4){fprintf(stderr,"usage: N start end [chunk]\n");return 2;}
 unsigned long N=strtoul(argv[1],0,10), START=strtoul(argv[2],0,10), END=strtoul(argv[3],0,10);
 unsigned long CHUNK=argc>=5?strtoul(argv[4],0,10):0;
 const unsigned long S=26594276905UL;
 if(END>S+1){fprintf(stderr,"range too high\n");return 2;}
 mpz_t mod,half,inv3,res,bal,tmp; mpz_inits(mod,half,inv3,res,bal,tmp,NULL);
 mpz_set_ui(mod,1); mpz_mul_2exp(mod,mod,N); mpz_set_ui(half,1); mpz_mul_2exp(half,half,N-1);
 mpz_set_ui(inv3,3); if(mpz_invert(inv3,inv3,mod)==0)return 3;
 mpz_powm_ui(res,inv3,S+1UL-START,mod);
 if(mpz_cmp(res,half)<=0) mpz_set(bal,res); else mpz_sub(bal,res,mod); // signed balanced
 unsigned long global_mb=ULONG_MAX, global_mr=START;
 unsigned long local_mb=ULONG_MAX, local_mr=START, local_start=START;
 for(unsigned long r=START;r<=END;r++){
   mpz_abs(tmp,bal); unsigned long bits=mpz_sgn(tmp)==0?1:mpz_sizeinbase(tmp,2);
   if(bits<global_mb){global_mb=bits;global_mr=r;}
   if(bits<local_mb){local_mb=bits;local_mr=r;}
   int boundary = CHUNK && ((r-local_start+1)>=CHUNK || r==END);
   if(boundary){printf("N=%lu chunk=%lu..%lu min_bits=%lu at_r=%lu\n",N,local_start,r,local_mb,local_mr); fflush(stdout); local_start=r+1; local_mb=ULONG_MAX; local_mr=r+1;}
   if(r<END){
     mpz_mul_ui(bal,bal,3);
     if(mpz_cmp(bal,half)>0) mpz_sub(bal,bal,mod);
     else { mpz_neg(tmp,half); if(mpz_cmp(bal,tmp)<0) mpz_add(bal,bal,mod); }
   }
 }
 if(!CHUNK) printf("N=%lu chunk=%lu..%lu min_bits=%lu at_r=%lu\n",N,START,END,global_mb,global_mr);
 fprintf(stderr,"GLOBAL N=%lu range=%lu..%lu min_bits=%lu at_r=%lu\n",N,START,END,global_mb,global_mr);
 mpz_clears(mod,half,inv3,res,bal,tmp,NULL); return 0;
}
