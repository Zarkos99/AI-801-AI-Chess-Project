
from Action import Action
from ChessEnums import Piece, Player, Space
from Coord import Coord
from State import State
from UtilityFunctions import    ForEachSpaceDiagonal, ForEachSpaceL, IsEmpty,\
                                IsOpponentPiece, IsPlayerPiece


# Pawns can move in 4 ways:
# 1. One space forward (if empty)
# 2. Two spaces forward (if both empty and first time moving)
# 3. One space forward-diagonal (only to capture)
# 4. En Pessant (if opponent's last move was pawn moving two spaces and ending
#    horizontally adjacent to this pawn)
# Note: If any move results in pawn at end of board, this is promotion
def PawnActions(par_state : State, par_space : Space):
    actions = []
    are_moves = len(par_state.moves) > 0
    board = par_state.board
    coord = Coord.fromSpace(par_space)
    player = par_state.player
    is_white = player == Player.White
    promotion_start = Piece.W_N if is_white else Piece.B_N
    promotion_stop = Piece.W_K if is_white else Piece.B_K
    r_en_pessant = 4 if is_white else 3
    r_last = 7 if is_white else 0
    r_first = 1 if is_white else 6
    v = 1 if is_white else -1
    coord_forward_1 = Coord(coord.c, coord.r + v)
    is_first_move = coord.r == r_first
    is_r_en_pessant = coord.r == r_en_pessant
    space_forward_1 = coord_forward_1.toSpace()
    is_forward_1_end = coord_forward_1.r == r_last
    piece_forward_1 = board[space_forward_1]
    is_forward_1_empty = IsEmpty(piece_forward_1)
    
    # 1. One space forward (if empty)
    if is_forward_1_empty:
        action = Action(par_space, space_forward_1)
        
        # If move results in pawn at end of board, this is promotion
        if is_forward_1_end:
            for promotion in range(promotion_start, promotion_stop):
                action.promotion = promotion
                actions.append(action)
        else:
            actions.append(action)
        
        coord_forward_2 = Coord(coord.c, coord.r + 2*v)
        space_forward_2 = coord_forward_2.toSpace()
        piece_forward_2 = board[space_forward_2]
        is_forward_2_empty = IsEmpty(piece_forward_2)

        # 2. Two spaces forward (if both empty and first time moving)
        if is_first_move and is_forward_2_empty:
            actions.append(Action(par_space, space_forward_2))
    
    for h in range(-1, 2, 2):
        coord_diag = Coord(coord.c + h, coord.r + v)
        is_diag_valid = coord_diag.isValid()

        if is_diag_valid:
            space_diag = coord_diag.toSpace()
            piece_diag = board[space_diag]
            is_opponent_piece_diag = IsOpponentPiece(piece_diag, player)
            
            # 3. One space forward-diagonal (only to capture)
            if is_opponent_piece_diag:
                action = Action(par_space, space_diag)
                
                # If move results in pawn at end of board, this is promotion
                if is_forward_1_end:
                    for promotion in range(promotion_start, promotion_stop):
                        action.promotion = promotion
                        actions.append(action)
                else:
                    actions.append(action)
            
            # 4. En Pessant (if opponent's last move was pawn moving two spaces
            #    and ending horizontally adjacent to this pawn)
            if is_r_en_pessant:
                coord_side = Coord(coord.c + h, coord.r)
                space_side = coord_side.toSpace()
                piece_side = board[space_side]
                is_pawn_side = piece_side == Piece.W_P\
                            or piece_side == Piece.B_P
                is_opponent_pawn_side = is_pawn_side\
                                    and IsOpponentPiece(piece_side, player)
                
                if is_opponent_pawn_side and are_moves:
                    last_move = par_state.moves[-1]
                    coord_last_move_orig = Coord.fromSpace(last_move.orig)
                    coord_last_move_dest = Coord.fromSpace(last_move.dest)
                    is_last_move_pawn_side = last_move.dest == space_side
                    space_distance = abs(coord_last_move_orig.r\
                                       - coord_last_move_dest.r)
                    is_2_space_move = space_distance == 2
                    
                    if is_last_move_pawn_side and is_2_space_move:
                        actions.append(Action(par_space, space_diag))
                        
    return actions


# Knights move in an "L" pattern. This can be thought of as moving two squares
# horizontally then one square vertically, or moving one square horizontally
# then two squares vertically.
def KnightActions(par_state : State, par_space):
    actions = []
    board = par_state.board
    player = par_state.player
    
    def function(par_space_dest):
        nonlocal actions
        nonlocal board
        nonlocal par_space
        nonlocal player
        
        piece_dest = board[par_space_dest]
        is_player_piece_dest = IsPlayerPiece(piece_dest, player)

        if not is_player_piece_dest:
            actions.append(Action(par_space, par_space_dest))
    
    ForEachSpaceL(function, par_space)

    return actions


# A bishop moves any number of vacant squares diagonally.
def BishopActions(par_state : State, par_space):
    actions = []
    board = par_state.board
    player = par_state.player
    
    def function(par_space_dest):
        nonlocal actions
        nonlocal board
        nonlocal par_space
        nonlocal player
        
        piece_dest = board[par_space_dest]
        is_player_piece_dest = IsPlayerPiece(piece_dest, player)

        if not is_player_piece_dest:
            actions.append(Action(par_space, par_space_dest))
    
    ForEachSpaceDiagonal(function, board, par_space)

    return actions


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
        is_player_piece = IsPlayerPiece(piece, player)
        
        if is_player_piece:
            match piece:
                case Piece.W_P:
                    actions.extend(PawnActions(par_state, space))
                    
                case Piece.B_P:
                    actions.extend(PawnActions(par_state, space))
                    
                case Piece.W_N:
                    actions.extend(KnightActions(par_state, space))
                    
                case Piece.B_N:
                    actions.extend(KnightActions(par_state, space))
                    
                case Piece.W_B:
                    actions.extend(BishopActions(par_state, space))
                    
                case Piece.B_B:
                    actions.extend(BishopActions(par_state, space))
                    
                case Piece.W_R:
                    actions.extend(RookActions(par_state, space))
                    
                case Piece.B_R:
                    actions.extend(RookActions(par_state, space))
                    
                case Piece.W_Q:
                    actions.extend(QueenActions(par_state, space))
                    
                case Piece.B_Q:
                    actions.extend(QueenActions(par_state, space))
                    
                case Piece.W_K:
                    actions.extend(KingActions(par_state, space))

                case Piece.B_K:
                    actions.extend(KingActions(par_state, space))

                case _:
                    assert(0)
    
    return actions
