"""Module providing the Game class."""

from dataclasses import dataclass, field

from player import Player
from problem import Problem
from terminal_test import TerminalTest
from utility_function import UtilityFunction

@dataclass
class Game(Problem):
    """Class representing a game, which is a kind of search problem."""

    player: Player = field(default_factory=Player)
    terminal_test: TerminalTest = field(default_factory=TerminalTest)
    utility: UtilityFunction = field(default_factory=UtilityFunction)
