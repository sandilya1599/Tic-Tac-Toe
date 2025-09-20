from .enums import Result
from .cell_values import CellValue
from .board import Board

class BoardEvaluator:

    """
    For evaluating board
    """
    @staticmethod
    def evaluate_board(board: Board):
        if BoardEvaluator.is_draw(board):
            return Result.DRAW
        else:
            # Default result is in progress
            result = Result.IN_PROGRESS
            # perform validation on ROWS
            for row in range(board.rows):
                if board.get_cell(row, 0) == board.get_cell(row, 1) == board.get_cell(row, 2):
                    if board.get_cell(row, 0) == CellValue.Player1:
                        result = Result.PLAYER1
                    elif board.get_cell(row, 0) == CellValue.Player2:
                        result = Result.PLAYER2
            # perform validation on columns
            for col in range(board.cols):
                if board.get_cell(0, col) == board.get_cell(1, col) == board.get_cell(2, col):
                    if board.get_cell(0, col) == CellValue.Player1:
                        result = Result.PLAYER1
                    elif board.get_cell(0, col) == CellValue.Player2:
                        result = Result.PLAYER2
            
            # perform validation on cross
            if board.get_cell(0, 0) == board.get_cell(1, 1) == board.get_cell(2, 2) \
                or  board.get_cell(0, 2) == board.get_cell(1, 1) == board.get_cell(2, 0):
                if board.get_cell(1,1) == CellValue.Player1:
                    result = Result.PLAYER1
                elif board.get_cell(1,1) == CellValue.Player2:
                    result = Result.PLAYER2
            
            # Only current player can be winner, since he has played
            return result

    """
    Checks for Draw
    """
    @staticmethod
    def is_draw(board: Board):
        if board.move_count == board.rows * board.cols:
            return True
        else:
            return False
    
    """
    Check score
    """
    @staticmethod
    def score(result, depth):
        if result == Result.PLAYER2:  # AI wins
            return 10 - depth
        elif result == Result.PLAYER1:  # Human wins
            return depth - 10
        else:  # Draw
            return 0

