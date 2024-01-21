from team import Team

class League:
    
    # Initializes a new instance of the class.
    def __init__(self):
        self.teams = []

    # Adds a team to the list of teams.
    def add_team(self, team):
        if team not in self.teams:
            self.teams.append(team)


    #Schedule a round-robin tournament for the teams.
    def schedule_round_robin(self):
        num_teams = len(self.teams)
        if num_teams % 2 != 0:
            self.teams.append("bye")  # Add a placeholder if the number of teams is odd
        num_teams = len(self.teams)
        for _ in range(num_teams - 1):
            print("Week", _ + 1)
            for i in range(num_teams // 2):
                team1 = self.teams[i]
                team2 = self.teams[num_teams - i - 1]
                print(team1, "vs", team2)
            self.rotate_teams()
     
     #Rotates the teams in the tournament by moving the last team in the list to the second position.
    def rotate_teams(self):
        num_teams = len(self.teams)
        rotating_team = self.teams.pop(num_teams - 1)
        self.teams.insert(1, rotating_team)

league = League()
team = Team("Team A")
team = Team("Team B")
team = Team("Team C")
team = Team("Team D")
league.add_team("Team A")
league.add_team("Team B")
league.add_team("Team C")
league.add_team("Team D")
league.schedule_round_robin()