import pygame
from gamevar import *

"""
Obstacle generation and maintenance during the game loop.
"""
def static_obstacle(width,height):
    DISPLAY.blit(STATIC_OBSTACLE,(width,height))

def dynamic_obstacle(width,height,speed=0):
    width+=speed
    width%=display_width+50
    width+=-100
    DISPLAY.blit(DYNAMIC_OBSTACLE,(width,height))
    return width

def dynamic_obstacles(speed=0):
    width=0
    for i in range(0,17,4):
        width+=dynamic_obstacle(0,(i+0.65)*display_height/21,speed)
    return width//5

static_obstacle_arr = [(15,1.5),(250,1.5),(550,1.5),(750,1.5),(1150,1.5),(400,5.5),(850,5.5),(122,9.5),(750,9.5),(1000,9.5),(1350,9.5),(250,13.5),(550,13.5),(890,13.5),(1250,13.5)]
static_obstacle_arr = [(i,j*display_height/21) for i,j in static_obstacle_arr]

def static_obstacles():
    for i,j in static_obstacle_arr:
        static_obstacle(i,j)
