"""Module providing the UninformedSearch class."""

from enum import Enum

class UninformedSearch(Enum):
    """Class representing an uninformed search, which is the set of search strategies that have no\
       additional information about states beyond that provided in the problem definition."""

    BREADTH_FIRST_SEARCH = 'Breadth-First Search'
