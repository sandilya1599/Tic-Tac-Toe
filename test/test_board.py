import unittest
from src.models.board import Board
from src.models.enums import Result
from src.models.cell_values import CellValue

class TestBoard(unittest.TestCase):
    def test_board_initialization(self):
        board = Board(3)
        self.assertEqual(board.dim, 3)
        self.assertEqual(board.move_count, 0)
        for row in range(3):
            for col in range(3):
                self.assertEqual(board.get_cell(row, col), CellValue.Empty)

    def test_board_move(self):
        board = Board(3)
        board.set_cell(0, 0, CellValue.Player1)
        self.assertEqual(board.get_cell(0, 0), CellValue.Player1)
        self.assertEqual(board.move_count, 1)

    def test_to_tuple(self):
        board = Board(2)
        board.set_cell(0, 0, CellValue.Player1)
        board.set_cell(1, 1, CellValue.Player2)
        expected_tuple = (
            (CellValue.Player1.value, CellValue.Empty.value, CellValue.Empty.value, CellValue.Player2.value)
        )
        self.assertEqual(board.to_tuple(), expected_tuple)

if __name__ == '__main__':
    unittest.main()