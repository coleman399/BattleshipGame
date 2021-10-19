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
        self.display_board()
        game_mode = self.choose_game_mode()
        if game_mode == True:
            self.player_vs_player()
        else:
            self.player_vs_ai()


    def welcome(self):
        print("--- welcome to battleship! ---")

    def display_board(self):
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
        self.player_two.fleet_list = self.create_fleet(self.player_two)

        self.player_one.game_board.print_gameboard()

    def player_vs_ai(self):
        self.player_one = Human(input("name of player one: "))
        self.player_one.fleet_list = self.create_fleet(self.player_one)
        self.computer.fleet_list = self.create_fleet(self.computer)

    def create_fleet(self, player):
        for ship in player.fleet_list:
            occupied = True
            is_vertical = None
            set_ship = None
            while(occupied):
                occupied = False
                try:# ToDo: make sure you fix input errors for row and column
                    row = int(input(f"what row would you like to place your {ship.name}? "))
                    column = int(input(f"what column would you like to place your {ship.name}? "))
                except:
                    print("Please use numbers 0 through 9 as inputs.")    
                self.set_vertical(ship)
                if ship.is_vertical == True:
                    for p in range(ship.ship_length):
                        if not self.game_board.is_ocean(row + p, column):
                            self.fleet_list[ship] = ship(row, column)
                            is_vertical = True
                            occupied = True
                            is_vertical = True
                else:
                    for p in range(ship.ship_length):
                        if not self.game_board.is_ocean(row, column - p):
                            is_vertical = False
                            occupied = True
            if is_vertical == True:
                player.board[row][column] = "^"
                player.board[row + ship.ship_length-1][column] = "v"
                if set_ship != None:
                    player.number_board[row][column] = set_ship
                    player.number_board[row + ship.ship_length - 1][column] = set_ship
                for p in range(ship.ship_length - 2):
                    player.board[row + p + 1][column] = "+"
                    if set_ship != None:
                        player.number_board[row + p + 1][column] = set_ship
            else:
                player.board[row][column] = ">"
                player.board[row][column - ship.ship_length + 1] = "<"
                if set_ship != None:
                    player.number_board[row][column] = set_ship
                    player.number_board[row][column - ship.ship_length + 1] = set_ship
                for p in range(ship.ship_length - 2):
                    player.board[row][column - p - 1] = "+"
                    if set_ship != None:
                        player.number_board[row][column - p - 1] = set_ship 

    def set_vertical(self, ship):
        loop = True
        while loop is True:
            answer = input(f"would you like {ship.name} placed vertically? ")
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
