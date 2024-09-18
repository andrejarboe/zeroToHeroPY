game_on = True
game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

display_game(game_list)

def position_choice():

    choice = 'wrong'

    while choice not in range(0,3):

        choice = input("Pick a position (0,1,2): ")

        if int(choice) not in range(0,3):
            print("Sorry, invalid choice! ")
    
    return int(choice)

# position_choice()

def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement

    return game_list

replacement_choice(game_list, 1)

print(game_list)

def gameon_Choice():

    while choice not in ['Y, N']:
        choice = input("Keep playing? (Y) Yes or (N) No")

        if choice is not ['Y, N']:
            print("Sorry, please Y or N ")
    
    if choice == "Y":
        return True
    else:
        return False

gameon_Choice()

while game_on:
    display_game()

    position = position_choice()

    replacement_choice(game_list, position)