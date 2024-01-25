import random
from team import Team
from player import Player
from copy import copy

class Map:
    def __init__(self, team1: Team, team2: Team):
        self.team1 = copy(team1)
        self.team2 = copy(team2)
        self.t1rounds = 0
        self.t2rounds = 0
        #Economy should range from 0 to 5
        # 0 -> Full Eco/Pistol
        # 1 -> 1/2 Eco
        # 2 -> Force Buy
        # 3+ -> Full Buy
        # 3 - 5 provides the same bonus, but 4 and 5 are insulation so teams can still full buy after a loss
        self.t1economy = 0
        self.t2economy = 0
        
    def simulate_round(self):
        #Don't need to actually simulate a round step-by-step, just determine a winner
        t1_avg = self.team1.calculate_team_average_rating()

    def simulate_map(self):
        while (self.t1rounds < 13 and self.team2rounds < 13) or (self.t1rounds - self.t2rounds < 2 and self.t1rounds - self.t2rounds > -2):
            self.simulate_round()

class Match:
    def __init__(self, team1, team2, best_of):
        self.team1 = copy(team1)
        self.team2 = copy(team2)
        self.best_of = best_of
        
    def simulate_match(self):
        wins_required = (self.best_of // 2) + 1
        while (self.team1.wins < wins_required and self.team2.wins < wins_required):
            self.simulate_map()