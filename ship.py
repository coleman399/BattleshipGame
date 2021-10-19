class Ship():
    def __init__(self, name, length):
        self.name = name
        self.ship_length = length
        self.row = None
        self.column = None
        self.is_vertical = None
    
    def set_location(self, row, column, is_vertical):
        self.row = row
        self.column = column
        self.is_vertical = is_vertical