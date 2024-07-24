"""Module providing the Environment class."""

from dataclasses import dataclass


@dataclass
class Environment:
    """Class representing an environment, which can be perceived and acted upon by an agent."""

    # Temporary, substitute for whether an environment requires further action by the agent.
    def __bool__(self):
        pass

    def __call__(self):
        pass
