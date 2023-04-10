import random
from game_log_writer import ttt_gamelogwriter, lastgame

#This function asks the user whether they want to play against the computer or against another player, 
# and returns the choice as a string ('PC' or 'Players').
def initial():
    choose = int(input("1.PC 2.Players \nEnter a number : "))
    if choose == 1:
        return 'PC'
    else:
        return 'Players'

# This function takes a list of 9 strings representing the current state of the tic tac toe board, 
# and displays it on the console.
def display_board(board):
    print('\n' * 5)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

# Test Board
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

# This function prompts the user to choose either 'X' or 'O' as their marker, 
# and returns a tuple of both players' markers.
def player_input():
    '''
    OUTPUT = (Player 1 marker,Player 2 marker)
    '''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1:Chooose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#  This function takes the current state of the board, a marker ('X' or 'O'), and a position (1-9), 
#  and updates the board with the marker at the specified position.
def place_marker(board, marker, position):
    board[position] = marker

# This function takes the current state of the board and a marker ('X' or 'O'), and checks if the marker has won the game. 
# Returns True if the marker has won, False otherwise.
def check_win(board, mark):
    return (board[1] == board[2] == board[3] == mark) or \
           (board[4] == board[5] == board[6] == mark) or \
           (board[7] == board[8] == board[9] == mark) or \
           (board[7] == board[4] == board[1] == mark) or \
           (board[2] == board[5] == board[8] == mark) or \
           (board[9] == board[6] == board[3] == mark) or \
           (board[1] == board[5] == board[9] == mark) or \
           (board[7] == board[5] == board[3] == mark)

# This function checks if a space on the board is empty. 
# Returns True if the space is empty, False otherwise.
def space_check(board, position):
    return board[position] == ' '

# This function checks if the board is full. 
# Returns True if the board is full, False otherwise.
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # BOARD IS FULL IF WE RETURN TRUE

    return True

# This function prompts the player to choose a position on the board (1-9) 
# and returns the chosen position as an integer.
def player_choice(board):
    global position
    position = None

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Choose a position: (1-9) '))
        except:
            print("Hey it doesn't seem you are giving a number!!")

    return position

# This function randomly decides which player goes first. 
# If pc is True, then the computer is playing and this function decides whether the computer or the player goes first. 
# Returns the name of the player who goes first ('Player 1', 'Player 2', or 'PC').
def choose_first(pc):
    flip = random.randint(0,1)

    if pc == True:
        if flip == 0:
            return 'Player 1'
        else:
            return'PC'

    else:
        if flip == 0:
            return 'Player 1'
        else:
            return 'Player 2'

# This function prompts the user to play again and returns True if the user enters 'Yes', False otherwise.
def replay():
    choice = input("Play again? Yes or No: ").upper()

    return choice == 'YES'

# This is the main function that runs the tic tac toe game. 
# It calls the other functions to get the user's choices, set up the board, and run the game loop. 
# The game loop checks for a win or a tie, updates the board, and switches the turn to the other player. 
# It also writes the game results to a CSV file.
def play_ttt():
    eee = initial()
    game_count = lastgame('ttt_game_log.csv')
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first(pc = False)
    print(turn + ' will go first')

    play_game = input("Ready to play? y or n : ").lower()

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':

            display_board(the_board)
            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if check_win(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON THE GAME !!!')
                ttt_gamelogwriter(game_count, 'Player 1')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    ttt_gamelogwriter(game_count, 'Tie')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)

            place_marker(the_board, player2_marker, position)

            if check_win(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON THE GAME !!!')
                ttt_gamelogwriter(game_count, 'Player 2')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    ttt_gamelogwriter(game_count, 'Tie')
                    break
                else:
                    turn = 'Player 1'
