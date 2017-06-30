# by Obosa Obazuaye, HMC '14: Summer 2011

from hw9pr1 import next_life_generation
# make sure this is implemented!

import time
from turtle import *
import csgrid; from csgrid import *
from random import *

# summary of keypresses:
print("  PAUSE: 'p'")
print(" RESUME: 'Return'/'Enter'")
print("  RESET: 'Space'")
print("  CLOSE: 'Esc'")
print()
print("Start with start() ...")
print()

# the function to start:
def start( width=20, height=20 ):
    # start-up turtle stuff
    reset()  # clear the screen
    tracer(False) # turn off turtle animation
    delay(0)  # go as fast as possible
    global board, screen
    screen = Screen()
    board = randomCells( width, height )
    screen.listen()
    onscreenclick(lifeMouseHandler)
    screen.onkey(showgood2, "Return")
    screen.onkey(bye, "Escape")
    screen.onkey(blank, "space")
    show(board)
    done()


global board

def allZeroes(L):
    """Checks if the board is all zeroes"""
    if type(board[0]) == int: #If the board is only 1 list...
        return L == [0]*len(L)
    else: #If the board is a grid...
        counter = 0
        for List in L:
            if List == [0]*len(List): counter+=1
        return counter == len(L)
    
def showgood():
    """Makes the next life generation appear"""
    global board
    board = next_life_generation(board)
    show(board)

running = True
def showgood2():
    """Sets the board to keep moving through generations of life.
        Allows for pausing with "p", resuming with "Enter"/"Return",
        and automatically pauses the game if the board stops changing
        or becomes blank."""
    global board
    global running
    screen.onkey(gamepause, "p")
    screen.onkey(gameresume, "Return")
    screen.listen()
    if running:
        if board == next_life_generation(board) == \
           next_life_generation(next_life_generation(board)) or allZeroes(board):
            running = False
        else:
            showgood()
            screen.ontimer(showgood2, t=0)
            #The t value above sets how many milliseconds there are
            # between each generation of life. Set it low (e.g. 0 seconds, or 500
            # for half a second, etc.) for fast movement, or
            # set it high (e.g. 1000 for 1 second, 3000 for 3 seconds, etc.)
            # for fast slower movement.

def gamepause():
    """Pauses the game"""
    global running
    running = False

def gameresume():
    """Resumes a paused game."""
    global running
    running = True
    showgood2()
    
def blank():
    """Makes the board blank (resets the board)"""
    global board
    height = len(board)
    width = len(board[0])
    board = createBoard(width,height) # of zeros
    show(board)


###hw9pr1 answers


def createOneRow(width):
    """ returns one row of zeros of width "width"...  
         You might use this in your createBoard(width, height) function """
    row = []
    #print "width is", width
    for col in range(width):
        row += [0]
    return row


def createBoard(width,height):
    """ returns a 2d array of width and height """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def randomCells(width,height):
    """ Takes an empty board as input and modifies that board
        so that its inner cells (non-edge) are either 0 or 1
    """
    A = createBoard( width, height )
    
    for row in range(1,height-1):
        for col in range(1,width-1):
            A[row][col] = choice( [0,1] )  

    return A

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A


def printBoard(A):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write)
    """
    for row in A:               # row is the whole row
        for col in row:         # col is the individual element
            print(col,end='')   # print that element
        print()                 # and a newline after each row


def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
        but, only in the * interior * of the 2d array
    """
    A = createBoard(width, height)

    for row in range(1,height-1):
        for col in range(1,width-1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A


def innerCells(w,h):
    """ returns a 2d array that has a one cell border of empty cells around all live cells
        with a width of w and height h
    """
    A = createBoard(w,h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = 1
    return A


def randomCells(w,h):
    """ returns array of randomly assigned 1's and 0's, 
        except for outer edge of 0's
    """
    A = createBoard(w,h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = choice([0,1])
    return A


def copy(A):
    """ creates "deep" copy of 2d array A
    """
    height = len(A)
    width = len(A[0])
    newA = createBoard( width, height )
    for row in range(1, height-1):
        for col in range(1, width-1):
            newA[row][col] = A[row][col]
    return newA


def innerReverse(A):
    """ inverses all cells in A, except outer edge of 0's
    """
    height = len(A)
    width = len(A[0])
    newA = createBoard( width, height )
    for row in range(1, height-1):
        for col in range(1, width-1):
            newA[row][col] = (A[row][col] + 1)%2
    return newA


def countNeighbors(row,col,A):
    """ returns number of live neighbors for the cell at (row,col) in A
    """
    count = 0
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            count += A[r][c]
    count -= A[row][col]
    return count


def next_life_generation(A):
    """ makes a copy of A and then advances one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays at 0.
    """
    height = len(A)
    width = len(A[0])
    newA = createBoard( width, height )
    for row in range(1, height-1):
        for col in range(1, width-1):
            if countNeighbors(row,col,A) == 2:
                newA[row][col]=A[row][col]
            elif countNeighbors(row,col,A) == 3:
                newA[row][col]=1
            #elif countNeighbors(row,col,A) < 2 or countNeighbors(row,col,A)>3:
            else:
                newA[row][col]=0
    return newA

    
