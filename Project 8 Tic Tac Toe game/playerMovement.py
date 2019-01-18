#player movement
import gameboard as f1
from gameboard import board
from gameboard import printgameboard

def playerMovement(board,icon):
    if icon == "X":
        playerNumber = 1
    elif icon == "Y":
        playerNumber = 2

    playerReminder = "It's Your turn player {} ".format(playerNumber)
    print(playerReminder)

    playerPositioning = int(input("please give me a number(1-9): "))

    if board[playerPositioning - 1] == " ":
        board[playerPositioning -1 ] = icon

def checkForFullBoard():
    global board
    counter = 0
    for i in board:
        if i == "X" or i == "Y":
            counter += 1
    if counter == 9:
        print("clearing gameboard")
        board = [" " for i in range(9)]
    return (board)

def victoryCheck():
    global board
    counter = 0
    for i in board[0:3]:
        if "X" in i:
            counter +=1
            if counter == 3:
                print("player one has won")
                board = [" " for i in range(9)]
                return (board)
    for i in board[3:6]:
        if "X" in i:
            counter +=1
            if counter == 3:
                print("player one has won")
                board = [" " for i in range(9)]
                return (board)
    for i in board[6:9]:
        if "X" in i:
            counter +=1
            if counter == 3:
                print("player one has won")
                board = [" " for i in range(9)]
                return (board)
    # for Y inside of board
    for i in board[0:3]:
        if "Y" in i:
            counter +=1
            if counter == 3:
                print("player Two has won")
                board = [" " for i in range(9)]
                return (board)
    for i in board[3:6]:
        if "Y" in i:
            counter +=1
            if counter == 3:
                print("player Two has won")
                board = [" " for i in range(9)]
                return (board)
    for i in board[6:9]:
        if "Y" in i:
            counter +=1
            if counter == 3:
                print("player Two has won")
                board = [" " for i in range(9)]
                return (board)
    

while True:
    playerMovement(board,"X")
    printgameboard(board)
    playerMovement(board,"Y")
    printgameboard(board)
    checkForFullBoard()
    victoryCheck()
