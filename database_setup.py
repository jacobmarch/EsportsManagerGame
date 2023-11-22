import sqlite3
import random



#Create an array of 40 esports team names
team_names = ["LOUD", "Cloud9", "NRG Esports", "Leviatan", "FURIA", "Evil Geniuses", "Sentinels", "100 Thieves", "MIBR", "KRU Esports", "DRX", "Paper Rex", "T1", "ZETA DIVISION", "Team Secret", "Gen. G", "RRQ", "Global Esports", "Talon Esports", "DFM", "FNATIC", "NaVi", "Team Liquid", "Giants Gaming", "FUT Esports", "Team Vitality", "BBL Esports", "Team Heretics", "KOI", "Karmine Corp", "EDward Gaming", "Bilibili Gaming", "Trace Esports", "Rare Atom", "Attacking Soul Esports", "TOP Esports", "Dragon Ranger Gaming", "FPX", "Titan Esports Club", "17Gaming"]

conn = sqlite3.connect('esports_manager.db')

cursor = conn.cursor()

#Create a table for teams that has the following rows: id, name, region, wins, losses.
cursor.execute("CREATE TABLE teams (id INTEGER PRIMARY KEY, name TEXT, region TEXT, wins INTEGER, losses INTEGER)")

#Create a function that inserts 40 teams into the teams table. The names should be randomly generated. Each region should have ten teams assigned to it. The wins and losses should be set to 0.

for i in range(40):
    name = team_names[i]
    if i < 10:
        region = 'AMER'
    elif i < 20:
        region = 'APAC'
    elif i < 30:
        region = 'EMEA'
    else:
        region = 'CHIN'
    wins = 0
    losses = 0
    cursor.execute("INSERT INTO teams (name, region, wins, losses) VALUES (?, ?, ?, ?)", (name, region, wins, losses))

#Create a table for players that has the following rows: id, name, role (1 = duelist, 2 = initiator, 3 = sentinel, 4 = controller), mechanics, positioning, utility, communication, igl.
cursor.execute("CREATE TABLE players (id INTEGER PRIMARY KEY, name TEXT, role INTEGER, mechanics INTEGER, positioning INTEGER, utility INTEGER, communication INTEGER, igl BOOLEAN)")

#Create a function that inserts 100 players into the players table. The names should be a line from 'firstname.txt' and 'lastname.txt' files. The mechanics, positioning, utility, communication, and igl values should be randomly generated between 1 and 100.
with open('firstname.txt') as f:
    first_names = f.read().splitlines()
with open('lastname.txt') as f:
    last_names = f.read().splitlines()
for i in range(280):
    name = random.choice(first_names) + ' ' + random.choice(last_names)
    role = random.randint(1, 4)
    mechanics = random.randint(1, 100)
    positioning = random.randint(1, 100)
    utility = random.randint(1, 100)
    communication = random.randint(1, 100)
    #IGL should be weighted so only about 5% of players will have it
    igl_check = random.randint(1, 20)
    if igl_check == 1:
        igl = True
    else:
        igl = False
    cursor.execute("INSERT INTO players (name, role, mechanics, positioning, utility, communication, igl) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, role, mechanics, positioning, utility, communication, igl))

#Create a table for matches that has the following rows: id, winning_team, losing_team, winning_score, losing_score, mvp_player_id where mvp_player_id is a foreign key pointing to the id in players table.
cursor.execute("""
    CREATE TABLE matches (
        id INTEGER PRIMARY KEY,
        winning_team INTEGER,
        losing_team INTEGER,
        winning_score INTEGER,
        losing_score INTEGER,
        mvp_player_id INTEGER,
        FOREIGN KEY (mvp_player_id) REFERENCES players (id),
        FOREIGN KEY (winning_team) REFERENCES teams (id),
        FOREIGN KEY (losing_team) REFERENCES teams (id)
    )
""")

#Create a table to assign players to teams with two columns: team_id and player_id where team_id is a foreign key pointing to the id in teams table and player_id is a foreign key pointing to the id in players table. This table should be how multiple players are joined to one team. Only the player id should be unique in this table.
cursor.execute("""
    CREATE TABLE team_players (
        team_id INTEGER,
        player_id INTEGER,
        FOREIGN KEY (team_id) REFERENCES teams (id),
        FOREIGN KEY (player_id) REFERENCES players (id),
        UNIQUE (team_id, player_id)
    )
    """)

#Randomly assign 7 players to each team in the team_players table
for i in range(40):
    for j in range(7):
        player_id = j
        team_id = i + 1
        cursor.execute("INSERT INTO team_players (team_id, player_id) VALUES (?, ?)", (team_id, player_id))

#Create a table for tournaments with the following columns: id, city, year, type (type is an integer from 0 to 2)
cursor.execute("CREATE TABLE tournaments (id INTEGER PRIMARY KEY, city TEXT, year INTEGER, type INTEGER)")

#Create a table for tournaments_teams with the following columns: tournament_id, team_id
cursor.execute("CREATE TABLE tournament_teams (tournament_id INTEGER, team_id INTEGER, FOREIGN KEY (tournament_id) REFERENCES tournaments (id), FOREIGN KEY (team_id) REFERENCES teams (id))")

#Create a table for tournament_matches with the following columns: tournament_id, match_id
cursor.execute("""
    CREATE TABLE tournament_matches (
        tournament_id INTEGER,
        match_id INTEGER,
        FOREIGN KEY (tournament_id) REFERENCES tournaments (id),
        FOREIGN KEY (match_id) REFERENCES matches (id)
    )
""")

conn.commit()

conn.close()