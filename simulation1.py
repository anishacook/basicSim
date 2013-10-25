'''
Anisha Cook
Simulation 1
Takes into accound only: innoculated vs not innoculated
# people vaccinated < 48.1% (2011-2012 year of influenza vaccination in US)
% of people infected when in contact with infected person = 100% 
infection occurs when person is directly right, left, up, or down of infected person
for example:
ROUND 1:
+++
+1+
+++

ROUND 2:
+2+
212
+2+

Board-making data adapted from Richard White's Python Life Simulation 

'''

import random
import os



def printBoard(board,width,height):
    """prints the board every generation"""

    for j in range(height):
        thisLine = ""
        for i in range(width):
            thisLine += board[i][j]
        print thisLine

def createBoard():
    """initializes a board"""
    board = []
    width = 10
    height = 10
    for i in range(width):
        board.append([])
        board[i] = []
        for j in range(height):
            board[i].append('+')
    return board,width,height

def fillBoard(board,width,height):
    """randomly fill board at beginning of simulation"""
    for cell in range(60):
        x = random.randrange(width)
        y = random.randrange(height)
        board[x][y] = "." #where . signifies innoculation
    x = random.randrange(width)
    y = random.randrange(height)
    board[x][y] = 'O'
    return board

def findInfectedCells(board, width, height):
    infectedCells = []
    for i in range(width):
        for j in range(height):
            if board[i][j] != '.':  
                if board[i][j] != '+':
                    infectedCells.append([i,j])
    return infectedCells #list of coordinates X,Y

def checkNeighbors(board,width,height,cellX,cellY): #cellX, cellY are coordinates of infected cell. MUST DO THIS FOR EVERY INFECTED CELL
    """count up all the neighbors in the 8 cells
    around a cell. Make sure you don't try to 
    count cells 'off the screen' that don't 
    exist in the array!"""
    newInfected = []
    if (0 <= cellY-1 < height):
        if board[cellX][cellY-1] == '+':
            newInfected.append([cellX, cellY-1])
    if (0 <= cellY+1 < height):
        if board[cellX][cellY+1] == '+':
            newInfected.append([cellX, cellY+1])
    if (0 <= cellX-1 < width):
        if board[cellX-1][cellY] == '+':
            newInfected.append([cellX-1, cellY])
    if (0 <= cellX+1 < width):
        if board[cellX+1][cellY] == '+':
            newInfected.append([cellX+1, cellY])
    return newInfected
'''

    for i in range(cellX-1,cellX+1):
        if (i == cellX):
            pass
        else:
            if (0 <= i < width):
                if board[i][cellY] == '+':
                    newInfected.append([i, cellY])
    for j in range(cellY-1, cellY+1):
        if (j == cellY):
            pass
        else:
            if (0 <= j < width):
                if board[cellX][j] == '+':
                    newInfected.append([cellX, j])
'''

def infectNew(board, newInfected, generationStr): #MUST DO THIS FOR EVERY INFECTED CELL FROM PREVIOUS GENERATION
    for coordinates in newInfected:
        cellX = coordinates[0]
        cellY = coordinates[1]
        board[cellX][cellY] = generationStr
    return board


def evolve(board, width, height,generation, genList):
    os.system("clear")
    thisGenInfected = findInfectedCells(board, width, height)
    finished = True
    if generation > 9:
        generationStr = genList[generation]
    else:
        generationStr = str(generation)
    for set in thisGenInfected:
        cellX = set[0]
        cellY = set[1]
        newInfected = checkNeighbors(board, width, height, cellX, cellY)
        if newInfected != []:
            finished = False 
        if finished == False:
            board = infectNew(board, newInfected, generationStr)
    if finished == False:    
        printBoard(board, width, height)
    return finished

def wrapup(board, width, height, generation):
    numberInfectedCells = 0
    innoculatedPeople = 0
    for i in range(width):
        for j in range(height):
            if board[i][j] != '.':  
                if board[i][j] != '+':
                    numberInfectedCells += 1
                    board [i][j] = '.'
                else:
                    board[i][j] = 'O'
            else: 
                board[i][j] = 'O'
                innoculatedPeople += 1
    print '\n\n\n', numberInfectedCells, 'people were infected over the course of', generation, 'periods after patient zero was infected, where', innoculatedPeople,'% were vaccinated.\n\nYOUR POPULATION (where O = healthy person and . = infected person):\n'
    printBoard(board, width, height)
    print "\n\n\n"

def main():
    os.system("clear")
    board, width, height = createBoard()
    board = fillBoard(board, width, height)
    printBoard(board, width, height)
    done = False
    generation = 0
    genList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while done == False:
        print '\n\n\n\n"." marks an innoculated person, "+" marks a healthy but susceptible person, a number/letter marks an infected person\n\nGenerations are numbered 0-9 and a-z \n\n\nHit <Enter> to continue to evolve'
        keepGoing = raw_input('')
        if keepGoing == '':
            generation += 1
            finished = evolve(board, width, height, generation, genList)
            if finished == True:
                done == True
                wrapup(board, width, height, generation)
                break

main()


    

