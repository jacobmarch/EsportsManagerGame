import random

def play_game_player(player_team, np_team):
    # Find the average rating of each of the players on the player team
    player_ratings = [player.rating for player in player_team.players]
    avg_player_rating = sum(player_ratings) / len(player_ratings)

    rounds_won_team1 = 0
    rounds_won_team2 = 0


    #Need to come up with basic formula for determining the winning team of each round and run until team has won
    while rounds_won_team1 < 13 and rounds_won_team2 < 13 or abs(rounds_won_team1 - rounds_won_team2) < 2:
        random_win_factor_team1 = random.randint(0,30)
        random_win_factor_team2 = random.randint(0,30)
        if (random_win_factor_team1 + avg_player_rating) > (random_win_factor_team2 + np_team.rating):
            rounds_won_team1 += 1
        elif (random_win_factor_team1 + avg_player_rating) < (random_win_factor_team2 + np_team.rating):
            rounds_won_team2 += 1
        else:
            continue
    
    if (rounds_won_team1 > rounds_won_team2):
        player_team.wins += 1
        np_team.losses += 1
    elif (rounds_won_team1 < rounds_won_team2):
        player_team.losses += 1
        np_team.wins += 1

    return rounds_won_team1, rounds_won_team2

def play_game_nonplayer(np_team, np_team2):

    rounds_won_team1 = 0
    rounds_won_team2 = 0

    while rounds_won_team1 < 13 and rounds_won_team2 < 13 or abs(rounds_won_team1 - rounds_won_team2) < 2:
        random_win_factor_team1 = random.randint(0,30)
        random_win_factor_team2 = random.randint(0,30)
        if (random_win_factor_team1 + np_team.rating) > (random_win_factor_team2 + np_team2.rating):
            rounds_won_team1 += 1
        elif (random_win_factor_team1 + np_team.rating) < (random_win_factor_team2 + np_team2.rating):
            rounds_won_team2 += 1
        else:
            continue
    
    if (rounds_won_team1 > rounds_won_team2):
        np_team.wins += 1
        np_team2.losses += 1
    elif (rounds_won_team1 < rounds_won_team2):
        np_team.losses += 1
        np_team2.wins += 1
    
    return rounds_won_team1, rounds_won_team2

    