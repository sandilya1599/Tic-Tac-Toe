from game.game import Game
from players.human_player import HumanPlayer
from players.computer_player import ComputerPlayer
from models.enums import Result

def initialize_game() -> Game:
    player1 = HumanPlayer('Hooman')
    player2 = ComputerPlayer('Kamputa', depth_limit=2)
    return Game(player1, player2)


def game_play_loop(game : Game):
    # Start the gameplay loop
    game.play()

    if game.result != Result.IN_PROGRESS:
        print(f'Game completed. Winner is {game.result}')

if __name__ == "__main__":
    game = initialize_game()
    game_play_loop(game)