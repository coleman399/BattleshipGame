from human import Human
from player import Player
from computer import Computer
from game_board import Gameboard

import sys
import random

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
            turn = True
            while self.player_one.health > 0 and self.player_two.health > 0:
                while turn: 
                    if self.attack(self.player_one, self.player_two) == 0:
                        turn = False
                    else:
                        loop = True
                        while(loop):
                            user_input = input("Would you like to play again(y/n)? ").lower()
                            if user_input == "y":
                                self.run_game()
                            elif user_input == "n":
                                print("              --- Thank You For Playing! ----")
                                sys.exit()
                            else:
                                print("Please use the 'y' and 'n' keys to make a selection.")
                else:
                    if self.attack(self.player_two, self.player_one) == 0:
                        turn = True
                    else:
                        loop = True
                        while(loop):
                            user_input = input("Would you like to play again(y/n)? ").lower()
                            if user_input == "y":
                                self.run_game()
                            elif user_input == "n":
                                print("              --- Thank You For Playing! ----")
                                sys.exit()
                            else:
                                print("Please use the 'y' and 'n' keys to make a selection.")
            else:
                loop = True
                while(loop):
                    user_input = input("Would you like to play again(y/n)? ").lower()
                    if user_input == "y":
                        self.run_game()
                    elif user_input == "n":
                        print("              --- Thank You For Playing! ----")
                        sys.exit()
                    else:
                        print("Please use the 'y' and 'n' keys to make a selection.")
        else:
            self.player_vs_ai()
            turn = True
            while self.player_one.health > 0 and self.computer.health > 0:
                while turn:
                    if self.attack(self.player_one, self.computer) == 0:
                        turn = False
                    else:
                        sys.exit()
                else:
                    if self.ai_attack(self.player_one, self.computer) == 0:
                        turn = True
                    else:
                        sys.exit()
            else:
                sys.exit()
    def welcome(self):
        print("                             --- Welcome to Battleship! ---")

    def display_board(self, player):
        try:
            if player.name == player.name:
                print(f"                             --- {player.name}'s GAME BOARD ---")
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
        self.player_one = Human(input("Player One's Name: "))
        self.player_two = Human(input("Player Two's Name: "))
        # creating each player's fleet
        self.display_board(self.player_one)
        self.player_one.fleet_list = self.create_fleet(self.player_one)
        self.display_board(self.player_two)
        self.player_two.fleet_list = self.create_fleet(self.player_two)


    def player_vs_ai(self):
        self.player_one = Human(input("Player One's Name: "))
        self.display_board(self.player_one)
        self.player_one.fleet_list = self.create_fleet(self.player_one)
        self.computer.fleet_list = self.ai_create_fleet(self.computer)

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
        row = -1
        column = -1
        while True: 
            if row < 0 or row > 9:
                if ship != None:
                    row = int(input(f"{player.name}: what row would you like to place your {ship.name}? "))
                else:
                    return
            elif column < 0 or column > 9:
                column = int(input(f"{player.name}: what column would you like to place your {ship.name}? "))
            else:
                return row, column

    def attack(self, attacker, defender):
        while attacker.health >= 0 and defender.health >= 0:
            try: 
                self.display_board(attacker)
                guess_row = int(input(f"{attacker.name}: What row would you like to fire at? "))
                guess_column = int(input(f"{attacker.name}: What column would you like to fire at? "))
                while not self.is_ocean(guess_row, guess_column, attacker.radar):
                    print("Invalid Shot")
                    guess_row = int(input(f"{attacker.name}: What row would you like to fire at? "))
                    guess_column = int(input(f"{attacker.name}: What column would you like to fire at? "))
                if defender.board[guess_row][guess_column] != self.game_board.ocean:
                    defender.health -= 1
                    if defender.health > 0:
                        attacker.radar[guess_row][guess_column] = self.game_board.hit
                        self.display_board(attacker)
                        print("HIT!")
                        return 0
                    else:
                        attacker.radar[guess_row][guess_column] = self.game_board.hit
                        self.display_board(attacker)
                        print(f"{attacker.name} Wins!")
                        return 1
                else:
                    attacker.radar[guess_row][guess_column] = self.game_board.miss
                    self.display_board(attacker)
                    print("MISS!")
                    return 0
            except:
                self.attack(attacker, defender)

    def ai_attack(self, player, computer):
        while player.health >= 0 and computer.health >= 0:
            try:
                self.display_board(computer)
                guess_row = random.randint(0, 9)
                guess_column = random.randint(0, 9)
                if player.board[guess_row][guess_column] != self.game_board.ocean:
                    player.health -= 1
                    if player.health > 0:
                        computer.radar[guess_row][guess_column] = self.game_board.hit
                        self.display_board(computer)
                        print("HIT!")
                        return 0
                    else:
                        computer.radar[guess_row][guess_column] = self.game_board.hit
                        self.display_board(computer)
                        print(f"{computer.name} Wins!")
                        return 1
                else:
                    computer.radar[guess_row][guess_column] = self.game_board.miss
                    self.display_board(computer)
                    print("MISS!")
                    return 0
            except:
                self.attack(player, computer)
    
    def ai_create_fleet(self, computer):
        for ship in computer.fleet_list:
            occupied = True
            set_ship = None
            if ship != None:
                while(occupied):
                    occupied = False
                    random_num = random.randint(0, 1)
                    x_coordinate = random.randint(0, 9)
                    y_coordinate = random.randint(0, 9)
                    coordinates = []
                    coordinates.append(x_coordinate)
                    coordinates.append(y_coordinate)
                    if random_num == 1:
                        ship.is_vertical = True
                    else:
                        ship.is_vertical = False
                    if (ship.is_vertical):
                        for p in range(ship.ship_length):
                            if not self.is_ocean(coordinates[0] + p, coordinates[1], computer.board):
                                computer.fleet_list.append(ship.set_location(coordinates[0], coordinates[1], ship.is_vertical))
                                occupied = True                            
                    else:
                        for p in range(ship.ship_length):
                            if not self.is_ocean(coordinates[0], coordinates[1] - p, computer.board):
                                occupied = True
                if(ship.is_vertical):
                    computer.board[coordinates[0]][coordinates[1]] = " ^ "
                    computer.board[coordinates[0] + ship.ship_length - 1][coordinates[1]] = " v "
                    if set_ship != None:
                        computer.number_board[coordinates[0]][coordinates[1]] = set_ship
                        computer.number_board[coordinates[0] + ship.ship_length - 1][coordinates[1]] = set_ship
                    for p in range(ship.ship_length - 2):
                        computer.board[coordinates[0] + p + 1][coordinates[1]] = " + "
                        if set_ship != None:
                            computer.number_board[coordinates[0] + p + 1][coordinates[1]] = set_ship
                else:
                    computer.board[coordinates[0]][coordinates[1]] = " > "
                    computer.board[coordinates[0]][coordinates[1] - ship.ship_length + 1] = " < "
                    if set_ship != None:
                        computer.number_board[coordinates[0]][coordinates[1]] = set_ship
                        computer.number_board[coordinates[0]][coordinates[1] - ship.ship_length + 1] = set_ship
                    for p in range(ship.ship_length - 2):
                        computer.board[coordinates[0]][coordinates[1] - p - 1] = " + "
                        if set_ship != None:
                            computer.number_board[coordinates[0]][coordinates[1] - p - 1] = set_ship

                self.display_board(computer)