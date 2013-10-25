'''
Anisha Cook
roomSim5.py

'''


'''

'''

import os
import random
import math
import termcolor
from termcolor import colored




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
            board[x][y] = colored('0','green')
            personLocations.append([x,y])
    x = random.randrange(width-1)
    y = random.randrange(height-1)
    while board[x][y] != ' ':
        x = random.randrange(width-1)
        y = random.randrange(height-1)  
    board[x][y] = colored('0', 'blue')
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

def moveSlow(board,width,height,List, personLocations):
    for coordinate in personLocations:
        oldX = coordinate[0]
        oldY = coordinate[1]   
        randDir = random.randrange(8)
        if randDir == 0:
            if (0 <= oldX-1 < width-1):
                if board[oldX-1][oldY] == ' ':
                    board[oldX-1][oldY] = board[oldX][oldY]
                    board[oldX][oldY] = ' '
                    personLocations.append([oldX-1, oldY])
                    personLocations.remove([oldX,oldY])
                else: hi = True
            else: hi = True

        elif randDir == 1:
            if (0 <= oldX+1 < width-1):
                if board[oldX+1][oldY] == ' ':
                    board[oldX+1][oldY] = board[oldX][oldY]
                    board[oldX][oldY] = ' '
                    personLocations.append([oldX+1, oldY])
                    personLocations.remove([oldX,oldY])
                else: hi = True
            else: hi = True

        elif randDir ==2:
            if (0 <= oldY-1 < height-1):
                if board[oldX][oldY-1] == ' ':
                    board[oldX][oldY-1] = board[oldX][oldY]
                    board[oldX][oldY] = ' '
                    personLocations.append([oldX, oldY-1])
                    personLocations.remove([oldX,oldY])
                else: hi = True
            else: hi = True

        elif randDir ==3:
            if (0 <= oldY+1 < height-1):
                if board[oldX][oldY+1] == ' ':
                    board[oldX][oldY+1] = board[oldX][oldY]
                    board[oldX][oldY] = ' '
                    personLocations.append([oldX, oldY+1])
                    personLocations.remove([oldX,oldY])
                else: hi = True
            else: hi = True

        elif randDir == 4 or 5 or 6 or 7:
            hi = True
        else: 
            hi = True
    return board, personLocations

def moveRegular(board,width,height, List, personLocations):
    for coordinate in List:
        oldX = coordinate[0]
        oldY = coordinate[1]   
        randDir = random.randrange(4)
        if randDir == 0:
            if (0 <= oldX-1 < width-1):
                if board[oldX-1][oldY] == ' ':
                    board[oldX-1][oldY] = board[oldX][oldY]
                    board[oldX][oldY] = ' '
                    personLocations.append([oldX-1, oldY])
                    personLocations.remove([oldX,oldY])
                else: hi = True
            else: hi = True

        elif randDir == 1:
            if (0 <= oldX+1 < width-1):
                if board[oldX+1][oldY] == ' ':
                    board[oldX+1][oldY] = board[oldX][oldY]
                    board[oldX][oldY] = ' '
                    personLocations.append([oldX+1, oldY])
                    personLocations.remove([oldX,oldY])
                else: hi = True
            else: hi = True

        elif randDir ==2:
            if (0 <= oldY-1 < height-1):
                if board[oldX][oldY-1] == ' ':
                    board[oldX][oldY-1] = board[oldX][oldY]
                    board[oldX][oldY] = ' '
                    personLocations.append([oldX, oldY-1])
                    personLocations.remove([oldX,oldY])
                else: hi = True
            else: hi = True

        elif randDir ==3:
            if (0 <= oldY+1 < height-1):
                if board[oldX][oldY+1] == ' ':
                    board[oldX][oldY+1] = board[oldX][oldY]
                    board[oldX][oldY] = ' '
                    personLocations.append([oldX, oldY+1])
                    personLocations.remove([oldX,oldY])
                else: hi = True
            else: hi = True
    return board, personLocations

def evaluatePeople(board, personLocations):
    healthyList = []
    incubationList = []
    symptomaticList = []
    deadList = []
    for coordinate in personLocations:
        x = coordinate[0]
        y = coordinate[1]
        if board[x][y] == colored('0','green'):
            healthyList.append([x,y])
        elif [x,y] == colored('0','blue'):
            incubationList.append([x,y])
        elif [x,y] == colored('0','red'):
            symptomaticList.append([x,y])
        elif [x,y] == colored('X','red'):
            deadList.append([x,y])
    return healthyList, incubationList, symptomaticList, deadList
    
def infectNew(board,xCoord, yCoord, width, height):
    newInfected = []
    if (0 <= yCoord-1 < height-1):
        if board[xCoord][yCoord-1] == colored('0','green'):
            newInfected.append([xCoord, yCoord-1])
    if (0 <= yCoord+1 < height-1):
        if board[xCoord][yCoord+1] == colored('0','green'):
            newInfected.append([xCoord, yCoord+1])
    if (0 <= xCoord-1 < width-1):
        if board[xCoord-1][yCoord] == colored('0','green'):
            newInfected.append([xCoord-1, yCoord])
    if (0 <= xCoord+1 < width-1):
        if board[xCoord+1][yCoord] == colored('0','green'):
            newInfected.append([xCoord+1, yCoord])
    for coordinate in newInfected:
        x = coordinate[0]
        y = coordinate[1]
        board[x][y] = colored('0', 'blue')
    newInfected = []
    if (0 <= yCoord-1 < height-1):
        if board[xCoord][yCoord-1] == colored('0','blue'):
            newInfected.append([xCoord, yCoord-1])
    if (0 <= yCoord+1 < height-1):
        if board[xCoord][yCoord+1] == colored('0','blue'):
            newInfected.append([xCoord, yCoord+1])
    if (0 <= xCoord-1 < width-1):
        if board[xCoord-1][yCoord] == colored('0','blue'):
            newInfected.append([xCoord-1, yCoord])
    if (0 <= xCoord+1 < width-1):
        if board[xCoord+1][yCoord] == colored('0','blue'):
            newInfected.append([xCoord+1, yCoord])
    for coordinate in newInfected:
        x = coordinate[0]
        y = coordinate[1]
        board[x][y] = colored('0', 'red')
    newInfected = []
    if (0 <= yCoord-1 < height-1):
        if board[xCoord][yCoord-1] == colored('0','red'):
            newInfected.append([xCoord, yCoord-1])
    if (0 <= yCoord+1 < height-1):
        if board[xCoord][yCoord+1] == colored('0','red'):
            newInfected.append([xCoord, yCoord+1])
    if (0 <= xCoord-1 < width-1):
        if board[xCoord-1][yCoord] == colored('0','red'):
            newInfected.append([xCoord-1, yCoord])
    if (0 <= xCoord+1 < width-1):
        if board[xCoord+1][yCoord] == colored('0','red'):
            newInfected.append([xCoord+1, yCoord])
    for coordinate in newInfected:
        x = coordinate[0]
        y = coordinate[1]
        board[x][y] = colored('X', 'red')
    return board


def main():
    board, width, height = createBoard()
    board = makeWalls(board)
    board, personLocations, infectedList = fillPeople(board,width,height)
    printBoard(board,width,height)
    pause = raw_input('')
    elapsedTime = 0
    while pause != '.':
        healthyList, incubationList, symptomaticList, deadList = evaluatePeople(board, personLocations)
        board, personLocations = moveRegular(board,width,height, healthyList, personLocations)
        board, personLocations = moveRegular(board, width, height, incubationList, personLocations)
        board, personLocations = moveSlow(board, width, height, symptomaticList, personLocations)
        infectedList = []
        for coordinate in incubationList:
            infectedList.append(coordinate)
        for coordinate in symptomaticList:
            infectedList.append(coordinate)
        for coordinate in deadList:
            infectedList.append(coordinate)
        for coordinate in infectedList:
            xCoord = coordinate[0]
            yCoord = coordinate[1]
            board = infectNew(board, xCoord, yCoord, width, height)
        printBoard(board,width,height)
        elapsedTime += 1
        pause = raw_input('')

main()
