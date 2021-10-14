from game_board import Gameboard
from fleet import Fleet


class PlayGame:
    def __init__(self):
        self.game_board = Gameboard()
        self.fleet = Fleet()
        self.player_one = ""
        self.player_two = ""
    
    def play_game(self):
        self.display_board()
        self.place_fleet()

    def display_board(self):
        self.game_board.print_gameboard()

    def place_fleet(self):
        self.fleet.fleet()