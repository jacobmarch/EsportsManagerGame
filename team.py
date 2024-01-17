from player import Player

class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.starters = []
        self.bench = []

    def add_player(self, player):
        if len(self.starters) < 5:
            self.starters.append(player)
        else:
            self.bench.append(player)
    
    def remove_player(self, player):
        if player in self.starters:
            self.starters.remove(player)
        else:
            self.bench.remove(player)
        # If there are less than 5 starters, move a player from the bench to the starters
        if len(self.starters) < 5 and self.bench:
            self.starters.append(self.bench.pop(0))
            