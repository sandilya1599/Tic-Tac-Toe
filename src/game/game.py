from players.player import Player
from models.board import Board
from models.cell_values import CellValue
from models.enums import BoardState, Turn, Result
from models.board_evaluator import BoardEvaluator

class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.__set_defaults__()
    
    """
    Helper function to  set default values
    """
    def __set_defaults__(self):
        self.turn = Turn.PLAYER1 # defaults to player 1
        self.state = BoardState.IN_PROGRESS # defaults
        self.result = Result.IN_PROGRESS # defaults
        self.board = Board(3)

    """
    Helper function to get current player
    """
    def __get_current_player__(self) -> Player:
        if self.turn == Turn.PLAYER1:
            return self.player1
        else:
            return self.player2
    
    """
    Helper function to get cell value to update
    """
    def __get_cell_value__(self) -> CellValue:
        if self.turn == Turn.PLAYER1:
            return CellValue.Player1
        else:
            return CellValue.Player2

    """
    Helper function to Update board for a valid move
    """
    def __update_board__(self, row: int, col: int) -> None:
        normalized_row = row - 1
        normalized_col = col - 1

        cell_value = self.__get_cell_value__()
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
    def __update_winner__(self, result: Result) -> None:
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
            current_player = self.__get_current_player__()

            # Do this until the current player gives a valid move
            while True:
                # ask them to make a move
                (row, col) = current_player.get_move(self.board)

                # check for its validity
                if self.valid_move(row, col):
                    self.__update_board__(row, col)
                    # If current move is valid, check for winner
                    result = BoardEvaluator.evaluate_board(self.board)
                    if result == Result.IN_PROGRESS:
                        # switch turn if game is still in progress
                        self.switch_turn()
                    else:
                        # If not update winner
                        self.__update_winner__(result)
                    break
            # Display only for a valid move
            print('State of board after update:')
            self.board.display()
            print()