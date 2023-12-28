import random
import os
from game import *

player_team = None
current_year = 2023
amer_team_names = ["Sentinels", "LOUD", "NRG", "EG", "Leviatan", "Kru", "MiBR", "Furia", "Cloud9", "100Thieves"]
apac_team_names = ["DRX", "Paper Rex", "T1", "ZETA DIVISION", "Team Secret", "Gen. G", "RRQ", "Global Esports", "Talon Esports", "DFM"]
emea_team_names = ["FNATIC", "NaVi", "Team Liquid", "Giants Gaming", "FUT Esports", "Team Vitality", "BBL Esports", "Team Heretics", "KOI", "Karmine Corp"]
china_team_names = ["EDward Gaming", "Bilibili Gaming", "Trace Esports", "Rare Atom", "Attacking Soul Esports", "TOP Esports", "Dragon Ranger Gaming", "FPX", "Titan Esports Club", "17Gaming"]
team_copy_made = False
teams_to_be_sorted = []

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class NP_Team:
    def __init__(self, name, region, rating):
        self.name = name
        self.region = region
        self.rating = rating
        self.wins = 0
        self.losses = 0

class Player:
    def __init__(self, name, rating, role, salary):
        self.name = name
        self.rating = rating
        self.role = role
        self.salary = salary
        
class Team:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        self.players = []
        self.wins = 0
        self.losses = 0
        self.coach = None
        self.budget = None
        self.current_salary = 0
        self.schedule = []
        
    def add_player(self, player):
        if (player.salary + self.current_salary) > self.budget:
            print("Player salary exceeds budget")
        elif (len(self.players) + 1) > 6:
            print("Team is full. Please press continue.")
        else:
            self.players.append(player)
            self.current_salary += player.salary
            
    def remove_player(self, player):
        if (len(self.players) == 0):
            print("Team is empty.")
        else:
            self.players.remove(player)
            self.current_salary -= player.salary
        
    def add_coach(self, coach):
        self.coach = coach
        
    def remove_coach(self):
        self.coach = None
        
    def remove_player(self, player):
        self.players.remove(player)
        self.current_salary -= player.salary

    def create_schedule(self):
        if self.region == "Americas":
            # Randomly create a schedule using the teams from this array except for the player team
            for team in amer_team_names:
                if team == self.name or team == player_team.name:
                    continue
                else:
                    self.schedule.append(NP_Team(team, self.region, random.randint(30, 70)))
            random.shuffle(self.schedule)
        elif self.region == "EMEA":
            for team in emea_team_names:
                if team == self.name or team == player_team.name:
                    continue
                else:
                    self.schedule.append(NP_Team(team, self.region, random.randint(30, 70)))
            random.shuffle(self.schedule)
        elif self.region == "APAC":
            for team in apac_team_names:
                if team == self.name or team == player_team.name:
                    continue
                else:
                    self.schedule.append(NP_Team(team, self.region, random.randint(30, 70)))
            random.shuffle(self.schedule)
        elif self.region == "China":
            for team in china_team_names:
                if team == self.name or team == player_team.name:
                    continue
                else:
                    self.schedule.append(NP_Team(team, self.region, random.randint(30, 70)))
            random.shuffle(self.schedule)

    def display_schedule(self):
        print("\n" + self.name + "'s " + str(current_year) + " Schedule:")
        for i, team in enumerate(self.schedule):
            print(str(i + 1) + ". " + team.name)

def display_standings(current_week):
    global team_copy_made
    global teams_to_be_sorted
    print("\nWeek " + str(current_week) + " Standings:")
    print("{:<20}{:<5}{:<5}".format("Team", "W", "L"))
    print("\n")
    if team_copy_made == False:
        player_ratings = [player.rating for player in player_team.players]
        avg_rating = sum(player_ratings) / len(player_ratings)
        player_team_filler = NP_Team(player_team.name, player_team.region, avg_rating)
        player_team_filler.wins = player_team.wins
        player_team_filler.losses = player_team.losses
        all_teams = player_team.schedule.copy()
        all_teams.append(player_team_filler)
        team_copy_made = True
        teams_to_be_sorted = all_teams.copy()
    else:
        existing_team_filler = next((team for team in teams_to_be_sorted if team.name == player_team.name), None)
        if existing_team_filler is not None:
            existing_team_filler.wins = player_team.wins
            existing_team_filler.losses = player_team.losses
    sorted_teams = sorted(teams_to_be_sorted, key=lambda x: x.wins, reverse=True)
    for i, team in enumerate(player_team.schedule):
        print("{:<20}{:<5}{:<5}".format(sorted_teams[i].name, sorted_teams[i].wins, sorted_teams[i].losses))



def region_select():
    while True:    
        i = 1
        print("\n1. Americas")
        print("2. Europe")
        print("3. Asia Pacific")
        print("4. China\n")
        region_choice = int(input("Enter your choice: "))
        if region_choice == 1:
            for team in amer_team_names:
                print(str(i) + ". " + team)
                i += 1
            return region_choice
        elif region_choice == 2:
            for team in emea_team_names:
                print(str(i) + ". " + team)
                i += 1
            return region_choice
        elif region_choice == 3:
            for team in apac_team_names:
                print(str(i) + ". " + team)
                i += 1
            return region_choice
        elif region_choice == 4:
            for team in china_team_names:
                print(str(i) + ". " + team)
                i += 1
            return region_choice
        else:
            print("Invalid choice")
            
# This should generate a list of 15 players for the user to choose from. For each player, the first name, last name, rating, role, and salary should be generated and printed out. The first and last name should be gotten from the firtname.txt file and lastname.txt file.            
def initial_player_select():
    clear_console()
    with open('firstname.txt') as f:
        first_names = f.read().splitlines()
    with open('lastname.txt') as f:
        last_names = f.read().splitlines()
    players = []
    for i in range(15):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = first_name + " " + last_name
        rating = random.randint(1, 100)
        role = random.choice(["Duelist", "Controller", "Flex", "Sentinel", "Initiator"])
        salary = (random.randint(15, 30) * 1000) + (1000 * rating)
        players.append(Player(name, rating, role, salary))
    
    print("\nYou have selected " + player_team.name + " as your team.\n")
    print("Your initial budget is $" + str(player_team.budget) +".\nChoose your initial team members:\n")    
    print("Here are the available players:\n")    
    print("{:<4} {:<20} {:<10} {:<10} {:<10}".format("#", "Name", "Rating", "Role", "Salary"))
    for i, player in enumerate(players):
        print("{:<4} {:<20} {:<10} {:<10} {:<10}".format(i + 1, player.name, player.rating, player.role, player.salary))

    print("\n")
    initial_clear_complete = False
    while True:
        print("You have " + str(player_team.budget - player_team.current_salary) + " reamining in your budget.\n")
        player_choice = int(input("Enter the number of the player you want to add to your team: "))
        clear_console()
        if player_choice > 0 and player_choice <= 15:
            curr_length = len(player_team.players)
            player_team.add_player(players[player_choice - 1])
            if curr_length < len(player_team.players):
                print(players[player_choice - 1].name + " has been added to your team.")
                players.pop(player_choice - 1)
        elif player_choice == 0 and len(player_team.players) >= 5:
            break
        elif len(player_team.players) < 5 and player_choice == 0:
            print("Not enough players. You currently have " + str(len(player_team.players)) + " players on your roster.\n\nYou must have 5 to continue.")
        elif player_choice < 0 and player_choice >= (len(player_team.players) * -1):
            players.append(player_team.players[abs(player_choice) - 1])
            print(player_team.players[abs(player_choice) - 1].name + " has been removed from your team.")
            player_team.remove_player(player_team.players[abs(player_choice) - 1])
        else:
            print("Invalid choice")
        if initial_clear_complete:
            clear_console()
        print("\nYour Current Roster:\n")
        print("{:<4} {:<20} {:<10} {:<10} {:<10}".format("#", "Name", "Rating", "Role", "Salary"))
        for i, player in enumerate(player_team.players):
            print("{:<4} {:<20} {:<10} {:<10} {:<10}".format(i + 1, player.name, player.rating, player.role, player.salary))
        print("\nAvailable Players:\n")
        print("{:<4} {:<20} {:<10} {:<10} {:<10}".format("#", "Name", "Rating", "Role", "Salary"))
        for i, player in enumerate(players):
            print("{:<4} {:<20} {:<10} {:<10} {:<10}".format(i + 1, player.name, player.rating, player.role, player.salary))
        print("\n 0. Continue\n")
        initial_clear_complete = True

while True:
    clear_console()
    print("\nWelcome to Esports Manager!\n")
    print("1. Select Region")
    print("2. Exit\n")
    choice = int(input("Enter your choice: "))
    clear_console()
    if choice == 1:
        print("Choose A Region:")
        region_choice = region_select()
        choice = int(input("Enter your choice: "))
        clear_console()
        if region_choice == 1:
            player_team = Team(amer_team_names[choice - 1], "Americas")
        elif region_choice == 2:
            player_team = Team(emea_team_names[choice - 1], "EMEA")
        elif region_choice == 3:
            player_team = Team(apac_team_names[choice - 1], "APAC")
        elif region_choice == 4:
            player_team = Team(china_team_names[choice - 1], "China")
        player_team.budget = 400000
        initial_player_select()
        print("\n")
        print("Your final roster for the " + str(current_year) + " season:\n")
        print("{:<4} {:<20} {:<10} {:<10} {:<10}".format("#", "Name", "Rating", "Role", "Salary"))
        for i, player in enumerate(player_team.players):
            print("{:<4} {:<20} {:<10} {:<10} {:<10}".format(i + 1, player.name, player.rating, player.role, player.salary))
        print("\n")
        # Make the user input any key to move on
        input("Press any key to continue...")
        clear_console()
        ### Create a schedule for the season
        player_team.create_schedule()
        ### Display schedule
        player_team.display_schedule()
        input("Press any key to continue...")
        ### Create a method to play each game, week-by-week
        clear_console()
        
        current_pos = 0
        for i, team in enumerate(player_team.schedule):
            print("\nWeek " + str(i + 1) + ":")
            score1, score2 = play_game_player(player_team, player_team.schedule[i])
            score3, score4 = play_game_nonplayer(player_team.schedule[(i + 1) % 9], player_team.schedule[(i + 2) % 9])
            score5, score6 = play_game_nonplayer(player_team.schedule[(i + 3) % 9], player_team.schedule[(i + 4) % 9])
            score7, score8 = play_game_nonplayer(player_team.schedule[(i + 5) % 9], player_team.schedule[(i + 6) % 9])
            score9, score10 = play_game_nonplayer(player_team.schedule[(i + 7) % 9], player_team.schedule[(i + 8) % 9])
            # Ouput the scores of each match is a neatly formatted table
            print("\n")
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(player_team.name, str(score1), " vs ", str(score2), player_team.schedule[i].name))
            print("\n")
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(player_team.schedule[(i + 1) % 9].name, str(score3), " vs ", str(score4), player_team.schedule[(i + 2) % 9].name))
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(player_team.schedule[(i + 3) % 9].name, str(score5), " vs ", str(score6), player_team.schedule[(i + 4) % 9].name))
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(player_team.schedule[(i + 5) % 9].name, str(score7), " vs ", str(score8), player_team.schedule[(i + 6) % 9].name))
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(player_team.schedule[(i + 7) % 9].name, str(score9), " vs ", str(score10), player_team.schedule[(i + 8) % 9].name))
            input("Press any key to continue...")
            current_pos += 1
            clear_console()
            display_standings(i + 1)
            input("Press any key to continue...")
            clear_console()

        ### Display results of each game

    elif choice == 2:
        clear_console()
        break
    else:
        print("Invalid choice")