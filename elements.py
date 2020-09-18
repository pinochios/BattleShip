# __import__
from header import *

# __main functions__


def boardInput():
    while True:
        try:
            w = int(input("Enter the width of the board: "))
        except ValueError:
            print("Invalid value, please try again")
        else:
            if w > 26 or w <= 0:
                print("Maximum width is 26, please try again")
            else:
                break

    while True:
        try:
            h = int(input("Enter the height of the board: "))
        except ValueError:
            print("Invalid value, please try again")
        else:
            break

    return [w, h]


def boardGenerator(w, h):

    board = []
    for a in range(w*h):
        board.append(0)
    return board


def boardRenderer(board, w, h):
    i = 0
    print("   ", end='')
    # Index Row using a-z
    for a in range(w):
        print(" ", end='')
        print(alphabet[a], end='')
    print()

    for a in range(h):
        print(a+1, end='')  # Column index
        if a < 9:
            print("   ", end='')  # spacing after index for 1-digit
        else:
            print("  ", end='')  # spacing after index for 2-digit

        # board rendering
        for b in range(w):
            print(board[i], end='')
            print(" ", end='')
            i += 1
        print()

# Find the postion of the value in a list[?] when given a coordinate[x,y]


def positionToIndex(x, y, w, h):
    index = (x-1) + (y-1)*w
    #print("index:", index)
    return index


def positionValue(index, board):
    # print(board[index])
    return value
