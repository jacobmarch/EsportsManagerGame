import random
from team import Team
from player import Player

class Interaction:
    def __init__(self, players_involved):
        self.players_involved = players_involved

    def determine_interaction_type(self):
        if self.players_involved == 2:
            self.type_of_interaction = random.choice(["1v1", ])
        

class Round:
    def __init__(self, team1, team2, t1_economy, t2_economy):
        self.team1 = team1
        self.team2 = team2
        self.player_states = []
        for i in range (1, 10):
            self.player_states.append("alive")


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