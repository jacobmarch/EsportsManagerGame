class Match:
    def __init__(self, team1, team2):
        self.id = id
        self.winning_team = None
        self.losing_team = None
        self.winning_score = None
        self.losing_score = None
        self.mvp_player_id = None
        self.team1 = team1
        self.team2 = team2
    
    def play_game(self, database_manager):
        team1_players = database_manager.get_players_for_team(self.team1)
        team2_players = database_manager.get_players_for_team(self.team2)