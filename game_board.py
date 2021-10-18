from player import Player
import copy

class Gameboard(Player):
    def __init__(self):
        self.gameboard_size = 10
        self.ocean = "[ ]"
        self.fire = "[O]"
        self.hit = "[X]"
        self.blank_board = []
        super().__init__()

        for row in range(self.gameboard_size):
            self.blank_board.append([self.ocean] * self.gameboard_size)

    def print_gameboard(self):
        self.create_player_board()

        count = 0
        print("                   RADAR                  ||              PLAYER BOARD             ")
        print("   0   1   2   3   4   5   6   7   8   9  ||  0   1   2   3   4   5   6   7   8   9")
        for row in range(self.gameboard_size):
            print(count, " ".join(self.player_radar[row]), "||", " ".join(self.player_board[row]))
            count += 1 

    def place_ships(self):
        for ship in self.fleet:
            self.player_board = self.fleet.fleet_list[ship], self.player_board, ship

    def is_ocean(self, row, column, player_board):
        if row < 0 or row >= self.gameboard_size:
            return 0
        elif column < 0 or column >= self.gameboard_size:
            return 0
        if player_board[row][column] == self.ocean:
            return 1
        else:
            return 0

    def create_player_board(self):
        self.player_board = copy.deepcopy(self.blank_board)
        self.player_radar = copy.deepcopy(self.blank_board)
