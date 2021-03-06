from random import randint

board = []

for x in range(6):
    board.append(["O"] * 4)


def print_board(board):
    for row in board:
        print " ".join(row)


print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
# To cheat, uncomment these:
# print ship_row
# print ship_col


# Everything from here on should go in your for loop!
def check_status(guess_row, guess_col):
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "@"
        print_board(board)
    elif guess_row not in range(5) or guess_col not in range(5):
        print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        print_board(board)


misses = 0
while misses < 4:
    misses += 1
    print "Move: %s" % misses
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    check_status(guess_row, guess_col)
    if guess_row == ship_row and guess_col == ship_col:
        break

print "Game Over"
