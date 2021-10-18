from ship import Ship
class Destroyer(Ship):
    def __init__(self, row, column):
        self.name = "Destroyer"
        self.ship_length = 2
        self.row = row
        self.column = column
        self.set_vertical()

    def set_vertical(self):
        loop = True

        while loop is True:
            answer = input(
                "would you like to your Destroyer placed vertically? ")
            if answer == "y":
                self.vertical = True
                loop = False
                continue
            elif answer == "n":
                loop = False
                continue
            else:
                print("please use the 'y' or 'n' keys to make a selection.")