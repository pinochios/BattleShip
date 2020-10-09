# __import__
import math
import click
import sys
from random import randint

from error import *
from header import *
from keyboardInput import *

# __main functions__


def findAllIndex(list, givenValue):
    """
    find all index with the value given in a list
    """
    result = []
    for index, value in enumerate(list):
        if value == givenValue:
            result.append(index)
    return result


def positionToIndex(x, y, w, h):
    """Find the index when given a coordinate[x,y]

    Args:
        x ([int]): [x to convert]
        y ([int]): [y to convert]
        w ([int]): [board.w]
        h ([int]): [board.w]

    Returns:
        [int]: [index]
    """
    index = (x-1) + (y-1)*w
    #print("index:", index)
    return index


def indexToPosition(index, w, h):
    """Find the coordinate[x,y] when given an index

    Args:
        index ([int]): [index to convert]
        w ([int]): [board.w]
        h ([int]): [board.w]

    Returns:
        [list]: [x,y]
    """
    x = (index+1) % w
    y = math.ceil((index+1)/w)

    if x == 0:
        x = w

    return [x, y]


def positionValue(index, board):
    """
    Return value when given a index
    """
    value = board[index]
    # print(value)
    return value


def alpToCoordinate(x):
    """
    alphabetical coordinate to coordinate  
    """
    x = alphabet.index(x) + 1
    return x


def coordinateToAlp(x):
    """
    coordinate to alphabetical coordinate
    """
    x = alphabet[x-1]
    return x


def boardInput():
    """Ask for user input for the board size (8-26)

    Raises:
        ValueTooLargeError: ["Maximum width is 26, please try again"]
        ValueTooSmallError: ["Minimum width is 8, please try again"]
        ValueTooLargeError: ["Maximum height is 26, please try again"]
        ValueTooSmallError: ["Minimum height is 8, please try again"]

    Returns:
        [list]: [w,h]
    """
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
    """Ask for user input of  x(a-z) and y(0-26) and convert to x(0-26) and y(0-26)

    Args:
        w (int): board width
        h (int): board height
        prompt (string): prompt to display

    Raises:
        ValueError: ["Invalid coordinate, please try again"]
        ValueTooLargeError: ["Maximum coordinate x is (width),please try again"]
        ValueTooSmallError: ["Maximum coordinate y is (height),please try again"]

    Returns:
        [list]: [x,y]
    """
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
        except KeyboardInterrupt:
            sys.exit()
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
        except KeyboardInterrupt:
            sys.exit()
        else:
            break

    return[x, y]


def keyboardShipMove(Ship, Board, BoardBoarder, BoardTemporary, playerName):
    """
    docstring : import keyboard input and move Ship using moveHitbox(), boardRenderer()
    """
    print(playerName, " place your ships:\n\n")
    BoardTemporary.boardRenderer()
    while True:
        std_checkBoarder = BoardBoarder.checkBoarder(Ship)
        std_checkOccupancy = Board.checkOccupancy(Ship)
        x = 0
        y = 0
        key = keyboardInput()
        click.clear()
        if key == 'up' and not (std_checkBoarder == 'top' or std_checkBoarder == 'tr' or std_checkBoarder == 'tl'):
            y = -1
        elif key == 'down' and not (std_checkBoarder == 'bottom' or std_checkBoarder == 'br' or std_checkBoarder == 'bl'):
            y = 1
        elif key == 'left' and not (std_checkBoarder == 'left' or std_checkBoarder == 'bl' or std_checkBoarder == 'tl'):
            x = -1
        elif key == 'right' and not (std_checkBoarder == 'right' or std_checkBoarder == 'br' or std_checkBoarder == 'tr'):
            x = 1
        elif key == 'cv':
            click.clear()
            BoardTemporary.removeShip(Ship)
            Ship.rotateHitbox(Board)
        elif key == 'confirm' and not std_checkOccupancy:
            # copy the temporary board to the main board
            Board.board = BoardTemporary.board.copy()
            break
        elif std_checkOccupancy:
            print(
                "----------------------- Space Already Occupied -----------------------")
        else:
            print("----------------------- Invalid Input -----------------------")

        BoardTemporary.removeShip(Ship)
        Ship.moveHitbox(x, y, Board)
        BoardTemporary.placeShip(Ship)
        print("-----------------------", playerName,
              "place your ships" "-----------------------",)
        BoardTemporary.boardRenderer()

        # def shipGenerator(shipWidth, shipHeight, shipSize, shipNum):

        # __main class__


class Player():
    def __init__(self, name):
        self.name = name
        self.shipHit = 0
        self.attempt = []

    def initBoard(self, boardSize):
        """Init all necessary board for the player

        Args:
            boardSize([w,h]) - width height of board from user input
        """
        boardTemplate = []
        self.board = Board(boardTemplate.copy(), boardSize[0], boardSize[1])
        self.board.boardGenerator()

        self.boardBoarder = Board(
            boardTemplate.copy(), boardSize[0], boardSize[1])
        self.boardBoarder.boardGenerator()
        self.boardBoarder.boardBoarder()

        self.boardTemporary = Board(
            boardTemplate.copy(), boardSize[0], boardSize[1])
        self.boardTemporary.boardGenerator()

    def initShip(self):
        """ 
        Init all ships to the board and let user move ships desire location
        """
        # ship objects
        self.largeShipSpec = ShipSpec(self.board.w, self.board.h, "large")
        self.largeShip = Ship(self.largeShipSpec.shipSetup()[
            0], self.largeShipSpec.shipSetup()[1])

        self.mediumShipSpec = ShipSpec(self.board.w, self.board.h, "medium")
        self.mediumShip = Ship(self.mediumShipSpec.shipSetup()[
            0], self.mediumShipSpec.shipSetup()[1])

        self.smallShipSpec = ShipSpec(self.board.w, self.board.h, "small")
        self.smallShip = Ship(self.smallShipSpec.shipSetup()[
            0], self.smallShipSpec.shipSetup()[1])

        # init ship
        self.largeShip.initLocation(0)
        self.largeShip.initHitbox(self.board)
        self.mediumShip.initLocation(0)
        self.mediumShip.initHitbox(self.board)
        self.smallShip.initLocation(0)
        self.smallShip.initHitbox(self.board)

        # user move ships
        # first place ship in temporary board
        self.boardTemporary.placeShip(self.largeShip)
        keyboardShipMove(self.largeShip, self.board,
                         self.boardBoarder, self.boardTemporary, self.name)

        # first place ship in temporary board
        self.boardTemporary.placeShip(self.mediumShip)
        keyboardShipMove(self.mediumShip, self.board,
                         self.boardBoarder, self.boardTemporary, self.name)

        # first place ship in temporary board
        self.boardTemporary.placeShip(self.smallShip)
        keyboardShipMove(self.smallShip, self.board,
                         self.boardBoarder, self.boardTemporary, self.name)


class Board:
    def __init__(self, board, w, h):
        self.board = board
        self.w = w
        self.h = h

    def boardGenerator(self):
        """
        generate board base on w,h
        """
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

    def boardBoarder(self):
        """
        generate boardBoarder base on w,h

        * USE IN CONJUNCTION WITH boardGenerator()*
        """
        # set board hidden value index
        # top vertical index value = t
        l = []
        for x in range(self.w):  # Add each position index that need to be change to list
            l.append(positionToIndex(x+1, 1, self.w, self.h))
        for a in l:  # Replace Value using the Given Index
            self.board.pop(a)
            self.board.insert(a, 't')
        self.t_Boarder = l  # store list to object

        # bottom vertical index value = b
        l = []
        for x in range(self.w):
            l.append(positionToIndex(x+1, self.h, self.w, self.h))
        for a in l:
            self.board.pop(a)
            self.board.insert(a, 'b')
        self.b_Boarder = l  # store list to object

        # left index value = r
        l = []
        for y in range(self.h):
            l.append(positionToIndex(1, y+1, self.w, self.h))
        for a in l:
            self.board.pop(a)
            self.board.insert(a, 'l')
        self.l_Boarder = l  # store list to object

        # right index value = r
        l = []
        for y in range(self.h):
            l.append(positionToIndex(self.w, y+1, self.w, self.h))
        for a in l:
            self.board.pop(a)
            self.board.insert(a, 'r')
        self.r_Boarder = l  # store list to object

        # top left hidden value = a
        self.board.pop(0)
        self.board.insert(0, 'tl')
        self.tl_Boarder = 0  # store list to object

        # top right hidden value = b
        i = positionToIndex(self.w, 1, self.w, self.h)
        self.board.pop(i)
        self.board.insert(i, 'tr')
        self.tr_Boarder = i  # store list to object

        # bottom left hidden value = c
        i = positionToIndex(1, self.h, self.w, self.h)
        self.board.pop(i)
        self.board.insert(i, 'bl')
        self.bl_Boarder = i  # store list to object

        # bottom right hidden value = d
        i = positionToIndex(self.w, self.h, self.w, self.h)
        self.board.pop(i)
        self.board.insert(i, 'br')
        self.br_Boarder = i  # store list to object

    def boardRenderer(self):
        """
        Render Board
        """
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
        """Place Ship Object onto the board using hitbox attribute

        Args:
            ship (object): [ship to place]
        """
        self.oldValue = []

        for a in ship.hitbox:  # Replace Value using the Given Hitbox Indices
            self.oldValue.append(self.board[a])   # Record Old Value
            self.board.pop(a)
            self.board.insert(a, 's')

    def removeShip(self, ship):
        """Remove Ship Object onto the board using hitbox attribute

        Args:
            ship (object): [ship to remove]
        """
        # fill space occupied by ship
        i = 0
        for a in ship.hitbox:  # Replace Value using the Given Hitbox Indices
            self.board.pop(a)
            self.board.insert(a, self.oldValue[i])
            i += 1

    def checkBoarder(self, ship):
        """ ****USE WITH BOARDBOARDER[object]*** Check if a ship is up against the boarder

        Args:
            ship (Ship[object]): use hitbox location to compare to boardhiddenvalue

        Returns:
            [string]: left, right, top, bottom, tl ,tr, bl ,br
        """
        status = 'Null'
        for c in self.l_Boarder:
            if (ship.tl == c or ship.tr == c or ship.bl == c or ship.br == c):
                status = 'left'
        for c in self.r_Boarder:
            if (ship.tl == c or ship.tr == c or ship.bl == c or ship.br == c):
                status = 'right'
        for c in self.t_Boarder:
            if (ship.tl == c or ship.tr == c or ship.bl == c or ship.br == c):
                status = 'top'
        for c in self.b_Boarder:
            if (ship.tl == c or ship.tr == c or ship.bl == c or ship.br == c):
                status = 'bottom'

        c = self.tl_Boarder
        if (ship.tl == c or ship.tr == c or ship.bl == c or ship.br == c):
            status = 'tl'

        c = self.tr_Boarder
        if (ship.tl == c or ship.tr == c or ship.bl == c or ship.br == c):
            status = 'tr'

        c = self.bl_Boarder
        if (ship.tl == c or ship.tr == c or ship.bl == c or ship.br == c):
            status = 'bl'

        c = self.br_Boarder
        if (ship.tl == c or ship.tr == c or ship.bl == c or ship.br == c):
            status = 'br'
        return status

    def checkOccupancy(self, ship):
        """
        docstring
        """
        for i, c in enumerate(self.board):
            status = False
            if c == 's' and (ship.tl == i or ship.tr == i or ship.bl == i or ship.br == i):
                status = 'True'
                return status
                break

        return status

# Ship Placement from user input; with variable ship size/number according to board size


class ShipSpec:
    def __init__(self, w, h, shipSize):
        self.w = w
        self.h = h
        self.shipSize = shipSize

    def shipSetup(self):  # TODO - Improve Ship Size Algorithm
        """Configure ship size based on board width,height

        Returns:
            [list]: [shipLength, shipWidth]
        """
        # Setup:
        area = self.w * self.h
        # Length of ship base on size of board
        if self.shipSize == "large":
            shipLength = math.floor(area/math.sqrt(area)/2)
        elif self.shipSize == "medium":
            shipLength = math.floor(area/math.sqrt(area)/2)
            shipLength = shipLength - 1
        elif self.shipSize == "small":
            shipLength = math.floor(area/math.sqrt(area)/2)
            shipLength = shipLength - 2
        else:
            print("Invalid Size")

        # Width of ship base on size of board
        if area <= 65:
            shipWidth = 1
        elif area < 150:
            shipWidth = 2
        elif area < 250:
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
        """Set starting Location

        Args:
            initIndex ([int]): [index for starting position]
        """
        self.initIndex = initIndex

    def initHitbox(self, board):
        """Generate all 4 corneer of hitbox and entire hitbox as hitbox[list]

        Args:
            board (object): [description]
        """
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

        # Update Hitbox[List]

        self.hitbox = []
        w = self.tr_x-self.tl_x+1
        h = self.br_y-self.tl_y+1
        for x in range(w):  # Add each position index that need to be change to list
            for y in range(h):
                self.hitbox.append(positionToIndex(
                    self.tl_x+x, self.tl_y+y, board.w, board.h))

    def moveHitbox(self, x, y, board):
        """Move Ship Hitbox

        Args:
            x (int): delta x
            y (int): delta y
            board (obj): [description]
        """
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

        # Update Hitbox[List]
        self.hitbox = []
        w = self.tr_x-self.tl_x+1
        h = self.br_y-self.tl_y+1
        for x in range(w):  # Add each position index that need to be change to list
            for y in range(h):
                self.hitbox.append(positionToIndex(
                    self.tl_x+x, self.tl_y+y, board.w, board.h))

    def rotateHitbox(self, board):
        """ 
        rotate ship by updating all hitbox
        """

        shipWidth = self.shipWidth
        shipLength = self.shipLength

        self.shipLength = shipWidth
        self.shipWidth = shipLength

        # self.tl = self.tl (anchor point)
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

        # Update Hitbox[List]
        self.hitbox = []
        w = self.tr_x-self.tl_x+1
        h = self.br_y-self.tl_y+1
        for x in range(w):  # Add each position index that need to be change to list
            for y in range(h):
                self.hitbox.append(positionToIndex(
                    self.tl_x+x, self.tl_y+y, board.w, board.h))


""" # TODO - place func elsewhere
def randomgenerator(w, h):
    seed(1)
    # generate some integers
    for _ in range(w*h):
        randomindex = randint(0, w*h)

    return randomindex
"""
