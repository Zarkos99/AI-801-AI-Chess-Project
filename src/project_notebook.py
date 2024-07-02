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

import ChessPuzzleData
from Action import Action
from Actions import Actions
from ChessEnums import Piece_Type, Player, Space
from Coord import Coord
from Node import Node, Expand, Solution
from PathCost import PathCost
from Result import Result
from Search import Search
from State import State
from UtilityFunctions import ForEachSpaceDiagonal, \
    ForEachSpaceHorizontalAndVertical, \
    ForEachSpaceL, IsCheckForPlayer, ToPlayer

print("Hello. This will be a great project.")

# (Temporary) Print classes / functions to ensure they compile

print(Action(Space.A1, Space.A2, Piece_Type.PAWN))
print(Action(Space.A1, Space.A1) == Action(Space.A2, Space.A2))

print(Coord(0, 0))
print(Coord.fromSpace(Space.A1))
print(Coord(0, 0).toSpace())

print(PathCost(State()))
print(float(PathCost(State())))

print(Result(State(), Action()))

print(State())


def Func(par_space): pass


print(IsCheckForPlayer(State().board, Player.White, Space.E1))
print(ForEachSpaceHorizontalAndVertical(Func, Space.A1, State().board))
print(ForEachSpaceDiagonal(Func, Space.A3, State().board))
print(ForEachSpaceL(Func, Space.A2))

print(len(Actions(State())))

print(Node(State()))
print(Expand(Node(State())))
print(Solution(Node(State())))

print(Search(State(), 1.0))

# Please add new classes and functions here to be printed
