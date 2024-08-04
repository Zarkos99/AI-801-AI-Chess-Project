"""Module providing the ChessPuzzleEnvironment class."""

from dataclasses import dataclass
from io import StringIO
from json import load
from os import listdir
from random import randrange

from chess.pgn import GameNode, read_game
from chess.svg import board
from IPython.display import display

from chess_puzzle import ChessPuzzle

@dataclass
class Environment:
    """Class representing an environment, which can be perceived and acted upon by an agent."""

    def __init__(self, puzzle_name: str = None):
        if puzzle_name is None:
            path = "puzzles"
            puzzle_list = listdir(path)
            random_puzzle_number = randrange(1, 1000)
            random_puzzle = puzzle_list[random_puzzle_number - 1]
            puzzle_name = path + "\\" + random_puzzle

        with open(puzzle_name, "r", encoding="utf-8") as f:
            deserialized_contents = load(f)

            self.__puzzle: ChessPuzzle = ChessPuzzle(**deserialized_contents)

        text_io = StringIO(self.__puzzle.pgn)

        self.__root: GameNode = read_game(text_io).root()
        self.gamenode: GameNode = self.__root
        self.display: bool = True

    def __call__(self) -> bool:
        if self.display:
            color = self.__root.turn()
            display(self.__puzzle.title)
            display(board(self.gamenode.board(), size=350, orientation=color))
            
            if self.gamenode.next():
                display("White to move" if color else "Black to move")
            else:
                display("Puzzle Complete!")

            self.display = False

        return self.gamenode.next()
