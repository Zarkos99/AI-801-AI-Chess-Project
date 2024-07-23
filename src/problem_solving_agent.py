"""Module providing the ProblemSolvingAgent class."""

from dataclasses import dataclass, field

from action import Action
from agent_program import AgentProgram
from atomic_representation import AtomicRepresentation
from goal import Goal
from percept import Percept
from problem import Problem
from search import search

@dataclass
class ProblemSolvingAgent(AgentProgram):
    """Class representing a problem-solving agent, which is one kind of goal-based agent that uses\
       atomic representations (that is, states of the world are considered as wholes, with no\
       internal structure visible to the problem-solving algorithms)."""

    def __call__(self, percept: Percept) -> Action:
        self.__state = self.__update_state(self.__state, percept)
        if self.__seq is None or len(self.__seq) <= 0:
            self.__goal = self.__formulate_goal(self.__state)
            self.__problem = self.__formulate_problem(self.__state, self.__goal)
            self.__seq = search(self.__problem)
            if self.__seq is None:
                return None

        action = self.__seq[0]

        self.__seq = self.__seq[1:]
        return action

    def __formulate_goal(self, _state: AtomicRepresentation) -> Goal:
        return Goal()

    def __formulate_problem(self, _state: AtomicRepresentation, _goal: Goal) -> Problem:
        return Problem()

    def __update_state(self,
                       _state: AtomicRepresentation,
                       _percept: Percept)-> AtomicRepresentation:
        return AtomicRepresentation()

    __seq: list[Action] = field(default_factory=list[Action])
    __state: AtomicRepresentation = None
    __goal: Goal = None
    __problem: Problem = None
