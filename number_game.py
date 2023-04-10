import random 
from game_log_writer import number_gamelogwriter, lastgame

# Generates a random number between 0 and 100
# Asks the user to guess the number and returns their guess and the generated number
def generate_numbers():
    n = random.randint(0,100+1)
    g = int(float(input("Enter a number from 0 to 100: ")))
    return g, n


# Plays the game of guessing a random number
# Calls the generate_numbers function to get the number to be guessed
# Keeps prompting the user to guess the number until they get it right
# Calls the number_gamelogwriter function to log the number of guesses it took to get the right answer
def play_game():
    g, n = generate_numbers()
    guess_count = lastgame('number_game_log.csv')
    while True:
        if g < n:
            print(f'Your guess {g} is too low')
            guess_count += 1
            g= int(float(input('Enter a number for 1 to 100: ')))
        elif g > n :
            print (f'Your guess {g} is too high')
            guess_count += 1
            g = int(float(input('Enter a number from 1 to 100: ')))
        else:
            print(f'Your guess {g} is right! \nCongratulations!')
            guess_count += 1
            number_gamelogwriter('number_game_log.csv',guess_count)
            break

