from destroyer import Destroyer
from battleship_two import BattleshipTwo
from battleship_one import BattleshipOne
from aircraft_carrier import AircraftCarrier
from submarine import Submarine

class Fleet:
    def __init__(self):
        self.fleet_list = []
        self.fleet()

    def fleet(self):
        aircraft_carrier = AircraftCarrier(False, 1, 1)
        battleship_one = BattleshipOne(False, 1, 1)
        battleship_two = BattleshipTwo(False, 1, 1)
        destroyer = Destroyer(False, 1, 1)
        submarine = Submarine(False, 1, 1)
        self.fleet_list.append(aircraft_carrier)
        self.fleet_list.append(battleship_one)
        self.fleet_list.append(battleship_two)
        self.fleet_list.append(destroyer)
        self.fleet_list.append(submarine)