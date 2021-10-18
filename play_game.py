from human import Human
from game_board import Gameboard
from fleet import Fleet
from player import Player
from computer import Computer
class PlayGame:
    def __init__(self):
        self.game_board = Gameboard()
        self.fleet = Fleet()
        self.player_one = Player()
        self.player_two = Player()
        self.computer = Computer()
    
    def play_game(self):
        self.welcome()
        self.display_rules()
        game_mode = self.choose_game_mode()
        if game_mode == True:
            self.player_vs_player()
        else:
            self.player_vs_ai()
        self.display_board()
        self.place_fleet()

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
                print("\n--- PVP GAME ---")
                return True
            elif user_input == '2':
                print("\n--- PVE GAME ---")
                return False
        except:
            print(f'Please enter one of the valid inputs')
            return self.choose_game_mode()

    def place_fleet(self):
        pass

    def player_vs_player(self):
        # Getting names of players
        self.player_one = Human(input("name of player one: "))
        self.player_two = Human(input("name of player two: "))
        # creating each player's fleet
        self.player_one.fleet_list.append(self.player_one.create_fleet())
        self.player_two.fleet_list.append(self.player_two.create_fleet())

    def player_vs_ai(self):
        self.player_one = Human(input("name of player one: "))
        self.player_one.fleet_list.append(self.player_one.create_fleet())