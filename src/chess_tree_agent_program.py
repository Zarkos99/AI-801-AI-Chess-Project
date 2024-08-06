"""Module providing the ChessTreeAgentProgram class."""

from dataclasses import dataclass

from agent_program import AgentProgram
from chess_tree_action import ChessTreeAction
from chess_tree_percept import ChessTreePercept

@dataclass
class ChessTreeAgentProgram(AgentProgram):
    """Class representing a chess tree agent program."""

    def __call__(self, percept: ChessTreePercept) -> ChessTreeAction:
        assert 0

    best: ChessTreeAction = None
    current: ChessTreeAction = None
    finished: bool = False
