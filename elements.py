# __import__
from header import *
from error import *
import math
# __main functions__


def boardInput():
    while True:
        try:
            w = int(input("Enter the width of the board: "))
            if w > 26:
                raise ValueTooLargeError
            elif w < 8:
                raise ValueTooSmallError
            else:
                pass
        except ValueError:
            print("Invalid value, please try again")
        except ValueTooLargeError:
            print("Maximum width is 26, please try again")
        except ValueTooSmallError:
            print("Minimum height is 8, please try again")
        else:
            break

    while True:
        try:
            h = int(input("Enter the height of the board: "))
            if h > 26:
                raise ValueTooLargeError
            elif h < 8:
                raise ValueTooSmallError
            else:
                pass
        except ValueError:
            print("Invalid value, please try again")
        except ValueTooLargeError:
            print("Maximum height is 26, please try again")
        except ValueTooSmallError:
            print("Minimum height is 8, please try again")
        else:
            break

    return [w, h]


def boardGenerator(w, h):

    board = []
    for a in range(w*h):
        board.append(0)
    """
    # Custom Generate
    for a in range(w*h):
        if a == 11:
            board.append(1)
        else:
            board.append(0)
    """
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

# Return value when given a index


def positionValue(index, board):
    value = board[index]
    # print(value)
    return value

# Input coordinate with error if its in the board boundary


def positionInput(w, h, prompt):
    print(prompt)
    while True:
        try:
            x = str(input("x: "))
            # Turn alpabetical coordinate to numerical coordinate
            x = alphabet.index(x) + 1
            if x > w:
                raise ValueTooLargeError
            else:
                pass
        except ValueError:
            print("Invalid coordinate, please try again")
        except ValueTooLargeError:
            print("Maximum coordinate x is",
                  alphabet[w-1], ", please try again")
        else:
            break
    while True:
        try:
            y = int(input("y: "))
            if y > h:
                raise ValueTooLargeError
            elif y < 1:
                raise ValueTooSmallError
            else:
                pass
        except ValueError:
            print("Invalid coordinate, please try again")
        except ValueTooLargeError:
            print("Maximum coordinate y is", h, ", please try again")
        except ValueTooSmallError:
            print("Minimum coordinate y is 1, please try again")
        else:
            break

    return[x, y]

# Ship Placement from user input; with variable ship size/number according to board size


def placeShip(w, h):
    # Setup:
    # Length of ship base on size of board
    lShipLength = math.floor(w/2)
    mShipLength = lShipLength - math.ceil(w/10)
    sShipLength = mShipLength - math.ceil(w/10)

    # Width of ship base on size of board
    if w <= 10 and h <= 10:
        shipWidth = 1
    elif w > 10 and h > 10:
        shipWidth = 2
    else:
        shipWidth = 3

    # Default Number of ship
    lShipNum = 1
    mShipNum = 2
    sShipNum = 3

    """
    # Number of ship base on size of board (ship occupy ~20% of board)
    t = w * h  # Total board area
    lShipArea = lShipNum * lShipLength * shipWidth  # Area of ship
    mShipArea = mShipNum * mShipLength * shipWidth
    sShipArea = sShipNum * sShipLength * shipWidth
    fraction = (lShipArea+mShipArea+sShipArea)/t  # Percentage occupied by ship
    print(fraction)
    """

    # Input

    # Placement (x,y,orientation)
