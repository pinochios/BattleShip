# __import__
import math
from random import randint

from error import *
from header import *

# __main functions__
# Find the index in a list[?] when given a coordinate[x,y]


def positionToIndex(x, y, w, h):
    index = (x-1) + (y-1)*w
    #print("index:", index)
    return index

# Find the coordinate[x,y] when given an index


def indexToPosition(index, w, h):
    x = (index+1) % w
    y = math.ceil((index+1)/w)

    return [x, y]

# Return value when given a index


def positionValue(index, board):
    value = board[index]
    # print(value)
    return value

# alphabetical coordinate to coordinate


def alpToCoordinate(x):
    x = alphabet.index(x) + 1
    return x

#  coordinate to alphabetical coordinate


def coordinateToAlp(x):
    x = alphabet[x-1]
    return x


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
            print("Minimum width is 8, please try again")
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

# Input coordinate with error if its in the board boundary


def positionInput(w, h, prompt):
    print(prompt)
    while True:
        try:
            x = str(input("x: "))
            # Turn alpabetical coordinate to numerical coordinate
            x = alpToCoordinate(x)
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


# def shipGenerator(shipWidth, shipHeight, shipSize, shipNum):

    # __main class__


class Board:
    def __init__(self, board, w, h):
        self.board = board
        self.w = w
        self.h = h

    def boardGenerator(self):
        # set board index
        for x in range(self.w*self.h):
            self.board.append(0)
        """
        # Custom Generate
        for a in range(w*h):
            if a == 11:
                board.append(1)
            else:
                board.append(0)
        """

    def boardHiddenvalGenerator(self):  # TODO : add self
        # set board hidden value index
        # top vertical index value = t
        l = []
        for x in range(self.w):  # Add each position index that need to be change to list
            l.append(positionToIndex(x+1, 1, self.w, self.h))
        for a in l:  # Replace Value using the Given Index
            self.board.pop(a)
            self.board.insert(a, 't')

        # bottom vertical index value = b
        l = []
        for x in range(self.w):
            l.append(positionToIndex(x+1, self.h, self.w, self.h))
        for a in l:
            self.board.pop(a)
            self.board.insert(a, 'b')

        # left index value = r
        l = []
        for y in range(self.h):
            l.append(positionToIndex(1, y+1, self.w, self.h))
        for a in l:
            self.board.pop(a)
            self.board.insert(a, 'l')

        # right index value = r
        l = []
        for y in range(self.h):
            l.append(positionToIndex(self.w, y+1, self.w, self.h))
        for a in l:
            self.board.pop(a)
            self.board.insert(a, 'r')

        # top left hidden value = a
        self.board.pop(0)
        self.board.insert(0, 'tl')

        # top right hidden value = b
        i = positionToIndex(self.w, 1, self.w, self.h)
        self.board.pop(i)
        self.board.insert(i, 'tr')

        # bottom left hidden value = c
        i = positionToIndex(1, self.h, self.w, self.h)
        self.board.pop(i)
        self.board.insert(i, 'bl')

        # bottom right hidden value = d
        i = positionToIndex(self.w, self.h, self.w, self.h)
        self.board.pop(i)
        self.board.insert(i, 'br')

    def boardRenderer(self):
        i = 0
        print("   ", end='')
        # Index Row using a-z
        for a in range(self.w):
            print(" ", end='')
            print(alphabet[a], end='')
        print()

        for a in range(self.h):
            print(a+1, end='')  # Column index
            if a < 9:
                print("   ", end='')  # spacing after index for 1-digit
            else:
                print("  ", end='')  # spacing after index for 2-digit

            # board rendering
            for b in range(self.w):
                print(self.board[i], end='')
                print(" ", end='')
                i += 1
            print()

    def placeShip(self, ship):
        # import hitbox of ship
        tl_x = ship.tl_x
        tl_y = ship.tl_y
        tr_x = ship.tr_x
        tr_y = ship.tr_y
        bl_x = ship.bl_x
        bl_y = ship.bl_y
        br_x = ship.br_x
        br_y = ship.br_y

        # fill space occupied by ship
        l = []
        w = tr_x-tl_x+1
        h = br_y-tl_y+1
        for x in range(w):  # Add each position index that need to be change to list
            for y in range(h):
                l.append(positionToIndex(tl_x+x, tl_y+y, self.w, self.h))
        for a in l:  # Replace Value using the Given Index
            self.board.pop(a)
            self.board.insert(a, 's')

    def removeShip(self, ship):
        # import hitbox of ship
        tl_x = ship.tl_x
        tl_y = ship.tl_y
        tr_x = ship.tr_x
        tr_y = ship.tr_y
        bl_x = ship.bl_x
        bl_y = ship.bl_y
        br_x = ship.br_x
        br_y = ship.br_y

        # fill space occupied by ship
        l = []
        w = tr_x-tl_x+1
        h = br_y-tl_y+1
        for x in range(w):  # Add each position index that need to be change to list
            for y in range(h):
                l.append(positionToIndex(tl_x+x, tl_y+y, self.w, self.h))
        for a in l:  # Replace Value using the Given Index
            self.board.pop(a)
            self.board.insert(a, '0')


# Ship Placement from user input; with variable ship size/number according to board size


class ShipSpec:
    def __init__(self, w, h, shipSize):
        self.w = w
        self.h = h
        self.shipSize = shipSize

    def shipSetup(self):  # TODO - Improve Ship Size Algorithm
        # Setup:
        area = self.w * self.h
        # Length of ship base on size of board
        if self.shipSize == "large":
            shipLength = math.floor(area/math.sqrt(area)/2)
        elif self.shipSize == "medium":
            shipLength = math.floor(area/math.sqrt(area)/2)
            shipLength = shipLength - math.ceil(area/100)
        elif self.shipSize == "small":
            shipLength = math.floor(area/math.sqrt(area)/2)
            shipLength = shipLength - math.ceil(area/100)
            shipLength = shipLength - math.ceil(area/100)
        else:
            print("Invalid Size")

        # Width of ship base on size of board
        if area <= 100:
            shipWidth = 1
        elif area < 150:
            shipWidth = 2
        elif area < 200:
            shipWidth = 3
        else:
            shipWidth = 4

        return [shipLength, shipWidth]

        #randomindex = randomgenerator(w, h)

        # generate some integers

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


class Ship:
    def __init__(self, shipLength, shipWidth):
        self.shipLength = shipLength
        self.shipWidth = shipWidth

    def initLocation(self, initIndex):
        self.initIndex = initIndex  # Set starting Location

    def initHitbox(self, board):  # Generate all 4 points of hitbox
        self.tl = self.initIndex
        self.tr = positionToIndex(
            indexToPosition(self.tl, board.w, board.h)[
                0] + self.shipWidth - 1,  # x
            indexToPosition(self.tl, board.w, board.h)[1],  # y
            board.w,
            board.h
        )
        self.bl = positionToIndex(
            indexToPosition(self.tl, board.w, board.h)[0],  # x
            indexToPosition(self.tl, board.w, board.h)[
                1] + self.shipLength - 1,  # y
            board.w,
            board.h
        )
        self.br = positionToIndex(
            indexToPosition(self.tl, board.w, board.h)[
                0] + self.shipWidth - 1,  # x
            indexToPosition(self.tl, board.w, board.h)[
                1] + self.shipLength - 1,  # y
            board.w,
            board.h
        )

        self.tl_x = indexToPosition(self.tl, board.w, board.h)[0]
        self.tl_y = indexToPosition(self.tl, board.w, board.h)[1]
        self.tr_x = indexToPosition(self.tr, board.w, board.h)[0]
        self.tr_y = indexToPosition(self.tr, board.w, board.h)[1]
        self.bl_x = indexToPosition(self.bl, board.w, board.h)[0]
        self.bl_y = indexToPosition(self.bl, board.w, board.h)[1]
        self.br_x = indexToPosition(self.br, board.w, board.h)[0]
        self.br_y = indexToPosition(self.br, board.w, board.h)[1]

    # Move Ship Hitbox
    def moveHitbox(self, x, y, board):
        self.tl_x = self.tl_x + x
        self.tl_y = self.tl_y + y
        self.tr_x = self.tr_x + x
        self.tr_y = self.tr_y + y
        self.bl_x = self.bl_x + x
        self.bl_y = self.bl_y + y
        self.br_x = self.br_x + x
        self.br_y = self.br_y + y

        self.tl = positionToIndex(self.tl_x, self.tl_y, board.w, board.h)
        self.tr = positionToIndex(self.tr_x, self.tr_y, board.w, board.h)
        self.bl = positionToIndex(self.bl_x, self.bl_y, board.w, board.h)
        self.br = positionToIndex(self.br_x, self.br_y, board.w, board.h)

    # Rotate Ship Clock Wise

    """def rotateCWHitbox(self, board):
        self.board = board
        tl = self.tl # Anchor Point
        tr = self.tr
        bl = self.bl
        br = self.br

        self.tr = br
        self.bl = 
        self.br = """


""" # TODO - place func elsewhere
def randomgenerator(w, h):
    seed(1)
    # generate some integers
    for _ in range(w*h):
        randomindex = randint(0, w*h)

    return randomindex
"""
