class Player:
    def __init__(self, name, role, mechanics, positioning, utility, communication, igl):
        self.name = name
        self.role = role
        self.mechanics = mechanics
        self.positioning = positioning
        self.utility = utility
        self.communication = communication
        self.igl = igl
        
class Team:
    def __init__(self, name, wins, losses):
        self.name = name
        self.starters = []
        self.bench = []
        self.wins = wins
        self.losses = losses
        
    def move_to_starters(self, player):
        self.bench.remove(player)
        self.starters.append(player)
    
    def move_to_bench(self, player):
        self.starters.remove(player)
        self.bench.append(player)
        
    def add_to_team(self, player):
        self.players.append(player)
        self.bench.append(player)