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

from Action import Action
from Actions import Actions
from ChessEnums import Player
from ChessEnums import Piece
from ChessEnums import Space
import ChessEnums
from Coord import Coord
from PathCost import PathCost
from Result import Result
from State import State
from UtilityFunctions import IsCheckForPlayer
from UtilityFunctions import ForEachSpaceHorizontalAndVertical
from UtilityFunctions import ForEachSpaceDiagonal
from UtilityFunctions import ForEachSpaceL
from UtilityFunctions import ToPlayer

print("Hello. This will be a great project.")

# (Temporary) Print classes / functions to ensure they compile

print(Action(Space.A1, Space.A2, Piece.W_P))
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
print(ForEachSpaceHorizontalAndVertical(Func, State().board, Space.A1))
print(ForEachSpaceDiagonal(Func, State().board, Space.A3))
print(ForEachSpaceL(Func, Space.A2))

print(len(Actions(State())))

# Please add new classes and functions here to be printed
