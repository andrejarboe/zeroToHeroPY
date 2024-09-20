game_on = True
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']


def display_board(board):
    # board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print(f"        |        |       ")
    print(f"   {board[0]}    |   {board[1]}    |   {board[2]}    ")
    print(f"________|________|_______")

    print(f"        |        |       ")
    print(f"   {board[3]}    |   {board[4]}    |   {board[5]}    ")
    print(f"________|________|_______")

    print(f"        |        |       ")
    print(f"   {board[6]}    |   {board[7]}    |   {board[8]}    ")
    print(f"        |        |       ")

# while game_on:


def playerInput():
    choice = 'A'
    while choice not in ['X', 'O']:
        choice = input("Player 1: Do you want to be X or O? ").upper()
        # print(f"choice; {choice}")
        if choice not in ['X', 'O']:
            print("Sorry, please X or O")
    return choice
def playerSelection(player1):
    if player1 == "X":
        return "O"
    else:
        return "x"

def chosePosition(currentPlayer):
    choice = '0'
    
    while int(choice) not in range (1,10):
        choice = input(f"{currentPlayer} Choose your next position: 1 - 9: ")

        if int(choice) not in range(1,10) or board[int(choice)] != ' ':
            print(f'Sorry, "{choice}" is an invalid choice! ')
            # choice = '0'

    return int(choice) - 1

def updateBoard(currentPlayer, position):
    board[position] = currentPlayer

def switchPlayer(currentPlayer):
    if currentPlayer == player1:
        currentPlayer = player2
    else:
        currentPlayer = player1

    return currentPlayer

def checkWin(currentPlayer):
    if board[0:2] == currentPlayer:
        return True
    elif board[3:5] == currentPlayer:
        return True
    elif board[5:8] == currentPlayer:
        return True
    # check diagonal
    elif board[5:8] == currentPlayer:
        return True
    else:
        return False
    
    


print("Welcome to Tic Tac Toe!")
player1 = playerInput()
player2 = playerSelection(player1)
currentPlayer = player1
print(f"Player 1 is {player1}")
print("Player1 will go first. ")
ready = input("Are you ready to start the game?: Yes or No ").lower()
if ready == "y" or ready == "yes":
    game_on = True
else: game_on = False

while game_on:
    display_board(board)
    position = chosePosition(currentPlayer)
    updateBoard(currentPlayer, position)
    game_on = checkWin(currentPlayer)
    currentPlayer = switchPlayer(currentPlayer)
    

# test_board = [' ',' ','O','X','O','X','O','X','O','X']