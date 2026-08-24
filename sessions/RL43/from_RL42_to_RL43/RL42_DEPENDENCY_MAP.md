# RL42 dependency map

## Final retained conclusion

`rho >= 49`

### Dependency chain

1. **Inherited exact branch framework**
   - near-resonant order-2 / `g=2` balanced-return branch;
   - `z=2^a/3^ell>1`, `z^2<16/15`;
   - endpoint ownership `4|G`;
   - exact ordered-rank numerator identity;
   - common-prefix / gap boundary facts used by the equality DP.

2. **RL42 moved-rank and prefix machinery**
   - ordered moved ranks encode excursion-owned odd mass;
   - `rho=sum |i_m-j_m|`;
   - prefix cap `2^(i_m)/3^(m-1)<=z^2`.

3. **RL42 transport-efficiency theorem**
   - `M_eff >= 3(z+1)G/z^2`;
   - `M_eff <= rho/2`;
   - therefore `rho>(45/4)G`;
   - with `4|G`, `rho>=46`.

4. **RL42 bounded crossing-excess certificate**
   - no physical sign-changing positive excursion with `e<=3`, `p<=47`;
   - under `rho<=47`, mandatory crossing has `e>=4`;
   - refined pointwise pricing gives `M_eff<=rho/2-1`;
   - therefore `rho>=48`.

5. **RL42 rho=48 equality certificate**
   - equality forces `G=4`, `P=P_+=44`, total excess `E=4`;
   - one `e=4` crossing, all other excursions `e=0`;
   - all local `e=4` crossings are `1->-4`;
   - safe boundary DP has zero near-resonant terminal endpoints;
   - therefore `rho!=48`.

6. **Conclusion**
   - `rho>=49`.

## Non-dependencies

The final chain does not require:

- the missing RL41 billion-scale area-26/27 transient tables;
- an infinite classification of all `e<=3` crossing excursions;
- the exploratory, not-yet-frozen `rho=49` search.
