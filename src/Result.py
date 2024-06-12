import chess_enums
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
    state.board[par_action.orig] = chess_enums.Piece.___

    # En Pessant
    if ((piece_orig == chess_enums.Piece.W_P or piece_orig == chess_enums.Piece.B_P) and piece_dest == chess_enums.Piece.___ and orig.c != dest.c):
        space_captured_pawn = Coord(
            dest.c, dest.r - 1 if player == chess_enums.Player.White else dest.r + 1)

        assert state.board[space_captured_pawn] == (
            chess_enums.Piece.B_P if player == chess_enums.Player.White else chess_enums.Piece.W_P)
        state.board[space_captured_pawn] = chess_enums.Piece.___

    # Castle
    if ((piece_orig == chess_enums.Piece.W_K or piece_orig == chess_enums.Piece.B_K) and abs(orig.c - dest.c) == 2):
        match par_action.dest:
            case chess_enums.Space.C1:
                state.board[chess_enums.Space.A1] = chess_enums.Piece.___
                state.board[chess_enums.Space.D1] = chess_enums.Piece.W_R
            case chess_enums.Space.G1:
                state.board[chess_enums.Space.H1] = chess_enums.Piece.___
                state.board[chess_enums.Space.F1] = chess_enums.Piece.W_R
            case chess_enums.Space.C8:
                state.board[chess_enums.Space.A8] = chess_enums.Piece.___
                state.board[chess_enums.Space.D8] = chess_enums.Piece.B_R
            case chess_enums.Space.G8:
                state.board[chess_enums.Space.H8] = chess_enums.Piece.___
                state.board[chess_enums.Space.F8] = chess_enums.Piece.B_R

    # Promotion
    if ((piece_orig == chess_enums.Piece.W_P and dest.r == 7) or (piece_orig == chess_enums.Piece.B_P and dest.r == 0)):
        state.board[par_action.dest] = par_action.promotion

    state.moves.push_back(par_action)

    if (piece_orig == chess_enums.Piece.W_K):
        state.king_space[chess_enums.Player.White] = par_action.dest
        state.king_moved[chess_enums.Player.White] = True

    if (piece_orig == chess_enums.Piece.B_K):
        state.king_space[chess_enums.Player.Black] = par_action.dest
        state.king_moved[chess_enums.Player.Black] = True

    if (par_action.orig == chess_enums.Space.A1):
        state.rookA_moved[chess_enums.Player.White] = True
    if (par_action.orig == chess_enums.Space.A8):
        state.rookA_moved[chess_enums.Player.Black] = True
    if (par_action.orig == chess_enums.Space.H1):
        state.rookH_moved[chess_enums.Player.White] = True
    if (par_action.orig == chess_enums.Space.H8):
        state.rookH_moved[chess_enums.Player.Black] = True

    # Check
    king_space = state.king_space[player]
    state.check = UtilityFunctions.IsCheckForPlayer(
        state.board, player, king_space)

    return state
