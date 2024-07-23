"""Module providing the project entry point."""

import pygame
from agent import Agent
from environment import Environment
from chess_puzzle_data import obtain_latest_daily_puzzle
from board_display import display_board, WIDTH, HEIGHT
# from rational_agent import RationalAgent


pygame.init()
pygame.display.set_caption('AI801 Chess UI')
pygame.font.Font('freesansbold.ttf', 20)
pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
FPS = 1  # cap really low for now


def main():
    """Function called as the project entry point."""

    environment = Environment()
    agent = Agent()  # RationalAgent()
    game = obtain_latest_daily_puzzle().game
    board = game.board()
    # Get from nominal chess board start to start of puzzle board
    for move in game.mainline_moves():
        board.push(move)
    display_board(board)

    run = True
    while run:
        environment()
        agent(environment)
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        timer.tick(FPS)  # limits FPS

        pygame.display.flip()
    # End while loop
    pygame.quit()


if __name__ == '__main__':
    main()
