from copy import deepcopy
from .player import Player
from models.board import Board
from models.enums import Turn, Result
from models.cell_values import CellValue
from models.board_evaluator import BoardEvaluator

class ComputerPlayer(Player):
    def __init__(self, name, depth_limit=None):
        super().__init__(name)
        self.depth_limit = depth_limit  # optional

    """
    Entry point for the player
    """
    def get_move(self, board):
        best_score = float('-inf')
        best_move = None

        # Loop over all empty cells
        for row in range(board.dim):
            for col in range(board.dim):
                if board.get_cell(row, col) == CellValue.Empty:
                    board_copy = board
                    board_copy.set_cell(row, col, CellValue.Player2)  # AI is O
                    score = self.minimax(board_copy, depth=0, maximizing=False)
                    board_copy.set_cell(row, col, CellValue.Empty)  # AI is O
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move
    

    """
    Mini Max Algorithm Logic
    """
    def minimax(self, board, depth, maximizing):
        result = BoardEvaluator.evaluate_board(board)
        if result != Result.IN_PROGRESS or (self.depth_limit and depth >= self.depth_limit):
            return BoardEvaluator.score(result, depth)

        if maximizing:
            best_score = float('-inf')
            for row in range(board.dim):
                for col in range(board.dim):
                    if board.get_cell(row, col) == CellValue.Empty:
                        board_copy = board
                        board_copy.set_cell(row, col, CellValue.Player2)
                        score = self.minimax(board_copy, depth + 1, False)
                        board_copy.set_cell(row, col, CellValue.Empty)
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(board.dim):
                for col in range(board.dim):
                    if board.get_cell(row, col) == CellValue.Empty:
                        board_copy = board
                        board_copy.set_cell(row, col, CellValue.Player1)
                        score = self.minimax(board_copy, depth + 1, True)
                        board_copy.set_cell(row, col, CellValue.Empty)
                        best_score = min(best_score, score)
            return best_score