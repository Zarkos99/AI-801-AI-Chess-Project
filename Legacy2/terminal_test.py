"""Module providing the TerminalTest class."""

from dataclasses import dataclass

from state import State

@dataclass
class TerminalTest:
    """Class representing a terminal test, which returns true when the game is over and false\
       otherwise."""

    def __call__(self, s: State) -> bool:
        is_terminal_state = s.is_variant_end()

        return is_terminal_state
