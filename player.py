import random

class Player:
    """
    Initializes a new instance of the class.

    Parameters:
        firstname (str): The first name of the person.
        lastname (str): The last name of the person.

    Returns:
        None
    """
    def __init__(self, firstname, lastname):
        # Assign firstname and lastname to instance variables
        self.firstname = firstname
        self.lastname = lastname
        
        # Choose a random role from a list of roles and assign it to the role instance variable
        self.role = random.choice(["Duelist", "Sentinel", "Controller", "Initiator", "Flex"])
        
        # Create a ratings dictionary with randomly generated ratings for different categories
        self.ratings = {
            "aim": random.randint(0, 100),
            "positioning": random.randint(0, 100),
            "utility": random.randint(0, 100),
            "gamesense": random.randint(0, 100),
            "consistency": random.randint(0, 100),
            "leadership": random.randint(0, 100),
            "mental": random.randint(0, 100)
        }
        
        # Calculate the average rating of the player
        def calculate_average_rating(self):
            total_rating = sum(self.ratings.values())
            self.average_rating = total_rating / len(self.ratings)
            
        
        
        
        # Check if the leadership rating and gamesense rating are both above 80
        # If so, set the instance variable igl to True, otherwise set it to False
        self.igl = self.ratings["leadership"] > 80 and self.ratings["gamesense"] > 80
        
        # Choose a random number between 0 and 2 to determine the gamertag composition
        adj_and_noun = random.randint(0, 2)
        
        # Generate gamertag based on the randomly chosen number
        if adj_and_noun == 0:
            # Generate gamertag by combining a random adjective and noun from separate files
            self.gamertag = random.choice(open("adjective.txt").readlines()).strip() + random.choice(open("noun.txt").readlines()).strip()
        elif adj_and_noun == 1:
            # Generate gamertag using only a random adjective from the file
            self.gamertag = random.choice(open("adjective.txt").readlines()).strip()
        else:
            # Generate gamertag using only a random noun from the file
            self.gamertag = random.choice(open("noun.txt").readlines()).strip()
        self.age = random.randint(18,24)
    
    def set_salary(self, salary):
        self.salary = salary
        