"""Executable metadata/reference layer for G10.RULES.v1.0.

This module intentionally does NOT implement chess move generation. G11 owns two
independent move generators. G10 freezes the state/history/terminal contract that
those implementations must conform to.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Iterable, Tuple

CASTLE_ORDER = "KQkq"


def normalize_rights(rights: Iterable[str]) -> str:
    s = set(rights)
    unknown = s.difference(CASTLE_ORDER)
    if unknown:
        raise ValueError(f"unknown castling rights: {sorted(unknown)}")
    return "".join(ch for ch in CASTLE_ORDER if ch in s)


def rep_key(board64: str, turn: str, castling_rights: str, ep_effective: str | None) -> str:
    if len(board64) != 64:
        raise ValueError("board64 must be 64 characters")
    if turn not in ("w", "b"):
        raise ValueError("turn must be w or b")
    rights = normalize_rights(castling_rights)
    ep = ep_effective or "-"
    return f"REP1|{board64}|{turn}|{rights or '-'}|{ep}"


@dataclass(frozen=True)
class MetaState:
    board64: str
    turn: str
    castling_rights: str
    ep_effective: str | None
    halfmove_clock: int
    rep_counts: Tuple[Tuple[str, int], ...]

    @staticmethod
    def make(board64: str, turn: str, castling_rights: str, ep_effective: str | None,
             halfmove_clock: int, rep_counts: Dict[str, int]) -> "MetaState":
        if halfmove_clock < 0:
            raise ValueError("negative halfmove clock")
        clean = tuple(sorted((k, int(v)) for k, v in rep_counts.items() if int(v) > 0))
        return MetaState(board64, turn, normalize_rights(castling_rights), ep_effective,
                         int(halfmove_clock), clean)

    @property
    def repetition_key(self) -> str:
        return rep_key(self.board64, self.turn, self.castling_rights, self.ep_effective)

    @property
    def counts(self) -> Dict[str, int]:
        return dict(self.rep_counts)

    @property
    def current_occurrences(self) -> int:
        return self.counts.get(self.repetition_key, 0)

    def can_claim_threefold_now(self) -> bool:
        return self.current_occurrences >= 3

    def can_claim_fifty_now(self) -> bool:
        return self.halfmove_clock >= 100


def apply_metadata_transition(
    state: MetaState,
    *,
    successor_board64: str,
    successor_turn: str,
    successor_castling_rights: str,
    successor_ep_effective: str | None,
    is_pawn_move: bool,
    is_capture: bool,
) -> MetaState:
    """Apply only G10 history metadata after a separately validated legal board move."""
    new_rights = normalize_rights(successor_castling_rights)
    old_rights = normalize_rights(state.castling_rights)
    if not set(new_rights).issubset(set(old_rights)):
        raise ValueError("castling rights cannot be restored")
    rights_reduced = new_rights != old_rights
    halfmove = 0 if (is_pawn_move or is_capture) else state.halfmove_clock + 1
    new_key = rep_key(successor_board64, successor_turn, new_rights, successor_ep_effective)
    if is_pawn_move or is_capture or rights_reduced:
        counts = {new_key: 1}
    else:
        counts = state.counts
        counts[new_key] = counts.get(new_key, 0) + 1
    return MetaState.make(successor_board64, successor_turn, new_rights,
                          successor_ep_effective, halfmove, counts)


def can_claim_threefold_by_successor(state: MetaState, successor: MetaState, *, barrier: bool) -> bool:
    """Claim by intended move: the move is named but not executed.

    A repetition barrier can never create a third occurrence of a pre-barrier key.
    """
    if barrier:
        return False
    before = state.counts.get(successor.repetition_key, 0)
    return before >= 2


def can_claim_fifty_by_move(state: MetaState, *, is_pawn_move: bool, is_capture: bool) -> bool:
    return (not is_pawn_move) and (not is_capture) and state.halfmove_clock + 1 >= 100


def automatic_after_move(*, is_checkmate: bool, is_stalemate: bool, is_dead: bool,
                         successor: MetaState) -> str | None:
    """Return canonical terminal label after a legal move, or None if active.

    Deadness and legal board terminals are supplied by the G11/G12 legality/deadness layer.
    """
    if is_checkmate:
        return "CHECKMATE"
    if is_stalemate:
        return "STALEMATE_DRAW"
    if is_dead:
        return "DEAD_POSITION_DRAW"
    if successor.current_occurrences >= 5:
        return "FIVEFOLD_DRAW"
    if successor.halfmove_clock >= 150:
        return "SEVENTY_FIVE_MOVE_DRAW"
    return None
