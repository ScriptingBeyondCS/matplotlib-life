# hw9pr1.py
#
# Name: Hanna Hoffman
#

#
# Here is a function that will help start hw9pr1's lab:
#

import random # for randomCells

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
            A[row][col] = random.choice([0,1])
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