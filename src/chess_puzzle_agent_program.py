"""Module providing the ChessPuzzleAgentProgram class."""

from dataclasses import dataclass

from agent_program import AgentProgram
from chess_puzzle_action import ChessPuzzleAction
from chess_puzzle_percept import ChessPuzzlePercept

@dataclass
class ChessPuzzleAgentProgram(AgentProgram):
    """Class representing a chess puzzle agent program."""

    def __init__(self):
        #sensors = ChessTreeSensors()
        #actuators = ChessTreeActuators()
        #architecture = Architecture(sensors, actuators)
        #agent_program = ChessTreeAgentProgram()
        #
        #self.__chess_tree_agent = Agent(architecture, agent_program)
        pass

    def __call__(self, percept: ChessPuzzlePercept) -> ChessPuzzleAction:
        #if percept.knowledge is None:
        #    percept.knowledge = ChessTreeEnvironment(percept.state)
        #
        #self.__chess_tree_agent(percept.knowledge)
        #
        #agent_program: ChessTreeAgentProgram = self.__chess_tree_agent._agent_program
        #
        #if agent_program.finished or not percept.time_remaining:
        #    action = ChessPuzzleAction(move=agent_program.best.move, thinking=False)
        #else:
        #    action = ChessPuzzleAction(move=agent_program.current.move, thinking=True)
        #
        #return action
        pass
