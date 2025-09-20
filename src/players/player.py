from abc import ABC, abstractmethod
from models.board import Board

class Player(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def get_move(self, board: Board):
        pass

    """
    Only preliminary validation of indexes is being done here
    """
    def validate_move(self, board: Board, row: int, col: int) -> bool:
        # return false in case either of row or column are out of bounds
        if (row > board.rows or row <= 0) or (col > board.cols or col <= 0):
            return False
        else:
            return True
    