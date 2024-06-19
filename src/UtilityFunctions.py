from chess_enums import Player
from chess_enums import Space
from chess_enums import Piece
from chess_enums import W_LAST
import Coord
import numpy


def IsCheckForPlayer(par_board: numpy.array, par_player: Player, par_king: Space):
    coord = Coord(par_king)
    check = False

    # Check Horizontal and Vertical movements
    def h_and_v(par_space: Space):
        nonlocal check
        piece = par_board[par_space]
        if (piece != Piece.___ and ToPlayer(piece) != par_player):
            if (piece == Piece.W_R or piece == Piece.B_R or piece == Piece.W_Q or piece == Piece.B_Q):
                check = True
                return

            if (piece == Piece.W_K or piece == Piece.B_K):
                coord_king = Coord(par_space)

                if (abs(coord.c - coord_king.c) + abs(coord.r - coord_king.r) == 1):
                    check = True
                    return

    ForEachSpaceHorizontalAndVertical(h_and_v, par_board, par_king)

    if check:
        return check

    # Check Diagonal movements
    def diag(par_space: Space):
        nonlocal check
        piece = par_board[par_space]
        if (piece != Piece.___ and ToPlayer(piece) != par_player):
            if (piece == Piece.W_B or piece == Piece.B_B or piece == Piece.W_Q or piece == Piece.B_Q):
                check = True
                return

            coord_piece = Coord(par_space)
            if (abs(coord.c - coord_piece.c) + abs(coord.r - coord_piece.r) == 2):
                if (piece == Piece.W_K or piece == Piece.B_K):
                    check = True
                    return
                if (piece == Piece.W_P or piece == Piece.B_P):
                    if ((par_player == Player.White and (coord_piece.r == coord.r + 1)) or (par_player == Player.Black and (coord_piece.r == coord.r - 1))):
                        check = True
                        return

    ForEachSpaceDiagonal(diag, par_board, par_king)

    if check:
        return check

    # Check L movements
    def L(par_space: Space):
        nonlocal check
        piece = par_board[par_space]
        if (piece != Piece.___ and ToPlayer(piece) != par_player):
            if (piece == Piece.W_N or piece == Piece.B_N):
                check = True
                return

    ForEachSpaceL(L, par_king)
    return check


def ForEachSpaceHorizontalAndVertical(par_function, par_board: numpy.array, par_space: Space):
    coord = Coord(par_space)

    for h in range(-1, 2):
        for v in range(-1, 2):
            if abs(h) + abs(v) != 1:
                continue

            dest = Coord(int(coord.c + h), int(coord.r + v))
            while 0 <= dest.c and dest.c < 8 and 0 <= dest.r and dest.r < 8:
                space = dest()
                par_function(space)

                if (par_board[space] != Piece.___):
                    break

                dest.c += h
                dest.r += v


def ForEachSpaceDiagonal(par_function, par_board: numpy.array, par_space: Space):
    coord = Coord(par_space)

    for h in range(-1, 2, 2):
        for v in range(-1, 2, 2):
            dest = Coord(int(coord.c + h), int(coord.r + v))
            while 0 <= dest.c and dest.c < 8 and 0 <= dest.r and dest.r < 8:
                space = dest()
                par_function(space)

                if (par_board[space] != Piece.___):
                    break

                dest.c += h
                dest.r += v


def ForEachSpaceL(par_function, par_space: Space):
    coord = Coord(par_space)

    for c in range(-2, 3):
        for r in range(-2, 3):
            if (abs(c) + abs(r)) != 3:
                continue

            if (coord.c + c < 0 or coord.c + c >= 8
                    or coord.r + r < 0 or coord.r + r >= 8):
                continue

            space = Coord(coord.c + c, coord.r + r)
            par_function(space)


def ToPlayer(par_piece: Piece) -> Player:
    assert (par_piece != Piece.___)
    return Player.White if par_piece <= W_LAST else Player.Black
