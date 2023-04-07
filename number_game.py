import random 
import game_log_writer

def generate_numbers():
    n = random.randint(0,100+1)
    g = int(float(input("Enter a number from 0 to 100: ")))
    return g, n

def play_game():
    g, n = generate_numbers()
    guess_count = 0
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
            game_log_writer.gamelogwriter('number_game_log.csv',guess_count)
            break

