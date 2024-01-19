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
        #duelist = aim + positioning; sentinel = positioning + gamesense; controller = utility + positioning; initiator = aim + utility; flex = double role
        self.d = self.ratings["aim"] + self.ratings["positioning"]
        self.s = self.ratings["positioning"] + self.ratings["gamesense"]
        self.c = self.ratings["utility"] + self.ratings["positioning"]
        self.i = self.ratings["aim"] + self.ratings["utility"]

        if self.d > self.s and self.d > self.c and self.d > self.i:
            self.role = "Duelist"
        elif self.s > self.d and self.s > self.c and self.s > self.i:
            self.role = "Sentinel"
        elif self.c > self.d and self.c > self.s and self.c > self.i:
            self.role = "Controller"
        elif self.i > self.d and self.i > self.s and self.i > self.c:
            self.role = "Initiator"
        elif self.d == self.s or self.d == self.c or self.d == self.i:
            self.role = "Flex"
        elif self.s == self.d or self.s == self.c or self.s == self.i:
            self.role = "Flex"
        elif self.c == self.d or self.c == self.s or self.c == self.i:
            self.role = "Flex"
        elif self.i == self.d or self.i == self.s or self.i == self.c:
            self.role = "Flex"
        
        
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
        