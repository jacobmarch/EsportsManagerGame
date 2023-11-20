import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database_manager import DatabaseManager
from database_setup import main_setup
import random

main_setup()

db_manager = DatabaseManager('esports_manager.db')

def determine_mvp(team_starters):
    # Adjust weights for randomness; higher-rated players are more likely to be MVP, but not guaranteed
    weights = [sum(int(rating) for rating in player[4:9]) + random.uniform(0, 100) for player in team_starters]
    mvp_index = weights.index(max(weights))
    return team_starters[mvp_index][0]

def update_players_display(team_name, players_listbox):
    players_listbox.delete(0, tk.END)
    players, players_string = db_manager.get_players_for_team(team_name)
    for player in players:
        players_listbox.insert(tk.END, player)

def simulate_game(team1, team2):
    team1_starters, team1_players = db_manager.get_players_for_team(team1)[:5]  # Assuming first 5 are starters
    team2_starters, team2_players = db_manager.get_players_for_team(team2)[:5]

    # Convert ratings from string to int and sum them
    team1_rating = sum(sum(int(rating) for rating in player[4:9]) for player in team1_players)
    team2_rating = sum(sum(int(rating) for rating in player[4:9]) for player in team2_players)


    team1_score, team2_score = 0, 0

    # Simulate rounds until a team reaches 13 points and is ahead by 2
    while not (team1_score >= 13 or team2_score >= 13) or abs(team1_score - team2_score) < 2:
        if random.uniform(0, team1_rating + team2_rating) < team1_rating:
            team1_score += 1
        else:
            team2_score += 1

    if team1_score > team2_score:
        winning_team_starters = team1_players
    else:
        winning_team_starters = team2_players
    print(winning_team_starters)
    mvp_player_id = determine_mvp(winning_team_starters)  # You need to define winning_team_starters
    db_manager.insert_match_result(team1, team2, team1_score, team2_score, mvp_player_id)

    return team1_score, team2_score


def update_past_games_display():
    past_games = db_manager.get_past_game_results()
    past_games_listbox.delete(0, tk.END)  # Clear the current list
    for game in past_games:
        past_games_listbox.insert(tk.END, f"{game[0]} vs {game[1]} - Winner: {game[2]}, Score: {game[3]}, MVP: {game[4]}")


# Function to handle the 'Play Game' button click
def on_play_game_clicked():
    team1 = left_team_var.get()
    team2 = right_team_var.get()

    if not team1 or not team2:
        messagebox.showwarning("Warning", "Please select both teams before playing the game.")
        return

    team1_score, team2_score = simulate_game(team1, team2)
    result_message = f"Match Result:\n{team1}: {team1_score}\n{team2}: {team2_score}"
    update_past_games_display()
    messagebox.showinfo("Game Result", result_message)

# GUI Application
app = tk.Tk()
app.title('Esports Game Simulation')

# Layout Configuration
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.rowconfigure(1, weight=1)

# Dropdown menus for team selection
left_team_var = tk.StringVar()
right_team_var = tk.StringVar()

left_team_dropdown = ttk.Combobox(app, textvariable=left_team_var, values=db_manager.get_teams())
right_team_dropdown = ttk.Combobox(app, textvariable=right_team_var, values=db_manager.get_teams())

left_team_dropdown.grid(column=0, row=0, padx=10, pady=10, sticky="ew")
right_team_dropdown.grid(column=1, row=0, padx=10, pady=10, sticky="ew")

# Listboxes for displaying players
left_players_listbox = tk.Listbox(app)
right_players_listbox = tk.Listbox(app)

left_players_listbox.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")
right_players_listbox.grid(column=1, row=1, padx=10, pady=10, sticky="nsew")

past_games_listbox = tk.Listbox(app)
past_games_listbox.grid(column=0, row=3, columnspan=2, sticky='nsew', pady=10)


# Dropdown event binding
def left_team_selected(event):
    update_players_display(left_team_var.get(), left_players_listbox)

def right_team_selected(event):
    update_players_display(right_team_var.get(), right_players_listbox)

left_team_dropdown.bind('<<ComboboxSelected>>', left_team_selected)
right_team_dropdown.bind('<<ComboboxSelected>>', right_team_selected)

play_game_button = tk.Button(app, text="Play Game", command=on_play_game_clicked)
play_game_button.grid(column=0, row=2, columnspan=2, pady=10)

update_past_games_display()

# Start the application
app.mainloop()
