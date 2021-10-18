from aircraft_carrier import AircraftCarrier
from battleship_one import BattleshipOne
from battleship_two import BattleshipTwo
from destroyer import Destroyer
from submarine import Submarine
class Player():

    def __init__(self):
        self.player_health = 18
        self.fleet_list = [AircraftCarrier(0, 0), BattleshipOne(0, 0), BattleshipTwo(0, 0), Destroyer(0, 0), Submarine(0, 0)]
        self.player_board = []
        self.player_radar = []