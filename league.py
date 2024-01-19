class League:
    def __init__(self):
        self.teams = []

    def add_team(self, team):
        if team not in self.teams:
            self.teams.append(team)

    def schedule_round_robin(self):
        num_teams = len(self.teams)
        if num_teams % 2 != 0:
            self.teams.append(None)  # Add a placeholder if the number of teams is odd

        for _ in range(num_teams - 1):
            print("Round", _ + 1)
            for i in range(num_teams // 2):
                team1 = self.teams[i]
                team2 = self.teams[num_teams - i - 1]
                if team1 is not None and team2 is not None:
                    print(team1, "vs", team2)
            self.rotate_teams()

    def rotate_teams(self):
        num_teams = len(self.teams)
        rotating_team = self.teams.pop(num_teams - 1)
        self.teams.insert(1, rotating_team)
