'''
Anisha Cook
Simulation 2

Similar to simulation 1, except more user-friendly and vaccination rate, population size/shape, and whether an infected person can infect up to 4 or 8 people is customizable by user
Takes into accound only: innoculated vs not innoculated
% of people infected when in contact with infected person = 100% 

eg/
transmissionType a:
ROUND 1:
+++
+1+
+++

ROUND 2:
+2+
212
+2+

transmissionType b:
ROUND 1:
+++
+1+
+++

ROUND 2:
222
212
222

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

def createBoard(width, height):
    """initializes a board"""
    board = []
    for i in range(width):
        board.append([])
        board[i] = []
        for j in range(height):
            board[i].append('+')
    return board

def fillBoard(board,width,height, vaccinationRate):
    """randomly fill board at beginning of simulation"""
    for cell in range(vaccinationRate):
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

def checkNeighbors(board,width,height,cellX,cellY, transmissionType): #cellX, cellY are coordinates of infected cell. MUST DO THIS FOR EVERY INFECTED CELL
    """count up all the neighbors in the 8 cells
    around a cell. Make sure you don't try to 
    count cells 'off the screen' that don't 
    exist in the array!"""
    newInfected = []
    if transmissionType == 'a':
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

    elif transmissionType == 'b':
        for i in range(cellX-1,cellX+1):
            for j in range(cellY-1, cellY+1):
                if (i == cellX) and (j == cellY):
                    pass
                else:
                    if (0 <= i < width) and (0 <= j < height):
                        if board[i][j] == '+':
                            newInfected.append([i,j])
    return newInfected

def infectNew(board, newInfected, generationStr): #MUST DO THIS FOR EVERY INFECTED CELL FROM PREVIOUS GENERATION
    for coordinates in newInfected:
        cellX = coordinates[0]
        cellY = coordinates[1]
        board[cellX][cellY] = generationStr
    return board


def evolve(board, width, height,generation, genList, transmissionType,):
    os.system("clear")
    thisGenInfected = findInfectedCells(board, width, height)
    finished = True
    if generation > 9:
        if generation <= 35:
            generationStr = genList[generation]
        else:
            finished = True
            #####
            wrapup(board,width,height,generation)
    else:
        generationStr = str(generation)
    for set in thisGenInfected:
        cellX = set[0]
        cellY = set[1]
        newInfected = checkNeighbors(board, width, height, cellX, cellY, transmissionType)
        if newInfected != []:
            finished = False 
        if finished == False:
            board = infectNew(board, newInfected, generationStr)
    if finished == False:    
        printBoard(board, width, height)
    return finished

def wrapup(board, width, height, generation):
    numberInfectedCells = 0.0
    innoculatedPeople = 0.0
    for i in range(width):
        for j in range(height):
            if board[i][j] != '.':  
                if board[i][j] != '+':
                    numberInfectedCells += 1.0
                    board [i][j] = '.'
                else:
                    board[i][j] = 'O'
            elif board[i][j] == '.': 
                board[i][j] = 'O'
                innoculatedPeople += 1.0
    numberPeople = width * height
    print '\n\nYOUR POPULATION (where O = healthy person and . = infected person):\n'
    printBoard(board, width, height)
    print '\n\n\n', numberInfectedCells, 'people out of', numberPeople, 'were infected over the course of', generation, 'periods after patient zero was infected, where', (innoculatedPeople/numberPeople)*100.0,'% were vaccinated.'
    done = True
    return done



def main():
    print '''
Transmission type "a":
    Infected person can infect up to four other surrounding people.
    eg/
          
          |  ROUND 1:  |  ROUND 2:  |
          |  +++       |  +2+       |
          |  +1+       |  212       |
          |  +++       |  +2+       |


Transmission type"b":
    Infected person can infect up to eight other surrounding people.
    eg/
          
          |  ROUND 1:  |  ROUND 2:  |
          |  +++       |  222       |
          |  +1+       |  212       |
          |  +++       |  222       |

type 'a' for transmission type a or 'b' for transmission type b and hit <Enter>'''
    transmissionType = raw_input('')
    if transmissionType == '': transmissionType = 'a'
    else: transmissionType = transmissionType[0].lower()
    print "\n\nPlease enter the dimensions of your population in format width, height"
    try:
        width, height = input('')
    except:
        width = 10
        height = 10
    print "\n\nPlease enter the upper limit of the vaccination rate of your population, assuming a percentage."
    try:
        vaccinationRate = input('')
    except: vaccinationRate = 50
    vaccinationRate = int((vaccinationRate/100.0)*(width*height))

    print '"." marks an innoculated person, "+" marks a healthy but susceptible person, a number/letter marks an infected person\n\nGenerations are numbered 0-9 and a-z \n\n'
    board = createBoard(width, height)
    board = fillBoard(board, width, height, vaccinationRate)
    printBoard(board, width, height)
    done = False
    generation = 0
    genList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while done == False:
        print '\nHit <Enter> to continue to evolve'
        keepGoing = raw_input('')
        if keepGoing == '':
            generation += 1
            finished = evolve(board, width, height, generation, genList, transmissionType)
            if finished == True:
                done = True
    done = wrapup(board, width, height, generation)


main()


    

