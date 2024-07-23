"""Chess puzzle data obtained from the Chess.com Published Data API"""

import urllib.request
import json
import io
# Python Chess Board Class: https://python-chess.readthedocs.io/en/latest/core.html#board
from dataclasses import dataclass
import chess
import chess.pgn


def obtain_latest_daily_puzzle():
    """Obtains the daily puzzle from the Chess.com Published Data API"""
    with urllib.request.urlopen("https://api.chess.com/pub/puzzle") as url:
        contents = url.read()
        deserialized_contents = json.loads(contents)
        return ChessPuzzle(**deserialized_contents)


def obtain_latest_random_puzzle():
    """Obtains a random puzzle from the Chess.com Published Data API"""
    with urllib.request.urlopen("https://api.chess.com/pub/puzzle/random") as url:
        contents = url.read()
        deserialized_contents = json.loads(contents)
        return ChessPuzzle(**deserialized_contents)


# Current board position is described with FEN (Forsyth–Edwards Notation) format
# Key notes for this format:
#  lowercase = black piece
#  uppercase = white piece
#  a integer represents the number of empty spaces until another piece or the end of the row
#  rows are seperated by '/'

@dataclass
class ChessPuzzle:
    """A class definition of the data obtained from the Chess.com Published Data API

       Important aspects of the data:
        -Board start state:                 ChessPuzzle.game.board()
        -Current Turn:                      ChessPuzzle.game.turn() (False = BLACK, True = WHITE)
        -Subsequent Moves (Iterable):       ChessPuzzle.game.mainline_moves
    """

# pylint: disable=too-many-arguments
    def __init__(self, title, url, publish_time, fen, pgn, image=None):
        print("Chess Puzzle: " + url)
        self.title = title
        self.url = url
        self.publish_time = publish_time
        self.fen = fen
        self.image = image
        self.game = self.convert_pgn_to_game(pgn)

    def convert_pgn_to_game(self, raw_pgn):
        """Converts raw pgn format to a Python Chess game type"""
        # Portable Game Notation (PGN) is used to describe subsequent moves
        string_io = io.StringIO(raw_pgn)
        game = chess.pgn.read_game(string_io)
        return game
