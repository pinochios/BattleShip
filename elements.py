#import

#main functions
def boardGenerator(w,h):
    board = []
    for a in range(w*h):
        board.append(0)
    return board

def boardRenderer(board,w,h):
    for a in range(w):
        for b in range(h):
            print(board[a], end='')
            print(" ", end='')
        print()
