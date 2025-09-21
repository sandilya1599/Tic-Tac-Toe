from src.game.game import Game
from src.models.board import Board
from src.models.enums import Turn, BoardState, Result
from src.players.human_player import HumanPlayer
from src.players.computer_player import ComputerPlayer
import unittest

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = HumanPlayer("Alice")
        self.player2 = ComputerPlayer("Bot")
        self.game = Game(self.player1, self.player2)
    
    def test_initial_state(self):
        self.assertEqual(self.game.turn, Turn.PLAYER1)  # PLAYER1
        self.assertEqual(self.game.state, BoardState.IN_PROGRESS)  # IN_PROGRESS
        self.assertEqual(self.game.result, Result.IN_PROGRESS)  # IN_PROGRESS
        self.assertIsInstance(self.game.board, Board)
        self.assertEqual(self.game.board.dim, 3)
    
    def test_switch_turn(self):
        self.assertEqual(self.game.turn, Turn.PLAYER1)
        self.game.switch_turn()
        self.assertEqual(self.game.turn, Turn.PLAYER2)
        self.game.switch_turn()
        self.assertEqual(self.game.turn, Turn.PLAYER1)
    
    def test_valid_move(self):
        self.assertTrue(self.game.valid_move(1, 1))  # Valid move
        self.game._update_board(1, 1)
        self.assertFalse(self.game.valid_move(1, 1))  # Cell already occupied
        self.assertFalse(self.game.valid_move(0, 0))  # Out of bounds
        self.assertFalse(self.game.valid_move(4, 4))  # Out of bounds
        self.assertFalse(self.game.valid_move(0, 1))  # Out of bounds
        self.assertFalse(self.game.valid_move(3, 4))  # Out of bounds
    
    def test_current_player_and_cell_value(self):
        self.assertEqual(self.game._get_current_player(), self.player1)
        self.game.switch_turn()
        self.assertEqual(self.game._get_current_player(), self.player2)

if __name__ == '__main__':
    unittest.main()