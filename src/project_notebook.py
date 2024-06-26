"""Module providing a function to test jupyter notebook."""
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

from actions import all_actions
from chess_enums import Piece, Player, Space
# import chess_enums
from coord import Coord
from PathCost import PathCost
from result import Result
from state import State
from UtilityFunctions import    ForEachSpaceDiagonal,\
                                ForEachSpaceHorizontalAndVertical,\
                                ForEachSpaceL, IsCheckForPlayer, ToPlayer

print("Hello. This will be a great project.")

# (Temporary) Print classes / functions to ensure they compile

print(Action(Space.A1, Space.A2, Piece.W_P))
print(Action(Space.A1, Space.A1) == Action(Space.A2, Space.A2))

print(Coord(0, 0))
print(Coord.from_space(Space.A1))
print(Coord(0, 0).to_space())

print(PathCost(State()))
print(float(PathCost(State())))

print(Result(State(), Action()))

print(State())

def func(par_space): pass
print(IsCheckForPlayer(State().board, Player.White, Space.E1))
print(ForEachSpaceHorizontalAndVertical(func, Space.A1, State().board))
print(ForEachSpaceDiagonal(func, Space.A3, State().board))
print(ForEachSpaceL(func, Space.A2))

print(len(all_actions(State())))

# Please add new classes and functions here to be printed
