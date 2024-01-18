import random

class Coach:
    """
    Initializes a new instance of the class with the given `firstname` and `lastname`.

    Parameters:
        firstname (str): The first name of the person.
        lastname (str): The last name of the person.

    Returns:
        None
    """
    def __init__(self, firstname, lastname):
        
        # Assign the firstname and lastname to instance variables
        self.firstname = firstname
        self.lastname = lastname
        
        # Create a dictionary called ratings with different categories and assign random ratings
        self.ratings = {
            "leadership": random.randint(0, 100),
            "gamesense": random.randint(0, 100),
            "preparation": random.randint(0, 100),
            "consistency": random.randint(0, 100),
            "mental": random.randint(0, 100)
        }
        
        # Generate a random number between 0 and 2 to determine the gamertag format
        adj_and_noun = random.randint(0, 2)
        
        # If adj_and_noun is 0, concatenate a random adjective and noun from files
        if adj_and_noun == 0:
            adjectives = open("adjective.txt").readlines()
            nouns = open("noun.txt").readlines()
            self.gamertag = random.choice(adjectives).strip() + random.choice(nouns).strip()
        
        # If adj_and_noun is 1, select a random adjective from file
        elif adj_and_noun == 1:
            adjectives = open("adjective.txt").readlines()
            self.gamertag = random.choice(adjectives).strip()
        
        # If adj_and_noun is 2, select a random noun from file
        else:
            nouns = open("noun.txt").readlines()
            self.gamertag = random.choice(nouns).strip()
