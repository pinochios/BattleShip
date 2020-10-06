import click

from elements import *
from header import *
# welcome menu
print("----------------------------------------------")
print("\n\n\n\n     ///   BattleShip by Kan & Bose   ///     \n\n\n\n")
print("----------------------------------------------")
try:
    input("\nPress enter to continue...")
except SyntaxError:
    pass

print("\n\n<<< Player 1 >>>\n")
Player_1 = Player(input("What's your name?: "))
print("\n\n<<< Player 2 >>>\n")
Player_2 = Player(input("What's your name?: "))

# Input Board Size
print("\n<<< Boardsize setup >>>\n")
print("(minimum size is 8 x 8)\n\n")

boardSize = boardInput()

Player_1.initBoard(boardSize)
Player_1.initShip()

Player_2.initBoard(boardSize)
Player_2.initShip()





# __test__ : move ship
"""
# __test__ : move ship
board.placeShip(largeShip)
board.boardRenderer()
board.removeShip(largeShip)
largeShip.moveHitbox(-1, 2, board)
board.placeShip(largeShip)
board.boardRenderer()"""

"""board.removeShip(largeShip)
board.boardRenderer()"""


"""
#__test__ : board hidden renderer
boardHiddenval.boardRenderer()
"""

"""
# __test__ : input position
coordinate = positionInput(boardSize[0], boardSize[1], "Enter Coordinate")

# __test__ : positionToIndex from a coordinate Example
index = positionToIndex(
    coordinate[0], coordinate[1], boardSize[0], boardSize[1])

# __test__ : index to coordinate
print(indexToPosition(index, boardSize[0], boardSize[1]))
"""

"""
# __test__ : positionValue from an index Example
print(positionValue(index, board))
"""
#placeShip(board, boardHiddenval, boardSize[0], boardSize[1])
