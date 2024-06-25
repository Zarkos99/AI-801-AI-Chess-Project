"""A UI FEN helper"""
class ChessPiece:
    """Defines a UI Chess Piece"""
    def __init__(self, piece_type, color):
        self.piece_type = piece_type
        self.color = color

    def __repr__(self):
        return f"{self.color}{self.piece_type}"

def parse_fen(fen):
    """Parse a FEN (Forsyth-Edwards Notation) string into an array of pieces"""
    piece_mapping = {
        'p': 'pawn', 'r': 'rook', 'n': 'knight', 'b': 'bishop', 'q': 'queen', 'k': 'king',
        'P': 'pawn', 'R': 'rook', 'N': 'knight', 'B': 'bishop', 'Q': 'queen', 'K': 'king'
    }

    rows = fen.split(' ')[0].split('/')
    board = []

    for row in rows:
        board_row = []
        for char in row:
            if char.isdigit():
                board_row.extend([None] * int(char))
            else:
                piece_type = piece_mapping[char]
                color = 'white' if char.isupper() else 'black'
                board_row.append(ChessPiece(piece_type, color))
        board.append(board_row)

    return board
