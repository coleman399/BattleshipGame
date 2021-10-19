from player import Player

class Human(Player):
    def __init__(self, player):
        self.name = player
        super().__init__()
