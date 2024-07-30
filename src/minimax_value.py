"""Module providing the MinimaxValue class."""

from dataclasses import dataclass, field

from actions import Actions
from node import Node
from player import Player
from state import State
from terminal_test import TerminalTest
from transition_model import TransitionModel
from utility_function import UtilityFunction

@dataclass
class MinimaxValue:
    """Class representing the minimax value of a node, which is the utility of being in the\
       corresponding state, assuming that both players play optimally from there to the end of the\
       game."""

    def __call__(self, n: Node) -> float:
        minimax = self.__minimax(n.state)

        return minimax

    def __minimax(self, s: State) -> float:
        if self.__terminal_test(s):
            return self.__utility(s)

        if s.turn is self.__max:
            return max(self.__minimax(self.__result(s, a)) for a in self.__actions(s))

        if s.turn is self.__min:
            return min(self.__minimax(self.__result(s, a)) for a in self.__actions(s))

        assert False
        return 0.0

    __utility: UtilityFunction = field(default_factory=UtilityFunction)
    __terminal_test: TerminalTest = field(default_factory=TerminalTest)
    __actions: Actions = field(default_factory=Actions)
    __result: TransitionModel = field(default_factory=TransitionModel)
    __max: Player = field(default_factory=Player)
    __min: Player = field(default_factory=Player)
