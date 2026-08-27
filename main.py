global current_player
global board

board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
current_player = 1

extra_turn = False

player1_pits = range(1,7)
player2_pits = range(8,14)

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
        return pit in player1_pits and board[pit] > 0
    else:
        return pit in player2_pits and board[pit] > 0

def move_stones(pit):
    global current_player, extra_turn
    stones = board[pit]
    board[pit] = 0
    index = pit

    while stones > 0:
        index = (index + 1) % 14
        if current_player == 1 and index == 0:
            continue
        if current_player == 2 and index == 7:
            continue
        board[index] += 1
        stones -= 1

    extra_turn = (current_player == 1 and index == 7) or (current_player == 2 and index == 0)

    if board[index] == 1:
        opposite_index = 14 - index
        if current_player == 1 and 1 <= index <= 6:
            if board[opposite_index] > 0:
                board[7] += board[opposite_index] + board[index]
        elif current_player == 2 and 8 <= index <= 13:
            if board[opposite_index] > 0:
                board[0] += board[opposite_index] + board[index]
        board[opposite_index] = 0
        board[index] = 0

def take_turn():
    global current_player
    possible_moves = ""
    if current_player == 1:
        print("Player 1's Turn!")
        for i in player1_pits:
            if is_valid_move(i):
                possible_moves += str(i) + " "
    else:
        print("Player 2's Turn!")
        for i in player2_pits:
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
        calculate_winner()
        return True
    return False

def game_loop():
    global current_player, extra_turn
    while not game_over():
        print_board()
        take_turn()
        if not extra_turn:
            current_player = 3 - current_player
        extra_turn = False
    print_board()
    print("Game Over!")

def calculate_winner():
    if sum(player1_pits) == 0:
        if (sum(player2_pits) + board[0]) < board[7]:
            print("Player 1 wins!")
    if sum(player1_pits) == 0:
        if (sum(player1_pits) + board[7]) < board[0]:
            print("Player 2 wins!")

game_loop()