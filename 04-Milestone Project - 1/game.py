import random

def display_board(board):
    # board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print('\n'*100)
    # clear_output()
    print(f"        |        |       ")
    print(f"   {board[1]}    |   {board[2]}    |   {board[3]}    ")
    print(f"________|________|_______")

    print(f"        |        |       ")
    print(f"   {board[4]}    |   {board[5]}    |   {board[6]}    ")
    print(f"________|________|_______")

    print(f"        |        |       ")
    print(f"   {board[7]}    |   {board[8]}    |   {board[9]}    ")
    print(f"        |        |       ")
    
    # print(f"=========================")


# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)
# display_board(test_board)

def player_input():
    '''
        OUTPUT = (player1 marker, player 2 marker)
    ''' 

    marker = ''

    #  ask player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# 
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (
        # check all rows
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        # check all columns
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark) or
        # check 2 diaangonals 
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[7] == mark and board[5] == mark and board[3] == mark) 
    )


def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

# check tie
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full
    return True

# CHOOSE POSITION
def choosePosition(board):
    position = 0

    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose a position (1-9) '))
    return position

def replay():
    choice = input('Play again? Enter Yes or No: ')
    return choice == 'Yes' or 'y' or 'yes'

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = [' '] * 10
    player1Marker, player2Marker = player_input()
    
    turn = choose_first()
    print(f"{turn} will go first")

    playGame = input('Ready to play? y or n?: ')

    if playGame == 'y':
        gameOn = True
    else:
        gameOn = False


    while gameOn:
        #Player 1 Turn
        if turn == 'Player 1':
            display_board(board)
            
            # choose position
            position = choosePosition(board)

            # place marker
            place_marker(board, player1Marker, position)

            # check win 
            if win_check(board, player1Marker):
                display_board(board)
                print(f'{turn} is the winner!!!')
                gameOn = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print(f'Tie Game!!!')
                    gameOn = False
                else:
                    # change turns.
                    turn = 'Player 2'

        # Player2's turn.
        else:
            display_board(board)
            
            # choose position
            position = choosePosition(board)

            # place marker
            place_marker(board, player2Marker, position)

            # check win 
            if win_check(board, player2Marker):
                display_board(board)
                print(f'{turn} is the winner!!!')
                gameOn = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print(f'Tie Game!!!')
                    gameOn = False
                else:
                    # change turns.
                    turn = 'Player 1'

    if not replay():
        break
