import unittest
from g10_contract import (
    MetaState, apply_metadata_transition, automatic_after_move,
    can_claim_fifty_by_move, can_claim_threefold_by_successor, rep_key
)

EMPTYISH_A = "K" + "."*62 + "k"
EMPTYISH_B = ".K" + "."*60 + "k."
EMPTYISH_C = "..K" + "."*58 + "k.."

class ContractTests(unittest.TestCase):
    def make(self, board=EMPTYISH_A, turn="w", rights="KQkq", hm=0, counts=None):
        k = rep_key(board, turn, rights, None)
        return MetaState.make(board, turn, rights, None, hm, counts or {k: 1})

    def test_quiet_move_increments_halfmove_and_history(self):
        s = self.make(rights="")
        t = apply_metadata_transition(s, successor_board64=EMPTYISH_B, successor_turn="b",
            successor_castling_rights="", successor_ep_effective=None,
            is_pawn_move=False, is_capture=False)
        self.assertEqual(t.halfmove_clock, 1)
        self.assertEqual(len(t.rep_counts), 2)
        self.assertEqual(t.current_occurrences, 1)

    def test_pawn_move_is_repetition_barrier_and_resets_halfmove(self):
        s = self.make(rights="", hm=73)
        t = apply_metadata_transition(s, successor_board64=EMPTYISH_B, successor_turn="b",
            successor_castling_rights="", successor_ep_effective=None,
            is_pawn_move=True, is_capture=False)
        self.assertEqual(t.halfmove_clock, 0)
        self.assertEqual(t.rep_counts, ((t.repetition_key, 1),))

    def test_capture_is_repetition_barrier(self):
        s = self.make(rights="", hm=40)
        t = apply_metadata_transition(s, successor_board64=EMPTYISH_B, successor_turn="b",
            successor_castling_rights="", successor_ep_effective=None,
            is_pawn_move=False, is_capture=True)
        self.assertEqual(t.halfmove_clock, 0)
        self.assertEqual(t.current_occurrences, 1)
        self.assertEqual(len(t.rep_counts), 1)

    def test_castling_right_loss_is_barrier_but_not_halfmove_reset(self):
        s = self.make(rights="KQ", hm=17)
        t = apply_metadata_transition(s, successor_board64=EMPTYISH_B, successor_turn="b",
            successor_castling_rights="Q", successor_ep_effective=None,
            is_pawn_move=False, is_capture=False)
        self.assertEqual(t.halfmove_clock, 18)
        self.assertEqual(len(t.rep_counts), 1)

    def test_castling_right_cannot_restore(self):
        s = self.make(rights="Q")
        with self.assertRaises(ValueError):
            apply_metadata_transition(s, successor_board64=EMPTYISH_B, successor_turn="b",
                successor_castling_rights="KQ", successor_ep_effective=None,
                is_pawn_move=False, is_capture=False)

    def test_threefold_now(self):
        s0 = self.make(rights="")
        k = s0.repetition_key
        s = MetaState.make(s0.board64, s0.turn, "", None, 10, {k: 3})
        self.assertTrue(s.can_claim_threefold_now())

    def test_threefold_by_intended_move(self):
        s = self.make(rights="")
        target_key = rep_key(EMPTYISH_B, "b", "", None)
        s = MetaState.make(s.board64, s.turn, "", None, 10,
                           {s.repetition_key: 1, target_key: 2})
        t = MetaState.make(EMPTYISH_B, "b", "", None, 11,
                           {s.repetition_key: 1, target_key: 3})
        self.assertTrue(can_claim_threefold_by_successor(s, t, barrier=False))
        self.assertFalse(can_claim_threefold_by_successor(s, t, barrier=True))

    def test_fifty_move_claim_now_and_by_move(self):
        s = self.make(rights="", hm=100)
        self.assertTrue(s.can_claim_fifty_now())
        p = self.make(rights="", hm=99)
        self.assertTrue(can_claim_fifty_by_move(p, is_pawn_move=False, is_capture=False))
        self.assertFalse(can_claim_fifty_by_move(p, is_pawn_move=True, is_capture=False))

    def test_fivefold_automatic(self):
        s0 = self.make(rights="")
        k = s0.repetition_key
        s = MetaState.make(s0.board64, s0.turn, "", None, 50, {k: 5})
        self.assertEqual(automatic_after_move(is_checkmate=False, is_stalemate=False,
            is_dead=False, successor=s), "FIVEFOLD_DRAW")

    def test_seventy_five_automatic(self):
        s = self.make(rights="", hm=150)
        self.assertEqual(automatic_after_move(is_checkmate=False, is_stalemate=False,
            is_dead=False, successor=s), "SEVENTY_FIVE_MOVE_DRAW")

    def test_checkmate_precedes_75_move(self):
        s = self.make(rights="", hm=150)
        self.assertEqual(automatic_after_move(is_checkmate=True, is_stalemate=False,
            is_dead=False, successor=s), "CHECKMATE")

if __name__ == "__main__":
    unittest.main(verbosity=2)
