from player import Player
from coach import Coach

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
    
    def set_coach(self, coach):
        self.coach = coach
    
    def calculate_team_average_rating(self, starters):
        total_rating = 0
        num_starters = len(starters)

        for starter in starters:
            total_rating += starter.calculate_average_rating()
    
        self.team_average_rating = total_rating / num_starters
               