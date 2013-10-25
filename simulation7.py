'''
Anisha Cook
Simulation 7

simulation 6 but does print out the board every generation. essentially a more user-friendly and color-improved version of 5b. note that color makes it much slower than 4b

Takes into accound only: innoculated vs not innoculated
% of people infected when in contact with infected person = 100% 


Board-making data adapted from Richard White's Python Life Simulation 

'''

import random
import os
import termcolor
from termcolor import colored



def printBoard(board,width,height):

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
            board[i].append(colored('+','blue'))
    return board

def fillBoard(board,width,height, vaccinationRate):
    """randomly fill board at beginning of simulation"""
    for cell in range(vaccinationRate):
        x = random.randrange(width)
        y = random.randrange(height)
        board[x][y] = colored('.','green') #where . signifies innoculation
    x = random.randrange(width)
    y = random.randrange(height)
    board[x][y] = colored('0','red')
    patientZero = [x,y]
    return board, patientZero

def findInfectedCells(board, width, height):
    infectedCells = []
    for i in range(width):
        for j in range(height):
            if board[i][j] != colored('.','green'):  
                if board[i][j] != colored('+','blue'):
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
            if board[cellX][cellY-1] == colored('+','blue'):
                newInfected.append([cellX, cellY-1])
        if (0 <= cellY+1 < height):
            if board[cellX][cellY+1] == colored('+','blue'):
                newInfected.append([cellX, cellY+1])
        if (0 <= cellX-1 < width):
            if board[cellX-1][cellY] == colored('+','blue'):
                newInfected.append([cellX-1, cellY])
        if (0 <= cellX+1 < width):
            if board[cellX+1][cellY] == colored('+','blue'):
                newInfected.append([cellX+1, cellY])

    elif transmissionType == 'b':
        if (0 <= cellY-1 < height):
            if board[cellX][cellY-1] == colored('+','blue'):
                newInfected.append([cellX, cellY-1])
        if (0 <= cellY+1 < height):
            if board[cellX][cellY+1] == colored('+','blue'):
                newInfected.append([cellX, cellY+1])
        if (0 <= cellX-1 < width):
            if board[cellX-1][cellY] == colored('+','blue'):
                newInfected.append([cellX-1, cellY])
        if (0 <= cellX+1 < width):
            if board[cellX+1][cellY] == colored('+','blue'):
                newInfected.append([cellX+1, cellY])

        if (0 <= cellY-1 < height) and (0 <= cellX-1 < width):
            if board[cellX-1][cellY-1] == colored('+','blue'):
                newInfected.append([cellX-1, cellY-1])
        if (0 <= cellY+1 < height) and (0 <= cellX-1 < width):
            if board[cellX-1][cellY+1] == colored('+','blue'):
                newInfected.append([cellX-1, cellY+1])
        if (0 <= cellX+1 < width) and (0 <= cellY-1 < height):
            if board[cellX+1][cellY-1] == colored('+','blue'):
                newInfected.append([cellX-1, cellY+1])
        if (0 <= cellX+1 < width) and (0 <= cellY+1 < height):
            if board[cellX+1][cellY+1] == colored('+','blue'):
                newInfected.append([cellX+1, cellY+1])
    return newInfected
'''THIS IS BETTER THOUGH B/C OF REDUNDANCY IN CODE PLEASE TRY TO FIX AT SOME POINT
        for i in range(cellX-1,cellX+1):
            for j in range(cellY-1, cellY+1):
                if (i == cellX) and (j == cellY):
                    pass
                else:
                    if (0 <= i < width) and (0 <= j < height):
                        if board[i][j] == '+':
                            newInfected.append([i,j])
'''


def infectNew(board, newInfected, generationStr): #MUST DO THIS FOR EVERY INFECTED CELL FROM PREVIOUS GENERATION
    for coordinates in newInfected:
        cellX = coordinates[0]
        cellY = coordinates[1]
        board[cellX][cellY] = colored(generationStr, 'red')
    return board


def evolve(board, width, height,generation, genList, transmissionType):
    os.system("clear")
    thisGenInfected = findInfectedCells(board, width, height)
    finished = True
    try:
        generationStr = str(genList[generation])
    except: generationStr = '0'
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

def endBoard(board, width, height, generation, patientZero):
    numberInfectedCells = 0.0
    innoculatedPeople = 0.0
    numberOkaySusceptibles = 0.0
    for i in range(width):
        for j in range(height):
            if board[i][j] != colored('.','green'):  
                if board[i][j] != colored('+','blue'):
                    board[i][j] = colored(board[i][j], 'red')
                    numberInfectedCells += 1.0
                else:
                    board[i][j] = colored('+', 'blue')
                    numberOkaySusceptibles += 1.0
            elif board[i][j] == colored('.','green'): 
                board[i][j] = colored('.','green')
                innoculatedPeople += 1.0
    board[patientZero[0]][patientZero[1]] = colored('O','yellow')
    os.system("clear")
    print '\n\nYOUR POPULATION(where the yellow O signifies patient zero, a blue + indicates a susceptible person who was not infected, a green . indicates a vaccinated person):\n'
    printBoard(board, width, height)
    wrapup(width, height, generation, innoculatedPeople, numberInfectedCells, numberOkaySusceptibles)    
    
def wrapup(width, height, generation, innoculatedPeople, numberInfectedCells, numberOkaySusceptibles):
    numberPeople = width * height
    notVaccinated = (numberPeople - innoculatedPeople)
    print '\n\n\n', numberInfectedCells, 'people out of', numberPeople, 'were infected over the course of', generation, 'periods after patient zero was infected, where',innoculatedPeople,'people, or', (innoculatedPeople/numberPeople)*100.0,'%, were vaccinated. Out of the', notVaccinated,'that were not vaccinated,',numberOkaySusceptibles,'people, or', (numberOkaySusceptibles/notVaccinated)*100.0, '%, did not contract the disease.'




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
        width = 60
        height = 60
    print "\n\nPlease enter the upper limit of the vaccination rate of your population, assuming a percentage."
    try:
        vaccinationRate = input('')
    except: vaccinationRate = 50
    vaccinationRate = int((vaccinationRate/100.0)*(width*height))

    print '"." marks an innoculated person, "+" marks a healthy but susceptible person, a number/letter marks an infected person\n\nGenerations are numbered 0-9 and a-z \n\n'
    board = createBoard(width, height)
    board, patientZero = fillBoard(board, width, height, vaccinationRate)
    os.system("clear")
    printBoard(board, width, height)
    print 'Creating simulation...'
    done = False
    generation = 0
    genList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while done == False:
        generation += 1
        finished = evolve(board, width, height, generation, genList, transmissionType)
        if finished == True:
            done = True
    endBoard(board, width, height, generation, patientZero)


main()


    

