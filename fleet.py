from ship import Ship
class Fleet():
    def __init__(self):
        self.fleet_list = []
        self.build_fleet()

    def build_fleet(self):
        self.aircraft_carrier = Ship("Aircraft Carrier", 5)
        self.battleship_1 = Ship("Battleship 1", 4)
        self.battleship_2 = Ship("Battleship 2", 4)
        self.submarine = Ship("Submarine", 3)
        self.destroyer = Ship("Destroyer", 2)

        self.fleet_list.append(self.aircraft_carrier)
        self.fleet_list.append(self.battleship_1)
        self.fleet_list.append(self.battleship_2)
        self.fleet_list.append(self.submarine)
        self.fleet_list.append(self.destroyer)

    def place_fleet(self, row, column, is_vertical):
        self.aircraft_carrier = self.aircraft_carrier.set_location(row, column, is_vertical)
        self.battleship_1 = self.battleship_1.set_location(row, column, is_vertical)
        self.battleship_2 = self.battleship_2.set_location(row, column, is_vertical)
        self.submarine = self.submarine.set_location(row, column, is_vertical)
        self.destroyer = self.destroyer.set_location(row, column, is_vertical)

        self.fleet_list.append(self.aircraft_carrier)
        self.fleet_list.append(self.battleship_1)
        self.fleet_list.append(self.battleship_2)
        self.fleet_list.append(self.submarine)
        self.fleet_list.append(self.destroyer)