"""Actions module"""
from action import Action
from chess_enums import Piece, Player, Space
from coord import Coord
from result import Result
from state import State
from utility_functions import for_each_space_horizontal_and_vertical, for_each_space_l
from utility_functions import is_player_piece, for_each_space_diagonal, is_empty, is_opponent_piece


# Pawns can move in 4 ways:
# 1. One space forward (if empty)
# 2. Two spaces forward (if both empty and first time moving)
# 3. One space forward-diagonal (only to capture)
# 4. En Pessant (if opponent's last move was pawn moving two spaces and ending
#    horizontally adjacent to this pawn)
# Note: If any move results in pawn at end of board, this is promotion
def pawn_actions(par_state : State, par_space : Space):
    """actions for pawns"""
    actions = []
    are_moves = len(par_state.moves) > 0
    board = par_state.board
    coord = Coord.from_space(par_space)
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
    space_forward_1 = coord_forward_1.to_space()
    is_forward_1_end = coord_forward_1.r == r_last
    piece_forward_1 = board[space_forward_1]
    is_forward_1_empty = is_empty(piece_forward_1)

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
        space_forward_2 = coord_forward_2.to_space()
        piece_forward_2 = board[space_forward_2]
        is_forward_2_empty = is_empty(piece_forward_2)

        # 2. Two spaces forward (if both empty and first time moving)
        if is_first_move and is_forward_2_empty:
            actions.append(Action(par_space, space_forward_2))

    for h in range(-1, 2, 2):
        coord_diag = Coord(coord.c + h, coord.r + v)
        is_diag_valid = coord_diag.is_valid()

        if is_diag_valid:
            space_diag = coord_diag.to_space()
            piece_diag = board[space_diag]
            is_opponent_piece_diag = is_opponent_piece(piece_diag, player)

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
                space_side = coord_side.to_space()
                piece_side = board[space_side]
                is_pawn_side = piece_side == Piece.W_P\
                            or piece_side == Piece.B_P
                is_opponent_pawn_side = is_pawn_side\
                                    and is_opponent_piece(piece_side, player)

                if is_opponent_pawn_side and are_moves:
                    last_move = par_state.moves[-1]
                    coord_last_move_orig = Coord.from_space(last_move.orig)
                    coord_last_move_dest = Coord.from_space(last_move.dest)
                    is_last_move_pawn_side = last_move.dest == space_side
                    space_distance = abs(coord_last_move_orig.r\
                                       - coord_last_move_dest.r)
                    is_2_space_move = space_distance == 2

                    if is_last_move_pawn_side and is_2_space_move:
                        actions.append(Action(par_space, space_diag))

    return actions

def simple_actions(par_state : State, par_space, par_function):
    """Used for pieces with simple movement rules
        1. Knight: moves in an "L" pattern. This can be thought of as moving two
        squares horizontally then one square vertically, or moving one square
        horizontally then two squares vertically.
        2. Bishop: moves any number of vacant squares diagonally.
        3. Rook: moves any number of vacant squares horizontally or vertically.
        4. Queen: moves any number of vacant squares horizontally, vertically, or diagonally."""
    actions = []
    board = par_state.board
    player = par_state.player

    def function(par_space_dest):
        nonlocal actions
        nonlocal board
        nonlocal par_space
        nonlocal player

        piece_dest = board[par_space_dest]
        is_player_piece_dest = is_player_piece(piece_dest, player)

        if not is_player_piece_dest:
            actions.append(Action(par_space, par_space_dest))

    par_function(function, par_space, board)

    return actions

def king_actions(par_state : State, par_space):
    """ The king moves exactly one square horizontally, vertically, or diagonally.
        A special move with the king known as castling is allowed only once per
        player, per game"""
    actions = []
    board = par_state.board
    coord = Coord.from_space(par_space)
    player = par_state.player

    # The king moves exactly one square horizontally, vertically, or diagonally
    for h in range(-1, 2):
        for v in range(-1, 2):
            if h == 0 and v == 0:
                continue

            coord_dest = Coord(coord.c + h, coord.r + v)
            is_valid_dest = coord_dest.is_valid()

            if is_valid_dest:
                space_dest = coord_dest.to_space()
                piece_dest = board[space_dest]
                result = is_player_piece(piece_dest, player)

                if not result:
                    actions.append(Action(par_space, space_dest))

    # A special move with the king known as castling is allowed only once per
    # player, per game
    has_king_moved = par_state.king_moved[player]

    if not has_king_moved:
        has_a_moved = par_state.rookA_moved[player]
        has_h_moved = par_state.rookH_moved[player]
        spaces_between = [[[Space.F1, Space.G1],\
                           [Space.F8, Space.G8]],\
                          [[Space.B1, Space.C1, Space.D1],\
                           [Space.B8, Space.C8, Space.D8]]]

        for is_queenside in range(0, 2):
            has_rook_moved = has_a_moved if is_queenside else has_h_moved
            sign = -1 if is_queenside else 1

            if not has_rook_moved:
                are_pieces_between = False

                for space in spaces_between[is_queenside][player]:
                    is_empty_space = is_empty(space)
                    if not is_empty_space:
                        are_pieces_between = True
                        break

                if not are_pieces_between:
                    is_any_check = False

                    for i in range(0, 3):
                        coord_i = Coord(coord.c + i * sign, coord.r)
                        action_i = Action(par_space, coord_i.to_space())
                        state_i = Result(par_state, action_i)
                        is_check_i = state_i.check

                        if is_check_i:
                            is_any_check = True
                            break

                    if not is_any_check:
                        coord_dest = Coord(coord.c + 2 * sign, coord.r)
                        space_dest = coord_dest.to_space()
                        actions.append(Action(par_space, space_dest))

    return actions


def all_actions(par_state : State):
    """all actions for a board state"""
    actions = []
    board = par_state.board
    player = par_state.player

    # For each board space
    for space in Space:
        piece = board[space]

        # Check for current player's pieces
        result = is_player_piece(piece, player)

        if result:
            match piece:
                case Piece.W_P:
                    actions.extend(pawn_actions(par_state, space))

                case Piece.B_P:
                    actions.extend(pawn_actions(par_state, space))

                case Piece.W_N:
                    actions.extend(
                        simple_actions(par_state, space, for_each_space_l))

                case Piece.B_N:
                    actions.extend(
                        simple_actions(par_state, space, for_each_space_l))

                case Piece.W_B:
                    actions.extend(
                        simple_actions(par_state, space, for_each_space_diagonal))

                case Piece.B_B:
                    actions.extend(
                        simple_actions(par_state, space, for_each_space_diagonal))

                case Piece.W_R:
                    actions.extend(
                        simple_actions(par_state, space,
                                      for_each_space_horizontal_and_vertical))

                case Piece.B_R:
                    actions.extend(
                        simple_actions(par_state, space,
                                      for_each_space_horizontal_and_vertical))

                case Piece.W_Q:
                    actions.extend(
                        simple_actions(par_state, space, for_each_space_diagonal))
                    actions.extend(
                        simple_actions(par_state, space,
                                      for_each_space_horizontal_and_vertical))

                case Piece.B_Q:
                    actions.extend(
                        simple_actions(par_state, space, for_each_space_diagonal))
                    actions.extend(
                        simple_actions(par_state, space,
                                      for_each_space_horizontal_and_vertical))

                case Piece.W_K:
                    actions.extend(king_actions(par_state, space))

                case Piece.B_K:
                    actions.extend(king_actions(par_state, space))

                case _:
                    assert 0

    return actions
