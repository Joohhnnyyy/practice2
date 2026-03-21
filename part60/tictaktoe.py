import math

board = [" " for _ in range(9)]

# Display the board
def print_board():
    print("\nCurrent Board")
    print("-----------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-----------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-----------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-----------------")


def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True

    return False


def is_draw():
    return " " not in board


# Minimax with Alpha-Beta pruning
def minimax(is_max, alpha, beta):

    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:

        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False, alpha, beta)
                board[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:

        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True, alpha, beta)
                board[i] = " "
                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best


def best_move():

    best_score = -math.inf
    move = -1

    for i in range(9):

        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, -math.inf, math.inf)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


print("\n========== TIC TAC TOE (AI) ==========")
print("You are X")
print("AI is O")
print("Positions are numbered 1-9\n")

while True:

    print_board()

    player_move = int(input("Enter position (1-9): ")) - 1

    if board[player_move] != " ":
        print("Invalid move. Try again.")
        continue

    board[player_move] = "X"

    if check_winner("X"):
        print_board()
        print("\n🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("\nGame Draw!")
        break

    ai = best_move()
    board[ai] = "O"

    print("\nAI chooses position", ai+1)

    if check_winner("O"):
        print_board()
        print("\n🤖 AI Wins!")
        break

    if is_draw():
        print_board()
        print("\nGame Draw!")
        break