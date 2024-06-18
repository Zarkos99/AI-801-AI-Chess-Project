"""Module providing core chess enums."""

from enum import Enum

Player = Enum('Player', ['White', 'Black'], start=0)

Piece = Enum('Piece', [
    '___',
    'W_P', 'W_N', 'W_B', 'W_R', 'W_Q', 'W_K',
    'B_P', 'B_N', 'B_B', 'B_R', 'B_Q', 'B_K',
], start = 0)

W_FIRST = Piece.W_P
W_LAST = Piece.W_K
B_FIRST = Piece.B_P
B_LAST = Piece.B_K

Space = Enum('Space', [
    'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
    'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
    'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8',
    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
    'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8',
    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
    'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8',
    'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8',
], start = 0)

def to_player(par_piece):
    """helper to_playeer"""
    assert par_piece != Piece.___

    if par_piece.value <= W_LAST.value:
        return Player.White
    else:
        return Player.Black
