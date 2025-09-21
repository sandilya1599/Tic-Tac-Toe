from players.player import Player
from models.board import Board
from models.cell_values import CellValue
from models.enums import BoardState, Turn, Result
from models.board_evaluator import BoardEvaluator

class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self._set_defaults()
    
    """
    Helper function to  set default values
    """
    def _set_defaults(self):
        self.turn = Turn.PLAYER1 # defaults to player 1
        self.state = BoardState.IN_PROGRESS # defaults
        self.result = Result.IN_PROGRESS # defaults
        self.board = Board(3)

    """
    Helper function to get current player
    """
    def _get_current_player(self) -> Player:
        if self.turn == Turn.PLAYER1:
            return self.player1
        else:
            return self.player2
    
    """
    Helper function to get cell value to update
    """
    def _get_cell_value(self) -> CellValue:
        if self.turn == Turn.PLAYER1:
            return CellValue.Player1
        else:
            return CellValue.Player2

    """
    Helper function to Update board for a valid move
    """
    def _update_board(self, row: int, col: int) -> None:
        normalized_row = row - 1
        normalized_col = col - 1

        cell_value = self._get_cell_value()
        self.board.set_cell(normalized_row, normalized_col, cell_value)

    """
    Switches turn
    """
    def switch_turn(self):
        if self.turn == Turn.PLAYER1:
            self.turn = Turn.PLAYER2
        else:
            self.turn = Turn.PLAYER1    

    """
    Validates Move
    """
    def valid_move(self, row: int, col: int) -> bool:
        # first check if that row, col is occupied
        normalised_row = (row - 1)
        normalised_col = (col - 1)

        # Check that cell is not occupied
        if self.board.get_cell(normalised_row, normalised_col) != CellValue.Empty:
            return False
        else:
            return True

    """
    Helper function to update winner
    """
    def _update_winner(self, result: Result) -> None:
        self.state = BoardState.COMPLETED
        self.result = result

    """
    Asks current player to make a move
    """
    def play(self):
        while self.state == BoardState.IN_PROGRESS:
            print('State of board before update:')
            self.board.display()
            print()
            
            # get current player
            current_player = self._get_current_player()

            # Do this until the current player gives a valid move
            while True:
                # ask them to make a move
                (row, col) = current_player.get_move(self.board)

                # check for its validity
                if self.valid_move(row, col):
                    self._update_board(row, col)
                    # If current move is valid, check for winner
                    result = BoardEvaluator.evaluate_board(self.board)
                    if result == Result.IN_PROGRESS:
                        # switch turn if game is still in progress
                        self.switch_turn()
                    else:
                        # If not update winner
                        self._update_winner(result)
                    break
            # Display only for a valid move
            print('State of board after update:')
            self.board.display()
            print()