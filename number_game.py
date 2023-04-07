import random 

def generate_numbers():
    n = random.randint(0,100+1)
    g = int(float(input("Enter a number from 0 to 100: ")))
    return g, n

def play_game():
    g, n = generate_numbers()
    while True:
        if g < n:
            print(f'Your guess {g} is too low')
            g= int(float(input('Enter a number for 1 to 100: ')))
        elif g > n :
            print (f'Your guess {g} is too high')
            g = int(float(input('Enter a number from 1 to 100: ')))
        else:
            print(f'Your guess {g} is right! \nCongratulations!')
            input()
            break

