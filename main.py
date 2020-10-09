import click

from elements import *
from header import *
# welcome menu
print("----------------------------------------------")
print("\n\n\n\n     ///   BattleShip by Kan & Bose   ///     \n\n\n\n")
print("----------------------------------------------")
try:
    input("\nPress enter to continue...")
    click.clear()
except SyntaxError:
    pass

print("------------------------------------------------")
print("-                                              -")
print("-            <<< Player 1 setup >>>            -")
print("-                                              -")
print("------------------------------------------------")
Player_1 = Player(input("\nWhat's your name?: "))
print("------------------------------------------------")
print("-                                              -")
print("-            <<< Player 2 setup >>>            -")
print("-                                              -")
print("------------------------------------------------")
Player_2 = Player(input("\nWhat's your name?: "))

click.clear()

# Input Board Size
print("------------------------------------------------")
print("-                                              -")
print("-           <<< Boardsize setup >>>            -")
print("-           (minimum size is 8 x 8)            -")
print("-          (maximum size is 26 x 26)           -")
print("-                                              -")
print("------------------------------------------------")
boardSize = boardInput()

click.clear()
print("------------------------------------------------")
print("                                                ")
print("      <<<", Player_1.name, " ships setup >>>      ")
print("                                                ")
print("------------------------------------------------")
Player_1.initBoard(boardSize)
Player_1.initShip()

click.clear()
print("------------------------------------------------")
print("                                                ")
print("           <<<", Player_2.name, " ships setup >>>      ")
print("                                                ")
print("------------------------------------------------")
Player_2.initBoard(boardSize)
Player_2.initShip()

selectMode = False

while selectMode == False:

    print("------------------------------------------------")
    print("-                                              -")
    print("-           <<< Game setup setup >>>           -")
    print("-                                              -")
    print("-                                              -")
    print("-                [1] Easy Mode                 -")
    print("-                [2] Hard Mode                 -")
    print("-                                              -")
    print("-                                              -")
    print("------------------------------------------------")
    print("Easy Mode - 1 hit to destroy a ship")
    print("Hard Mode - all hit to destroy a ship\n\n")
    print("\nselect mode:")

    mode = input()
    click.clear()

    if mode == '1' or mode == '2':
        selectMode = True

    else:
        print("\n\nInvalide Mode\n\n")

turn = 0  # to know whose turn is it
gameover = False

shipNeedToHit = len(Player_1.largeShip.hitbox) + \
    len(Player_1.mediumShip.hitbox) + len(Player_1.smallShip.hitbox)

while gameover == False:

    hit = False

    if(turn % 2 == 0):
        p = Player_2
    else:
        p = Player_1

    print("<<<   Attack ", p.name, "   >>>")
    print("------------------------------------------------")

    playingBoard = Board(p.attempt, boardSize[0], boardSize[1])
    playingBoard.boardGenerator()
    playingBoard.boardRenderer()

    raw_decision = positionInput(
        boardSize[0], boardSize[1], "guess the coordinate of the opponent's ships")
    index_decision = positionToIndex(
        raw_decision[0], raw_decision[1], boardSize[0], boardSize[1])

    while hit == False:

        for a in p.largeShip.hitbox:

            if index_decision == a:

                if mode == '1':
                    for a in p.largeShip.hitbox:
                        p.attempt[a] = 's'
                        p.shipHit += 1

                if mode == '2':
                    p.attempt[index_decision] = 's'
                    p.shipHit += 1

                print("Hit !!")
                hit = True

        for a in p.mediumShip.hitbox:

            if index_decision == a:

                if mode == '1':
                    for a in p.mediumShip.hitbox:
                        p.attempt[a] = 's'
                        p.shipHit += 1

                if mode == '2':
                    p.attempt[index_decision] = 's'
                    p.shipHit += 1

                print("Hit !!")
                hit = True

        for a in p.smallShip.hitbox:

            if index_decision == a:

                if mode == '1':
                    for a in p.smallShip.hitbox:
                        p.attempt[a] = 's'
                        p.shipHit += 1

                if mode == '2':
                    p.attempt[index_decision] = 's'
                    p.shipHit += 1

                print("Hit !!")
                hit = True

        if hit == False:
            p.attempt[index_decision] = 'x'
            print("Oops, no ship there...")

        break

    playingBoard.boardGenerator()
    playingBoard.boardRenderer()

    try:
        input("\nPress enter to continue...")
        click.clear()
    except SyntaxError:
        pass

    turn += 1

    if p.shipHit >= shipNeedToHit:
        gameover = True


click.clear()
print("------------------------------------------------")
print("-                                              -")
print("-             <<< GameOver !! >>>              -")
print("-                                              -")
print("------------------------------------------------")
print(p.name, "lose, play again for revenge -_-")

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
