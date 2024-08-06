"""Module providing the ChessPuzzleEnvironment class."""

#from dataclasses import dataclass
#from io import StringIO
#from json import load
#from os import listdir
#from random import randrange
#from time import time
#
#from chess.pgn import read_game
#from chess.svg import board
#from IPython.display import clear_output, display
#
#from chess_puzzle import ChessPuzzle
#from environment import Environment
#
#TIME_LIMIT = 3.0
#
#@dataclass
#class ChessPuzzleEnvironment(Environment):
#    """Class representing a chess puzzle environment."""
#
#    def __init__(self, puzzle_name: str = None):
#        if puzzle_name is None:
#            path = "puzzles"
#            puzzle_list = listdir(path)
#            random_puzzle_number = randrange(1, 1000)
#            random_puzzle = puzzle_list[random_puzzle_number - 1]
#            puzzle_name = path + "\\" + random_puzzle
#
#        with open(puzzle_name, "r", encoding="utf-8") as f:
#            deserialized_contents = load(f)
#
#            self.__puzzle = ChessPuzzle(**deserialized_contents)
#
#        text_io = StringIO(self.__puzzle.pgn)
#
#        self.game = read_game(text_io)
#
#        color = self.game.turn()
#        display(self.__puzzle.title)
#        display(board(self.game.board(), size=350, orientation=color))
#        display("White to move" if color else "Black to move")
#        clear_output(wait=True)
#
#        self.time_remaining = TIME_LIMIT
#        self.__start_time = time()
#
#    def __call__(self) -> bool:
#        time_elapsed = time() - self.__start_time
#
#        self.time_remaining = time_elapsed < TIME_LIMIT
#
#        return True
