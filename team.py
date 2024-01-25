from player import Player
from coach import Coach


class Team:
    def __init__(self, name):
        """
        Initialize a Team object.

        Args:
        - name (str): The name of the team.
        """
        self.name = name
        self.wins = 0
        self.losses = 0
        self.starters = []  # List of players in the starting lineup
        self.bench = []  # List of players on the bench

    def add_player(self, player):
        """
        Add a player to the team.

        If there are less than 5 players in the starting lineup, the player is added to the starters.
        Otherwise, the player is added to the bench.

        Args:
        - player (str): The name of the player.
        """
        if len(self.starters) < 5:
            self.starters.append(player)
        else:
            self.bench.append(player)

    def remove_player(self, player):
        """
        Remove a player from the team.

        If the player is in the starting lineup, they are removed from the starters.
        Otherwise, they are removed from the bench.

        If there are less than 5 starters and players on the bench, a player from the bench is moved to the starters.

        Args:
        - player (str): The name of the player.
        """
        if player in self.starters:
            self.starters.remove(player)
        else:
            self.bench.remove(player)

        if len(self.starters) < 5 and self.bench:
            self.starters.append(self.bench.pop(0))

    def set_coach(self, coach):
        """
        Set the coach of the team.

        Args:
        - coach (Coach): The coach of the team.
        """
        self.coach = coach
    
    def calculate_team_average_rating(self, starters):
        """
        Calculate the average rating for a team based on the ratings of the starters.

        Parameters:
            self (obj): The instance of the class
            starters (list): List of player objects

        Returns:
            None
        """
        total_rating = 0

        for starter in starters:
            total_rating += starter.calculate_average_rating()
    
        team_average_rating = total_rating / len(starters)
        
        return team_average_rating
               