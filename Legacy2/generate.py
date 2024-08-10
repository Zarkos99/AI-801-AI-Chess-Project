"""Module providing the generate function."""

from problem import Problem

def generate(problem: Problem, s):
    """Function that applies each legal action to the current state, and generates the resulting\
       new set of states."""
    for a in problem.actions(s):
        state = problem.result(s, a)
        yield state
