
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def is_game_over(board):
    return is_winner(board, "X") or is_winner(board, "O") or is_full(board)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if is_winner(board, "X"):
        return -1
    if is_winner(board, "O"):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    best_move = (-1, -1)
    for i, j in get_empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe")
    print_board(board)

    while not is_game_over(board):
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] == " ":
            board[row][col] = "X"
            print_board(board)
        else:
            print("Invalid move. Try again.")
            continue

        if not is_game_over(board):
            ai_row, ai_col = best_move(board)
            board[ai_row][ai_col] = "O"
            print("AI's move:")
            print_board(board)

    if is_winner(board, "X"):
        print("You win!")
    elif is_winner(board, "O"):
        print("AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
