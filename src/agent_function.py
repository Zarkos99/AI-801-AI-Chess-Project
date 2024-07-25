"""Module providing the AgentFunction class."""

from typing import Dict
from chess_puzzle_data import obtain_latest_daily_puzzle, ChessPuzzle

class AgentFunction:
    """Class representing an agent function, which is an abstract mathematical description of an
       agent's behavior that maps any given percept sequence to an action."""

    def __init__(self, puzzle: ChessPuzzle) -> None:
        self.partial_table: Dict[str, str] = {} #init this as empty
        self.process_game(puzzle) # process the puzzle we were given

    def evaluateFen(self, fen_state: str) -> str:
        print(self.partial_table) # TODO can be removed just for debug
        return self.partial_table.get(fen_state, "No action found")

    # allow for processesing of additional puzzles
    def process_game(self, puzzle: ChessPuzzle):
        partial_table: Dict[str, str] = {}

        board = puzzle.game.board()
        percept_sequence = []
        node = puzzle.game

        while node.variations:
            next_node = node.variation(0)
            move = next_node.move
            percept_sequence.append(board.san(move))

            if len(percept_sequence) >= 1:  # Ensure we have a previous percept to map the action to
                # The percept sequence up to the current move maps to the current move (action)
                partial_table[board.fen()] = percept_sequence[-1]

            board.push(move)
            node = next_node

        self.partial_table.update(partial_table)

# Use Kostis daily puzzle data parsed game
puzzleOTD = obtain_latest_daily_puzzle()
agent = AgentFunction(puzzleOTD)

fen_state = puzzleOTD.game.board().fen()
print(fen_state)
action = agent.evaluateFen(fen_state)
print(action)
