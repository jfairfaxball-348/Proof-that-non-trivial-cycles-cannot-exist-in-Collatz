# RL313 lossless transport note

This connector-worker transition uses documented lossless transport rather than
a ZIP archive, matching the current repository protocol.

Authoritative incoming identity:

- base commit: `d65157eaf04a870c3e6ad4da21f33af8684c43c8`
- base tree: `f0665a4e073cd667da203187067cda0a1e0cb666`
- incoming target blob:
  `authoritative/RL313_DIVISOR_ALIGNED_BALANCED_DESCENT_TARGET.md`
  = `7c628693bf09b8584be8b5b041dc27ce10bd1a5b`
- incoming START_HERE blob:
  `fa01595adc03affa9d72a3fe2872feab3c460fe1`

The complete frozen RL313 generation is the set of files in `sessions/RL313/`
covered by `SHA256SUMS.txt`.

The successor authority is exactly the two files covered by
`RL313_SUCCESSOR_SHA256SUMS.txt`.

Fresh reconstruction procedure:

1. copy the hashed RL313 session files into an empty `sessions/RL313/`;
2. verify `SHA256SUMS.txt`;
3. run `python3 verify_rl313_closeout.py`;
4. reconstruct `authoritative/` from the two successor files only;
5. verify `RL313_SUCCESSOR_SHA256SUMS.txt`;
6. require successor number RL314 and no RL313 target remaining in
   `authoritative/`.

Knowledge catalogues are intentionally unchanged and `stale/deferred`.
