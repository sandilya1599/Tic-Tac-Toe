from enum import Enum


class BoardState(Enum):
    IN_PROGRESS = 0
    COMPLETED = 1

class Result(Enum):
    DRAW = 0
    PLAYER1 = 1
    PLAYER2 = 2
    IN_PROGRESS = 3

class Turn(Enum):
    PLAYER1 = 1
    PLAYER2 = 2