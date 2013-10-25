'''
Anisha Cook
roomSim2.py
roomSim1 but with background colors
'''


import os
import random
import math
import termcolor
from termcolor import colored



def createBoard():
    """initializes a board"""
    board = []
    width = 20
    height = 10
    for i in range(width):
        board.append([])
        board[i] = []
        for j in range(height):
            board[i].append(colored(' ', 'on_blue'))
    return board, width, height

def makeWalls(board):
    for y in range(0,5):
        board[6][y] = '|'
        board[12][y] = '|'
    for x in range(0,5):
        board[x][4] = '_'
    for x in range(6,11):
        board[x][4] = '_'
    for x in range(12,15):
        board[x][4] = '_'
    for x in range(16,19):
        board[x][4] = '_'
    for y in range(5,10):
        board[16][y] = '|'
    board[6][4] = 'L'
    board[12][4] = 'L'
    return board

def fillPeople(board, width, height):
    personLocations = []
    for i in range(10):
        x = random.randrange(width)
        y = random.randrange(height)
        if board[x][y] == colored(' ', 'on_blue'):
            board[x][y] = '0'
            personLocations.append([x,y])
   
    return board, personLocations

def printBoard(board,width,height):
    os.system("clear")
    for j in range(height):
        thisLine = ""
        for i in range(width):
            thisLine += board[i][j]
        print thisLine

def movePeople(board,width,height,personLocations):
    newPersonLocs = []
    for coordinate in personLocations:
        oldX = coordinate[0]
        oldY = coordinate[1]   
        randDir = random.randrange(4)
        if randDir == 0:
            if (0 <= oldX-1 < width):
                if board[oldX-1][oldY] == colored(' ', 'on_blue'):
                    board[oldX][oldY] = colored(' ', 'on_blue')
                    newPersonLocs.append([oldX-1, oldY])
                    board[oldX-1][oldY] = '0'
                else: newPersonLocs.append([oldX, oldY])
            else: newPersonLocs.append([oldX, oldY])


        elif randDir == 1:
            if (0 <= oldX+1 < width):
                if board[oldX+1][oldY] == colored(' ', 'on_blue'):
                    board[oldX][oldY] = colored(' ', 'on_blue')
                    newPersonLocs.append([oldX+1, oldY])
                    board[oldX+1][oldY] = '0'
                else: newPersonLocs.append([oldX, oldY])
            else: newPersonLocs.append([oldX, oldY])


        elif randDir ==2:
            if (0 <= oldY-1 < height):
                if board[oldX][oldY-1] == colored(' ', 'on_blue'):
                    board[oldX][oldY] = colored(' ', 'on_blue')
                    newPersonLocs.append([oldX, oldY-1])
                    board[oldX][oldY-1] = '0'
                else: newPersonLocs.append([oldX, oldY])
            else: newPersonLocs.append([oldX, oldY])


        elif randDir ==3:
            if (0 <= oldY+1 < height):
                if board[oldX][oldY+1] == colored(' ', 'on_blue'):
                    board[oldX][oldY] = colored(' ', 'on_blue')
                    newPersonLocs.append([oldX, oldY+1])
                    board[oldX][oldY+1] = '0'
                else: newPersonLocs.append([oldX, oldY])
            else:newPersonLocs.append([oldX, oldY])
        else: 
            newPersonLocs.append([oldX, oldY])
    personLocations = newPersonLocs
    return board, personLocations


def main():
    board, width, height = createBoard()
    board = makeWalls(board)
    board, personLocations = fillPeople(board,width,height)
    printBoard(board,width,height)
    pause = raw_input('')
    while pause != '.':
        board, personLocations = movePeople(board,width,height,personLocations)
        printBoard(board,width,height)
        pause = raw_input('')

main()
