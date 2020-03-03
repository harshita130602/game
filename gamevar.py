import pygame
from config import *

"""
Variables used for the players in the game and the background
"""

PLAYER_2 = pygame.image.load('img/p2.png')
PLAYER_2 = pygame.transform.scale(PLAYER_2,(128*display_width//1600,128*display_width//1600))
PLAYER_1 = pygame.image.load('img/p1.png')
PLAYER_1 = pygame.transform.scale(PLAYER_1,(128*display_width//1600,128*display_width//1600))
DYNAMIC_OBSTACLE = pygame.image.load('img/dynamic_obstacle.png')
DYNAMIC_OBSTACLE = pygame.transform.scale(DYNAMIC_OBSTACLE,(200*display_width//1600,200*display_width//1600))
STATIC_OBSTACLE = pygame.image.load('img/static_obstacle.png')
STATIC_OBSTACLE = pygame.transform.scale(STATIC_OBSTACLE,(250*display_width//1600,250*display_width//1600))
DISPLAY = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Infinite Madness')
clock = pygame.time.Clock()
win_text = "To Infinity and Beyond!"
crash_text = "Press F for Respect."
dynamic_obstacle_height=26
dynamic_obstacle_width=64
static_obstacle_height=94
static_obstacle_width=158
cursor_width=55
cursor_height=79

down = 795.0
left=-37.0
right=1511.0
up=-23.0

global win_1
global win_2
speed_counter1=2
speed_counter2=2
win_2=False
win_1=False

"""
Static Background Generation!
"""
def background():
    DISPLAY.fill(aqua)
    for i in range(0,21,4):
        pygame.draw.rect(DISPLAY,gray,(0,i*display_height/21,display_width,display_height//21))