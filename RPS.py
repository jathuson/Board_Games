
import random

#Get player choices and check if they are valid
def get_user_choice():
    choice = input("Player 1 Enter a choice (r, p, s): ")
    possible_actions = ["r", "p", "s"]
    if choice in possible_actions:
        return choice
    else:
        print("Invalid choice, Please enter a valid choice")

#Compute the results of the game
def game(choice1, choice2):
    if choice1 == choice2 :
        return "It is a tie."
    elif choice1 == "r":
        if choice2 == "s":
            return "Player 1 wins"
        else:
            return "Player 2 wins"
    elif choice1 == "p":
        if choice2 == "r":
            return "Player 1 wins"
        else:
            return "Player 2 wins"
    elif choice1 == "s":
        if choice2 == "p":
            return "Player 1 wins"
        else:
            return "Player 2 wins"

def play_rps():
    Play_again = True
    game_count = 0
    while Play_again:
        choice1 = get_user_choice()
        choice2 = get_user_choice()
        print(f"Player 1 chose {choice1} and Player 2 chose {choice2}")

        result = game(choice1,choice2)
        print(result)
        
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break




