player1 = 'X'
player2 = 'O'

board = [["a1", "a2", "a3"],
         ["b1", "b2", "b3"],
         ["c1", "c2", "c3"]]


def player1_turn(schema):
    if schema == "a1":
        board[0][0] = player1
    elif schema == 'a2':
        board[0][1] = player1
    elif schema == 'a3':
        board[0][2] = player1
    elif schema == 'b1':
        board[1][0] = player1
    elif schema == 'b2':
        board[1][1] = player1
    elif schema == 'b3':
        board[1][2] = player1
    elif schema == 'c1':
        board[2][0] = player1
    elif schema == 'c2':
        board[2][1] = player1
    elif schema == 'c3':
        board[2][2] = player1


def player2_turn(schema):
    if schema == "a1":
        board[0][0] = player2
    elif schema == 'a2':
        board[0][1] = player2
    elif schema == 'a3':
        board[0][2] = player2
    elif schema == 'b1':
        board[1][0] = player2
    elif schema == 'b2':
        board[1][1] = player2
    elif schema == 'b3':
        board[1][2] = player2
    elif schema == 'c1':
        board[2][0] = player2
    elif schema == 'c2':
        board[2][1] = player2
    elif schema == 'c3':
        board[2][2] = player2


def check_win(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def position():
    current_player = player1
    while True:
        print(f"{board[0]}\n{board[1]}\n{board[2]}")
        print(f"{current_player} turn")
        print("Game board is 3x3 and each row is named from a-c and column 1-3. Example: a1(1st row 1st column)")
        schema = input("Enter valid field schema: ")
        if current_player == player1:
            player1_turn(schema)
        else:
            player2_turn(schema)

        if check_win(current_player):
            print(f'{current_player} won!')
            break

        current_player = player2 if current_player == player1 else player1
position()
