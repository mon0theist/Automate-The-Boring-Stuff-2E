#! /usr/bin/python
#
# ATBS2E - Chapter 4 - Conway's Game of Life
#
# Conway’s Game of Life is an example of cellular automata: a set of rules
# governing the behavior of a field made up of discrete cells. In practice, it
# creates a pretty animation to look at. You can draw out each step on graph paper,
# using the squares as cells. A filled-in square will be “alive” and an empty
# square will be “dead.” If a living square has two or three living neighbors,
# it continues to live on the next step. If a dead square has exactly three
# living neighbors, it comes alive on the next step. Every other square dies or
# remains dead on the next step. You can see an example of the progression of
# steps in Figure 4-8.
#
# Even though the rules are simple, there are many surprising behaviors that emerge.
# Patterns in Conway’s Game of Life can move, self-replicate, or even mimic CPUs.
# But at the foundation of all of this complex, advanced behavior is a rather
# simple program.

# We can use a list of lists to represent the two-dimensional field. The inner
# list represents each column of squares and stores a '#' hash string for living
# squares and a ' ' space string for dead squares. Type the following source code
# into the file editor, and save the file as conway.py. It’s fine if you don’t
# quite understand how all of the code works; just enter it and follow along
# with comments and explanations provided here as close as you can

# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop.
    print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print() # Print a newline at the end of the row.

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or
numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.
