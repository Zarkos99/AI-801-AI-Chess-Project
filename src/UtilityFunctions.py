from ChessEnums import Player, Space, Piece_Type, Piece_Type_LAST
from ChessPiece import ChessPiece
from Coord import Coord
import numpy


def IsCheckForPlayer(par_board: numpy.array, par_player: Player, par_king: Space):
    coord = Coord.fromSpace(par_king)
    check = False

    # Check Horizontal and Vertical movements
    def h_and_v(par_space: Space):
        nonlocal check
        piece = par_board[par_space]
        if (piece != Piece_Type.___ and ToPlayer(piece) != par_player):
            if (piece == Piece_Type.ROOK or piece == Piece_Type.QUEEN):
                check = True
                return

            if (piece == Piece_Type.KING):
                coord_king = Coord.fromSpace(par_space)

                if (abs(coord.c - coord_king.c) + abs(coord.r - coord_king.r) == 1):
                    check = True
                    return

    ForEachSpaceHorizontalAndVertical(h_and_v, par_king, par_board)

    if check:
        return check

    # Check Diagonal movements
    def diag(par_space: Space):
        nonlocal check
        piece = par_board[par_space]
        if (piece != Piece_Type.___ and ToPlayer(piece) != par_player):
            if (piece == Piece_Type.BISHOP or piece == Piece_Type.QUEEN):
                check = True
                return

            coord_piece = Coord.fromSpace(par_space)
            if (abs(coord.c - coord_piece.c) + abs(coord.r - coord_piece.r) == 2):
                if (piece == Piece_Type.KING):
                    check = True
                    return
                if (piece == Piece_Type.PAWN):
                    if ((par_player == Player.WHITE and (coord_piece.r == coord.r + 1)) or (par_player == Player.BLACK and (coord_piece.r == coord.r - 1))):
                        check = True
                        return

    ForEachSpaceDiagonal(diag, par_king, par_board)

    if check:
        return check

    # Check L movements
    def L(par_space: Space):
        nonlocal check
        piece = par_board[par_space]
        if (piece != Piece_Type.___ and ToPlayer(piece) != par_player):
            if (piece == Piece_Type.KNIGHT):
                check = True
                return

    ForEachSpaceL(L, par_king)
    return check


def IsEmpty(par_piece):
    is_empty = par_piece == Piece_Type.___

    return is_empty


def IsOpponentPiece(par_piece, par_player):
    if not IsPiece(par_piece):
        return False

    is_opponent_piece = ToPlayer(par_piece) != par_player

    return is_opponent_piece


def IsPiece(par_piece):
    is_piece = not IsEmpty(par_piece)

    return is_piece


def IsPlayerPiece(par_piece, par_player):
    if not IsPiece(par_piece):
        return False

    is_player_piece = ToPlayer(par_piece) == par_player

    return is_player_piece


def ForEachSpaceHorizontalAndVertical(par_function, par_space: Space, par_board: numpy.array):
    coord = Coord.fromSpace(par_space)

    for h in range(-1, 2):
        for v in range(-1, 2):
            if abs(h) + abs(v) != 1:
                continue

            dest = Coord(int(coord.c + h), int(coord.r + v))

            while dest.isValid():
                space = dest.toSpace()
                par_function(space)

                if (par_board[space] != Piece_Type.___):
                    break

                dest.c += h
                dest.r += v


def ForEachSpaceDiagonal(par_function, par_space: Space, par_board: numpy.array):
    coord = Coord.fromSpace(par_space)

    for h in range(-1, 2, 2):
        for v in range(-1, 2, 2):
            dest = Coord(int(coord.c + h), int(coord.r + v))

            while dest.isValid():
                space = dest.toSpace()
                par_function(space)

                if (par_board[space] != Piece_Type.___):
                    break

                dest.c += h
                dest.r += v


def ForEachSpaceL(par_function, par_space: Space, par_board: numpy.array = []):
    coord = Coord.fromSpace(par_space)

    for c in range(-2, 3):
        for r in range(-2, 3):
            if (abs(c) + abs(r)) != 3:
                continue

            dest = Coord(coord.c + c, coord.r + r)

            if dest.isValid():
                space = dest.toSpace()
                par_function(space)


def ToPlayer(par_piece: Piece_Type) -> Player:
    assert (par_piece != Piece_Type.___)
    return Player.WHITE if par_piece <= Piece_Type_LAST else Player.BLACK


def mapFenCharToPiece(char: str):
    """Parse a FEN (Forsyth-Edwards Notation) string into a piece"""
    piece_mapping = {'p': Piece_Type.PAWN, 'r': Piece_Type.ROOK, 'n': Piece_Type.KNIGHT,
                     'b': Piece_Type.BISHOP, 'q': Piece_Type.QUEEN, 'k': Piece_Type.KING}

    return ChessPiece(piece_mapping[char.lower()], Player.WHITE if char.isupper() else Player.BLACK)


def mapPgnCharToPiece(char, player):
    """Parse a PGN (Portable Game Notation) string into a piece"""
    piece_mapping = {
        'P': [Piece_Type.PAWN,  Piece_Type.B_P], 'R': [Piece_Type.ROOK, Piece_Type.B_R], 'N': [Piece_Type.KNIGHT, Piece_Type.B_N], 'B': [Piece_Type.W_B, Piece_Type.B_B], 'Q': [Piece_Type.W_Q, Piece_Type.B_Q], 'K': [Piece_Type.KING, Piece_Type.B_K]
    }
    return piece_mapping[char][0] if player == Player.WHITE else piece_mapping[char][1]
