A simple cricket game built using Python
This game tries to simulates a cricket match with real conditions ,where the user plays against the computer using number inputs.

=>Game Overview:

The user selects a team

The computer selects a different team

Match format (T20I / ODI) is chosen

Stadium is selected and pitch type is determined

Toss decides who bats first

Match is played ball-by-ball

Wickets fall when user input matches computer input

Otherwise, runs are added

Match ends when overs are completed or all wickets fall
Game Flow

User selects their team

Computer selects a different team


User selects match format:

T20I (20 overs)

ODI (50 overs)

User selects stadium

Pitch type is determined based on stadium

Playing XI for both teams is displayed

Toss takes place (Heads / Tails)

Toss winner chooses to Bat or Bowl

Match details are displayed:

Format

Stadium

Pitch type

Teams

Match begins:

User enters a number (1–6)

Computer generates a random number (1–6)

Same number → Wicket

Different numbers → Runs added

Innings ends when:

10 wickets fall or

Overs are completed

Second innings is played

Winner is decided based on runs

Invalid Input Rules=>

Only numbers between 1 and 6 are valid

Invalid input gives a warning

More than 2 invalid inputs results in 1 penalty run to the batting side

Technologies Used=>

Python 3

Libraries=>

random

pyinputplus

How to Run

Install Python 3

Install dependency:

pip install pyinputplus

Run the game=>

python game.py

