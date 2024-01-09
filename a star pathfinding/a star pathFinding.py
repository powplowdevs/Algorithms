import math
import pygame as pg
import random


 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
ORANGE = (255,215,0)
PINK = (255,192,203)

#vars
target_spot = [0,0]
start = [0,0]
open_grids = []
closed_grids = []
side_options = []
dead = []
side_av = False
con = False

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 7
HEIGHT = 7
 
# This sets the margin between each cell
MARGIN = 5
 
#BUFFER between draws
BUFFER = 0

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []

#cost added to diagnal moves
G = 0

#ended
ended = False

#display size
D_WIDTH = 50
D_HEIGHT = 50

def create_grid():
    for row in range(D_WIDTH):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(D_HEIGHT):
            grid[row].append(0)  # Append a cell
    
    #color grid
    #add enviroment blocks

    for x in range(D_WIDTH):
        for y in range(D_HEIGHT):
            block_state = random.randint(0,7)
            if block_state < 2:
                grid[y][x] = 3


    #add start and end blocks 
    for i in range(2):
        x = random.randint(1,D_WIDTH-1)
        y = random.randint(1,D_HEIGHT-1)

        if i == 0:
            grid[y][x] = 1
            start[0] = y
            start[1] = x
        elif i == 1:
            target_spot[0] = y
            target_spot[1] = x 
            grid[y][x] = 2

# Initialize pg
pg.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [(D_WIDTH*HEIGHT)+251, (D_WIDTH*WIDTH)+251]
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
    for row in range(D_WIDTH):
        for column in range(D_HEIGHT):
            color = WHITE
            #start
            if grid[row][column] == 1:
                color = GREEN
            #target
            if grid[row][column] == 2:
                color = RED
            #others
            if grid[row][column] == 3:
                color = BLACK
            if grid[row][column] == 4:
                color = WHITE
            if grid[row][column] == 5:
                color = BLUE
            if grid[row][column] == 6:
                color = ORANGE
            if grid[row][column] == 7:
                color = PINK
            if grid[row][column] == 8:
                color = WHITE
            pg.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
    
# -------- Path finder logic -----------


# Limit to 60 frames per second
clock.tick(60)

create_grid()

open_grids.append(start)

#print(f"start: {start}\nend: {target_spot}")
draw()
pg.display.flip()
base_start = start

def path_find():
    global ended, grid, open_grids, closed_grids, start, target_spot, side_options, side_av, con, dead
    while True:
        f_values = []
        xys = []
        for i in range(8):
            try:
                #define spot
                #get distance from spot to target_spot
                #add G to distance
                #check if spot is eqal to target_spot (if so ended = true and break)
                #add spot to xys
                #draw spot

                if i == 0:
                    spot = [start[0]-1,start[1]-1]
                    distance = math.dist([spot[1],spot[0]], [target_spot[1],target_spot[0]])
                    distance += G
                    if grid[spot[0]][spot[1]] == 3 or [spot[0],spot[1]] in closed_grids or [spot[0],spot[1]] in dead:
                        distance += 99999
                    if spot == target_spot:
                        ended = True
                        break
                    xys.append(spot)
                    if grid[spot[0]][spot[1]] != 3:
                        grid[spot[0]][spot[1]] = 5
            
                if i == 1:
                    spot = [start[0]-1,start[1]]
                    distance = math.dist([spot[1],spot[0]], [target_spot[1],target_spot[0]])
                    distance += G
                    if grid[spot[0]][spot[1]] == 3 or [spot[0],spot[1]] in closed_grids or [spot[0],spot[1]] in dead:
                        distance += 99999
                    if spot == target_spot:
                        ended = True
                        break
                    xys.append(spot)
                    if grid[spot[0]][spot[1]] != 3:
                        grid[spot[0]][spot[1]] = 5
                
                if i == 2:
                    spot = [start[0]-1,start[1]+1]
                    distance = math.dist([spot[1],spot[0]], [target_spot[1],target_spot[0]])
                    distance += G
                    if grid[spot[0]][spot[1]] == 3 or [spot[0],spot[1]] in closed_grids or [spot[0],spot[1]] in dead:
                        distance += 99999
                    if spot == target_spot:
                        ended = True
                        break
                    xys.append(spot)
                    if grid[spot[0]][spot[1]] != 3:
                        grid[spot[0]][spot[1]] = 5
            
                if i == 3:
                    spot = [start[0],start[1]-1]
                    distance = math.dist([spot[1],spot[0]], [target_spot[1],target_spot[0]])
                    distance += G
                    if grid[spot[0]][spot[1]] == 3 or [spot[0],spot[1]] in closed_grids or [spot[0],spot[1]] in dead:
                        distance += 99999
                    if spot == target_spot:
                        ended = True
                        break
                    xys.append(spot)
                    if grid[spot[0]][spot[1]] != 3:
                        grid[spot[0]][spot[1]] = 5
                
                if i == 4: 
                    spot = [start[0],start[1]+1]
                    distance = math.dist([spot[1],spot[0]], [target_spot[1],target_spot[0]])
                    distance += G
                    if grid[spot[0]][spot[1]] == 3 or [spot[0],spot[1]] in closed_grids or [spot[0],spot[1]] in dead:
                        distance += 99999
                    if spot == target_spot:
                        ended = True
                        break
                    xys.append(spot)
                    if grid[spot[0]][spot[1]] != 3:
                        grid[spot[0]][spot[1]] = 5
                
                if i == 5:
                    spot = [start[0]+1,start[1]-1]
                    distance = math.dist([spot[1],spot[0]], [target_spot[1],target_spot[0]])
                    distance += G
                    if grid[spot[0]][spot[1]] == 3 or [spot[0],spot[1]] in closed_grids or [spot[0],spot[1]] in dead:
                        distance += 99999
                    if spot == target_spot:
                        ended = True
                        break
                    xys.append(spot)
                    if grid[spot[0]][spot[1]] != 3:
                        grid[spot[0]][spot[1]] = 5
            
                if i == 6:
                    spot = [start[0]+1,start[1]]
                    distance = math.dist([spot[1],spot[0]], [target_spot[1],target_spot[0]])
                    distance += G
                    if grid[spot[0]][spot[1]] == 3 or [spot[0],spot[1]] in closed_grids or [spot[0],spot[1]] in dead:
                        distance += 99999
                    if spot == target_spot:
                        ended = True
                        break
                    xys.append(spot)
                    if grid[spot[0]][spot[1]] != 3:
                        grid[spot[0]][spot[1]] = 5
                    
                if i == 7:
                    spot = [start[0]+1,start[1]+1]
                    distance = math.dist([spot[1],spot[0]], [target_spot[1],target_spot[0]])
                    distance += G
                    if grid[spot[0]][spot[1]] == 3 or [spot[0],spot[1]] in closed_grids or [spot[0],spot[1]] in dead:
                        distance += 99999
                    if spot == target_spot:
                        ended = True
                        break
                    xys.append(spot)
                    if grid[spot[0]][spot[1]] != 3:
                        grid[spot[0]][spot[1]] = 5
                
                f_values.append(distance)
                
                draw()
                pg.display.flip()
                pg.time.wait(BUFFER)

            except:
                pass #close to wall so not every node is open
        
        if ended:
            print("HIT")
            if not side_av:
                print("DONE!")
                grid[base_start[0]][base_start[1]] = 1
                grid[target_spot[0]][target_spot[1]] = 2
                for index, value in enumerate(closed_grids):
                    grid[value[0]][value[1]] = 7
                    draw()
                    pg.display.flip()
                    pg.time.wait(50) 
                
                break
            else:
                print("yo")
                side_av = False
                start = [side_options[0][2][0],side_options[0][2][1]]
                ended = False
                con = True
                
        
        current = f_values.index(min(f_values))
        
        if side_av:   
            #print(side_options)
            if side_options[0][1] < min(f_values):
                #xys = sos
                print("yo")
                grid[side_options[0][2][0]][side_options[0][2][1]] = 7
                closed_grids.append([side_options[0][2][0],side_options[0][2][1]])
                start = [side_options[0][2][0],side_options[0][2][1]]
                side_av = False
                side_options = []
                draw()
                pg.time.wait(1000)
            else:
                print("no2")
                grid[xys[current][0]][xys[current][1]] = 6
            
                closed_grids.append([xys[current][0],xys[current][1]])

                start = [xys[current][0],xys[current][1]]
            
        else:
            grid[xys[current][0]][xys[current][1]] = 6
        
            closed_grids.append([xys[current][0],xys[current][1]])

            start = [xys[current][0],xys[current][1]]
        
            
        if not side_av and len(side_options) == 1 or not side_av and len(side_options) == 0:
            for index, value in enumerate(f_values):
                if value == min(f_values) and index != current:
                    side_options.append([index, value, [xys[current][0], xys[current][1]]])
                    side_av = True
                    print("same")
                    #pg.time.wait(1000)

        if side_av and len(dead) == 0:
            dead.append([xys[current][0], xys[current][1] ])
        
            
        grid[xys[current][0]][xys[current][1]] = 6
        
        closed_grids.append([xys[current][0],xys[current][1]])

        start = [xys[current][0],xys[current][1]]

        draw()
        pg.display.flip()

        
        


        # Go ahead and update the screen with what we've drawn.
        pg.display.flip()

        pg.time.wait(0)
draw()

x = 0
y = 0
last = [0,0]
drawing = False

while True:
    ev = pg.event.get()
    for event in ev:
        if event.type == pg.KEYDOWN:
            #print([x,y], "\n", last)
            if event.key == pg.K_LEFT:
                if grid[last[0]][last[1]] != 3 and grid[last[0]][last[1]] != 2 and grid[last[0]][last[1]] != 1:
                    grid[last[0]][last[1]] = 8
                x -= 1
                last = [y,x]
                if not drawing:
                    grid[y][x] = 7
                else:
                    grid[y][x] = 3
                draw()
                pg.display.flip()
            if event.key == pg.K_RIGHT:
                if grid[last[0]][last[1]] != 3 and grid[last[0]][last[1]] != 2 and grid[last[0]][last[1]] != 1:
                    grid[last[0]][last[1]] = 8
                x += 1 
                last = [y,x]
                if not drawing:
                    grid[y][x] = 7
                else:
                    grid[y][x] = 3
                draw()
                pg.display.flip()
            if  event.key == pg.K_UP:
                if grid[last[0]][last[1]] != 3 and grid[last[0]][last[1]] != 2 and grid[last[0]][last[1]] != 1:
                    grid[last[0]][last[1]] = 8
                y -= 1
                last = [y,x]
                if not drawing:
                    grid[y][x] = 7
                else:
                    grid[y][x] = 3
                draw()
                pg.display.flip()
            if event.key == pg.K_DOWN:
                if grid[last[0]][last[1]] != 3 and grid[last[0]][last[1]] != 2 and grid[last[0]][last[1]] != 1:
                    grid[last[0]][last[1]] = 8
                y += 1
                last = [y,x]
                if not drawing:
                    grid[y][x] = 7
                else:
                    grid[y][x] = 3
             
            
                draw()
                pg.display.flip()

            if event.key == pg.K_SPACE:
                drawing = not drawing
                
            if event.key == pg.K_s:
                ended =  False
                path_find()
                target_spot = [0,0]
                start = [0,0]
                open_grids = []
                closed_grids = []
                grid = []
                side_options = []
                create_grid()
                draw()
                base_start = start
                



