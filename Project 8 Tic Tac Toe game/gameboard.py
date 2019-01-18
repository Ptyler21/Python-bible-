#gameboard

board = [" " for i in range(9)]

def printgameboard(board):
    #rows of the gameboard
    rowOne = "|{}|{}|{}|".format(board[0],board[1],board[2])
    rowTwo = "|{}|{}|{}|".format(board[3],board[4],board[5])
    rowThree = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print(rowOne)
    print(rowTwo)
    print(rowThree)
'''
def playerMovement(board):
    playerPositioning = int(input("please give me a position(1-9): "))

    if board[playerPositioning -1] == " ":
        board[playerPositioning -1 ] = "X"

while True:
    playerMovement(board)
    printgameboard(board)
'''
