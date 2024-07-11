import unittest
from unittest.mock import patch, MagicMock
import urllib.request
import json
import re
from ChessEnums import Player
from ChessPuzzleData import obtain_latest_daily_puzzle, obtain_latest_random_puzzle, ChessPuzzle

class TestChessPuzzle(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_obtain_latest_daily_puzzle(self, mock_urlopen):
        # Mock response from chess.com API
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "title": "Daily Puzzle",
            "url": "https://www.chess.com/puzzles/problem/2022",
            "publish_time": 1640995200,
            "fen": "r1bqkbnr/pppppppp/n7/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
            "pgn": "[Event \"?\"]\n[Site \"?\"]\n[Date \"2022.01.01\"]\n1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 c6 12. Nc3 Qc7 13. a3 Re8 14. d5 cxd5 15. cxd5 Nc5 16. Bc2 Bf8 17. b4 Nb7 18. Bb2 g6 19. Qd2 Bg7 20. Rac1 Qb6 21. Bb1 Bd7 22. Qe3 Qd8 23. g4 Rc8 24. Nd2 Qe7 25. f4 h5 26. g5 exf4 27. Qxf4 Be5 28. Qe3 Nh7 29. Nf3 Bxh3 30. Nxe5 Qxe5 31. Qxh3 Qxg5+ 32. Kh1 Qe5 33. Rf1 Ng5 34. Qh4 Rc4 35. Qf2 Re7 36. Qf6 Re8 37. Rf4 Nd8 38. Rh4 Kg7 39. Qf3 Rf8 40. Qf2 Rh8 41. Qb2 Nxe4 42. Nxe4 Rxe4 43. Bxe4 f5 44. Bxf5 Rf8 45. Qg2 Rxf5 46. Qh2 Rf6 47. Qg2 Re6 48. Qd2 Re7 49. Qe3 Kg8 50. Qd4 Qe8 51. Qe5 dxe5 52. Qd5+ Rf7 53. Rg1 Qe6 54. Rxg6+ Qxg6 55. Rh2 Rf5 56. Rf2 Qg3 57. Rg2 Rf2 58. Rxg3+ Kxg8 59. Rg1+ Kf7 60. Rg2 Qg3 61. Qxg3 Rxg2 62. Rxa8 Rxa8 63. Rh2 Ra1#"
        }).encode('utf-8')
        mock_urlopen.return_value = mock_response

        # Call the function under test
        daily_puzzle = obtain_latest_daily_puzzle()

        # Assertions to verify puzzle attributes
        self.assertEqual(daily_puzzle.title, "Daily Puzzle")
        self.assertEqual(daily_puzzle.url, "https://www.chess.com/puzzles/problem/2022")
        self.assertEqual(daily_puzzle.publish_time, 1640995200)
        self.assertEqual(daily_puzzle.fen_board_start, "r1bqkbnr/pppppppp/n7/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    @patch('urllib.request.urlopen')
    def test_obtain_latest_random_puzzle(self, mock_urlopen):
        # Mock response from chess.com API
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "title": "Random Puzzle",
            "url": "https://www.chess.com/puzzles/problem/2023",
            "publish_time": 1640995201,
            "fen": "r1bqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
            "pgn": "[Event \"?\"]\n[Site \"?\"]\n[Date \"2022.01.02\"]\n1. d4 d5 2. c4 c6 3. Nc3 Nf6 4. Nf3 e6 5. Bg5 Be7 6. e3 O-O 7. Rc1 Nbd7 8. Qc2 Re8 9. Bd3 Nf8 10. O-O a6 11. a4 b6 12. Rfd1 Bb7 13. cxd5 exd5 14. Ne5 N6d7 15. Bf4 Nxe5 16. dxe5 g6 17. Bg3 Ne6 18. f4 Bc5 19. Bf2 Qe7 20. Rb1 Rad8 21. b4 Bxb4 22. Qb3 Bxc3 23. Qxc3 b5 24. axb5 axb5 25. Rdc1 Rc8 26. Qb3 Ba8 27. Qxb5 Red8 28. Qa5 Rb8 29. Ra1 Rb7 30. Qa6 Rbb8 31. Rcb1 c5 32. Qa2 Rbc8 33. Rb2 c4 34. Be2 Nc5 35. Qa3 Qe6 36. Bf3 Nd3 37. Re2 Rb8 38. Bh4 Rd7 39. Bh4 Rc7 40. Bf6 Qf8 41. Rf1 Rc6 42. Rb1 Nc5 43. Reb2 Ra7 44. Qc1 Nb3 45. Qd1 Rcb7 46. h4 Na5 47. Ra2 Rb3 48. Qe2 h5 49. Rba1 R3b5 50. Qd1 Nc6 51. Bf3 Qc5 52. g4 hxg4 53. Bxg4 Qxe3+ 54. Qe2 Qxf4 55. Bf3 Nd4 56. Qf2 Nxf3+ 57. Kh1 d4 58. Rf1 Rb3 59. Ra7 Nxh4+ 60. Rf3 Qg3 61. Qxg3 Rxg3 62. Rxa8 Rxa8 63. Rh2 Ra1#"
        }).encode('utf-8')
        mock_urlopen.return_value = mock_response

        # Call the function under test
        random_puzzle = obtain_latest_random_puzzle()

        # Assertions to verify puzzle attributes
        self.assertEqual(random_puzzle.title, "Random Puzzle")
        self.assertEqual(random_puzzle.url, "https://www.chess.com/puzzles/problem/2023")
        self.assertEqual(random_puzzle.publish_time, 1640995201)
        self.assertEqual(random_puzzle.fen_board_start, "r1bqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    def test_findColorToPlay(self):
        # Mock ChessPuzzle object for testing
        puzzle = ChessPuzzle(
            title="Test Puzzle",
            url="https://www.chess.com",
            publish_time=1640995200,
            fen="r1bqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
            pgn="[Event \"?\"]\n[Site \"?\"]\n[Date \"2022.01.01\"]\n1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 c6 12. Nc3 Qc7 13. a3 Re8 14. d5 cxd5 15. cxd5 Nc5 16. Bc2 Bf8 17. b4 Nb7 18. Bb2 g6 19. Qd2 Bg7 20. Rac1 Qb6 21. Bb1 Bd7 22. Qe3 Qd8 23. g4 Rc8 24. Nd2 Qe7 25. f4 h5 26. g5 exf4 27. Qxf4 Be5 28. Qe3 Nh7 29. Nf3 Bxh3 30. Nxe5 Qxe5 31. Qxh3 Qxg5+ 32. Kh1 Qe5 33. Rf1 Ng5 34. Qh4 Rc4 35. Qf2 Re7 36. Qf6 Re8 37. Rf4 Nd8 38. Rh4 Kg7 39. Qf3 Rf8 40. Qf2 Rh8 41. Qb2 Nxe4 42. Nxe4 Rxe4 43. Bxe4 f5 44. Bxf5 Rf8 45. Qg2 Rf6 46. Qh2 Rf7 47. Qg2 Re6 48. Qd2 Re7 49. Qe3 Kg8 50. Qd4 Qe8 51. Qe5 dxe5 52. Qd5+ Rf7 53. Rg1 Qe6 54. Rxg6+ Qxg6 55. Rh2 Rf5 56. Rf2 Qg3 57. Rg2 Rf2 58. Rxg3+ Kxg8 59. Rg1+ Kf7 60. Rg2 Qg3 61. Qxg3 Rxg2 62. Rxa8 Rxa8 63. Rh2 Ra1#"
        )

        # Call method under test
        color_to_play = puzzle.findColorToPlay()

        # Assertion to verify the correct color is returned
        self.assertEqual(color_to_play, Player.WHITE)

if __name__ == '__main__':
    unittest.main()
