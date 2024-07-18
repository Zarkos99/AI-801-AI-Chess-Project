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
    piece_orig = par_state.board[par_action.orig.value]
    piece_dest = par_state.board[par_action.dest.value]
    player = par_state.player

    state.board[par_action.dest.value] = state.board[par_action.orig.value]
    state.board[par_action.orig.value] = ChessPiece()

    # En Passant
    if piece_orig.piece_type == Piece_Type.PAWN and piece_dest.piece_type == Piece_Type.___ and orig.c != dest.c:
        space_captured_pawn = Coord(dest.c, dest.r - 1 if player == Player.WHITE else dest.r + 1)
        assert state.board[space_captured_pawn.toSpace().value].piece_type == Piece_Type.PAWN
        state.board[space_captured_pawn.toSpace().value] = ChessPiece()

    # Castling
    if piece_orig.piece_type == Piece_Type.KING and abs(orig.c - dest.c) == 2:
        if par_action.dest == Space.C1:
            state.board[Space.A1.value] = ChessPiece()
            state.board[Space.D1.value] = ChessPiece(Piece_Type.ROOK, Player.WHITE)
        elif par_action.dest == Space.G1:
            state.board[Space.H1.value] = ChessPiece()
            state.board[Space.F1.value] = ChessPiece(Piece_Type.ROOK, Player.WHITE)
        elif par_action.dest == Space.C8:
            state.board[Space.A8.value] = ChessPiece()
            state.board[Space.D8.value] = ChessPiece(Piece_Type.ROOK, Player.BLACK)
        elif par_action.dest == Space.G8:
            state.board[Space.H8.value] = ChessPiece()
            state.board[Space.F8.value] = ChessPiece(Piece_Type.ROOK, Player.BLACK)

    # Promotion
    if piece_orig.piece_type == Piece_Type.PAWN and (dest.r == 7 or dest.r == 0):
        state.board[par_action.dest.value] = ChessPiece(par_action.promotion, player)

    state.moves.append(par_action)

    if piece_orig.piece_type == Piece_Type.KING:
        state.king_space[player.value] = par_action.dest
        state.king_moved[player.value] = True

    if par_action.orig == Space.A1:
        state.rookA_moved[Player.WHITE.value] = True
    if par_action.orig == Space.A8:
        state.rookA_moved[Player.BLACK.value] = True
    if par_action.orig == Space.H1:
        state.rookH_moved[Player.WHITE.value] = True
    if par_action.orig == Space.H8:
        state.rookH_moved[Player.BLACK.value] = True

    # Check
    king_space = state.king_space[player.value]
    state.check = UtilityFunctions.IsCheckForPlayer(state.board, player, king_space)

    return state
