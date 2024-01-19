import random
from team import Team

class Round:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

class Map:
    def __init__(self, team1, team2, name):
        self.name = name
        self.team1 = team1
        self.team2 = team2

class Match:
    def __init__(self, team1, team2, best_of):
        self.team1 = team1
        self.team2 = team2
        self.best_of = best_of