#player movement
import gameboard as f1
from gameboard import board
from gameboard import printgameboard
import random

#basically main

def playerMovement(board,icon):
    if icon == "X":
        playerNumber = 1
    '''
    elif icon == "Y":
        playerNumber = 2
    '''
    playerReminder = "It's Your turn player {} ".format(playerNumber)
    print(playerReminder)

    playerOnePositioning = int(input("please give me a number(1-9): "))


    if board[playerOnePositioning - 1] == " ":
        board[playerOnePositioning -1 ] = icon

def computerMovement(board,icon):
    playerTwoPosition = random.randint(1,9)
    if board[playerTwoPosition -1 ] == " ":
        board[playerTwoPosition - 1] = icon

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

def victoryCheck(icon):
    global board

    if board[0] == icon and board[1]  == icon and board[2] == icon:
        if icon == "X":
            player = 1
        elif icon == "Y":
            player = 2
        victoryNotif = "Player {} has won".format(player)
        print(victoryNotif)
        board = [" " for i in range(9)]
        return(board)
    elif board[3] == icon and board[4] == icon and board[5] == icon:
        if icon == "X":
            player = 1
        elif icon == "Y":
            player = 2
        victoryNotif = "player {} has won".format(player)
        print(victoryNotif)
        board = [" " for i in range(9)]
        return(board)
    elif board[6] == icon and board[7] == icon and board[8] == icon:
        if icon == "X":
            player = 1
        elif icon == "Y":
            player = 2
        victoryNotif = "Player {} has won".format(player)
        print(victoryNotif)
        board = [" " for i in range(9)]
        return(board)

    elif board[0] == icon and board[3] == icon and board[6] == icon:
        if icon == "X":
            player = 1
        elif icon == "Y":
            player = 2
        victoryNotif = "Player {} has won".format(player)
        print(victoryNotif)
        board = [" " for i in range(9)]
        return(board)
    elif board[1] == icon and board[4] == icon and board[7] == icon:
        if icon == "X":
            player = 1
        elif icon == "Y":
            player = 2
        victoryNotif = "Player {} has won".format(player)
        print(victoryNotif)
        board = [" " for i in range(9)]
        return(board)
    elif board[2] == icon and board[5] == icon and board[8] == icon:
        if icon == "X":
            player = 1
        elif icon == "Y":
            player = 2
        victoryNotif = "Player {} has won".format(player)
        print(victoryNotif)
        board = [" " for i in range(9)]
        return(board)
    elif board[0] == icon and board[4] == icon and board[8] == icon:
        if icon == "X":
            player = 1
        elif icon == "Y":
            player = 2
        victoryNotif = "Player {} has won".format(player)
        board = [" " for i in range(9)]
        print(victoryNotif)
        return(board)
    elif board[2] == icon and board[4] == icon and board[6] == icon:
        if icon == "X":
            player = 1
        elif icon == "Y":
            player = 2
        victoryNotif = "Player {} has won".format(player)
        print(victoryNotif)
        boar = [" " for i in range(9)]
        return(board)




while True:
    playerMovement(board,"X")
    printgameboard(board)
    victoryCheck("X")
    computerMovement(board,"Y")
    #playerMovement(board,"Y")
    printgameboard(board)
    victoryCheck("Y")
    checkForFullBoard()
    #victoryCheck()
