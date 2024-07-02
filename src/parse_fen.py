"""A UI FEN helper"""
from ChessEnums import Player
from ChessPiece import ChessPiece
import UtilityFunctions


def parse_fen(fen):
    rows = fen.split(' ')[0].split('/')
    board = []

    for row in rows:
        board_row = []
        for char in row:
            if char.isdigit():
                board_row.extend([None] * int(char))
            else:
                piece = UtilityFunctions.mapFenCharToPiece(char)
                board_row.append(ChessPiece(piece.piece_type, piece.color))
        board.append(board_row)

    return board
