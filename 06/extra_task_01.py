import os

_SIDE_SIZE = 3

def create_square_field(side_size: int) -> list:
    field = [[0] * side_size for i in range(side_size)]

    return field

def clear_screen():
    # For some terminals that don't understand 'cls' or 'clear'
    for i in range(100):
        print()

    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

def print_field(field: list, sym: list):
    x = len(field[0])
    y = len(field)
    x_scale: int = 0
    y_scale: int = 0

    clear_screen()

    for ix in range(x * 2 + 1):
        if ix == 0:
            print("  ", end="")
        if (ix % 2) != 0:
            x_scale += 1
            print(f"{x_scale}", end="")
        else:
            print(" ", end="")
    print()

    for iy in range(y * 2 + 1):
        if (iy % 2) == 0:
            for ix in range(x + 1):
                if ix == 0:
                    print("  +", end="")
                else:
                    print("+", end="")
                if ix < x:
                    print("-", end="")

            print()
        else:
            for ix in range(x * 2):
                if (ix % 2) == 0:
                    if ix == 0:
                        y_scale += 1
                        print(f"{y_scale} |", end="")
                    print(sym[field[iy // 2][ix // 2]], end="")
                else:
                    print("|", end="")

            print()

def make_step(field: list, gamers: list, curr_user: int, sym: list):
    step_in_progress: bool = True

    while(step_in_progress):
        print("Player's '{}' step...".format(gamers[curr_user]))
        row_step = int(input("Enter the row number: ")) - 1
        col_step = int(input("Enter the column number: ")) - 1

        if row_step > len(field) or col_step > len(field) or \
           row_step < 0 or col_step < 0:
            print("Invalid value entered, try again.")
        elif field[row_step][col_step] != 0:
            print("This field is occupied. Specify another.")
        else:
            field[row_step][col_step] = curr_user + 1
            step_in_progress = False

def victory_check(field: list, sym: list, gamers: list):
    user_1: int = 0
    user_2: int = 0

    # Horizontal check
    for row_val in field: 
        for col_val in row_val: 
            if col_val == sym.index(gamers[0]):
                user_1 += 1
            elif col_val == sym.index(gamers[1]):
                user_2 += 1

        if user_1 == len(field):
            return True, 0
        elif user_2 == len(field):
            return True, 1
        else:
            user_1 = 0
            user_2 = 0

    # Vertical check
    for col_idx in range(len(field[0])): 
        for row_val in field: 
            if row_val[col_idx] == sym.index(gamers[0]):
                user_1 += 1
            if row_val[col_idx] == sym.index(gamers[1]):
                user_2 += 1

        if user_1 == len(field):
            return True, 0
        elif user_2 == len(field):
            return True, 1
        else:
            user_1 = 0
            user_2 = 0

    # First diagonal check
    for i in range(len(field)):
        if field[i][i] == sym.index(gamers[0]):
            user_1 += 1
        if field[i][i] == sym.index(gamers[1]):
            user_2 += 1

    if user_1 == len(field):
        return True, 0
    elif user_2 == len(field):
        return True, 1
    else:
        user_1 = 0
        user_2 = 0

    # Second diagonal check
    for i in range(len(field)):
        if field[i][(len(field) - 1) - i] == sym.index(gamers[0]):
            user_1 += 1
        if field[i][(len(field) - 1) - i] == sym.index(gamers[1]):
            user_2 += 1

    if user_1 == len(field):
        return True, 0
    elif user_2 == len(field):
        return True, 1
    else:
        user_1 = 0
        user_2 = 0

    return False, -1

def check_drawn_game(field: list) -> bool:
    sum: int = 0

    for row_val in field: 
        for col_val in row_val:
            if col_val != 0:
                sum += 1
    
    if sum >= len(field) * len(field):
        return True
    else:
        return False


gamers: list = ["X", "0"]
sym = [" ", "X", "0"]
user_piece: int = 1
pc_piece: int = 2
game_over: bool = False
drawn_game: bool = False
game_in_progress: bool = True
curr_user: int = 0
winner: int = -1

field: int = create_square_field(_SIDE_SIZE)
print_field(field, sym)

while(game_in_progress):
    make_step(field, gamers, curr_user, sym)
    print_field(field, sym)

    game_over, winner = victory_check(field, sym, gamers)
    if game_over:
        game_in_progress = False
        print("The game is over. Winner: {}".format(gamers[winner]))
    elif check_drawn_game(field):
        game_in_progress = False
        print("The game is over in a draw.")
    else:
        if curr_user == 0:
            curr_user = 1
        else:
            curr_user = 0