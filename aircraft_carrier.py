class AircraftCarrier():
    def __init__(self, row, column):
        self.name = "Aircraft Carrier"
        self.ship_length = 5
        self.row = row
        self.column = column
        self.is_vertical = None
    
    def set_vertical(self):
        loop = True

        while loop is True:
            answer = input("would you like to your Aircraft Carrier placed vertically? ")
            if answer == "y":
                self.is_vertical = True
                loop = False
                continue
            elif answer == "n":
                self.is_vertical = False
                loop = False
                continue
            else:
                print("please use the 'y' or 'n' keys to make a selection.")
