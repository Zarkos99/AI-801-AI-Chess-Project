import urllib.request
import json
import re
import UtilityFunctions
from ChessEnums import Player


def obtain_latest_daily_puzzle():
    contents = urllib.request.urlopen(
        "https://api.chess.com/pub/puzzle").read()
    deserialized_contents = json.loads(contents)
    return ChessPuzzle(**deserialized_contents)


def obtain_latest_random_puzzle():
    contents = urllib.request.urlopen(
        "https://api.chess.com/pub/puzzle/random").read()
    deserialized_contents = json.loads(contents)
    return ChessPuzzle(**deserialized_contents)


class ChessPuzzle():
    def __init__(self, title, url, publish_time, fen, pgn, image):
        self.title = title
        self.url = url
        self.publish_time = publish_time
        # Current board position is described with FEN (Forsyth–Edwards Notation) format
        # Key notes for this format:
        #   lowercase = black piece
        #   uppercase = white piece
        #   a integer represents the number of empty spaces until another piece or the end of the row
        #   rows are seperated by '/'
        self.fen_board_start = fen
        # Portable Game Notation (PGN) is used to describe subsequent moves
        self.raw_pgn = pgn
        self.solution = self.convertPgnToListOfMoves()

    def findColorToPlay(self):
        fen_color_to_play = self.fen_board_start.split(" ")[1]
        return Player.White if fen_color_to_play == "w" else Player.Black

    def convertPgnToListOfMoves(self):
        # Obtain last line in the pgn which contains the subsequent moves
        string_moves = self.raw_pgn.splitlines()[-1]
        # Remove double, and triple digit numbers followed by a period from the pgn movelist
        # Replace double spaces with single spaces
        # Remove the final score of "#-#"
        return re.sub(r'[0-9]+-[0-9]+', ' ', re.sub(r'  ', ' ', re.sub(
            r'[0-9]+[0-9]+.', '', re.sub(r'[0-9]+[0-9]+[0-9]+.', '', string_moves)))).strip().split(" ")


daily_puzzle_info = obtain_latest_daily_puzzle()

print(daily_puzzle_info.convertPgnToListOfMoves())
