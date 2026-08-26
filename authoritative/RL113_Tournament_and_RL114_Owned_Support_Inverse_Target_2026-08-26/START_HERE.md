# RL113 authoritative start — tournament result and RL114 kickoff

Read in this order:

1. `RL112_TO_RL113_TOURNAMENT_AND_AUDIT.md`;
2. `RL113_RL114_OWNED_SUPPORT_INVERSE_TARGET.md`;
3. `audit/TOURNAMENT_LEDGER.md` and `audit/ROUTE_CARDS.md`;
4. `verification/verify_rl113_tournament.py`.

RL113 completes the required twelve-route tournament. It makes no Gate closure
claim. Its winner is the owned-support inverse route, and RL114 is authorized
to work only on its stated first proof obligation. The ordered fallback ledger
is binding: a route that closes, fails, or is blocked is not silently retried
ahead of the next viable entry.
