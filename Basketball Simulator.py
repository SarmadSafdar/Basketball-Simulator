'''
Sarmad Safdar
CSC-121 Final Project
Project: This project is a basketball game simulator created with the Python library, Tkinter.
The program allows users to draft players for two teams, input points for each team after each game, and determine the series winner in a user-friendly GUI.
'''
import tkinter as tk
import random

# Define the Team class
class Team:
    def __init__(self, name):
        self.name = name
        self.regSeasonWin = 0
        self.regSeasonLose = 0
        self.playoffWin = 0
        self.playoffLose = 0
        self.points = []

    def add_points(self, points):
        self.points.append(points)

    def increment_playoff_win(self):

        self.playoffWin += 1

    def increment_playoff_lose(self):
        self.playoffLose += 1

# Initialize the list of players
players = ["Larry", "Nicholas", "Sarmad", "Samba", "Lebron", "Jimmy", "Jayson", "Ann", "Sarah", "Candice"]
homeTeam = Team("Home Team")
awayTeam = Team("Away Team")
current_game = 1
winner = False

# Function to draft players for the home and away teams
def is_draft_complete():
    return len(players) == 0

def draft_players():
    if not is_draft_complete():
        player_team1 = random.choice(players)
        home_team_roster.insert(tk.END, player_team1)
        players.remove(player_team1)

        if not is_draft_complete():
            player_team2 = random.choice(players)
            away_team_roster.insert(tk.END, player_team2)
            players.remove(player_team2)

    if is_draft_complete():
        draft_button.config(state=tk.DISABLED)

# Function to submit points for each game
def submit_points():
    global current_game, winner

    # Update team names with the names entered by the user
    home_team_name = home_team_name_entry.get() or "Home Team"
    away_team_name = away_team_name_entry.get() or "Away Team"
    homeTeam.name = home_team_name
    awayTeam.name = away_team_name

    if winner:
        return

    home_team_points = int(home_team_points_entry.get())
    away_team_points = int(away_team_points_entry.get())

    homeTeam.add_points(home_team_points)
    awayTeam.add_points(away_team_points)

    if home_team_points > away_team_points:
        homeTeam.increment_playoff_win()
        awayTeam.increment_playoff_lose()
    else:
        awayTeam.increment_playoff_win()
        homeTeam.increment_playoff_lose()

    if homeTeam.playoffWin == 4 or awayTeam.playoffWin == 4:
        winner = True
        result_label.config(text=f"The winner is {homeTeam.name if homeTeam.playoffWin == 4 else awayTeam.name}")
        submit_points_button.config(state=tk.DISABLED)
    else:
        result_label.config(text=f"Series: {homeTeam.name} {homeTeam.playoffWin} - {awayTeam.name} {awayTeam.playoffWin}")

    current_game += 1

    # Clear the points entries after each game
    home_team_points_entry.delete(0, tk.END)
    away_team_points_entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Basketball Game Simulator")

# Create frames for team names, draft, and points
team_name_frame = tk.Frame(root)
team_name_frame.pack(padx=10, pady=10)

home_team_name_label = tk.Label(team_name_frame, text="Home Team:")
home_team_name_label.grid(row=0, column=0)
home_team_name_entry = tk.Entry(team_name_frame)
home_team_name_entry.grid(row=0, column=1)

away_team_name_label = tk.Label(team_name_frame, text="Away Team:")
away_team_name_label.grid(row=1, column=0)
away_team_name_entry = tk.Entry(team_name_frame)
away_team_name_entry.grid(row=1, column=1)

draft_frame = tk.Frame(root)
draft_frame.pack(padx=10, pady=10)

# Create roster listboxes for home and away teams
home_team_roster_label = tk.Label(draft_frame, text="Home Team Roster:")
home_team_roster_label.grid(row=0, column=0)
home_team_roster = tk.Listbox(draft_frame, height=10, width=15)
home_team_roster.grid(row=1, column=0)

away_team_roster_label = tk.Label(draft_frame, text="Away Team Roster:")
away_team_roster_label.grid(row=0, column=1)
away_team_roster = tk.Listbox(draft_frame, height=10, width=15)
away_team_roster.grid(row=1, column= 1)

# Create the "Draft Players" button and assign the "draft_players" function as its command
draft_button = tk.Button(draft_frame, text="Draft Players", command=draft_players)
draft_button.grid(row=2, columnspan=2)

# Create a frame to input points for each team
points_frame = tk.Frame(root)
points_frame.pack(padx=10, pady=10)

home_team_points_label = tk.Label(points_frame, text="Home Team Points:")
home_team_points_label.grid(row=0, column=0)
home_team_points_entry = tk.Entry(points_frame)
home_team_points_entry.grid(row=0, column=1)

away_team_points_label = tk.Label(points_frame, text="Away Team Points:")
away_team_points_label.grid(row=1, column=0)
away_team_points_entry = tk.Entry(points_frame)
away_team_points_entry.grid(row=1, column=1)

# Create the "Submit Points" button and assign the "submit_points" function as its command
submit_points_button = tk.Button(points_frame, text="Submit Points", command=submit_points)
submit_points_button.grid(row=2, columnspan=2)

# Create the label to display the game results
result_label = tk.Label(root, text="")
result_label.pack(padx=10, pady=10)

def reset_game():
    global winner, current_game, homeTeam, awayTeam, players

    # Reset team stats
    homeTeam = Team("Home Team")
    awayTeam = Team("Away Team")

    # Reset game variables
    current_game = 1
    winner = False

    # Reset result label
    result_label.config(text="")
    submit_points_button.config(state=tk.NORMAL)

    # Reset rosters
    home_team_roster.delete(0, tk.END)
    away_team_roster.delete(0, tk.END)
    players = ["Larry", "Nicholas", "Sarmad", "Samba", "Lebron", "Jimmy", "Jayson", "Ann", "Sarah", "Candice"]

    # Reset draft button
    draft_button.config(state=tk.NORMAL)


# Create a function to terminate the application
def terminate_app():
    root.destroy()

# Create a frame to hold the "Terminate" button
terminate_frame = tk.Frame(root)
terminate_frame.pack(padx=10, pady=10)

# Create the "Reset" button and assign the "reset_game" function as its command
reset_button = tk.Button(terminate_frame, text="Reset", command=reset_game)
reset_button.pack(side=tk.LEFT)

# Create the "Terminate" button and assign the "terminate_app" function as its command
terminate_button = tk.Button(terminate_frame, text="Terminate", command=terminate_app)
terminate_button.pack(side=tk.LEFT)


# Start the main event loop for the Tkinter application
root.mainloop()

