from player import Player
class Fleet(Player):
    def __init__(self):
        self.player = Player()
        super().__init__()

    def create_fleet(self):
        for ship in self.player.fleet_list:
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
