from ..models.board import Board
from ..models.board_evaluator import BoardEvaluator
from ..models.cell_values import CellValue
from ..models.enums import Result, Turn
import json

state_map = {}

def minimax(board: Board, depth: int, maximizing: bool):
    # Create a unique key for the current board state and turn
    # This ensures that we cache the result for a specific board configuration
    # for a specific player's turn.
    board_tuple = board.to_tuple() # Assuming a method to get board data
    state_key = (board_tuple, maximizing)
    best_move = None
    
    # Check if the state has already been computed
    if state_key in state_map:
        return state_map[state_key][0]

    result = BoardEvaluator.evaluate_board(board)

    # Base case: a terminal state has been reached
    if result != Result.IN_PROGRESS:
        score = BoardEvaluator.score(result, depth)
        state_map[state_key] = (score, best_move) # Cache the result before returning
        return score

    if maximizing:
        best_score = float('-inf')
        for row in range(board.dim):
            for col in range(board.dim):
                if board.get_cell(row, col) == CellValue.Empty:
                    board.set_cell(row, col, CellValue.Player2)
                    score = minimax(board, depth + 1, False)
                    board.set_cell(row, col, CellValue.Empty)
                    if score >= best_score:
                        best_move = (row, col)
                        best_score = score
        state_map[state_key] = (best_score, best_move) # Cache the result
        return best_score
    else:
        best_score = float('inf')
        for row in range(board.dim):
            for col in range(board.dim):
                if board.get_cell(row, col) == CellValue.Empty:
                    board.set_cell(row, col, CellValue.Player1)
                    score = minimax(board, depth + 1, True)
                    board.set_cell(row, col, CellValue.Empty)
                    if score <= best_score:
                        best_move = (row, col)
                        best_score = score

        
        state_map[state_key] = (best_score, best_move) # Cache the result
        return best_score

def play(board: Board, turn: Turn):
    minimax(board, 0, turn == Turn.PLAYER2)

"""
Store as a string
"""
def to_str(self):
    return ''.join(str(self.get_cell(r, c).value) for r in range(self.dim) for c in range(self.dim))

if __name__ == "__main__":
    # create an empty board
    board = Board(dim=3)

    play(board, Turn.PLAYER1)
    play(board, Turn.PLAYER2)

    with open('minmax.json', 'w') as json_file:
        json.dump([
            {
                'board': str(key[0]),
                'maximizing': key[1],
                'score': value[0],
                'best_move': value[1] 
            } for key,value in state_map.items()
        ],
        json_file,
        indent= 4)