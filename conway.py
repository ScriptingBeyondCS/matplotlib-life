###############################################################################
# conway.py
#
# Author: electronut.in
# 
# Description:
#
# A simple Python/matplotlib implementation of Conway's Game of Life.
################################################################################

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 100
ON = 1
OFF = 0
vals = [ON, OFF]

# populate grid with random on/off - more off than on
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def update(data):
  global grid
  # copy grid since we require 8 neighbors for calculation
  # and we go line by line 
  if not paused:  
    newGrid = grid.copy()
    for i in range(N):
      for j in range(N):
        # compute 8-neighbor sum 
        # using toroidal boundary conditions - x and y wrap around 
        # so that the simulaton takes place on a toroidal surface.
        total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/ON
        # apply Conway's rules
        if grid[i, j]  == ON:
          if (total < 2) or (total > 3):
            newGrid[i, j] = OFF
        else:
          if total == 3:
            newGrid[i, j] = ON
  else:
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    newGrid = grid.copy()
  # update data
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]

def onclick(event):
  col = int(np.round(event.xdata))
  row = int(np.round(event.ydata))
  if grid[row,col] == ON:
    grid[row,col] = OFF
  else:
    grid[row,col] = ON 

paused = False
def onspace(event):
  global paused
  if event.key == ' ':
    paused = not paused

# set up animation
fig, ax = plt.subplots()
cid = fig.canvas.mpl_connect('button_press_event', onclick)
cid2 = fig.canvas.mpl_connect('key_press_event', onspace)
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()