from src.players.human_player import HumanPlayer
from src.models.board import Board
import unittest
from unittest.mock import patch

class TestHumanPlayer(unittest.TestCase):
    def setUp(self):
        self.player = HumanPlayer("Alice")
        self.board = Board(dim=3)

    def test_initialization(self):
        self.assertEqual(self.player.name, "Alice")
    
    def test_get_move(self):
        with patch('builtins.input', side_effect=['1', '2']):
            move = self.player.get_move(board=self.board)
            self.assertEqual(move, (1, 2))

    def test_get_move_invalid(self):
        with patch('builtins.input', side_effect=['4', '4', '2', '2']):
            move = self.player.get_move(board=self.board)
            self.assertEqual(move, (2, 2))
    
    def test_validate_move(self):
        self.assertTrue(self.player.validate_move(self.board, 1, 1))
        self.assertTrue(self.player.validate_move(self.board, 3, 3))
        self.assertFalse(self.player.validate_move(self.board, 0, 1))
        self.assertFalse(self.player.validate_move(self.board, 1, 0))
        self.assertFalse(self.player.validate_move(self.board, 4, 1))
        self.assertFalse(self.player.validate_move(self.board, 1, 4))


if __name__ == '__main__':
    unittest.main()