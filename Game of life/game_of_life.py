"""
Any live cell with two or three live neighbours survives. 
Any dead cell with three live neighbours becomes a live cell.
All other live cells die in the next generation. 
Similarly, all other dead cells stay dead.
"""

import pygame as pg

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
ORANGE = (255,215,0)

#vars
target_spot = [0,0]
start = [0,0]
open_grids = []
closed_grids = []

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# Set witdh and height for box
WIDTH_BOX = 30
HEIGHT_BOX = 30
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []


for row in range(WIDTH_BOX):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(HEIGHT_BOX):
        grid[row].append(0)  # Append a cell



# Initialize pg
pg.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [700, 700]
screen = pg.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pg.display.set_caption("PATH FINDING")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pg.time.Clock()
 
# -------- Main Program Loop -----------

# Set the screen background
screen.fill(BLACK)

# Draw the grid
def draw():
    for row in range(WIDTH_BOX):
        for column in range(HEIGHT_BOX):
            color = WHITE
            #alive
            if grid[row][column] == 1:
                color = GREEN
            if grid[row][column] == 2:
                color = ORANGE
            pg.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])


#GAME LOGIC ---------


def update():
    cells_to_die = []
    cells_to_live = []
    for row in range(WIDTH_BOX):
        for column in range(HEIGHT_BOX):
            if grid[row][column] == 1:
                #alive cell logic
                #Any live cell with two or three live neighbours survives. else die
                liveing_neighbours = 0
                for i in range(8):
                    try:
                        if i == 0:
                            spot = grid[row-1][column-1]
                            if spot == 1:
                                liveing_neighbours += 1
                        if i == 1:
                            spot = grid[row][column-1]
                            if spot == 1:
                                liveing_neighbours += 1
                        if i == 2:
                            spot = grid[row+1][column-1]
                            if spot == 1:
                                liveing_neighbours += 1

                        if i == 3:
                            spot = grid[row-1][column]
                            if spot == 1:
                                liveing_neighbours += 1
                        if i == 4:
                            spot = grid[row+1][column]
                            if spot == 1:
                                liveing_neighbours += 1

                        if i == 5:
                            spot = grid[row-1][column+1]
                            if spot == 1:
                                liveing_neighbours += 1
                        if i == 6:
                            spot = grid[row][column+1]
                            if spot == 1:
                                liveing_neighbours += 1
                        if i == 7:
                            spot = grid[row+1][column+1]
                            if spot == 1:
                                liveing_neighbours += 1
                        
                        
                    except:
                        pass
                
                if liveing_neighbours != 2 and liveing_neighbours != 3:
                    cells_to_die.append([row,column])

            else:
                #dead cell logic
                #Any dead cell with three live neighbours becomes a live cell.
                liveing_neighbours = 0
                for i in range(8):
                    try:
                        if i == 0:
                            spot = grid[row-1][column-1]
                            if spot == 1:
                                liveing_neighbours += 1
                        if i == 1:
                            spot = grid[row][column-1]
                            if spot == 1:
                                liveing_neighbours += 1
                        if i == 2:
                            spot = grid[row+1][column-1]
                            if spot == 1:
                                liveing_neighbours += 1

                        if i == 3:
                            spot = grid[row-1][column]
                            if spot == 1:
                                liveing_neighbours += 1
                        if i == 4:
                            spot = grid[row+1][column]
                            if spot == 1:
                                liveing_neighbours += 1

                        if i == 5:
                            spot = grid[row-1][column+1]
                            if spot == 1:
                                liveing_neighbours += 1
                        if i == 6:
                            spot = grid[row][column+1]
                            if spot == 1:
                                liveing_neighbours += 1
                        if i == 7:
                            spot = grid[row+1][column+1]
                            if spot == 1:
                                liveing_neighbours += 1
                    except:
                        pass
                
                
                if liveing_neighbours == 3:
                    cells_to_live.append([row,column])

    for cell in cells_to_die:
        grid[cell[0]][cell[1]] = 0
    for cell in cells_to_live:
        grid[cell[0]][cell[1]] = 1
#--------------------

location = [10,10]
place = True

# Limit to 60 frames per second
clock.tick(60)

draw()
pg.display.flip()

run = True
while run:

    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_t:
                while True:
                    try:
                        draw()
                        update()
                        pg.display.flip()
                        pg.time.wait(100)
                    except KeyboardInterrupt:
                        break

            if event.key == pg.K_a and location[1] != 0:
                if not place:
                    if grid[location[0]][location[1]] != 1:
                        grid[location[0]][location[1]] = 0
                else:
                    place = False 
                location[1] -= 1
            if event.key == pg.K_w and location[0] != 0:
                if not place:
                    if grid[location[0]][location[1]] != 1:
                        grid[location[0]][location[1]] = 0
                else:
                    place = False
                location[0] -= 1
            if event.key == pg.K_d and location[1] != HEIGHT_BOX-1:
                if not place:
                    if grid[location[0]][location[1]] != 1:
                        grid[location[0]][location[1]] = 0
                else:
                    place = False
                location[1] += 1
            if event.key == pg.K_s and location[0] != WIDTH_BOX-1:
                if not place:
                    if grid[location[0]][location[1]] != 1:
                        grid[location[0]][location[1]] = 0
                else:
                    place = False
                location[0] += 1
        
            if event.key == pg.K_SPACE:
                place = True
    
    if grid[location[0]][location[1]] != 1:
        grid[location[0]][location[1]] = 2
    if place:
        if grid[location[0]][location[1]] != 1:
            grid[location[0]][location[1]] = 1
        else:
            grid[location[0]][location[1]] = 0
        place = False
    
    draw()
    pg.display.flip()
    pg.time.wait(250)


pg.quit()