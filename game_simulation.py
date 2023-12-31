import random
from database_manager import DatabaseManager

class GameSimulation:
    def __init__(self, db_manager):
        self.db_manager = db_manager  # Instance of DatabaseManager class
        self.starters = {}
        self.bench = {}

    @staticmethod
    def determine_mvp(team_starters):
        # Adjust weights for randomness; higher-rated players are more likely to be MVP, but not guaranteed
        weights = [sum(int(rating) for rating in player[4:9]) + random.uniform(0, 100) for player in team_starters]
        mvp_index = weights.index(max(weights))
        return team_starters[mvp_index][0]

    def set_starters(self, team_name, starter_ids):
        # Validate and set starters for a team
        self.starters[team_name] = starter_ids

    def set_bench(self, team_name, bench_ids):
        # Validate and set bench players for a team
        self.bench[team_name] = bench_ids

    def simulate_game(self, team1, team2):
        team1_starters, team1_players = self.db_manager.get_players_for_team(team1)[:5]  # Assuming first 5 are starters
        team2_starters, team2_players = self.db_manager.get_players_for_team(team2)[:5]

        # Convert ratings from string to int and sum them
        team1_rating = sum(sum(int(rating) for rating in player[4:9]) for player in team1_players)
        team2_rating = sum(sum(int(rating) for rating in player[4:9]) for player in team2_players)

        team1_score, team2_score = 0, 0

        # Simulate rounds until a team reaches 13 points and is ahead by 2
        while not (team1_score >= 13 or team2_score >= 13) or abs(team1_score - team2_score) < 2:
            if random.uniform(0, team1_rating + team2_rating) < team1_rating:
                team1_score += 1
            else:
                team2_score += 1

        if team1_score > team2_score:
            winning_team_starters = team1_players
        else:
            winning_team_starters = team2_players
        mvp_player_id = self.determine_mvp(winning_team_starters)  # You need to define winning_team_starters
        self.db_manager.insert_match_result(team1, team2, team1_score, team2_score, mvp_player_id)

        return team1_score, team2_score