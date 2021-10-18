from game_board import Gameboard
from fleet import Fleet
class Player(Fleet):

    def __init__(self):
        self.game_board = Gameboard()
        self.fleet_list = None
        self.player_health = 18
