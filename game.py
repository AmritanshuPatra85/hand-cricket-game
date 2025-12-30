import random
import pyinputplus as pyip

# Game conditions selection
print('Select the team and players')

Teams = {
    "India": ["Rohit", "Gill(c)", "Virat", "Shreyas", "KL", "Hardik", "Axar", "Jadeja", "Bumrah", "Siraj", "Arshdeep"],
    "Australia": ["Smith", "Warner", "Cummins", "Starc", "Hazlewood", "Labuschagne", "Maxwell", "Carey", "Zampa", "Head", "Green"],
    "New Zealand": ["Williamson", "Conway", "Boult", "Southee", "Henry", "Mitchell", "Latham", "Phillips", "Santner", "Allen", "Ravindra"],
    "England": ["Root", "Stokes", "Buttler", "Bairstow", "Archer", "Wood", "Rashid", "Woakes", "Brook", "Moeen", "Livingstone"],
    "South Africa": ["De Kock", "Markram", "Rabada", "Nortje", "Bavuma", "Miller", "Klaasen", "Maharaj", "Ngidi", "Jansen", "Shamsi"]
}

print('\n-------Select the Format---------')
Format = {
    "T20I": "20 overs",
    "ODI": "50 overs"
}

print("\n--------Select the stadium--------")
Stadium = {
    "Chepauk": "Spin Friendly",
    "Lords": "Swing Friendly",
    "MCG": "Batting Friendly",
    "Cape Town": "Seam Friendly"
}

match_format = pyip.inputChoice(list(Format.keys()))
stadium = pyip.inputChoice(list(Stadium.keys()))

user_team = pyip.inputChoice(list(Teams.keys()))
computer_team = random.choice([t for t in Teams if t != user_team])

user_playing_xi = Teams[user_team]
computer_playing_xi = Teams[computer_team]

# Toss
print("\n--- TOSS ---")
user_call = pyip.inputChoice(['Heads', 'Tails'], prompt="Call the toss (Heads/Tails): ")

coin_flip = random.choice(['Heads', 'Tails'])
print(f"The coin shows: {coin_flip}")

if user_call == coin_flip:
    print("You won the toss!")
    toss_decision = pyip.inputChoice(['Bat', 'Bowl'], prompt="What do you want to do? (Bat/Bowl): ")
    user_bats_first = toss_decision == 'Bat'
else:
    print("Computer won the toss!")
    toss_decision = random.choice(['Bat', 'Bowl'])
    print(f"Computer chose to {toss_decision} first.")
    user_bats_first = toss_decision != 'Bat'

print(f"Format: {match_format}")
print(f"Venue: {stadium} ({Stadium[stadium]})")
print(f"Teams: {user_team} vs {computer_team}")

print(f"\n{user_team} Playing XI:")
for i, player in enumerate(user_playing_xi, 1):
    print(f"{i}. {player}")

print(f"\n{computer_team} Playing XI:")
for i, player in enumerate(computer_playing_xi, 1):
    print(f"{i}. {player}")

# ---------------- MATCH ---------------- #

def play(batting_team, batting_players, bowling_team, total_overs):
    runs = 0
    wickets = 0
    balls_played = 0
    extras = 0

    current_batsman_index = 0
    current_batsman = batting_players[current_batsman_index]

    print(f"\n{batting_team} is batting!")
    print(f"{current_batsman} is on strike.\n")

    while wickets < 10 and balls_played < total_overs * 6:
        current_over = balls_played // 6
        ball_in_over = balls_played % 6

        print(f"Over {current_over}.{ball_in_over} | Score: {runs}/{wickets}")

        try:
            user_input = pyip.inputInt("Enter your input (1-6): ", min=1, max=6)
            extras = 0
        except:
            print("WARNING: Invalid input!")
            extras += 1
            if extras > 2:
                runs += 1
                print("Penalty run awarded.")
                extras = 0
            continue

        computer_input = random.randint(1, 6)
        print(f"Computer input: {computer_input}")

        if user_input == computer_input:
            wickets += 1
            print(f"WICKET! {current_batsman} OUT!")

            if wickets < 10:
                current_batsman_index += 1
                current_batsman = batting_players[current_batsman_index]
                print(f"{current_batsman} comes in.\n")
        else:
            runs += user_input
            print(f"{user_input} runs scored.\n")

        balls_played += 1

    print(f"\nInnings complete: {runs}/{wickets}")
    return runs, wickets

# Overs
total_overs = 20 if match_format == "T20I" else 50

# Match flow
if user_bats_first:
    user_score, _ = play(user_team, user_playing_xi, computer_team, total_overs)
    comp_score, _ = play(computer_team, computer_playing_xi, user_team, total_overs)
else:
    comp_score, _ = play(computer_team, computer_playing_xi, user_team, total_overs)
    user_score, _ = play(user_team, user_playing_xi, computer_team, total_overs)

# Result
if user_score > comp_score:
    print(f"\n{user_team} wins!")
elif comp_score > user_score:
    print(f"\n{computer_team} wins!")
else:
    print("\nMatch tied!")
