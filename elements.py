# import
alphabet = []
for letter in range(97, 123):
    alphabet.append(chr(letter))

# main functions


def boardInput():
    w = 0
    h = 0
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
            print(board[a], end='')
            print(" ", end='')
        print()


def positionToIndex(x, y, w, h):
    index = (x-1) + (y-1)*w
    print(index)


def positionChecker(index):
    pass
