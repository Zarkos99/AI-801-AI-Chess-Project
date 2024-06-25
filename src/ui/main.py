import pygame
from parse_fen import parse_fen

pygame.init()
WIDTH = 600
HEIGHT = 600
TILE_WIDTH = WIDTH / 8
TILE_HEIGHT = HEIGHT / 8
asset_size = (TILE_WIDTH, TILE_HEIGHT)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('AI801 Chess UI')
font = pygame.font.Font('freesansbold.ttf', 20)
timer = pygame.time.Clock()
FPS = 1 #cap really low for now

FEN_SAMPLE ="r1b2rk1/1p3pp1/p1nR3p/4n2q/1PB1NQ1B/8/6PP/5RK1 w - - 0 1"

# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, asset_size)
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, asset_size)
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, asset_size)
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, asset_size)
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, asset_size)
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, asset_size)
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, asset_size)
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, asset_size)
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, asset_size)
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, asset_size)
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))

game_piece_asset_map = {
    "black_queen": black_queen,
    "black_king": black_knight,
    "black_rook": black_rook,
    "black_bishop": black_bishop,
    "black_pawn": black_pawn,
    "black_knight": black_knight,
    "white_queen": white_queen,
    "white_king": white_knight,
    "white_rook": white_rook,
    "white_bishop": white_bishop,
    "white_pawn": black_pawn,
    "white_knight": white_knight,
}

# draw main game board
def draw_board():
    """Draws the 8 x 8 Chess board"""
    fill_primary_color = True
    for r in range(8):
        for c in range(8):
            fill_color = 'white' if fill_primary_color else 'dark grey'
            pygame.draw.rect(
                screen,
                fill_color,
                [c * TILE_WIDTH, r * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT]
            )
            fill_primary_color = not fill_primary_color
            if c == 7: # end of the row start offset again
                fill_primary_color = not fill_primary_color

# draw pieces onto board
def draw_pieces(fen_state: str):
    """Draws fen state pieces to the board"""
    board_items = parse_fen(fen_state)
    for row in range(8):
        for col in range(8):
            board_item = board_items[row][col]
            if board_item is not None:
                asset_name = board_item.color + "_" + board_item.piece_type
                screen.blit(game_piece_asset_map[asset_name], (row * TILE_WIDTH, col * TILE_HEIGHT))

RUN = True
while RUN:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    timer.tick(FPS) # limits FPS
    screen.fill('dark blue')
    draw_board()
    draw_pieces(FEN_SAMPLE)
    pygame.display.flip()
pygame.quit()
