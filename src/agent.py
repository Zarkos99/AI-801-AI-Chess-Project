"""Module providing the Agent class."""

from dataclasses import dataclass

from agent_program import AgentProgram
from architecture import Architecture
from environment import Environment

@dataclass
class Agent:
    """Class representing an agent, which can perceive its environment through sensors and act\
       upon that environment through actuators."""

    def __call__(self, environment: Environment):
        percept = self.__architecture.sensors(environment)
        action = self.__agent_program(percept)

        self.__architecture.actuators(action, environment)

    __agent_program: AgentProgram = AgentProgram()
    __architecture: Architecture = Architecture()
