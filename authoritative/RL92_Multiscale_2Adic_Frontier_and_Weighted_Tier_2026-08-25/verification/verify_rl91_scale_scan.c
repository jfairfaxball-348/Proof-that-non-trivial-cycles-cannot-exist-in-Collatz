#include <gmp.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){
 if(argc<4){fprintf(stderr,"usage: N start end\n");return 2;}
 unsigned long N=strtoul(argv[1],0,10), START=strtoul(argv[2],0,10), END=strtoul(argv[3],0,10);
 const unsigned long S=26594276905UL;
 if(END>S+1){fprintf(stderr,"range too high\n"); return 2;}
 mpz_t mod,inv3,res,alt,bal; mpz_inits(mod,inv3,res,alt,bal,NULL);
 mpz_set_ui(mod,1); mpz_mul_2exp(mod,mod,N); mpz_set_ui(inv3,3); if(mpz_invert(inv3,inv3,mod)==0) return 3;
 mpz_powm_ui(res,inv3,S+1UL-START,mod);
 unsigned long mb=~0UL,mr=START;
 for(unsigned long r=START;r<=END;r++){
   mpz_sub(alt,mod,res); if(mpz_cmp(res,alt)<=0) mpz_set(bal,res); else mpz_set(bal,alt);
   unsigned long bits=mpz_sizeinbase(bal,2); if(bits<mb){mb=bits;mr=r;}
   if(r<END){mpz_mul_ui(res,res,3); mpz_fdiv_r_2exp(res,res,N);} }
 printf("N=%lu chunk=%lu..%lu min_bits=%lu at_r=%lu\n",N,START,END,mb,mr);
 mpz_clears(mod,inv3,res,alt,bal,NULL); return 0; }
