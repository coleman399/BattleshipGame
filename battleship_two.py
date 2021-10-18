from ship import Ship
class BattleshipTwo(Ship):
    def __init__(self, row, index):
        self.length = 4
        self.row = row
        self.index = index
        self.set_vertical()

    def set_vertical(self):
        loop = True

        while loop is True:
            answer = input(
                "would you like Battleship 2 placed vertically? ")
            if answer == "y":
                self.vertical = True
                loop = False
                continue
            elif answer == "n":
                loop = False
                continue
            else:
                print("please use the 'y' or 'n' keys to make a selection.")
