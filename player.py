from game_board import Gameboard
from fleet import Fleet
class Player():

    def __init__(self):
        self.health = 2
        self.fleet = Fleet()
        self.game_board = Gameboard()
        self.fleet_list = self.fleet.fleet_list
        self.board = self.game_board.board
        self.radar = self.game_board.radar
        self.number_board = self.game_board.number_board
