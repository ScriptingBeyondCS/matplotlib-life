###############################################################################
# by Hanna Hoffman, HMC '20: Summer 2017
#
# array => matplotlib graphics portion by electronut.in
# based off of turtle graphics version by Obosa Obazuaye, HMC '14
################################################################################
from hw9pr1 import next_life_generation, randomCells
# make sure these two are implemented!!

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import colors

#summary of keypresses
print(" PAUSE/PLAY: spacebar")
print(" (next) STEP: n")
print(" RESET: 'Enter'/'Return' ")
print()

paused = False
reset = False
ON = 1
OFF = 0

def start(width=20, height=20):
    """ wrapper function """
    global grid
    global mat
    global fig

    board = randomCells(width, height)
    # board is a list of lists; what students' functions interact with 
    grid = np.array(board)
    # grid is numpy.ndarray; what matplotlib interacts with

    fig, ax = plt.subplots()
    cid = fig.canvas.mpl_connect('button_press_event', on_click)
    cid2 = fig.canvas.mpl_connect('key_press_event', on_space)
    cid3 = fig.canvas.mpl_connect('key_press_event', on_return)

    cmap = colors.ListedColormap(['xkcd:light navy blue','xkcd:celery'])
    bounds = [-.5, .5, 1.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    mat = ax.matshow(grid, cmap=cmap, norm=norm)
    ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
    plt.show()


def update(data):
    """ updates grid/board to next state if not paused
        shows changed cells when not paused
    """
    global grid
    global reset
    if reset:
        board = randomCells(20, 20)
        grid = np.array(board)
        reset = False
        newGrid = grid.copy()
    elif not paused:  
        board = grid.tolist() # turn np.ndarray into list of lists 
        newBoard = next_life_generation(board) 
        newGrid = np.array(newBoard)
    else:
        cid = fig.canvas.mpl_connect('button_press_event', on_click)
        cid4 = fig.canvas.mpl_connect('key_press_event', on_step)
        newGrid = grid.copy()
    # update data
    mat.set_data(newGrid)
    grid = newGrid
    return [mat]


def on_click(event):
    """ flips cell state when cell is clicked """
    col = int(np.round(event.xdata))
    row = int(np.round(event.ydata))
    if grid[row,col] == ON:
        grid[row,col] = OFF
    else:
        grid[row,col] = ON 


def on_space(event):
    """ effectively pauses/resumes animation
        when space is pressed
    """
    global paused
    if event.key == ' ':
        paused = not paused


def on_return(event):
    """ resets to a random board when
        return is pressed
    """
    global reset
    if event.key == 'enter':
        reset = True

def on_step(event):
    """ steps forward once
        when 'n' is pressed
    """
    global grid
    if event.key == 'n':
        board = grid.tolist() # turn np.ndarray into list of lists 
        newBoard = next_life_generation(board) 
        newGrid = np.array(newBoard)
        grid = newGrid

start()