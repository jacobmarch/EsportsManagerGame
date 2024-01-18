import sqlite3 as sql

class DatabaseManager:
    
    """
    Initializes a new instance of the class with the specified database name.

    Parameters:
        db_name (str): The name of the database to connect to.

    Returns:
        None
    """
    def __init__(self, db_name):
        self.db_name = db_name + ".db"
        self.db = sql.connect(self.db_name)

    def __del__(self):
        self.db.close()
        
def init_tables(self):
    # Create a cursor object to interact with the database
    cursor = self.db.cursor()

    # Create the PLAYERS table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PLAYERS (
            id INTEGER PRIMARY KEY, 
            firstname TEXT,
            lastname TEXT,
            role TEXT, 
            igl BOOLEAN,
            aim INTEGER,
            positioning INTEGER,
            utility INTEGER,
            gamesense INTEGER,
            consistency INTEGER,
            leadership INTEGER,
            mental INTEGER,
            gamertag TEXT,
            salary INTEGER,
            team_id INTEGER FOREIGN KEY REFERENCES TEAMS(id) ON DELETE SET NULL ON UPDATE CASCADE,
            age INTEGER
        )
    """)

    # Create the COACHES table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS COACHES (
            id INTEGER PRIMARY KEY,
            firstname TEXT,
            lastname TEXT,
            leadership INTEGER,
            gamesense INTEGER,
            preparation INTEGER,
            consistency INTEGER,
            mental INTEGER,
            team_id INTEGER FOREIGN KEY REFERENCES TEAMS(id) ON DELETE SET NULL ON UPDATE CASCADE,
            age INTEGER,
            salary INTEGER
        )
    """)

    # Create the TEAMS table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TEAMS (
            id INTEGER PRIMARY KEY,
            name TEXT,
            wins INTEGER,
            losses INTEGER
        )
    """)

    # Create the PLAYERS_TEAMS table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PLAYERS_TEAMS (
            player_id INTEGER FOREIGN KEY REFERENCES PLAYERS(id) ON DELETE CASCADE ON UPDATE CASCADE ON INSERT CASCADE,
            team_id INTEGER FOREIGN KEY REFERENCES TEAMS(id) ON DELETE CASCADE ON UPDATE CASCADE ON INSERT CASCADE
        )
    """)

    # Commit the changes to the database
    self.db.commit()

    # Close the cursor
    cursor.close()
