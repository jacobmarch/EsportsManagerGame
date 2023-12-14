import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        
        
amer_team_names = ["Sentinels", "LOUD", "NRG", "EG", "Leviatan", "Kru", "MiBR", "Furia", "Cloud9", "100Thieves"]
apac_team_names = ["DRX", "Paper Rex", "T1", "ZETA DIVISION", "Team Secret", "Gen. G", "RRQ", "Global Esports", "Talon Esports", "DFM"]
emea_team_names = ["FNATIC", "NaVi", "Team Liquid", "Giants Gaming", "FUT Esports", "Team Vitality", "BBL Esports", "Team Heretics", "KOI", "Karmine Corp"]
china_team_names = ["EDward Gaming", "Bilibili Gaming", "Trace Esports", "Rare Atom", "Attacking Soul Esports", "TOP Esports", "Dragon Ranger Gaming", "FPX", "Titan Esports Club", "17Gaming"]

player_team = None

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
        print("\nYour Current Roster:\n")
        print("{:<4} {:<20} {:<10} {:<10} {:<10}".format("#", "Name", "Rating", "Role", "Salary"))
        for i, player in enumerate(player_team.players):
            print("{:<4} {:<20} {:<10} {:<10} {:<10}".format(i + 1, player.name, player.rating, player.role, player.salary))
        print("\nAvailable Players:\n")
        print("{:<4} {:<20} {:<10} {:<10} {:<10}".format("#", "Name", "Rating", "Role", "Salary"))
        for i, player in enumerate(players):
            print("{:<4} {:<20} {:<10} {:<10} {:<10}".format(i + 1, player.name, player.rating, player.role, player.salary))
        print("\n 0. Continue\n")

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
    elif choice == 2:
        break
    else:
        print("Invalid choice")