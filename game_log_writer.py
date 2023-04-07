import csv 
def create_game_log():
     with open('number_game_log.csv', 'w', newline='') as file:
          writer = csv.writer(file)

          writer.writerow(["Game #", "Outcome", "Number of Tries"])
          
     
def number_gamelogwriter(guess_count):
     with open('number_game_log.csv', 'a', newline='') as file:
          writer = csv.writer(file)

          writer.writerow([2,"Correct", guess_count])

def ttt_gamelogwriter(game_count, player):
     with open('ttt_game_log.csv', 'a', newline = '') as file:
          writer = csv.writer(file)

          writer.writerow([game_count, player])