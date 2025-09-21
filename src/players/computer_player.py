from .player import Player
from ..models.board import Board
from ..models.cell_values import CellValue
import json
import os

class ComputerPlayer(Player):
    def __init__(self, name, depth_limit=None):
        super().__init__(name)
        self.depth_limit = depth_limit  # optional
        self._read_board_data()

    """
    Helper function to read JSON file
    """
    def _read_board_data(self):
        base_dir = os.path.dirname(__file__)
        path = os.path.join(base_dir, '../output/minmax.json')
        with open(path, 'r') as json_file:
            self.data = json.load(json_file)
    

    """
    Helper function to get best move for given board
    """
    def _get_best_move(self, board: Board):
        # Convert it to tuple
        board_tuple = board.to_tuple()
        # to string
        key = str(board_tuple)

        # Check if key has a best move
        for obj in self.data:
            if obj['board'] == key and obj['maximizing'] == True:
                move = obj['best_move']

        # return some random value if no best move        
        if move == None:
            for row in range(board.dim):
                for col in range(board.dim):
                    if board.get_cell(row, col) == CellValue.Empty:
                        move = (row,col)
                        break
        move = self._normalize_move(move)
        return move
    
    """
    Normalize computers move
    """
    def _normalize_move(self, move : tuple):
        row = move[0] + 1
        col = move[1] + 1
        return (row, col)

    """
    Entry point for the player
    """
    def get_move(self, board: Board):
        move = self._get_best_move(board)
        return move