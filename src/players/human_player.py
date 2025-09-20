from .player import Player
from models.board import Board

class HumanPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        

    """
    Read input from User here
    """
    def get_move(self, board: Board) -> tuple:
        
        while True:
            row = int(input('Enter row:'))
            column = int(input('Enter col:'))

            if self.validate_move(board, row, column):
                break
            else:
                print('Invalid row and column are entered.\n Please enter again.')
        
        return (row, column)
