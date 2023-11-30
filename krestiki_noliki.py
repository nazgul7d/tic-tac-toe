def krestiki_noliki():
    player1 = 'X'
    player2 = 'O'

    current_player = player1

    board = [[' 'for i in range(3)] for j in range(3)]

    # winning conditions

    def check_horizontal(board, player):
        for row in range(len(board)):
            if all(cell == player for cell in board[row]):
                return True
        return False
    
    def check_vertical(board, player):
        for col in range(len(board[0])):
            if all(board[row][col] == player for row in range(len(board))):
                    return True
        return False

    def check_diagonal(board, player):
        if all(board[i][i] == player for i in range(len(board))):
            return True
        return False
    
    def check_antidiagonal(board, player):
        num_rows = len(board)
        num_cols = len(board[0])
        if all(board[i][num_cols - 1 - i] == player for i in range(num_rows)):
            return True
        return False
    
    # check wins

    def check_win(board, player):
        return (
            check_horizontal(board, player) or
            check_vertical(board, player) or
            check_diagonal(board, player) or
            check_antidiagonal(board, player)
        )
    
    # print the board
    def print_board(board):
        for row in board:
            print('|'.join(row))
            print('-' * 5)
    
    # check if board is full
    def is_board_full(board):
        return all(cell != ' ' for row in board for cell in row)
    
    def make_move(row, col):
        if board[row][col] == ' ':
            board[row][col] = current_player
            return True
        else:
            print("Invalid row or col selection. Please try again" )
            return False
    
    # switch players after every move
    def switch_player():
        nonlocal current_player
        current_player = player2 if current_player == player1 else player1 
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if 0 <= row < 3 and 0 <= col < 3:
            if make_move(row, col):
                if check_win(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                else:
                    switch_player()
        else:
            print("Invalid row or column. Try again.")

krestiki_noliki()






