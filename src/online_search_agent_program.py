"""Module providing the OnlineSearchAgentProgram class."""

from dataclasses import dataclass, field

from action import Action
from actions import Actions
from agent_program import AgentProgram
from goal_test import GoalTest
from percept import Percept
from state import State

STOP: Action = None

@dataclass
class OnlineSearchAgentProgram(AgentProgram):
    """Class representing an online search agent program, which interleaves computation and\
       action: first it takes an action, then it observes the environment and computes the next\
       action."""

    def __call__(self, percept: Percept) -> Action:
        sp = percept.state

        if self.__goal_test(sp):
            return STOP

        if sp not in self.__untried:
            self.__untried[sp] = self.__actions(sp)

        if self.__s is not None:
            self.__result[(self.__s, self.__a)] = sp
            self.__unbacktracked[sp].insert(0, self.__s)

        if not self.__untried[sp]:
            if not self.__unbacktracked[sp]:
                return STOP

            result_sp_b = self.__unbacktracked[sp].pop()
            b: Action = None

            for key in enumerate(self.__result):
                if key[0] == sp and self.__result[key] == result_sp_b:
                    b = key[1]
                    break

            self.__a = b
        else:
            self.__a = self.__untried[sp].pop()
        self.__s = sp

        return self.__a

    __actions: Actions = field(default_factory=Actions)
    __goal_test: GoalTest = field(default_factory=GoalTest)
    __result: dict[tuple[State, Action], State] = field(default_factory=dict[tuple[State, Action],
                                                                             State])
    __untried: dict[State, list[Action]] = field(default_factory=dict[State, list[Action]])
    __unbacktracked: dict[State, list[State]] = field(default_factory=dict[State, State])
    __s: State = None
    __a: Action = None
