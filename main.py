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

# Input Board Size
boardSize = boardInput()

# Generate board according to var:boardSize and pass it to var:board
board = Board(boardTemplate, boardSize[0], boardSize[1])
board.boardGenerator()

boardBoarder = Board(boardTemplate2, boardSize[0], boardSize[1])
boardBoarder.boardGenerator()
boardBoarder.boardBoarder()

boardTemporary = Board(boardTemplate3, boardSize[0], boardSize[1])
boardTemporary.boardGenerator()

# Render board by using var:board to render function
board.boardRenderer()

# ship objects
largeShipSpec = ShipSpec(board.w, board.h, "large")
largeShip = Ship(largeShipSpec.shipSetup()[
                 0], largeShipSpec.shipSetup()[1])

mediumShipSpec = ShipSpec(board.w, board.h, "medium")
mediumShip = Ship(mediumShipSpec.shipSetup()[
                  0], mediumShipSpec.shipSetup()[1])

smallShipSpec = ShipSpec(board.w, board.h, "small")
smallShip = Ship(smallShipSpec.shipSetup()[
                 0], smallShipSpec.shipSetup()[1])

# init location of ship
largeShip.initLocation(0)
largeShip.initHitbox(board)
mediumShip.initLocation(0)
mediumShip.initHitbox(board)
"""
smallShip.initLocation(20)
smallShip.initHitbox(board)"""
#print(largeShip.tl, largeShip.tr, largeShip.bl, largeShip.br)

# move first ship

board.placeShip(largeShip)
board.boardRenderer()
keyboardShipMove(largeShip, board, boardBoarder, boardTemporary)

# move second ship

board.placeShip(mediumShip)
board.boardRenderer()
keyboardShipMove(mediumShip, board, boardBoarder, boardTemporary)

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
