import csv 

# Function to create or clear a game log file with the given headers
def create_game_log(file_name, headers):
     with open(file_name, 'w', newline='') as file:
          writer = csv.writer(file)

          writer.writerow(headers)
          
# Function to write a record to the number game log file
def number_gamelogwriter(guess_count):
     try:
        game_count = int(game_count) # Attempt to convert game_count to int
     except TypeError:
        game_count = 1 # Set game_count to 1 if a TypeError occurs
     except ValueError:
        game_count = 1 # Set game_count to 1 if a ValueError occurs

     with open('number_game_log.csv', 'a', newline='') as file:
          writer = csv.writer(file)

          writer.writerow([2,"Correct", guess_count]) # Write a record to the number game log file


# Function to write a record to the Tic Tac Toe game log file
def ttt_gamelogwriter(game_count, player):
     try:
        game_count = int(game_count) # Attempt to convert game_count to int
     except TypeError:
        game_count = 1 # Set game_count to 1 if a TypeError occurs
     except ValueError:
        game_count = 1 # Set game_count to 1 if a ValueError occurs
     
     with open('ttt_game_log.csv', 'a', newline='') as file:
          writer = csv.writer(file)

          writer.writerow([game_count, player]) # Write a record to the Tic Tac Toe game log file


# Function to write a record to the Rock Paper Scissors game log file
def rps_gamelogwriter(game_count, player):
     try:
          game_count = int(game_count) # Attempt to convert game_count to int
     except TypeError:
        game_count = 1 # Set game_count to 1 if a TypeError occurs
     except ValueError:
        game_count = 1 # Set game_count to 1 if a ValueError occurs
     

     with open('rps_game_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([game_count, player]) # Write a record to the Rock Paper Scissors game log file


# Function to get the game number of the last game in the game log file
def lastgame(file_name):
     with open(file_name, "r", encoding="utf-8") as file:
        final_game_number = file.readlines()[-1][0] # Read the last line of the file and extract the game number
     return final_game_number # Return the game number of the last game in the game log file
