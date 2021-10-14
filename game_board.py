import copy

class Gameboard:
    def __init__(self):
        self.gameboard_size = 10
        self.ocean = "[ ]"
        self.fire = "[O]"
        self.hit = "[X]"
        self.blank_board = []

        for row in range(self.gameboard_size):
            self.blank_board.append([self.ocean] * self.gameboard_size)

        self.player_board = copy.deepcopy(self.blank_board)
        self.player_radar = copy.deepcopy(self.blank_board)

    def print_gameboard(self):
        count = 0
        print("                   RADAR                  ||              PLAYER BOARD             ")
        print("   0   1   2   3   4   5   6   7   8   9  ||  0   1   2   3   4   5   6   7   8   9")
        for row in range(self.gameboard_size):
            print(count, " ".join(self.player_radar[row]), "||", " ".join(self.player_board[row]))
            count += 1 
