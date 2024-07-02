from ChessPiece import ChessPiece
from ChessEnums import Piece_Type, Player, Space
from State import State
from Action import Action
from Coord import Coord
import UtilityFunctions


def Result(par_state: State, par_action: Action):
    state = par_state
    orig = Coord.fromSpace(par_action.orig)
    dest = Coord.fromSpace(par_action.dest)
    piece_orig = par_state.board[par_action.orig]
    piece_dest = par_state.board[par_action.dest]
    player = par_state.player

    state.board[par_action.dest] = state.board[par_action.orig]
    state.board[par_action.orig] = ChessPiece()

    # En Pessant
    if ((piece_orig == Piece_Type.PAWN) and piece_dest == Piece_Type.___ and orig.c != dest.c):
        space_captured_pawn = Coord(
            dest.c, dest.r - 1 if player == Player.White else dest.r + 1)

        assert state.board[space_captured_pawn] == (
            Piece_Type.PAWN if player == Player.White else Piece_Type.PAWN)
        state.board[space_captured_pawn] = Piece_Type.___

    # Castle
    if ((piece_orig == Piece_Type.KING) and abs(orig.c - dest.c) == 2):
        match par_action.dest:
            case Space.C1:
                state.board[Space.A1] = Piece_Type.___
                state.board[Space.D1] = Piece_Type.ROOK
            case Space.G1:
                state.board[Space.H1] = Piece_Type.___
                state.board[Space.F1] = Piece_Type.ROOK
            case Space.C8:
                state.board[Space.A8] = Piece_Type.___
                state.board[Space.D8] = Piece_Type.ROOK
            case Space.G8:
                state.board[Space.H8] = Piece_Type.___
                state.board[Space.F8] = Piece_Type.ROOK

    # Promotion
    if ((piece_orig == Piece_Type.PAWN and dest.r == 7) or (piece_orig == Piece_Type.PAWN and dest.r == 0)):
        state.board[par_action.dest] = par_action.promotion

    state.moves.append(par_action)

    if (piece_orig == Piece_Type.KING):
        state.king_space[Player.White] = par_action.dest
        state.king_moved[Player.White] = True

    if (piece_orig == Piece_Type.KING):
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
