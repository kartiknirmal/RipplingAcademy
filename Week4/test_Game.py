from unittest import TestCase
from unittest.mock import patch
import Game as m

class TestGame(TestCase):
    # @patch('builtins.input', side_effect=['1', '2'])
    def setUp(self):
        self.game = m.Game()

    def test_check_row(self):
        self.game.board.cells = [['X', 'X', 'X'], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_row()
        self.assertEqual(self.game.check_row(), True)

        self.game.board.cells = [['X', 'X', 'O'], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_row()
        self.assertEqual(self.game.check_row(), False)

        self.game.board.cells = [[' ', ' ', ' '], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_row()
        self.assertEqual(self.game.check_row(), False)
        # self.fail()

    def test_check_col(self):
        self.game.board.cells = [['X', 'X', 'X'], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_col()
        self.assertEqual(self.game.check_col(), False)

        self.game.board.cells = [['X', 'X', 'O'], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_col()
        self.assertEqual(self.game.check_col(), True)

        self.game.board.cells = [[' ', ' ', ' '], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_col()
        self.assertEqual(self.game.check_col(), False)
        # self.fail()

    def test_check_diagonal(self):
        self.game.board.cells = [['X', 'X', 'X'], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_diagonal()
        self.assertEqual(self.game.check_diagonal(), False)

        self.game.board.cells = [['X', 'X', 'O'], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_diagonal()
        self.assertEqual(self.game.check_diagonal(), False)

        self.game.board.cells = [[' ', ' ', ' '], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_diagonal()
        self.assertEqual(self.game.check_diagonal(), False)

        self.game.board.cells = [['O', ' ', ' '], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_diagonal()
        self.assertEqual(self.game.check_diagonal(), True)

        self.game.board.cells = [['O', ' ', 'X'], ['O', 'X', 'O'], ['X', ' ', 'O']]
        self.game.check_diagonal()
        self.assertEqual(self.game.check_diagonal(), True)
        # self.fail()

    def test_check_result(self):
        self.game.board.cells = [['X', 'X', 'X'], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_result()
        self.assertEqual(self.game.check_result(), True)

        self.game.board.cells = [['X', 'X', 'O'], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_result()
        self.assertEqual(self.game.check_result(), True)

        self.game.board.cells = [[' ', ' ', ' '], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_result()
        self.assertEqual(self.game.check_result(), False)

        self.game.board.cells = [['O', ' ', ' '], ['X', 'O', 'O'], [' ', ' ', 'O']]
        self.game.check_result()
        self.assertEqual(self.game.check_result(), True)

        self.game.board.cells = [['O', ' ', 'X'], ['O', 'X', 'O'], ['X', ' ', 'O']]
        self.game.check_result()
        self.assertEqual(self.game.check_result(), True)
        # self.fail()

    def test_start(self):
        self.fail()
