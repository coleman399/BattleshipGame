from destroyer import Destroyer
from battleship_two import BattleshipTwo
from battleship_one import BattleshipOne
from aircraft_carrier import AircraftCarrier
from submarine import Submarine

class Fleet:
    def __init__(self):
        self.fleet_list = []

    def fleet(self):
        aircraft_carrier = AircraftCarrier(int(input("what row would you like your Aircraft Carrier? ")), int(input("what column would you like your Aircraft Carrier? ")))
        battleship_one = BattleshipOne(int(input(f"what row would you like Battleship 1? ")), int(input(f"what column would you like Battleship 1? ")))
        battleship_two = BattleshipTwo(int(input(f"what row would you like Battleship 2? ")), int(input(f"what column would you like Battleship 2? ")))
        submarine = Submarine(int(input(f"what row would you like your Submarine? ")), int(input(f"what column would you like your Submarine? ")))
        destroyer = Destroyer(int(input(f"what row would you like your Destroyer? ")), int(input(f"what column would you like your Destroyer? ")))

        self.fleet_list.append(aircraft_carrier)
        self.fleet_list.append(battleship_one)
        self.fleet_list.append(battleship_two)
        self.fleet_list.append(destroyer)
        self.fleet_list.append(submarine)