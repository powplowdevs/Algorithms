"""
The Sierpinski triangle is a self-similar fractal. It consists of an equilateral triangle, 
with smaller equilateral triangles recursively removed from its remaining area. , 
which is named after the Polish mathematician Wacław Sierpiński. 
Wacław Franciszek Sierpiński (1882 – 1969) was a Polish mathematician.
"""

#steps:
#1:chose any of the starting points
#2:chose point anywhere in triangle and draw a line half way from it to selected point
#3:chose any of the starting points
#4:draw a line half way from it to last half way point
#loop 3 & 4

# from cv2 import line
import pygame
import pygame.display
import random

#start pygame
pygame.init()

#DISPLAY
display_SIZE = (700,700)
display = pygame.display.set_mode(display_SIZE)
clock = pygame.time.Clock()

#COLORS
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

#vars
point = [0,0]
triangal = [(350,50),(50,650),(650,650)]
running = True
last_point = random.choice(triangal)
points = []
first_point = True

#functions
def point_on_triangle():
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = sorted([random.random(), random.random()])
    s, t, u = x, y - x, 1 - y
    return (s * triangal[0][0] + t * triangal[1][0] + u * triangal[2][0],
            s * triangal[0][1] + t * triangal[1][1] + u * triangal[2][1])


def draw_point(pos,size):
    pygame.draw.circle(display, RED, pos, size)


def update():
    global last_point, points, first_point
    if first_point:
        random_point = point_on_triangle()
        new_point = ( (random_point[0] + last_point[0])/2, (random_point[1] + last_point[1])/2 )
        points.append(new_point)
        draw_point(new_point, 1)
        last_point = random_point
        first_point = False
    else:
        random_point = random.choice(triangal)
        new_point = ( (random_point[0] + last_point[0])/2, (random_point[1] + last_point[1])/2 )
        points.append(new_point)
        draw_point(new_point, 0.00001)
        last_point = new_point



while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    display.fill((0, 0, 0))

    for index, pos in enumerate(triangal):
        pygame.draw.circle(display, RED, pos, 10)
    for index, pos in enumerate(points):
        draw_point(pos,1)

    update()

    pygame.display.flip()

    #pygame.time.wait(1000)

pygame.time.wait(10000000)
pygame.quit()
