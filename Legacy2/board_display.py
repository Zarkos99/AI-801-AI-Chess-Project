"""Module providing the capability to display a chess board state."""

import io
import chess.svg
import pygame
import cairosvg

WIDTH = 800
HEIGHT = 800


def display_board(board):
    """"Display a chess board svg in a widget"""
    display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    display_surface.blit(get_board_img(board), (0, 0))


def get_board_img(board):
    """Converts an svg chess board to a pygame surface (pygame will display an empty \
    chess board otherwise)"""
    svg = chess.svg.board(board=board,  size=WIDTH)
    png_io = io.BytesIO()
    cairosvg.svg2png(bytestring=bytes(svg, "utf8"), write_to=png_io)
    png_io.seek(0)

    surf = pygame.image.load(png_io, "png")
    return surf
