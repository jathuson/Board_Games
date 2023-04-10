import random
from game_log_writer import rps_gamelogwriter, lastgame

#Get player choices and check if they are valid
def get_user_choice():
    choice = input("Player 1 Enter a choice (r, p, s): ")
    possible_actions = ["r", "p", "s"]
    if choice in possible_actions:
        return choice
    else:
        print("Invalid choice, Please enter a valid choice")

#Get computer choice
def get_computer_choice():
    possible_actions = ["r", "p", "s"]
    computer_choice = random.choice(possible_actions)
    return computer_choice

#Compute the results of the game
def game(choice1, choice2):
    if choice1 == choice2 :
        return "It is a tie.", 'Tie'
    elif choice1 == "r":
        if choice2 == "s":
            return "Player 1 wins", 'Player 1'
        else:
            return "Player 2 wins", 'Player 2'
    elif choice1 == "p":
        if choice2 == "r":
            return "Player 1 wins", 'Player 1'
        else:
            return "Player 2 wins", 'Player 2'
    elif choice1 == "s":
        if choice2 == "p":
            return "Player 1 wins", 'Player 1'
        else:
            return "Player 2 wins", 'Player 2'

#Play RPS game with choices for either against computer or 2 player game
def play_rps():
    game_count = lastgame('rps_game_log.csv')
    play_again = True
    
    while play_again:
        print("Welcome to Rock-Paper-Scissors!")
        print("Choose your opponent:")
        print("1. Another human player")
        print("2. Computer")
        
        opponent_choice = input("Enter your choice (1-2): ")
        while opponent_choice not in ['1', '2']:
            opponent_choice = input("Invalid choice. Enter 1 to play against another human or 2 to play against the computer: ")
        
        if opponent_choice == '1':
            choice1 = get_user_choice("Player 1")
            choice2 = get_user_choice("Player 2")
            print(f"Player 1 chose {choice1} and Player 2 chose {choice2}")
            result, winner = game(choice1, choice2)
        else:
            choice1 = get_user_choice("Player 1")
            choice2 = random.choice(['r', 'p', 's'])
            print(f"Player 1 chose {choice1} and the computer chose {choice2}")
            result, winner = game(choice1, choice2)
        
        print(result)
        rps_gamelogwriter(game_count, winner)
        
        play_again_input = input("Play again? (y/n): ")
        while play_again_input.lower() not in ['y', 'n']:
            play_again_input = input("Invalid input. Enter y to play again or n to quit: ")
        if play_again_input.lower() == "n":
            play_again = False



