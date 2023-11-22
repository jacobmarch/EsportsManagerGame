import sqlite3

class DatabaseManager:
    def __init__(self, database):
        self.database = database
        
    
    def get_players_for_team(self, team_name):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        # Execute a query to get all players for the given team using the players, teams, and team_players tables
        query = """
        SELECT players.name, players.role, players.mechanics, players.positioning, players.utility, players.communication, players.igl
        FROM players
        JOIN team_players ON players.id = team_players.player_id
        JOIN teams ON teams.id = team_players.team_id
        WHERE teams.name = ?
        """
        cursor.execute(query, (team_name,))
        players = cursor.fetchall()
        conn.close()
        return players
    
    def save_match(self, match):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        # Execute a query to insert a new match into the matches table
        query = """
        INSERT INTO matches (winning_team, losing_team, winning_score, losing_score, mvp_player_id)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (match.winning_team, match.losing_team, match.winning_score, match.losing_score, match.mvp_player_id))
        conn.commit()
        conn.close()
    
    def save_tournament_match(self, tournament_id, match_id):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        # Execute a query to insert a new tournament_match into the tournament_matches table
        query = """
        INSERT INTO tournament_matches (tournament_id, match_id)
        VALUES (?, ?)
        """
        cursor.execute(query, (tournament_id, match_id))
        conn.commit()
        conn.close()
        
    