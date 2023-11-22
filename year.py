from database_manager import DatabaseManager

# This class will be used to keep track of the major events in each year in the game
# This includes: two seasons, 8-team tournament, 12-team tournament, 16-team tournament
# These will all need to be separate classes: Tournament, Season, Team, Player
class Year:
    def __init__(self, year):
        self.year = year
        self.season1 = None
        self.master1 = None
        self.season2 = None
        self.master2 = None
        self.lcq = []
        self.champions = None
        self.regions = ["AMER", "APAC", "EMEA", "CHIN"]
        
    def create_tournaments(self, cities):
        self.master1 = Tournament(self.year, 8, cities[0])
        self.master2 = Tournament(self.year, 12, cities[1])
        for region in self.regions:
            self.lcq.append(Tournament(self.year, 7, region))
        self.champions = Tournament(self.year, 16, cities[2])
        
    def create_seasons(self):
        season
        
        
        
class Tournament:
    def __init__(self, year, number_of_teams, city):
        self.year = year
        self.number_of_teams = number_of_teams
        self.remaining_teams = []
        self.eliminated_teams = []
        self.city = city
        
    def add_team(self, team):
        self.remaining_teams.append(team)
    
    def eliminate_team(self, team):
        self.eliminated_teams.append(team)
        
    def get_remaining_teams(self):
        return self.remaining_teams
    
    def get_eliminated_teams(self):
        return self.eliminated_teams
    
    #Create group stage function should divide teams into groups of 4
    def create_group_stage(self):
        if len(self.remaining_teams) == 12:
            self.remaining_teams
        
    
        
class Season:
    def __init__(self, year):
        self.year = year
        
    