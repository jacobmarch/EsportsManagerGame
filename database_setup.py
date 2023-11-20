import sqlite3
import random

# Database setup
def setup_database():
    conn = sqlite3.connect('esports_manager.db')
    cursor = conn.cursor()
    
    # Create the Players table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        username TEXT NOT NULL,
        role TEXT NOT NULL,
        aim INTEGER NOT NULL,
        positioning INTEGER NOT NULL,
        utility INTEGER NOT NULL,
        leadership INTEGER NOT NULL,
        mental INTEGER NOT NULL,
        igl BOOLEAN NOT NULL CHECK (igl IN (0, 1))
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        wins INTEGER DEFAULT 0,
        losses INTEGER DEFAULT 0
    )
    ''')

    # Create the Team_Players junction table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS team_players (
        team_id INTEGER NOT NULL,
        player_id INTEGER NOT NULL,
        FOREIGN KEY (team_id) REFERENCES teams (id),
        FOREIGN KEY (player_id) REFERENCES players (id),
        PRIMARY KEY (team_id, player_id)
    )
    ''')

    # Create the matches table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team1_id INTEGER NOT NULL,
    team2_id INTEGER NOT NULL,
    winner_id INTEGER NOT NULL,
    loser_id INTEGER NOT NULL,
    score TEXT NOT NULL,
    mvp_player_id INTEGER NOT NULL,
    FOREIGN KEY (team1_id) REFERENCES teams (id),
    FOREIGN KEY (team2_id) REFERENCES teams (id),
    FOREIGN KEY (winner_id) REFERENCES teams (id),
    FOREIGN KEY (loser_id) REFERENCES teams (id),
    FOREIGN KEY (mvp_player_id) REFERENCES players (id))
    ''')
    
    conn.commit()
    conn.close()

# Function to get random names from files
def get_random_name_from_file(first_name_file, last_name_file):
    with open(first_name_file, 'r') as f:
        first_names = f.read().splitlines()

    with open(last_name_file, 'r') as f:
        last_names = f.read().splitlines()

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return first_name, last_name

# Function to generate random stats and roles
def generate_random_stat():
    return random.randint(0, 100)

def generate_random_role():
    roles = ['Sentinel', 'Smokes', 'Duelist', 'Initiator', 'Flex']
    return random.choice(roles)

def generate_random_igl():
    return random.choice([True] + [False] * 9)  # 10% True, 90% False

# Function to insert a new player into the database
def insert_player():
    first_name, last_name = get_random_name_from_file('firstname.txt', 'lastname.txt')
    username = first_name.lower() + last_name.lower()
    role = generate_random_role()
    aim = generate_random_stat()
    positioning = generate_random_stat()
    utility = generate_random_stat()
    leadership = generate_random_stat()
    mental = generate_random_stat()
    igl = generate_random_igl()
    
    conn = sqlite3.connect('esports_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO players (first_name, last_name, username, role, aim, positioning, utility, leadership, mental, igl)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, username, role, aim, positioning, utility, leadership, mental, igl))
    
    conn.commit()
    conn.close()

team_names = [
    "Cyber Dragons", "Quantum Ninjas", "Pixel Warriors", "Digital Eagles",
    "Neon Snipers", "Retro Raiders", "Virtual Vipers", "Cosmic Knights",
    "Shadow Hunters", "Tech Titans"
]

# Function to insert teams and assign players
def insert_teams_and_assign_players():
    conn = sqlite3.connect('esports_manager.db')
    cursor = conn.cursor()

    # Insert teams
    for name in team_names:
        cursor.execute('''
            INSERT INTO teams (name, wins, losses)
            VALUES (?, 0, 0)
        ''', (name,))

    conn.commit()

    # Fetch all player IDs
    cursor.execute('SELECT id FROM players')
    all_player_ids = [row[0] for row in cursor.fetchall()]
    random.shuffle(all_player_ids)  # Shuffle the list to randomize player assignment

    # Assign 6 to 10 players to each team, ensuring players are only assigned once
    for team_id in range(1, len(team_names) + 1):
        number_of_players = random.randint(6, 10)
        # Select the next batch of player IDs
        team_player_ids = all_player_ids[:number_of_players]
        all_player_ids = all_player_ids[number_of_players:]  # Remove the assigned players

        # Insert player-team relationships into the junction table
        for player_id in team_player_ids:
            cursor.execute('''
                INSERT INTO team_players (team_id, player_id)
                VALUES (?, ?)
            ''', (team_id, player_id))

    conn.commit()
    conn.close()


# Main function to set up the database and insert data
def main():
    for i in range(100):
        setup_database()
        insert_player()
    insert_teams_and_assign_players()

if __name__ == "__main__":
    main()
