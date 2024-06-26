"""utility_functions"""
import numpy
from chess_enums import Player
from chess_enums import Space
from chess_enums import Piece
from chess_enums import W_LAST
from coord import Coord


def is_check_for_player(par_board: numpy.array, par_player: Player, par_king: Space):
    """based on the board fo a player is it check?"""
    coord = Coord.from_space(par_king)
    check = False

    # Check Horizontal and Vertical movements
    def h_and_v(par_space: Space):
        nonlocal check
        piece = par_board[par_space]
        if (piece != Piece.___ and to_player(piece) != par_player):
            if piece == Piece.W_R or piece == Piece.B_R or piece == Piece.W_Q or piece == Piece.B_Q:
                check = True
                return

            if (piece == Piece.W_K or piece == Piece.B_K):
                coord_king = Coord(par_space, 0) # REVISIT - todo uppercase causes lint
                if abs(coord.c - coord_king.c) + abs(coord.r - coord_king.r) == 1:
                    check = True
                    return

    for_each_space_horizontal_and_vertical(h_and_v, par_king, par_board)

    if check:
        return check

    # Check Diagonal movements
    def diag(par_space: Space):
        nonlocal check
        piece = par_board[par_space]
        if (piece != Piece.___ and to_player(piece) != par_player):
            if piece == Piece.W_B or piece == Piece.B_B or piece == Piece.W_Q or piece == Piece.B_Q:
                check = True
                return

            coord_piece = Coord(par_space, 0) # REVISIT
            if abs(coord.c - coord_piece.c) + abs(coord.r - coord_piece.r) == 2:
                if (piece == Piece.W_K or piece == Piece.B_K):
                    check = True
                    return
                if (piece == Piece.W_P or piece == Piece.B_P):
                    if ((par_player == Player.White and (coord_piece.r == coord.r + 1))
                        or (par_player == Player.Black and (coord_piece.r == coord.r - 1))):
                        check = True
                        return

    for_each_space_diagonal(diag, par_king, par_board)

    if check:
        return check

    def check_knight_moves(par_space: Space):
        """Check L movements"""
        nonlocal check
        piece = par_board[par_space]
        if (piece != Piece.___ and to_player(piece) != par_player):
            if (piece == Piece.W_N or piece == Piece.B_N):
                check = True
                return

    check_knight_moves(par_king)
    return check


def is_empty(par_piece):
    """is a piece empty"""
    result = par_piece == Piece.___
    return result


def is_opponent_piece(par_piece, par_player):
    """util is opponent piece"""
    if not is_piece(par_piece):
        return False

    result = to_player(par_piece) != par_player
    return result


def is_piece(par_piece):
    """util is piece"""
    result = not is_empty(par_piece)
    return result


def is_player_piece(par_piece, par_player):
    """util is player piece"""
    if not is_piece(par_piece):
        return False

    result = to_player(par_piece) == par_player
    return result


def for_each_space_horizontal_and_vertical(par_function, par_space: Space, par_board: numpy.array):
    """Check spaces horizonally and vertially aka rooks"""
    coord = Coord.from_space(par_space)

    for h in range(-1, 2):
        for v in range(-1, 2):
            if abs(h) + abs(v) != 1:
                continue

            dest = Coord(int(coord.c + h), int(coord.r + v))

            while  dest.is_valid():
                space = dest.to_space()
                par_function(space)

                if par_board[space] != Piece.___:
                    break

                dest.c += h
                dest.r += v


def for_each_space_diagonal(par_function, par_space: Space, par_board: numpy.array):
    """check diagonal spaces"""
    coord = Coord.from_space(par_space)

    for h in range(-1, 2, 2):
        for v in range(-1, 2, 2):
            dest = Coord(int(coord.c + h), int(coord.r + v))

            while dest.is_valid():
                space = dest.to_space()
                par_function(space)

                if par_board[space] != Piece.___:
                    break

                dest.c += h
                dest.r += v


def for_each_space_l(par_function, par_space: Space):
    """for each space"""
    coord = Coord.from_space(par_space)

    for c in range(-2, 3):
        for r in range(-2, 3):
            if (abs(c) + abs(r)) != 3:
                continue

            dest = Coord(coord.c + c, coord.r + r)

            if dest.is_valid():
                space = dest.to_space()
                par_function(space)


def to_player(par_piece: Piece) -> Player:
    """to_player"""
    assert par_piece != Piece.___
    return Player.White if par_piece <= W_LAST else Player.Black
