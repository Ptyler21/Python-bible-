
board = [" " for i in range(9)]

def printGameBoard():
    rowOne = "|{}|{}|{}|".format(board[0],board[1],board[2])
    rowTwo = "|{}|{}|{}|".format(board[3],board[4],board[5])
    rowThree = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print(rowOne)
    print(rowTwo)
    print(rowThree)

def movement(icon):
    if icon == "X":
        playerNumber = 1
    elif icon == "Y":
        playerNumber = 2

    print("please go player {}".format(playerNumber))

    playerInput = int(input("please give me a number(1-9): "))

    if board[playerInput-1] == " ":
        board[playerInput -1] = icon

    else:
        print("the space is taken")
while True:
    printGameBoard()
    movement("X")
    printGameBoard()
    movement("Y")
    printGameBoard()
