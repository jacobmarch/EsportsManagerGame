import random
from team import Team
from player import Player

class Map:
    def __init__(self, team1: Team, team2: Team):
        # TODO: Add ability for maps to store the name of the map (Lotus, Haven, Ascent, etc)

        self.team1 = team1
        self.team2 = team2
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

        if self.t1economy < 0:
            self.t1economy = 0
        if self.t2economy < 0:
            self.t2economy = 0

        #Don't need to actually simulate a round step-by-step, just determine a winner
        t1_avg = self.team1.calculate_team_average_rating(self.team1.starters)
        t2_avg = self.team2.calculate_team_average_rating(self.team2.starters)

        t1_random_bonus = random.randint(10,30)
        t2_random_bonus = random.randint(10,30)

        t1_round_score = t1_avg + t1_random_bonus + (2 * self.t1economy)
        t2_round_score = t2_avg + t2_random_bonus + (2 * self.t2economy)

        if t1_round_score > t2_round_score:
            self.t1rounds += 1
            self.t1economy += 1
            self.t2economy -= 1
        elif t1_round_score == t2_round_score:
            decider = random.randint(0, 1)
            if decider == 0:
                self.t1rounds += 1
                self.t1economy += 1
                self.t2economy -= 1
            else:
                self.t2rounds += 1
                self.t1economy -= 1
                self.t2economy += 1
        else:
            self.t2rounds += 1
            self.t1economy -= 1
            self.t2economy += 1

    def simulate_map(self):
        while (self.t1rounds < 13 and self.t2rounds < 13) or (self.t1rounds - self.t2rounds < 2 and self.t1rounds - self.t2rounds > -2):
            self.simulate_round()
            input("Press Enter to continue...")
        return self.t1rounds, self.t2rounds

class Match:
    def __init__(self, team1: Team, team2: Team, best_of: int):
        self.team1 = team1
        self.team2 = team2
        self.best_of = best_of
        self.maps = []
        
    def simulate_match(self):
        wins_required = (self.best_of // 2) + 1
        t1_map_wins, t2_map_wins = 0, 0
        i = 0
        while (self.team1.wins < wins_required and self.team2.wins < wins_required):
            print("Starting Map " + str(i + 1))
            print("\nCurrent Score: " + self.team1.name + " " + str(self.team1.wins) + " - " + str(self.team2.wins) + " " + self.team2.name)
            self.maps.append(Map(self.team1, self.team2))

            t1_rounds_won, t2_rounds_won = self.maps[i].simulate_map()
            i += 1
            if t1_rounds_won > t2_rounds_won:
                t1_map_wins += 1
            else:
                t2_map_wins += 1
            input("Press Enter to continue...")

        if t1_map_wins > t2_map_wins:
            self.team1.wins += 1
            self.team2.losses += 1
        else:
            self.team1.losses += 1
            self.team2.wins += 1
        
