from ChessEnums import Piece
from ChessEnums import Player
from ChessEnums import Space
import State
import Action
import Coord
import UtilityFunctions


def Result(par_state: State, par_action: Action):
    state = par_state
    orig = par_action.orig
    dest = par_action.dest
    piece_orig = par_state.board[par_action.orig]
    piece_dest = par_state.board[par_action.dest]
    player = par_state.player

    state.board[par_action.dest] = state.board[par_action.orig]
    state.board[par_action.orig] = Piece.___

    # En Pessant
    if ((piece_orig == Piece.W_P or piece_orig == Piece.B_P) and piece_dest == Piece.___ and orig.c != dest.c):
        space_captured_pawn = Coord(
            dest.c, dest.r - 1 if player == Player.White else dest.r + 1)

        assert state.board[space_captured_pawn] == (
            Piece.B_P if player == Player.White else Piece.W_P)
        state.board[space_captured_pawn] = Piece.___

    # Castle
    if ((piece_orig == Piece.W_K or piece_orig == Piece.B_K) and abs(orig.c - dest.c) == 2):
        match par_action.dest:
            case Space.C1:
                state.board[Space.A1] = Piece.___
                state.board[Space.D1] = Piece.W_R
            case Space.G1:
                state.board[Space.H1] = Piece.___
                state.board[Space.F1] = Piece.W_R
            case Space.C8:
                state.board[Space.A8] = Piece.___
                state.board[Space.D8] = Piece.B_R
            case Space.G8:
                state.board[Space.H8] = Piece.___
                state.board[Space.F8] = Piece.B_R

    # Promotion
    if ((piece_orig == Piece.W_P and dest.r == 7) or (piece_orig == Piece.B_P and dest.r == 0)):
        state.board[par_action.dest] = par_action.promotion

    state.moves.append(par_action)

    if (piece_orig == Piece.W_K):
        state.king_space[Player.White] = par_action.dest
        state.king_moved[Player.White] = True

    if (piece_orig == Piece.B_K):
        state.king_space[Player.Black] = par_action.dest
        state.king_moved[Player.Black] = True

    if (par_action.orig == Space.A1):
        state.rookA_moved[Player.White] = True
    if (par_action.orig == Space.A8):
        state.rookA_moved[Player.Black] = True
    if (par_action.orig == Space.H1):
        state.rookH_moved[Player.White] = True
    if (par_action.orig == Space.H8):
        state.rookH_moved[Player.Black] = True

    # Check
    king_space = state.king_space[player]
    state.check = UtilityFunctions.IsCheckForPlayer(
        state.board, player, king_space)

    return state
