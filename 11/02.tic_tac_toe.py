first_line = input().split()
second_line = input().split()
third_line = input().split()

the_board = first_line + second_line + third_line

the_board = [int(player) for player in the_board]

first_player = 0
second_player = 0

if the_board[0] == the_board[1] == the_board[2]:
    if the_board[0] == 1:
        first_player += 1
    elif the_board[0] == 2:
        second_player += 1

if the_board[3] == the_board[4] == the_board[5]:
    if the_board[3] == 1:
        first_player += 1
    elif the_board[3] == 2:
        second_player += 1

if the_board[6] == the_board[7] == the_board[8]:
    if the_board[6] == 1:
        first_player += 1
    elif the_board[6] == 2:
        second_player += 1

if the_board[0] == the_board[3] == the_board[6]:
    if the_board[0] == 1:
        first_player += 1
    elif the_board[0] == 2:
        second_player += 1

if the_board[1] == the_board[4] == the_board[7]:
    if the_board[1] == 1:
        first_player += 1
    elif the_board[1] == 2:
        second_player += 1

if the_board[2] == the_board[5] == the_board[8]:
    if the_board[2] == 1:
        first_player += 1
    elif the_board[2] == 2:
        second_player += 11

if the_board[0] == the_board[4] == the_board[8]:
    if the_board[0] == 1:
        first_player += 1
    elif the_board[0] == 2:
        second_player += 1

if the_board[2] == the_board[4] == the_board[6]:
    if the_board[2] == 1:
        first_player += 1
    elif the_board[2] == 2:
        second_player += 1

if first_player == second_player:
    print("Draw!")
elif first_player > second_player:
    print("First player won")
else:
    print("Second player won")

