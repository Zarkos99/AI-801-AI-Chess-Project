"""Module providing the RationalAgent class."""

from dataclasses import dataclass

from chess import Board
from action import Action
from agent import Agent
# from agent_function import AgentFunction
# from performance_measure import PerformanceMeasure


def is_rational(_action: Action,
                # _performance_measure: PerformanceMeasure,
                _percept_sequence: Board,
                _actions: list[Action] = None,
                _prior_knowledge=None) -> bool:
    """What is rational at any given time depends on four things:\
       -The performance measure that defines the criterion of success.\
       -The agent's prior knowledge of the environment.\
       -The actions that the agent can perform.\
       -The agent's percept sequence to date."""


@dataclass
class RationalAgent(Agent):
    """Class representing a rational agent, which is an agent that does the right thing. For each\
       possible percept sequence, a rational agent should select an action that is expected to\
       maximize its performance measure, given the evidence provided by the percept sequence and\
       whatever built-in knowledge the agent has."""

    def __init_subclass__(cls):
        print('Hello Rational Agent')
        #agent_function = AgentFunction()
        #performance_measure = PerformanceMeasure()

        #for percept_sequence in agent_function.partial_table:
            #action = agent_function(percept_sequence)

            #assert is_rational(action, performance_measure, percept_sequence)
