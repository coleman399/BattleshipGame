from human import Human
from player import Player
from computer import Computer
from game_board import Gameboard

class RunGame:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
        self.computer = Computer()
        self.game_board = Gameboard()
    
    def run_game(self):
        self.welcome()
        self.display_rules()
        self.display_board(self.player_one)
        game_mode = self.choose_game_mode()
        if game_mode == True:
            self.player_vs_player()
        else:
            self.player_vs_ai()

    def welcome(self):
        print("--- welcome to battleship! ---")

    def display_board(self, player):
        try:
            if player.name == player.name:
                print(f"                              --- PLAYER {player.name}'s GAME BOARD ---")
                player.game_board.print_gameboard()
        except:
            self.game_board.print_gameboard()
    def display_rules(self):
        pass

    def choose_game_mode(self):
        try:
            user_input = input(f'Please select your game mode:\nEnter 1 for Player VS Player.\nEnter 2 for Player VS AI.\nSelection: ')
            if user_input == '1':
                print("\n--- PVP GAME ---\n")
                return True
            elif user_input == '2':
                print("\n--- PVE GAME ---\n")
                return False
        except:
            print(f'Please enter one of the valid inputs')
            return self.choose_game_mode()

    def player_vs_player(self):
        # Getting names of players
        self.player_one = Human(input("name of player one: "))
        self.player_two = Human(input("name of player two: "))
        # creating each player's fleet
        self.player_one.fleet_list = self.create_fleet(self.player_one)
        self.display_board(self.player_one)
        self.player_two.fleet_list = self.create_fleet(self.player_two)
        self.display_board(self.player_two)

    def player_vs_ai(self):
        self.player_one = Human(input("name of player one: "))
        self.player_one.fleet_list = self.create_fleet(self.player_one)
        self.computer.fleet_list = self.create_fleet(self.computer)

    # When ships are placed on the board horizontally the are placed at the desired (x, y) coordinate then "grow" to the left.
    #                    0   1   2   3   4
    # example: (0, 4) = [ ]  <   +   +   >
    # while ships are placed vertically the ships "grows" down
    # example: (0, 0) = 0  1   2   3
    #                 0 ^ [ ] [ ] [ ]
    #                 1 + [ ] [ ] [ ]
    #                 2 + [ ] [ ] [ ] 
    #                 3 v [ ] [ ] [ ]

    def create_fleet(self, player):
        for ship in player.fleet_list:
            occupied = True
            set_ship = None
            while(occupied):
                occupied = False
                coordinates = (self.check_coordinates(player, ship))
                self.set_vertical(player, ship)
                if ship.is_vertical == True:
                    for p in range(ship.ship_length):
                        if not self.is_ocean(coordinates[0] + p, coordinates[1], player.board):
                            player.fleet_list.append(ship.set_location(coordinates[0], coordinates[1], ship.is_vertical))
                            occupied = True
                            continue
                else:
                    for p in range(ship.ship_length):
                        if not self.is_ocean(coordinates[0], coordinates[1] - p, player.board):
                            occupied = True
                            continue
                if(occupied): 
                    print("Please select another location.")
            if ship.is_vertical == True:
                player.board[coordinates[0]][coordinates[1]] = " ^ "
                player.board[coordinates[0] + ship.ship_length-1][coordinates[1]] = " v "
                if set_ship != None:
                    player.number_board[coordinates[0]][coordinates[1]] = set_ship
                    player.number_board[coordinates[0] + ship.ship_length - 1][coordinates[1]] = set_ship
                for p in range(ship.ship_length - 2):
                    player.board[coordinates[0] + p + 1][coordinates[1]] = " + "
                    if set_ship != None:
                        player.number_board[coordinates[0] + p + 1][coordinates[1]] = set_ship
            else:
                player.board[coordinates[0]][coordinates[1]] = " > "
                player.board[coordinates[0]][coordinates[1] - ship.ship_length + 1] = " < "
                if set_ship != None:
                    player.number_board[coordinates[0]][coordinates[1]] = set_ship
                    player.number_board[coordinates[0]][coordinates[1] - ship.ship_length + 1] = set_ship
                for p in range(ship.ship_length - 2):
                    player.board[coordinates[0]][coordinates[1] - p - 1] = " + "
                    if set_ship != None:
                        player.number_board[coordinates[0]][coordinates[1] - p - 1] = set_ship
            self.display_board(player)

    def set_vertical(self, player, ship):
        loop = True
        while loop is True:
            answer = input(f"{player.name}: would you like {ship.name} placed vertically? ")
            if answer == "y":
                ship.is_vertical = True
                loop = False
                continue
            elif answer == "n":
                ship.is_vertical = False
                loop = False
                continue
            else:
                print("please use the 'y' or 'n' keys to make a selection.")

    def is_ocean(self, row, column, board):
        if row < 0 or row >= self.game_board.gameboard_size:
            return 0
        elif column < 0 or column >= self.game_board.gameboard_size:
            return 0
        if board[row][column] == self.game_board.ocean:
            return 1
        else:
            return 0

    def check_coordinates(self, player, ship):
        # TODO: inform user of ship length when asking for coordinates
        try:
            row = int(input(f"{player.name}: what row would you like to place your {ship.name}? "))
            column = int(input(f"{player.name}: what column would you like to place your {ship.name}? "))
            return row, column
        except:
            print("Please use numbers 0 through 9 as inputs.")
            self.check_coordinates(player, ship) 
