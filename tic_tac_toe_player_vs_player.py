board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player1 = "X"
player2 = "O"
current_player = player1
winner = None
game_running = True

# Print the board.


def print_board(field):
    print(f"{field[0]} | {field[1]} | {field[2]} |")
    print(f"{field[3]} | {field[4]} | {field[5]} |")
    print(f"{field[6]} | {field[7]} | {field[8]} |")


# Player 1 move.


def player1_move(field):
    valid_move = False
    while not valid_move:
        move = int(input("Player one move 1-9: "))
        if 0 <= move <= 9:
            if field[move-1] == "-":
                field[move-1] = player1
                valid_move = True
            else:
                print("Invalid move!")
        else:
            print("Invalid move!")
            continue


# Player 2 move.


def player2_move(field):
    valid_move = False
    while not valid_move:
        move = int(input("Player two move 1-9: "))
        if 0 <= move <= 9:
            if field[move-1] == "-":
                field[move-1] = player2
                valid_move = True
            else:
                print("Invalid move!")
        else:
            print("Invalid move!")
            continue


# Switch players.


def switch_players():
    global current_player
    if current_player == player1:
        player1_move(board)
        current_player = player2
    else:
        player2_move(board)
        current_player = player1


# Check for win or tie.


def check_horizontal(field):
    global winner
    if field[0] == field[1] == field[2] and field[0] != "-":
        winner = field[0]
        return True
    elif field[3] == field[4] == field[5] and field[3] != "-":
        winner = field[3]
        return True
    elif field[6] == field[7] == field[8] and field[6] != "-":
        winner = field[6]
        return True


def check_vertical(field):
    global winner
    if field[0] == field[3] == field[6] and field[0] != "-":
        winner = field[0]
        return True
    elif field[1] == field[4] == field[7] and field[1] != "-":
        winner = field[1]
        return True
    elif field[2] == field[5] == field[8] and field[2] != "-":
        winner = field[2]
        return True


def check_diagonal(field):
    global winner
    if field[0] == field[4] == field[8] and field[0] != "-":
        winner = field[0]
        return True
    elif field[2] == field[4] == field[6] and field[2] != "-":
        winner = field[2]
        return True


def check_tie():
    global winner
    if "-" not in board:
        winner = None
        return True


def check_winner():
    global game_running
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        game_running = False
        if winner == "X":
            print(f"\nWinner: Player 1 ({player1})")
            print_board(board)
        else:
            print(f"\nWinner: Player 2 ({player2})")
            print_board(board)
    elif check_tie():
        game_running = False
        print("Draw!")
        print_board(board)


# The game.


while game_running:
    print_board(board)
    switch_players()
    check_winner()
