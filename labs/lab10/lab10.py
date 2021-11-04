"""
Name: Anastasia Sillsbury
lab10.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def display_board(board):
    row1 = "{0} | {1} | {2}".format(board[0], board[1], board[2])
    row2 = "{0} | {1} | {2}".format(board[3], board[4], board[5])
    row3 = "{0} | {1} | {2}".format(board[6], board[7], board[8])
    print(row1)
    print("----------")
    print(row2)
    print("----------")
    print(row3)


def fill_spot(board, pos, char):
    if board[pos-1] == "X" or board[pos-1] == "O":
        return
    else:
        board[pos-1] = char
    display_board(board)

def is_legal(board, pos):
    if board[pos-1] == "X" or board[pos-1] == "O":
        return False
    else:
        return True


def game_won(board):
    if board[0] == board[1] and board[1] == board[2]:
        print("Game Over!")
        return True
    if board[3] == board[4] and board[4] == board[5]:
        print("Game Over!")
        return True
    if board[6] == board[7] and board[7] == board[8]:
        print("Game Over!")
        return True
    if board[0] == board[3] and board[3] == board[6]:
        print("Game Over!")
        return True
    if board[1] == board[4] and board[4] == board[7]:
        print("Game Over!")
        return True
    if board[2] == board[5] and board[5] == board[8]:
        print("Game Over!")
        return True
    if board[0] == board[4] and board[4] == board[8]:
        print("Game Over!")
        return True
    if board[2] == board[4] and board[4] == board[6]:
        print("Game Over!")
        return True


def game_over(board):
    if game_won:
        return True
    elif type(board[:]) != int:
        return True
    else:
        return False


def play_game():
    board = build_board()
    display_board(board)
    counter = 0
    while counter != 9:
        char = input("What is your character [X or O]: ")
        pos = eval(input("Enter a position [1-9]: "))
        if char == "O":
            is_legal(board, pos)
            fill_spot(board, pos, "0")
            game_won(board)
            game_over(board)
        else:
            is_legal(board, pos)
            fill_spot(board, pos, "X")
            game_won(board)
            game_over(board)
        counter = counter + 1


def main():
    play_game()


main()
