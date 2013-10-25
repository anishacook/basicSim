'''
Anisha Cook
roomSim3.py

'''


'''
Now infects people!
patient zero, subsequent infected people denoted with X
'''

import os
import random
import math




def createBoard():
    """initializes a board"""
    board = []
    width = 21
    height = 11
    for i in range(width):
        board.append([])
        board[i] = []
        for j in range(height):
            board[i].append(' ')
    return board, width, height

def makeWalls(board):
    for y in range(0,5):
        board[6][y] = '|'
        board[12][y] = '|'
    for x in range(0,5):
        board[x][4] = '-'
    for x in range(6,11):
        board[x][4] = '-'
    for x in range(12,15):
        board[x][4] = '-'
    for x in range(16,19):
        board[x][4] = '-'
    for y in range(5,11):
        board[16][y] = '|'
    for y in range(11):
        board[20][y] = '|'
    for x in range(21):
        board[x][10] = '-'
    board[6][4] = '+'
    board[12][4] = '+'
    board[16][4] = '+'
    board[16][10] = '+'
    board[20][10] = '+'
    return board

def fillPeople(board, width, height):
    personLocations = []
    for i in range(10):
        x = random.randrange(width-1)
        y = random.randrange(height-1)
        if board[x][y] == ' ':
            board[x][y] = '0'
            personLocations.append([x,y])
    x = random.randrange(width-1)
    y = random.randrange(height-1)
    board[x][y] = 'X'
    infectedList = [(x,y)]
    personLocations.append([x,y])
    return board, personLocations, infectedList

def printBoard(board,width,height):
    os.system("clear")
    for j in range(height):
        thisLine = ""
        for i in range(width):
            thisLine += board[i][j]
        print thisLine

def movePeople(board,width,height,personLocations, infectedList):
    newPersonLocs = []
    for coordinate in personLocations:
        oldX = coordinate[0]
        oldY = coordinate[1]   
        randDir = random.randrange(4)
        if randDir == 0:
            if (0 <= oldX-1 < width-1):
                if board[oldX-1][oldY] == ' ':
                    if board[oldX][oldY] == '0':
                        board[oldX-1][oldY] = '0'
                    elif board[oldX][oldY] == 'X':
                        board[oldX-1][oldY] = 'X'
                        infectedList.append([oldX-1, oldY])
                    board[oldX][oldY] = ' '
                    newPersonLocs.append([oldX-1, oldY])
                else: newPersonLocs.append([oldX, oldY])
            else: newPersonLocs.append([oldX, oldY])


        elif randDir == 1:
            if (0 <= oldX+1 < width-1):
                if board[oldX+1][oldY] == ' ':
                    if board[oldX][oldY] == '0':
                        board[oldX+1][oldY] = '0'
                    elif board[oldX][oldY] == 'X':
                        board[oldX+1][oldY] = 'X'
                        infectedList.append([oldX+1, oldY])
                    board[oldX][oldY] = ' '
                    newPersonLocs.append([oldX+1, oldY])
                else: newPersonLocs.append([oldX, oldY])
            else: newPersonLocs.append([oldX, oldY])


        elif randDir ==2:
            if (0 <= oldY-1 < height-1):
                if board[oldX][oldY-1] == ' ':
                    if board[oldX][oldY] == '0':
                        board[oldX][oldY-1] = '0'
                    elif board[oldX][oldY] == 'X':
                        board[oldX][oldY-1] = 'X'
                        infectedList.append([oldX, oldY-1])
                    board[oldX][oldY] = ' '
                    newPersonLocs.append([oldX, oldY-1])
                else: newPersonLocs.append([oldX, oldY])
            else: newPersonLocs.append([oldX, oldY])


        elif randDir ==3:
            if (0 <= oldY+1 < height-1):
                if board[oldX][oldY+1] == ' ':
                    if board[oldX][oldY] == '0':
                        board[oldX][oldY+1] = '0'
                    elif board[oldX][oldY] == 'X':
                        board[oldX][oldY+1] = 'X'
                        infectedList.append([oldX, oldY+1])
                    board[oldX][oldY] = ' '
                    newPersonLocs.append([oldX, oldY+1])
                else: newPersonLocs.append([oldX, oldY])
            else:newPersonLocs.append([oldX, oldY])
        else: 
            newPersonLocs.append([oldX, oldY])
    personLocations = newPersonLocs
    return board, personLocations, infectedList

def infectNew(board,infectedList, width, height):
    newInfected = []
    for coordinate in infectedList:
        xCoord = coordinate[0]
        yCoord = coordinate[1]
        if (0 <= yCoord-1 < height-1):
            if board[xCoord][yCoord-1] == '0':
                newInfected.append([xCoord, yCoord-1])
        if (0 <= yCoord+1 < height-1):
            if board[xCoord][yCoord+1] == '0':
                newInfected.append([xCoord, yCoord+1])
        if (0 <= xCoord-1 < width-1):
            if board[xCoord-1][yCoord] == '0':
                newInfected.append([xCoord-1, yCoord])
        if (0 <= xCoord+1 < width-1):
            if board[xCoord+1][yCoord] == '0':
                newInfected.append([xCoord+1, yCoord])
    for coordinate in newInfected:
        x = coordinate[0]
        y = coordinate[1]
        board[x][y] = 'X'
    return board


def main():
    board, width, height = createBoard()
    board = makeWalls(board)
    board, personLocations, infectedList = fillPeople(board,width,height)
    printBoard(board,width,height)
    pause = raw_input('')
    while pause != '.':
        board, personLocations, infectedList = movePeople(board,width,height,personLocations, infectedList)
        board = infectNew(board, infectedList, width, height)
        printBoard(board,width,height)
        pause = raw_input('')

main()
