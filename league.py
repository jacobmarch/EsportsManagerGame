from team import Team

class League:
    
    # Creates an array for the teams in the league
    def __init__(self):
        self.teams = []

    #Adds a team to the league
    def add_team(self, team):
        if team not in self.teams:
            self.teams.append(team)