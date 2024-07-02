
from Action import Action
from ChessEnums import Piece_Type, Player, Space
from Coord import Coord
from Result import Result
from State import State
from ChessPiece import ChessPiece
from UtilityFunctions import ForEachSpaceDiagonal, \
    ForEachSpaceHorizontalAndVertical, \
    ForEachSpaceL, IsEmpty, IsPlayerPiece, IsOpponentPiece


# Pawns can move in 4 ways:
# 1. One space forward (if empty)
# 2. Two spaces forward (if both empty and first time moving)
# 3. One space forward-diagonal (only to capture)
# 4. En Pessant (if opponent's last move was pawn moving two spaces and ending
#    horizontally adjacent to this pawn)
# Note: If any move results in pawn at end of board, this is promotion
def PawnActions(par_state: State, par_space: Space):
    actions = []
    are_moves = len(par_state.moves) > 0
    board = par_state.board
    coord = Coord.fromSpace(par_space)
    player = par_state.player
    is_white = player == Player.WHITE
    promotion_start = ChessPiece(Piece_Type.KING, player)
    promotion_stop = ChessPiece(Piece_Type.KING, player)
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
                is_pawn_side = piece_side == Piece_Type.PAWN
                is_opponent_pawn_side = is_pawn_side\
                    and IsOpponentPiece(piece_side, player)

                if is_opponent_pawn_side and are_moves:
                    last_move = par_state.moves[-1]
                    coord_last_move_orig = Coord.fromSpace(last_move.orig)
                    coord_last_move_dest = Coord.fromSpace(last_move.dest)
                    is_last_move_pawn_side = last_move.dest == space_side
                    space_distance = abs(coord_last_move_orig.r
                                         - coord_last_move_dest.r)
                    is_2_space_move = space_distance == 2

                    if is_last_move_pawn_side and is_2_space_move:
                        actions.append(Action(par_space, space_diag))

    return actions


# Used for pieces with simple movement rules
# 1. Knight: moves in an "L" pattern. This can be thought of as moving two
#    squares horizontally then one square vertically, or moving one square
#    horizontally then two squares vertically.
# 2. Bishop: moves any number of vacant squares diagonally.
# 3. Rook: moves any number of vacant squares horizontally or vertically.
# 4. Queen: moves any number of vacant squares horizontally, vertically, or
#    diagonally.
def SimpleActions(par_state: State, par_space, par_function):
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

    par_function(function, par_space, board)

    return actions


# The king moves exactly one square horizontally, vertically, or diagonally.
# A special move with the king known as castling is allowed only once per
# player, per game
def KingActions(par_state: State, par_space):
    actions = []
    board = par_state.board
    coord = Coord.fromSpace(par_space)
    player = par_state.player

    # The king moves exactly one square horizontally, vertically, or diagonally
    for h in range(-1, 2):
        for v in range(-1, 2):
            if h == 0 and v == 0:
                continue

            coord_dest = Coord(coord.c + h, coord.r + v)
            is_valid_dest = coord_dest.isValid()

            if is_valid_dest:
                space_dest = coord_dest.toSpace()
                piece_dest = board[space_dest]
                is_player_piece = IsPlayerPiece(piece_dest, player)

                if not is_player_piece:
                    actions.append(Action(par_space, space_dest))

    # A special move with the king known as castling is allowed only once per
    # player, per game
    has_king_moved = par_state.king_moved[player]

    if not has_king_moved:
        has_A_moved = par_state.rookA_moved[player]
        has_H_moved = par_state.rookH_moved[player]
        spaces_between = [[[Space.F1, Space.G1],
                           [Space.F8, Space.G8]],
                          [[Space.B1, Space.C1, Space.D1],
                           [Space.B8, Space.C8, Space.D8]]]

        for is_queenside in range(0, 2):
            has_rook_moved = has_A_moved if is_queenside else has_H_moved
            sign = -1 if is_queenside else 1

            if not has_rook_moved:
                are_pieces_between = False

                for space in spaces_between[is_queenside][player]:
                    is_empty_space = IsEmpty(space)
                    if not is_empty_space:
                        are_pieces_between = True
                        break

                if not are_pieces_between:
                    is_any_check = False

                    for i in range(0, 3):
                        coord_i = Coord(coord.c + i * sign, coord.r)
                        action_i = Action(par_space, coord_i.toSpace())
                        state_i = Result(par_state, action_i)
                        is_check_i = state_i.check

                        if is_check_i:
                            is_any_check = True
                            break

                    if not is_any_check:
                        coord_dest = Coord(coord.c + 2 * sign, coord.r)
                        space_dest = coord_dest.toSpace()
                        actions.append(Action(par_space, space_dest))

    return actions


def Actions(par_state: State):
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
                case Piece_Type.PAWN:
                    actions.extend(PawnActions(par_state, space))

                case Piece_Type.KNIGHT:
                    actions.extend(
                        SimpleActions(par_state, space, ForEachSpaceL))

                case Piece_Type.BISHOP:
                    actions.extend(
                        SimpleActions(par_state, space, ForEachSpaceDiagonal))

                case Piece_Type.ROOK:
                    actions.extend(
                        SimpleActions(par_state, space,
                                      ForEachSpaceHorizontalAndVertical))

                case Piece_Type.QUEEN:
                    actions.extend(
                        SimpleActions(par_state, space, ForEachSpaceDiagonal))
                    actions.extend(
                        SimpleActions(par_state, space,
                                      ForEachSpaceHorizontalAndVertical))

                case Piece_Type.KING:
                    actions.extend(KingActions(par_state, space))

                case _:
                    assert (0)

    return actions
