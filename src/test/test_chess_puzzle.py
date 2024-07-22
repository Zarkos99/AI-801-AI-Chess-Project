"""Test Suite for chess_puzzle_data"""

# Bring your packages onto the path so we can see src.chess_puzzle_data from this directory
# Avoiding auto-formatting with # nopep8 so the below 4 lines are not moved
import os  # nopep8
import sys  # nopep8
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # nopep8
sys.path.append(os.path.dirname(ROOT_DIR))  # nopep8

# pylint: disable=wrong-import-position
import unittest
from unittest.mock import patch, MagicMock
import json
import chess
# pylint: disable=import-error
from src.chess_puzzle_data import obtain_latest_daily_puzzle, \
    obtain_latest_random_puzzle, ChessPuzzle


TITLE = "Daily Puzzle"
URL = "https://www.chess.com/forum/view/daily-puzzles/7-11-2024-hanging-on-by-a-loose-thread"
PUBLISH_TIME = 1720681200
FEN = "4r1k1/5p2/6p1/7p/8/1bB2P2/1P1KNbP1/R7 b - - 0 1"
PGN = "[Result \"*\"]\r\n[FEN \"4r1k1/5p2/6p1/7p/8/1bB2P2/1P1KNbP1/R7 b - - 0 1\"]\r\n\r\n1... \
        Rd8+ 2. Nd4 Bxd4 3. Bxd4 Rxd4+ 4. Kc3 Ra4 5. Rxa4 Bxa4 *"


def obtain_puzzle_data():
    """Method to obtain generic puzzle data in json format"""
    return {
        "title": TITLE,
        "url": URL,
        "publish_time": PUBLISH_TIME,
        "fen": FEN,
        "pgn": PGN
    }


def mock_https_url(mock_urlopen):
    """Method to mock an https url request"""
    # Mock response from chess.com API
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(
        obtain_puzzle_data()).encode('utf-8')
    mock_urlopen.return_value = mock_response


class TestChessPuzzle(unittest.TestCase):
    """Test module for Chess puzzle data from the Chess.com Published Data API"""

    @patch('urllib.request.urlopen')
    def test_obtain_latest_daily_puzzle(self, mock_urlopen):
        """ Test case for obtaining the latest daily puzzle"""
        mock_https_url(mock_urlopen)

        # Call the function under test
        daily_puzzle = obtain_latest_daily_puzzle()
        expected_board = chess.Board(FEN)

        # Assertions to verify puzzle attributes
        self.assertEqual(daily_puzzle.title, TITLE)
        self.assertEqual(daily_puzzle.url, URL)
        self.assertEqual(daily_puzzle.publish_time, PUBLISH_TIME)
        self.assertEqual(expected_board, daily_puzzle.game.board())

    @patch('urllib.request.urlopen')
    def test_obtain_latest_random_puzzle(self, mock_urlopen):
        """Test case for obtaining the latest random puzzle"""
        mock_https_url(mock_urlopen)

        # Call the function under test
        random_puzzle = obtain_latest_random_puzzle()
        expected_board = chess.Board(FEN)

        # Assertions to verify puzzle attributes
        self.assertEqual(random_puzzle.title, TITLE)
        self.assertEqual(random_puzzle.url, URL)
        self.assertEqual(random_puzzle.publish_time, PUBLISH_TIME)
        self.assertEqual(expected_board, random_puzzle.game.board())

    def test_find_color_to_play(self):
        """Test case for determining the color to play"""
        # Mock ChessPuzzle object for testing
        puzzle = ChessPuzzle(title=TITLE, url=URL,
                             publish_time=PUBLISH_TIME, fen=FEN, pgn=PGN)

        # Call method under test
        color_to_play = puzzle.game.turn()

        # Assertion to verify the correct color is returned
        self.assertEqual(color_to_play, chess.BLACK)


if __name__ == '__main__':
    unittest.main()
