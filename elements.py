#import
alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter))

#main functions

def boardInput():
    w = 0
    h = 0
    while True:
        try:
            w = int(input("Enter the width of the board: "))
            if w > 26 or w <= 0:
                print("Maximum width is 26, please try again")
            else:
                break
        except ValueError:
            print("Invalid value, please try again")
            break              

    while True:
        try:
            h = int(input("Enter the height of the board: "))
        except ValueError:
            print("Invalid value, please try again")
        else:
            break

    return [w,h]



def boardGenerator(w,h):
    
    board = []
    for a in range(w*h):
        board.append(0)
    return board

def boardRenderer(board,w,h):
    print("   ", end='') #Space
    #Index Row using a-z
    for a in range(w):
        print(" ", end='')
        print(alphabet[a], end='')
    print()
    #Render The Board Out wih Column index
    for a in range(w):
        print(a+1, end='') #index
        if a<9:
            print("   ", end='') #spacing after index for 1-digit
        else:
            print("  ", end='') #spacing after index for 2-digit
        #board rendering
        for b in range(h): 
            print(board[a], end='')
            print(" ", end='')
        print()
