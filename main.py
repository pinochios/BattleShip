from elements import *

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
board = boardGenerator(boardSize[0], boardSize[1])

# Render board by using var:board to render function
boardRenderer(board, boardSize[0], boardSize[1])

positionToIndex(1, 2, boardSize[0], boardSize[1])
