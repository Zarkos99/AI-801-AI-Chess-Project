"""Module providing the Percept class."""

from dataclasses import dataclass
from chess import Board, __doc__ as chess_doc


@dataclass
class Percept:
    """Class representing a percept, which is the agent's perceptual inputs at any given instant."""

    __doc__ = chess_doc

    # pylint: disable=too-many-arguments
    def __init__(self, board: Board):
        self.board = board
        # Legal Moves
        self.is_legal_move = board.is_legal
        self.legal_moves = board.legal_moves
        # Attacks
        self.attackers = board.attackers
        self.attacks = board.attacks
        # Castling Rights
        self.has_castling_rights = board.has_castling_rights
        self.castling_rights = board.castling_rights
        self.is_move_castling = board.is_castling
        # Promotion
        self.promoted_pieces = board.promoted
        # Check conditions
        self.is_in_check = board.is_check
        self.gives_check = board.gives_check
        # Has legal en passant
        self.is_move_en_passant = board.is_en_passant
        self.has_legal_en_passant = board.has_legal_en_passant
        # Can claim draws
        self.can_claim_draw = board.can_claim_draw
        self.can_claim_fifty_moves = board.can_claim_fifty_moves
        self.can_claim_threefold_repetition = board.can_claim_threefold_repetition
        # Outcome
        self.move_outcome = board.outcome
