#player movement
import gameboard as f1
from gameboard import board
from gameboard import printgameboard

def playerMovement(board,icon):
    if icon == "X":
        playerNumber = 1
    elif icon == "Y":
        playerNumber = 2

    print("It's Your turn player {} ").format(playerNumber)

    playerPositioning = int(input("please give me a number(1-9): "))

    if board[playerPositioning - 1] == " ":
        board[playerPositioning -1 ] = icon

def checkForFullBoard():
    counter = 0
    for i in board:
        if i == "X" or i == "Y":
            counter += 1
    if counter == 8:
        print("clearing gameboard")
        global board
        board = [" " for i in range(9)]
    return (board)

while True:
    playerMovement(board,"X")
    printgameboard(board)
    playerMovement(board,"Y")
    printgameboard(board)
    checkForFullBoard()
