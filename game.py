import random

def play_game_player(player_team, np_team):
    # Find the average rating of each of the players on the player team
    player_ratings = [player.rating for player in player_team.players]
    avg_player_rating = sum(player_ratings) / len(player_ratings)

    # Determine the winning team based on the average rating
    random_win_factor_team1 = random.randint(0,30)
    random_win_factor_team2 = random.randint(0,30)

    rounds_won_team1 = 0
    rounds_won_team2 = 0


    #Need to copme up with basic formula for determining the winning team of each round and run until team has won
    while rounds_won_team1 < 13 and rounds_won_team2 < 13 or abs(rounds_won_team1 - rounds_won_team2) < 2:
        if random.randint(0, 100) < avg_player_rating + random_win_factor_team1:
            rounds_won_team1 += 1
        else:
            rounds_won_team2 += 1
        

    