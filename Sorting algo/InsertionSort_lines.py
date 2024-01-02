import pygame
import pygame.display
import random
import time

#start pygame
pygame.init()

#DISPLAY
SCREEN_SIZE = (1000,1000)
display = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

#COLORS
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

#vars
lines = []
amt = 500
heights = random.sample(range(0,amt),amt)
BUFFER_TIME = 0

#line object
class Line():
    def __init__(self, length):
        self.length = length
    def draw(self, x, color=WHITE):
        x = x
        pygame.draw.rect(display, color, pygame.Rect((x,0),(1,self.length*1)))

#functions
def update(index, color=""):
    #draw all lines
    display.fill((0,0,0))
    x = 0
    for line in lines:
        if x == index and color == "":
            line.draw((x*1)+x, RED)
        elif x == index and color == "G":
            line.draw((x*1)+x, GREEN)
        else:
            line.draw((x*1)+x)
        x+=1
    pygame.display.flip()
    pygame.time.wait(BUFFER_TIME)

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def start():
    global amt
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
    heights = random.sample(range(0,amt),amt)
 
#main func
def sort_lines():
    sorted = False
    index = 0
    #while not sorted
    #1. get the height on our line
    #2. get the height of the last line (if we are not at the ends)
    #3. if the last line is > the current line swap them
    #3. index -= 1
    #4. loop
    while not sorted:
        try:
            index += 1
            current = lines[index].length
            last = lines[index-1].length
            sub_sort = False
            while not sub_sort:
                if current < last and index != 0:
                    swapPositions(lines,index,index-1)
                    index-=1
                    current = lines[index].length
                    last = lines[index-1].length
                    update(index)
                else:
                    update(index, "G")
                    sub_sort = True
        except:
            break
            
while True:
    try:
        start_time = time.time()
        start()
        sort_lines()
        pygame.time.wait(BUFFER_TIME)
        print(f"Done, Time: {time.time()-start_time} ")
        #pygame.time.wait(10000000)
        #quit()
        reset()
    except KeyboardInterrupt:
        pygame.quit()