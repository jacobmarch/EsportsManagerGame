import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    @staticmethod
    def get_teams():
        conn = sqlite3.connect('esports_manager.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM teams')
        teams = cursor.fetchall()
        conn.close()
        return [team[0] for team in teams]

    @staticmethod
    def format_player_info(player):
        return (f"{player[1]} {player[2]}, Role: {player[3]}, "
                f"Ratings - Aim: {player[4]}, Positioning: {player[5]}, "
                f"Utility: {player[6]}, Leadership: {player[7]}, Mental: {player[8]}, "
                f"IGL: {'Yes' if player[9] else 'No'}")

    def get_players_for_team(self, team_name):
        conn = sqlite3.connect('esports_manager.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p.id, p.first_name, p.last_name, p.role, p.aim, p.positioning, 
            p.utility, p.leadership, p.mental, p.igl FROM players p
            JOIN team_players tp ON p.id = tp.player_id
            JOIN teams t ON tp.team_id = t.id
            WHERE t.name = ?
            ORDER BY (p.aim + p.positioning + p.utility + p.leadership + p.mental) DESC, p.igl DESC
        ''', (team_name,))
        players = cursor.fetchall()
        conn.close()

        # Categorize players into starters and bench
        starters = []
        bench = []
        roles_filled = set()
        igl_found = False

        # First, ensure we fill each role with the best player available
        for player in players:
            if player[3] not in roles_filled:
                starters.append(player)
                roles_filled.add(player[3])
                if player[9]:
                    igl_found = True
            else:
                bench.append(player)

        # If no IGL found yet, attempt to add one from the bench
        if not igl_found:
            for player in bench:
                if player[9]:
                    bench.remove(player)
                    starters.append(player)
                    igl_found = True
                    break

        # If we have too many starters due to adding an IGL, move extra to bench
        while len(starters) > 5:
            starters.sort(key=lambda p: sum(p[4:9]), reverse=True)  # Sort starters by total rating
            bench.append(starters.pop())  # Move the lowest rated starter to bench

        while len(starters) < 5:
            bench.sort(key=lambda p: sum(p[4:9]), reverse=False)  # Sort bench by total rating
            starters.append(bench.pop())  # Move the highest rated player from bench to starters

        # Format player information for display
        formatted_starters = ["Starter - " + self.format_player_info(player) for player in starters]
        formatted_bench = ["Bench - " + self.format_player_info(player) for player in bench]

        return formatted_starters + formatted_bench, starters

    @staticmethod
    def get_team_id(team_name):
        # This function fetches the team ID based on the team name
        conn = sqlite3.connect('esports_manager.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM teams WHERE name = ?', (team_name,))
        team_id = cursor.fetchone()[0]
        conn.close()
        return team_id

    def insert_match_result(self, team1, team2, team1_score, team2_score, mvp_player_id):
        conn = sqlite3.connect('esports_manager.db')
        cursor = conn.cursor()

        # Determine winner and loser
        winner, loser = (team1, team2) if team1_score > team2_score else (team2, team1)
        winner_id = self.get_team_id(winner)
        loser_id = self.get_team_id(loser)
        score = f"{team1_score}-{team2_score}"

        # Insert match result
        cursor.execute('''
            INSERT INTO matches (team1_id, team2_id, winner_id, loser_id, score, mvp_player_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.get_team_id(team1), self.get_team_id(team2), winner_id, loser_id, score, mvp_player_id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_past_game_results():
        conn = sqlite3.connect('esports_manager.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT t1.name as team1_name, t2.name as team2_name, 
            CASE WHEN m.winner_id = t1.id THEN t1.name ELSE t2.name END as winner_name, 
            m.score, p.first_name || ' ' || p.last_name as mvp_name
            FROM matches m
            JOIN teams t1 ON m.team1_id = t1.id
            JOIN teams t2 ON m.team2_id = t2.id
            JOIN players p ON m.mvp_player_id = p.id
            ORDER BY m.id DESC
        ''')
        past_games = cursor.fetchall()
        conn.close()
        return past_games