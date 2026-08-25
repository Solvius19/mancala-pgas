global current_player
global board

board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
current_player = 1

def print_board():
    numbers = ""
    print("      13  12  11  10  9   8")
    print("-------------------------------")

    for i in range(13, 7, -1):
        numbers += str(board[i]) + "   "
    print("B:   ", numbers, end="   ")
    print("\n   ",str(board[0]),"                      ", str(board[7]))


    numbers = ""
    for i in range(1, 7):
        numbers += str(board[i]) + "   "
    print("A:   ", numbers, end="   ")
    print("\n-------------------------------")
    print("      1   2   3   4   5   6")

def is_valid_move(pit):
    if current_player == 1:
        return any(board[pit] > 0 for i in range(1, 7))
    else:
        return any(board[pit] > 0 for i in range(8, 14))

def move_stones(pit):
    global current_player
    stones = board[pit]
    board[pit] = 0
    index = pit

    while stones > 0:
        index = (index + 1) % 14
        if board[index] == 0:
            # opposite side code
        board[index] += 1
        if stones == 1: # Accounts for Go Agains
            if (current_player == 1 and index == 7) or (current_player == 2 and index == 0):
                print("Go Again!")
                take_turn()
        stones -= 1

def take_turn():
    global current_player
    possible_moves = ""
    if current_player == 1:
        print("Player 1's Turn!")
        for i in range(1, 7):
            if is_valid_move(i):
                possible_moves += str(i) + " "
    else:
        print("Player 2's Turn!")
        for i in range(8, 14):
            if is_valid_move(i):
                possible_moves += str(i) + " "

    print("Valid Moves:", possible_moves)

    while True:
        try:
            choice = int(input("Choose a pocket: "))
            if current_player == 1:
                if 1 <= choice <= 6:
                    move_stones(choice)
                else:
                    print("Invalid choice. Please choose a pocket from 1 to 6.")
                    continue
            else:
                if 8 <= choice <= 13:
                    move_stones(choice)
                else:
                    print("Invalid choice. Please choose a pocket from 8 to 13.")
                    continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break

def game_over():
    if sum(board[1:7]) == 0 or sum(board[8:14]) == 0:
        return True
    return False

def game_loop():
    global current_player
    while not game_over():
        print_board()
        take_turn()
        current_player = 3 - current_player
    print_board()
    print("Game Over!")

def game_winner():
    print_board()

game_loop()