"""Module providing the Agent class."""

from dataclasses import dataclass, field

from agent_program import AgentProgram
from architecture import Architecture
from environment import Environment

@dataclass
class Agent:
    """Class representing an agent, which can perceive its environment through sensors and act\
       upon that environment through actuators."""

    def __call__(self, environment: Environment):
        percept = self._architecture.sensors(environment)
        action = self._agent_program(percept)

        self._architecture.actuators(action, environment)

    _architecture: Architecture = field(default_factory=Architecture)
    _agent_program: AgentProgram = field(default_factory=AgentProgram)
