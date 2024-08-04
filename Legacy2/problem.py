"""Module providing the Problem class."""

from dataclasses import dataclass, field

from actions import Actions
from goal_test import GoalTest
from path_cost import PathCost
from state import State
from step_cost import StepCost
from transition_model import TransitionModel

@dataclass
class Problem:
    """Class representing a problem, which is defined formally by five components: initial state,\
       actions, transition model, goal test, and path cost."""

    initial_state: State = None
    actions: Actions = field(default_factory=Actions)
    result: TransitionModel = field(default_factory=TransitionModel)
    goal_test: GoalTest = field(default_factory=GoalTest)
    path_cost: PathCost = field(default_factory=PathCost)
    step_cost: StepCost = field(default_factory=StepCost)
