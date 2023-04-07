''' This is the main file. Run this file to select and play a particular
    game.'''

from RPS import play_rps
from ttt import play_ttt
from number_game import play_game
# import checkers.play_checkers

game_lib = {
    1: "Tic-Tac-Toe",
    2: "Number Guessing Game",
    3: "Rock, Paper, Scissors"
}
while True:
    print("""
Your game library:
1: Tic-Tac-Toe
2: Number Guessing Game
3: Rock, Paper, Scissors
""")
    game_choice = input("""
What game would you like to play?
Input the game ID, or type 'exit' to exit.
""")

    if game_choice == '1':
        play_ttt()
        game_choice = None

    elif game_choice == '2':
        play_game()
        game_choice = None

    elif game_choice == '3':
        play_rps()
        game_choice = None
    elif game_choice == 'exit':
        break