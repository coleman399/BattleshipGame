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
        self.player_one_fleet = self.player_one.fleet.build_fleet()
        self.player_two_fleet = self.player_two.fleet.build_fleet()
        self.computer_fleet = self.computer.fleet.build_fleet()
    
    def run_game(self):
        self.welcome()
        self.display_rules()
        game_mode = self.choose_game_mode()
        if game_mode == 1:
            self.player_vs_player()
            self.turn(self.player_one, self.player_two)
        if game_mode == 2:
            self.player_vs_ai()
            self.turn(self.player_one, self.computer)    

    def welcome(self):
        print("\n----------------------------------  Welcome to Battleship!  ---------------------------------------------------\n")

    def display_board(self, player):
        try:
            if player.name == player.name:
                print(f"\n{player.name}'s GAME BOARD: ")
                player.game_board.print_gameboard()
        except:
            self.game_board.print_gameboard()
    
    def display_rules(self):
        print("First to find and destroy their enemy fleet wins!")
        print("\n                                    ---  Remember!  ---\n")
        print("When ships are placed on the board horizontally, they are placed at a desired (x, y) coordinate then 'grow' \nto the left.\n")
        print("                      0   1   2   3 ")
        print("Example: (0, 3) = 0  [ ]  <   +   > ")
        print("Submarine(size 3) 1  [ ] [ ] [ ] [ ]\n")
        print("While ships are placed vertically the ships 'grows' down.\n")
        print("                      0   1   2   3 ")
        print("Example: (0, 0) =  0  ^  [ ] [ ] [ ]")
        print("Submarine(size 3)  1  +  [ ] [ ] [ ]")
        print("                   2  +  [ ] [ ] [ ]")
        print("                   3  v  [ ] [ ] [ ]\n")
        print("If you attempt to place a ship that will grow outside board you will be asked to provide new coordinates.")
        print("\n                                    ---  Game Legend  ---\n")
        print("Ocean = [ ]")
        print("Miss  = [O]")
        print("Hit   = [X]")
        print("\n------------------------------  Good Luck and Have Fun!  ------------------------------------------------------\n")

    def choose_game_mode(self):
        try:
            user_input = input(f"Please select your game mode:\nEnter '1' for Player VS Player.\nEnter '2' for Player VS Environment.\nSelection: ")
            if user_input == '1':
                print("\n                                   --- PVP GAME ---\n")
                return 1
            elif user_input == '2':
                print("\n                                   --- PVE GAME ---\n")
                return 2
            else:
                print(f"Please use the '1' or '2' keys to make a selection.")
                return self.choose_game_mode()
        except:
            return

    def player_vs_player(self):
        # Getting names of players
        self.player_one = Human(input("Player One's Name: "))
        self.player_two = Human(input("Player Two's Name: "))
        # creating each player's fleet
        self.display_board(self.player_one)
        self.player_one_fleet = self.create_fleet(self.player_one)
        self.display_board(self.player_two)
        self.player_two_fleet = self.create_fleet(self.player_two)


    def player_vs_ai(self):
        self.player_one = Human(input("Player One's Name: "))
        self.display_board(self.player_one)
        self.player_one_fleet = self.create_fleet(self.player_one)
        self.computer_fleet = self.ai_create_fleet(self.computer)

    def create_fleet(self, player):
        for ship in player.fleet_list:
            occupied = True
            set_ship = None
            while(occupied):
                occupied = False
                coordinates = self.check_coordinates(player, ship)
                self.set_vertical(player, ship)
                if ship.is_vertical == True:
                    for p in range(ship.ship_length):
                        if not self.is_ocean(coordinates[0] + p, coordinates[1], player.board):
                            occupied = True
                            continue
                else:
                    for p in range(ship.ship_length):
                        if not self.is_ocean(coordinates[0], coordinates[1] - p, player.board):
                            occupied = True
                            continue
                if occupied == True:
                    print("\n                            ---- Invalid Coordinates! ----\n")
                    print("                                 ---- Try Again! ----")
                    self.display_board(player)
                if occupied == False:             
                    if ship.is_vertical == True:
                        ship.set_location(coordinates[0], coordinates[1], ship.is_vertical)
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
                        ship.set_location(coordinates[0], coordinates[1], ship.is_vertical)
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
            answer = input(f"{player.name}: would you like {ship.name} placed vertically? ").lower()
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
        coordinates = None
        loop = True
        while loop:
            if ship != None:
                try:
                    row = int(input(f"{player.name}: What row would you like to place your {ship.name}(size: {ship.ship_length})? "))
                    column = int(input(f"{player.name}: What column would you like to place your {ship.name}(size: {ship.ship_length})? "))
                except ValueError:
                    print("Using number keys, select '1' through '9' for coordinates.")
                    continue
                else:
                    if row in range(0, 9) and column in range(0, 9):
                        coordinates = (row, column)
                        return coordinates
    
    def attack(self, attacker, defender):
        while attacker.health > 0 and defender.health > 0:
            try: 
                self.display_board(attacker)
                guess_row = int(input(f"{attacker.name}: What row would you like to fire at? "))
                guess_column = int(input(f"{attacker.name}: What column would you like to fire at? "))
                while not self.is_ocean(guess_row, guess_column, attacker.radar):
                    print("                             --- Invalid Shot! ----")
                    guess_row = int(input(f"{attacker.name}: What row would you like to fire at? "))
                    guess_column = int(input(f"{attacker.name}: What column would you like to fire at? "))
                if defender.board[guess_row][guess_column] != self.game_board.ocean:
                    defender.health -= 1
                    if defender.health > 0:
                        attacker.radar[guess_row][guess_column] = self.game_board.hit
                        defender.board[guess_row][guess_column] = self.game_board.hit
                        print(f"\n                                 ----  {attacker.name} HIT!  ----\n")
                        return
                    else:
                        attacker.radar[guess_row][guess_column] = self.game_board.hit
                        defender.board[guess_row][guess_column] = self.game_board.hit
                        print(f"\n                                 ----  {attacker.name} WINS!  ----")
                        self.display_board(attacker)
                        return
                else:
                    attacker.radar[guess_row][guess_column] = self.game_board.miss
                    defender.board[guess_row][guess_column] = self.game_board.miss
                    print(f"\n                                 ----  {attacker.name} MISSED!  ----\n")
                    return
            except:
                self.attack(attacker, defender)

    def ai_attack(self, player, computer):
        while player.health > 0 and computer.health > 0:
                guess_row = random.randint(0, 9)
                guess_column = random.randint(0, 9)
                if player.board[guess_row][guess_column] != self.game_board.ocean:
                    player.health -= 1
                    if player.health > 0:
                        computer.radar[guess_row][guess_column] = self.game_board.hit
                        player.board[guess_row][guess_column] = self.game_board.hit
                        print(f"\n                         ----  The {computer.name} fires at ({guess_row},{guess_column})!  ----\n")
                        print(f"\n                            ----  The {computer.name} HIT!  ----\n")
                        return
                    else:
                        computer.radar[guess_row][guess_column] = self.game_board.hit
                        player.board[guess_row][guess_column] = self.game_board.hit
                        print(f"\n                         ----  The {computer.name} fires at ({guess_row},{guess_column})!  ----\n")
                        print(f"\n                            ----  The {computer.name} WINS!  ----")
                        self.display_board(computer)
                        return
                else:
                    computer.radar[guess_row][guess_column] = self.game_board.miss
                    player.board[guess_row][guess_column] = self.game_board.miss
                    print(f"\n                         ----  The {computer.name} fires at ({guess_row},{guess_column})!  ----\n")
                    print(f"\n                            ----  The {computer.name} MISSED!  ----\n")
                    return
    
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
                    if occupied == False:
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
    
    def turn(self, player1, player2):
        turn = 1
        while player1.health > 0 and player2.health > 0:
            if player2.name == "Computer":
                if turn == 1:
                    self.attack(player1, player2)
                    turn = 2
                if turn == 2:
                    self.ai_attack(player1, player2)
                    turn = 1
            else:
                if turn == 1: 
                    self.attack(player1, player2)
                    turn = 2
                if turn == 2:
                    self.attack(player2, player1)
                    turn = 1
        else:
            self.end_game()

    def end_game(self):
        loop = True
        while(loop):
            user_input = input("Would you like to play again(y/n)? ").lower()
            if user_input == "y":
                self.run_game()
            elif user_input == "n":
                print("\n                             --- Thank You For Playing! ----\n")
                sys.exit()
            else:
                print("Please use the 'y' and 'n' keys to make a selection.")
