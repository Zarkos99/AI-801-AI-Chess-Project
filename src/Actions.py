
from ChessEnums import Piece
from ChessEnums import Space
from Coord import Coord
from State import State
from UtilityFunctions import ToPlayer

def PawnActions(par_state, par_space): return []
def KnightActions(par_state, par_space): return []
def BishopActions(par_state, par_space): return []
def RookActions(par_state, par_space): return []
def QueenActions(par_state, par_space): return []
def KingActions(par_state, par_space): return []

def Actions(par_state : State):
    actions = []
    board = par_state.board
    player = par_state.player
    
    # For each board space
    for space in Space:
        piece = board[space]
        
        # Check for current player's pieces
        is_piece = piece != Piece.___
        current_player_piece = is_piece and ToPlayer(piece) == player
        
        if current_player_piece:
            coord = Coord.fromSpace(space)

            match piece:
                case Piece.W_P:
                    actions = PawnActions(par_state, space)
                    
                case Piece.B_P:
                    actions = PawnActions(par_state, space)
                    
                case Piece.W_N:
                    actions = KnightActions(par_state, space)
                    
                case Piece.B_N:
                    actions = KnightActions(par_state, space)
                    
                case Piece.W_B:
                    actions = BishopActions(par_state, space)
                    
                case Piece.B_B:
                    actions = BishopActions(par_state, space)
                    
                case Piece.W_R:
                    actions = RookActions(par_state, space)
                    
                case Piece.B_R:
                    actions = RookActions(par_state, space)
                    
                case Piece.W_Q:
                    actions = QueenActions(par_state, space)
                    
                case Piece.B_Q:
                    actions = QueenActions(par_state, space)
                    
                case Piece.W_K:
                    actions = KingActions(par_state, space)

                case Piece.B_K:
                    actions = KingActions(par_state, space)

                case _:
                    assert(0)
    
    return actions
