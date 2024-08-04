"""Module providing the SearchStrategy class."""

from enum import Enum

from uninformed_search import UninformedSearch

class SearchStrategy(Enum):
    """Class representing a search strategy, which is how search algorithms choose which state to\
       expand next."""

    UNINFORMED_SEARCH = UninformedSearch
