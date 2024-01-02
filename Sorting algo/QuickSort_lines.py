from re import T
import pygame
import pygame.display
import random
import time

#start pygame
pygame.init()

#DISPLAY
SCREEN_SIZE = (700,600)
display = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

#COLORS
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

#vars
lines = []
pivot_index = 0
last_loop = False
amt = 60
heights = random.sample(range(0,60),60)
BUFFER_TIME = 0

#line object
class Line():
    def __init__(self, length):
        self.length = length
    def draw(self, x, color=WHITE):
        x = x
        pygame.draw.rect(display, color, pygame.Rect((x,0),(10,self.length*10)))

#functions
def update(P1,P2):
    #draw all lines
    display.fill((0,0,0))
    x = 0
    pos1 = lines.index(P1)
    pos2 = lines.index(P2)
    for index, line in enumerate(lines):
        if index == pos1:
            line.draw((x*10)+x, GREEN)
        elif index == pos2:
            line.draw((x*10)+x, RED)
        else:
            line.draw((x*10)+x)
        x+=1
    pygame.display.flip()
    pygame.time.wait(BUFFER_TIME)

def swapPositions(linest, pos1, pos2):
    linest[pos1], linest[pos2] = linest[pos2], linest[pos1]
    return linest

def start():
    #create x amt of lines
    for i in range(amt):
        lines.append(Line(heights[i]))
    display.fill((0,0,0))
    x = 0
    for line in lines:
        line.draw((x*10)+x)
        x+=1
        pygame.display.flip()
        pygame.time.wait(BUFFER_TIME)

def reset():
    global lines, amt, heights
    lines = []
    amt = 60
    heights = random.sample(range(0,60),60)
 
#main func
def sort_lines():
    global pivot_index, lines, last_loop, start_time

    #pick a pivoit (at middle ruffly)
    #move pivoit to end of linest (just remove it then append it)
    #find item from left (first number from left larger than pivot) 
    #find item from right (first number from right smaller than pivot)
    #if item from left > item from right then we are done, swap item from left with out pivot 
    #if we are not done we will swap item from left with item from right
    if last_loop and pivot_index > len(lines)-1:
        print(f"Done, Time: {time.time()-start_time} ")
        pygame.time.wait(100)
        reset()
        start()
        # pygame.quit()
        # quit()
    if pivot_index > len(lines)-1:
        pivot_index = 0
        last_loop = True
    
    pivot = lines[pivot_index]
    #lines.remove(pivot)
    #lines.append(pivot)

        

    while True:
        IFL = 0
        IFR = 0
        index = 0
        for i in range(len(lines)):
            if lines[i].length <= pivot.length:
                IFR = lines[i]
        for i in range(len(lines)):
            index += 1
            if lines[len(lines)-index].length >= pivot.length: 
                IFL = lines[len(lines)-index]
        
        if lines.index(IFL)>lines.index(IFR) or lines.index(IFL)==lines.index(IFR):
            swapPositions(lines,lines.index(IFL),lines.index(pivot))
            pivot_index+=1
            update(IFL,IFR)
            sort_lines()
        else:
            swapPositions(lines,lines.index(IFR),lines.index(IFL))
            update(IFL,IFR)
        
        
            
while True:
    start_time = time.time()
    start()
    sort_lines()
    