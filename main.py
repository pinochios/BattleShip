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

boardHiddenval = Board(boardTemplate2, boardSize[0], boardSize[1])
boardHiddenval.boardGenerator()
boardHiddenval.boardHiddenvalGenerator()

# Render board by using var:board to render function
board.boardRenderer()


board.placeShip()

"""#__test__ : board hidden renderer
boardHiddenval.boardRenderer()"""

"""# __test__ : input position
coordinate = positionInput(boardSize[0], boardSize[1], "Enter Coordinate")

# __test__ : positionToIndex from a coordinate Example
index = positionToIndex(
    coordinate[0], coordinate[1], boardSize[0], boardSize[1])

# __test__ : positionValue from an index Example
print(positionValue(index, board))"""

#placeShip(board, boardHiddenval, boardSize[0], boardSize[1])
