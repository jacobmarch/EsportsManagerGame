import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database_manager import DatabaseManager
from game_simulation import GameSimulation, Tournament
from database_setup import main_setup
import random

main_setup()

db_manager = DatabaseManager('esports_manager.db')
game_simulator = GameSimulation(db_manager)

def update_players_display(team_name, players_listbox):
    players_listbox.delete(0, tk.END)
    players, players_string = db_manager.get_players_for_team(team_name)
    for player in players:
        players_listbox.insert(tk.END, player)

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
    if team1 == team2:
        messagebox.showwarning("Warning", "A team cannot play itself")
        return

    team1_score, team2_score = game_simulator.simulate_game(team1, team2)
    result_message = f"Match Result:\n{team1}: {team1_score}\n{team2}: {team2_score}"
    update_past_games_display()
    messagebox.showinfo("Game Result", result_message)

tournament = None

def on_create_tournament_clicked():
    tournament_window = tk.Toplevel(app)
    tournament_window.title("Tournament Bracket")

    tournament_complete = False

    # Allow the user to select 8 teams for the tournament
    label = tk.Label(tournament_window, text="Select 8 teams for the tournament:")
    label.pack()

    #Listbox for team selection
    team_listbox = tk.Listbox(tournament_window, selectmode='multiple', exportselection=False)
    team_listbox.pack()

    for team in db_manager.get_teams():
        team_listbox.insert(tk.END, team)

    start_tournament_button = tk.Button(tournament_window, text="Start Tournament", command=lambda: start_tournament(team_listbox))
    start_tournament_button.pack()

    def start_tournament(select_team_listbox):
        global tournament
        selected_indices = select_team_listbox.curselection()
        if len(selected_indices) != 8:
            messagebox.showwarning("Warning", "Please select exactly 8 teams.")
            return
        selected_teams = [select_team_listbox.get(i) for i in selected_indices]
        tournament = Tournament(selected_teams, game_simulator)
        update_bracket_display()

    def play_next_match():
        global tournament
        if tournament:
            result = tournament.play_match()
            if result:
                match, team1_score, team2_score, winner, other = result
                # Update bracket display and scores here
                # If final match played, update play match button to 'End Tournament'
                if tournament.current_round >= len(tournament.matches):
                    play_match_button.config(text="End Tournament", command=end_tournament)
            else:
                messagebox.showinfo("Tournament Complete", "The tournament is complete!")

    def end_tournament():
        tournament_window.destroy()

    # Play match button
    play_match_button = tk.Button(tournament_window, text="Play Match", command=play_next_match)
    play_match_button.pack()

    # Function to update bracket display
    def update_bracket_display():
        # Assuming you have a predefined Frame or similar widget to hold the bracket display
        bracket_frame = tk.Frame(tournament_window)
        bracket_frame.pack(fill="both", expand=True)

        # Assuming 'tournament.matches' holds the current round matches and 'tournament.next_round_matches' holds the next round
        for round_num, matches in enumerate(tournament.matches + tournament.next_round_matches, start=1):
            round_label = tk.Label(bracket_frame, text=f'Round {round_num}', font=('Helvetica', 16))
            round_label.pack()

            for match in matches:
                match_label_text = f"{match[0]} vs {match[1]}" if len(match) == 2 else "TBD"
                match_label = tk.Label(bracket_frame, text=match_label_text)
                match_label.pack()

        # Update the window to show the new bracket
        tournament_window.update()

    # Check if the tournament is complete, and if so, update the play match button
    if tournament_complete:
        play_match_button.config(text="End Tournament", command=end_tournament)

    tournament_window.mainloop()

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
past_games_listbox.grid(column=0, row=4, columnspan=2, sticky='nsew', pady=10)


# Dropdown event binding
def left_team_selected(event):
    update_players_display(left_team_var.get(), left_players_listbox)

def right_team_selected(event):
    update_players_display(right_team_var.get(), right_players_listbox)

left_team_dropdown.bind('<<ComboboxSelected>>', left_team_selected)
right_team_dropdown.bind('<<ComboboxSelected>>', right_team_selected)

play_game_button = tk.Button(app, text="Play Game", command=on_play_game_clicked)
play_game_button.grid(column=0, row=3, columnspan=2, pady=10)

create_tournament_button = tk.Button(app, text="Create Tournament", command=on_create_tournament_clicked)
create_tournament_button.grid(column=0, row=2, columnspan=2, pady=10)

update_past_games_display()

# Start the application
app.mainloop()
