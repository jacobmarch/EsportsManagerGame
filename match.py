import random
from team import Team
from player import Player
            
class Round:
    def __init__(self, team1, team2, t1_economy, t2_economy):
        self.team1 = team1
        self.team2 = team2
        self.t1_player_states = []
        self.t2_player_states = []
        self.t1_economy = t1_economy
        self.t2_economy = t2_economy
        for i in range (1, 5):
            self.t1_player_states.append("alive")
            self.t2_player_states.append("alive")

    def simulate_round(self):
        while self.t1_player_states.count("alive") > 0 and self.t2_player_states.count("alive") > 0:
            



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