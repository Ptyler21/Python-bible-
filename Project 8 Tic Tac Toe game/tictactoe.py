
board = [" " for i in range(9)]

def printGameBoard():
    rowOne = "|{}|{}|{}|".format(board[0],board[1],board[2])
    rowTwo = "|{}|{}|{}|".format(board[3],board[4],board[5])
    rowThree = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print(rowOne)
    print(rowTwo)
    print(rowThree)

while True:
    printGameBoard()
    userPosition = int(input("pick a board position(1-9): "))
    userPiece = "X"
    if board[userPosition - 1] == " ":
        board[userPosition -1] = "X"
    print("now it's the AI turn")
    if
    else:
        print("the space is taken!"
