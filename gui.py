import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import random

def get_teams():
    conn = sqlite3.connect('esports_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM teams')
    teams = cursor.fetchall()
    conn.close()
    return [team[0] for team in teams]

def get_players_for_team(team_name):
    conn = sqlite3.connect('esports_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.first_name, p.last_name, p.role, p.aim, p.positioning, p.utility, p.leadership, p.mental, p.igl 
        FROM players p
        JOIN team_players tp ON p.id = tp.player_id
        JOIN teams t ON tp.team_id = t.id
        WHERE t.name = ?
        ORDER BY p.aim + p.positioning + p.utility + p.leadership + p.mental DESC, p.igl DESC
    ''', (team_name,))
    players = cursor.fetchall()
    conn.close()

    # Categorize players into starters and bench
    starters = []
    bench = []
    roles_filled = set()
    igl_found = False

    for player in players:
        if len(starters) < 5 or (player[8] and not igl_found):
            # Ensure one starter has IGL experience and all roles are filled
            if player[2] not in roles_filled or (player[8] and not igl_found):
                starters.append(player)
                roles_filled.add(player[2])
                if player[8]:
                    igl_found = True
            else:
                bench.append(player)
        else:
            bench.append(player)

    while len(starters) < 5:
        player_to_move = bench.pop(0)
        starters.append(player_to_move)
        
    while len(starters) > 5:
        if starters[0][8]:
            player_to_move = starters.pop(1)
        else:
            player_to_move = starters.pop(0)
        bench.append(player_to_move)

    # Format player information for display
    formatted_starters = ["Starter - " + format_player_info(player) for player in starters]
    formatted_bench = ["Bench - " + format_player_info(player) for player in bench]

    return formatted_starters + formatted_bench, starters

def format_player_info(player):
    return (f"{player[0]} {player[1]}, Role: {player[2]}, "
            f"Ratings - Aim: {player[3]}, Positioning: {player[4]}, "
            f"Utility: {player[5]}, Leadership: {player[6]}, Mental: {player[7]}, "
            f"IGL: {'Yes' if player[8] else 'No'}")


def update_players_display(team_name, players_listbox):
    players_listbox.delete(0, tk.END)
    players, players_string = get_players_for_team(team_name)
    for player in players:
        players_listbox.insert(tk.END, player)

def simulate_game(team1, team2):
    team1_starters, team1_players = get_players_for_team(team1)[:5]  # Assuming first 5 are starters
    team2_starters, team2_players = get_players_for_team(team2)[:5]

    # Convert ratings from string to int and sum them
    team1_rating = sum(sum(int(rating) for rating in player[3:8]) for player in team1_players)
    team2_rating = sum(sum(int(rating) for rating in player[3:8]) for player in team2_players)


    team1_score, team2_score = 0, 0

    # Simulate rounds until a team reaches 13 points and is ahead by 2
    while not (team1_score >= 13 or team2_score >= 13) or abs(team1_score - team2_score) < 2:
        if random.uniform(0, team1_rating + team2_rating) < team1_rating:
            team1_score += 1
        else:
            team2_score += 1

    return team1_score, team2_score

# Function to handle the 'Play Game' button click
def on_play_game_clicked():
    team1 = left_team_var.get()
    team2 = right_team_var.get()

    if not team1 or not team2:
        messagebox.showwarning("Warning", "Please select both teams before playing the game.")
        return

    team1_score, team2_score = simulate_game(team1, team2)
    result_message = f"Match Result:\n{team1}: {team1_score}\n{team2}: {team2_score}"
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

left_team_dropdown = ttk.Combobox(app, textvariable=left_team_var, values=get_teams())
right_team_dropdown = ttk.Combobox(app, textvariable=right_team_var, values=get_teams())

left_team_dropdown.grid(column=0, row=0, padx=10, pady=10, sticky="ew")
right_team_dropdown.grid(column=1, row=0, padx=10, pady=10, sticky="ew")

# Listboxes for displaying players
left_players_listbox = tk.Listbox(app)
right_players_listbox = tk.Listbox(app)

left_players_listbox.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")
right_players_listbox.grid(column=1, row=1, padx=10, pady=10, sticky="nsew")

# Dropdown event binding
def left_team_selected(event):
    update_players_display(left_team_var.get(), left_players_listbox)

def right_team_selected(event):
    update_players_display(right_team_var.get(), right_players_listbox)

left_team_dropdown.bind('<<ComboboxSelected>>', left_team_selected)
right_team_dropdown.bind('<<ComboboxSelected>>', right_team_selected)

play_game_button = tk.Button(app, text="Play Game", command=on_play_game_clicked)
play_game_button.grid(column=0, row=2, columnspan=2, pady=10)

# Start the application
app.mainloop()
