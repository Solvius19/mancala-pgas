
board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
current_player = 1

def print_board():
    numbers = ""
    print("      13  12  11  10  9   8")
    print("-------------------------------")

    for i in range(13, 7, -1):
        numbers += str(board[i]) + "   "
    print("B:   ", numbers, end="   ")
    print("\n    0                        0")

    numbers = ""
    for i in range(1, 7):
        numbers += str(board[i]) + "   "
    print("A:   ", numbers, end="   ")
    print("\n-------------------------------")
    print("      1   2   3   4   5   6")

def is_valid_move(player, number):
    if player == 1:
        return any(board[i] > 0 for i in range(1, 7))
    else:
        return any(board[i] > 0 for i in range(8, 14))

def move_stones(player, pit):
    stones = board[pit]
    board[pit] = 0
    index = pit

    while stones > 0:
        index = (index + 1) % 14
        if (player == 1 and index == 7) or (player == 2 and index == 0):
            continue
        board[index] += 1
        stones -= 1

def take_turn(player):
    if player == 1:
        print("Player 1's Turn!")
    else:
        print("Player 2's Turn!")

    while (is_valid_move(player) == True):
        print_board()
    print("Valid Moves: ", end="")

    return index


print_board()