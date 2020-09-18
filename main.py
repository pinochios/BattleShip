from elements import *

#welcome menu
print("----------------------------------------------")
print("\n\n\n\n     ///   BattleShip by Kan & Bose   ///     \n\n\n\n")
print("----------------------------------------------")
try:
    input("\nPress enter to continue...")
except SyntaxError:
    pass





#generate board and pass it to var:board

boardSize = boardInput()

board = boardGenerator(boardSize[0],boardSize[1]) 

#Render board by passing var:board to render function
boardRenderer(board,boardSize[0],boardSize[1])

#menu
#print("///   Welcome to BattleShip   ///")
#print("\n\n\n")
