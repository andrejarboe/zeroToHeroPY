game_on = True

def display_board(board):
    # board = ['#','#','#','#','#','#','#','#','#','#']
    print(f"        |        |       ")
    print(f"   {board[0]}    |   {board[1]}    |   {board[2]}    ")
    print(f"________|________|_______")
    print(f"        |        |       ")
    print(f"   {board[3]}    |   {board[4]}    |   {board[5]}    ")
    print(f"        |        |       ")

# while game_on:
test_board = [' ',' ',' ','X','O','X','O','X','O','X']
display_board(test_board)