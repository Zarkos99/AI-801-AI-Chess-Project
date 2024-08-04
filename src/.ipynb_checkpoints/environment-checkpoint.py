"""Module providing the Environment class."""

from dataclasses import dataclass
from io import StringIO
from json import loads
from time import time
from urllib.request import urlopen

from chess.pgn import read_game
from chess.svg import board
from IPython.display import display

@dataclass
class Environment:
    """Class representing an environment, which can be perceived and acted upon by an agent."""

    @dataclass
    class Puzzle:
        """Class representing a puzzle, in the format specified by the source (chess.com)."""
        title: str
        url: str
        publish_time: int
        fen: str
        pgn: str
        image: str

    def __init__(self):
        with urlopen("https://api.chess.com/pub/puzzle") as url:
            s = url.read()
            deserialized_contents = loads(s)

            self.__puzzle = self.Puzzle(**deserialized_contents)

            text_io = StringIO(self.__puzzle.pgn)

            self.__game = read_game(text_io)

            display(board(self.__game.board(), size=350))

            print("White to move" if self.__game.turn() else "Black to move")
            print(self.__puzzle.url)
            self.__start_time = time()

    def __call__(self) -> bool:
        current_time = time()
        time_elapsed = current_time - self.__start_time

        #print("\rTimer: ", time_elapsed, end="\r")
        print(time_elapsed)
        return time_elapsed < 1
