from src.models.board_evaluator import BoardEvaluator
from src.models.board import Board
from src.models.enums import Result
from src.models.cell_values import CellValue
import unittest

class TestBoardEvaluator(unittest.TestCase):
    def test_evaluate_board_player1_wins_row(self):
        board = Board(3)
        board.set_cell(0, 0, CellValue.Player1)
        board.set_cell(0, 1, CellValue.Player1)
        board.set_cell(0, 2, CellValue.Player1)
        result = BoardEvaluator.evaluate_board(board)
        self.assertEqual(result, Result.PLAYER1)
    
    def test_evaluate_board_player2_wins_row(self):
        board = Board(3)
        board.set_cell(0, 0, CellValue.Player2)
        board.set_cell(0, 1, CellValue.Player2)
        board.set_cell(0, 2, CellValue.Player2)
        result = BoardEvaluator.evaluate_board(board)
        self.assertEqual(result, Result.PLAYER2)
    
    def test_evaluate_board_in_progress(self):
        board = Board(3)
        result = BoardEvaluator.evaluate_board(board)
        self.assertEqual(result, Result.IN_PROGRESS)

    def test_evaluate_board_draw(self):
        board = Board(3)
        board.set_cell(0, 0, CellValue.Player1)
        board.set_cell(0, 1, CellValue.Player2)
        board.set_cell(0, 2, CellValue.Player1)
        board.set_cell(1, 0, CellValue.Player2)
        board.set_cell(1, 1, CellValue.Player1)
        board.set_cell(1, 2, CellValue.Player2)
        board.set_cell(2, 0, CellValue.Player2)
        board.set_cell(2, 1, CellValue.Player1)
        board.set_cell(2, 2, CellValue.Player2)
        result = BoardEvaluator.evaluate_board(board)
        self.assertEqual(result, Result.DRAW)

    def test_is_draw_true(self):
        board = Board(3)
        for row in range(3):
            for col in range(3):
                board.set_cell(row, col, CellValue.Player1 if (row + col) % 2 == 0 else CellValue.Player2)
        self.assertTrue(BoardEvaluator.is_draw(board))


if __name__ == '__main__':
    unittest.main()