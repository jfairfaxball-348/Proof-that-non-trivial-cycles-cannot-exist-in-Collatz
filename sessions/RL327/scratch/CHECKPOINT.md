# Local RL checkpoint (NOT AUTHORITATIVE)

- BASE_HEAD: `f37a2984065548440a8ae0973060f97a40a44a2b`
- Current incoming RL: `RL327`
- Target: `authoritative/RL327_PARENT_BRIDGE_MECHANICAL_EXCESS_CONSUMER_TARGET.md`
- Last fully verified state: the consolidated owned-bridge, residue-weighted, and fixed-point bootstrap verifier plus independent red team both pass (2026-09-15T09:31:24Z).
- New result, proved analytic mathematics backed by exact finite certificates: for `n>=20390252058`, decompose `q_0,...,q_T` into zero runs (total `Z`) and positive runs (total `K`). Exact singleton ownership through combined zero length 47, exact two-positive bridge enumeration, and a 224-state/21,805-edge finite potential prove `Z<=24K+72`, hence `K>=ceil((T-71)/25)`.
- Singleton certificate range: every ordered pair `1<=z_left,z_right<=49` with total 47 through 98, every rational-mechanical factor, and every endpoint lift in `[2^71,2^76+2^36)`. After odd parity and high-carry minimality, candidate multiplicities are `{47:1034,48:342,49:106,50:35,51:10,52:1}` and zero above 52. Exact shared-state indexing leaves 5 links, represented conservatively by 4 ordered pair-type links.
- Two-positive certificate range: every ordered pair with total 47 through 98, both exhaustive positive shapes `0,1,1,0` and `0,2,1,0`, every factor, and every endpoint lift. High-carry multiplicities are `{47:468,48:163,49:62,50:20,51:4}` and zero above 51.
- Residue-weighted consequence: distinct residues `A*t mod ell` force more loss than the uniform coefficient estimate. A quartic rational exponential lower bound gives loss `>464841105.83030766` and the intermediate cap `n<=32603663706`.
- Fixed-point bootstrap: assuming `n>=32596612663`, the additional total-46 singleton layer leaves 2,414 owned endpoints, 187 pair types, and 9 exact links; the finite potential proves `19Z<=449K+1347`, hence `K>=5583403544`. Its weighted telescope gives `n<32596612662.03308`, contradicting the assumption. Therefore the final candidate cap is `n<=32596612662`, a contraction of `242678741` from RL326. Monotonicity covers all `rho>=60`; the companion inequality covers `rho<=59`.
- Classification: candidate theorem/certificate is locally fully verified but **NOT PROMOTED** until RL327 closeout.
- Corrections/demotions: none authoritative. A red team caught missing odd-parity filtering in an earlier scratch enumerator; all earlier scratch counts were discarded and every range was rerun with explicit parity. The repaired theorem, weighted consumer, and corrected total-46 bootstrap pass both verifier and red team.
- Stop-and-repair active: no.
- Next step: preserve the verified fixed-point checkpoint. Attempt a lower modulus layer only with the same parity/link audit; otherwise prepare closeout on user instruction.

This ignored directory is a resumability aid, never proof state or a promotion candidate.
