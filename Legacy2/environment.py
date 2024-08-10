"""Module providing the Environment class."""

from dataclasses import dataclass

import io

import chess
import chess.svg
import pygame

from chess import Board
from pygame.locals import *
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

from chess_puzzle_data import obtain_latest_daily_puzzle

@dataclass
class Environment:
    """Class representing an environment, which can be perceived and acted upon by an agent."""

    def __init__(self):
        # pylint: disable=no-member
        pygame.init()
        self.__size = [800, 800]
        self.__screen = pygame.display.set_mode(self.__size, )
        pygame.display.set_caption('AI801 Chess UI')
        self.__clock = pygame.time.Clock()
        self.__fps = 30
        
        fen = obtain_latest_daily_puzzle().fen
        self.__board = Board(fen)

    def __call__(self) -> bool:
        self.__clock.tick(self.__fps)

        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            # pylint: disable=no-member
            if event.type == pygame.QUIT:
                return False

        self.__screen.fill("white")

        board = chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")

        svg_wrapper = chess.svg.board(
            board,
            fill=dict.fromkeys(board.attacks(chess.E4), "#cc0000cc"),
            arrows=[chess.svg.Arrow(chess.E4, chess.F6, color="#0000cccc")],
            squares=chess.SquareSet(chess.BB_DARK_SQUARES & chess.BB_FILE_B),
            size=800,
        )
        
        initial_bytes = svg_wrapper.encode()
        file_arg = io.BytesIO(initial_bytes)
        
        svg = svg2rlg(file_arg)
        buffer = io.BytesIO()
        renderPM.drawToFile(svg, buffer)
        
        #image = pygame.image.load(file_arg)
        #b = pygame.image.tobytes(image, "RGB")
        #s = pygame.image.frombytes(b, [800,800, 4], "RGBA")
        #pygame.transform.scale(s, self.__size, self.__screen)

        self.__screen.blit(buffer, (0, 0))
        pygame.display.update()
        #pygame.display.flip()

        return True
