from destroyer import Destroyer
from battleship_two import BattleshipTwo
from battleship_one import BattleshipOne
from aircraft_carrier import AircraftCarrier
from submarine import Submarine
from game_board import Gameboard

class Fleet:
    def __init__(self):
        self.fleet_list = [Destroyer(), BattleshipOne(), BattleshipTwo(), AircraftCarrier(), Submarine()]
        self.player_board = Gameboard()

    def create_fleet(self):
        for ship in self.fleet_list:
            occupied = True
            while(occupied):
                occupied = False
                row = input(f"what row would you like to place your {ship.name}? ")
                column = input(f"what column would you like to place your {ship.name}? ")
                if ship.vertical == True:
                    for p in range(ship.ship_length):
                        if not self.player_board.is_ocean(row + p, column, self.player_board):
                            self.fleet_list[ship] = ship(row, column)
                            occupied = True
                else:
                    for p in range(ship.ship_length):
                        if not self.player_board.is_ocean(row, column - p, self.player_board):
                            occupied = True
            