import pygame,sys,time,timeit
from obstacles import *

########################################################################################################
#Players
def player2(x,y):
    DISPLAY.blit(PLAYER_2,(x,y))
def player1(x,y):
    DISPLAY.blit(PLAYER_1,(x,y))
########################################################################################################
#Message Dialogs

def text_objects(message,style):
    textSurface = style.render(message,True,navy_blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    TextSurf, TextRect = text_objects(text,font)
    TextRect.center = ((display_width//2, display_height//2))
    DISPLAY.blit(TextSurf,TextRect)

def win1(start,score_1,score_2,time1,time2,speed_counter1,speed_counter2):
    time1=timeit.default_timer()-start
    message_display("To Infinty and Beyond!")
    pygame.display.flip()
    time.sleep(2)
    speed_counter1+=2
    win_1=True
    game_loop2(score_1,score_2,time1,time2,speed_counter1,speed_counter2)

def crash1(start,score_1,score_2,time1,time2,speed_counter1,speed_counter2):
    time1=timeit.default_timer()-start
    message_display("Press F for respect!")
    pygame.display.flip()
    time.sleep(2)
    game_loop2(score_1,score_2,time1,time2,speed_counter1,speed_counter2)


def win2(start,score_1,score_2,time1,time2,speed_counter1,speed_counter2):
    time2=timeit.default_timer()-start
    pygame.display.flip()
    time.sleep(1)
    speed_counter2+=2
    win_2=True
    if win_1 and time1<time2:
        message_display("Player 1 won!")
    else:
        message_display("Player 2 won!")
    pygame.display.flip()
    time.sleep(1)
    game_loop1(0,0,0,0,speed_counter1,speed_counter2)

def crash2(start,score_1,score_2,time1,time2,speed_counter1,speed_counter2):
    time2=timeit.default_timer()-start
    # message_display("Press F for respect!")
    pygame.display.flip()
    time.sleep(1)
    if not win_1:
        if score_1 > score_2:
            message_display("Player 1 won!")
           
        elif score_2 > score_1:
            message_display("Player 2 won!")
           
        elif time1 > time2:
            message_display("Player 2 won!")
           
        else:
            message_display("Player 1 won!")
            
    else:
        message_display("Player 1 won!")
    pygame.display.flip()
    time.sleep(1)
    game_loop1(0,0,0,0,speed_counter1,speed_counter2)

######################################################################################################################################
#Collision

def collide(x,y,speed,dynamic_x):
    dynamic_x += 33
    for i,j in static_obstacle_arr:
        if i-cursor_width+5<x<i+static_obstacle_width+11 and j-26<y<j+148:
            return True
            
    for i in range(0,17,4):
        if dynamic_x-cursor_width<x<dynamic_x+dynamic_obstacle_width and ((i+1.67)*display_height/21)-cursor_height<y<((i+1.67)*display_height/21)+dynamic_obstacle_height:
            return True
           
    return False


def score_display(player_score,player):
    TextSurf, TextRect = text_objects("Score"+str(player)+": "+str(player_score),SCORE_FONT)
    TextRect.center = ((70,25))
    DISPLAY.blit(TextSurf,TextRect)
    pygame.display.flip()

#########################################################################################################################################
#GAME LOOPS

def game_loop2(score_1,score_2,time1,time2,speed_counter1,speed_counter2):
    x = (display_width*0.5)
    y = -50
    x_change = 0
    y_change = 0
    speed=0
    crashed = False
    while not crashed:
        background()
        start = timeit.default_timer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a :
                    x_change = -3
                elif event.key == pygame.K_d :
                    x_change = 3
                   
                elif event.key == pygame.K_w:
                    y_change = -2
                elif event.key == pygame.K_s:
                    y_change = 4
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
                   
        speed+=speed_counter2
        x += x_change
        if x<left:x=left
        if x>right:x=right
        y += y_change
        if y<up:y=up
        if y>down:y=down

        dynamic_x = dynamic_obstacles(speed)
        static_obstacles() 
        player2(x,y)
        score_2=max(score(x,y,True),score_2)
        score_display(score_2,2)
        if collide(x,y,speed,dynamic_x):
            crash2(start,score_1,score_2,time1,time2,speed_counter1,speed_counter2)
            
        elif y == down:
            win2(start,score_1,score_2,time1,time2,speed_counter1,speed_counter2)
           
        pygame.display.update()
        clock.tick(60)


def game_loop1(score_1,score_2,time1,time2,speed_counter1,speed_counter2):
    x = (display_width * 0.5)
    y = (display_height * 0.89)
    x_change = 0
    y_change = 0
    win_1=False
    win_2=False
    speed=0
    crashed = False
    while not crashed:
        background()
        start = timeit.default_timer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    x_change = -3
                    
                elif event.key == pygame.K_RIGHT :
                    x_change = 3
                elif event.key == pygame.K_UP:
                    y_change = -4
                   
                elif event.key == pygame.K_DOWN:
                    y_change = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        speed+=speed_counter1
        x += x_change
        if x<left:x=left
        if x>right:x=right
        y += y_change
        if y<up:y=up
        if y>down:y=down

        dynamic_x=dynamic_obstacles(speed)
        static_obstacles()
        score_1=max(score(x,y,False),score_1)
        player1(x,y)
        score_display(score_1,1)
        if collide(x,y,speed,dynamic_x):
            crash1(start,score_1,score_2,time1,time2,speed_counter1,speed_counter2)
        elif y<=up:
            win1(start,score_1,score_2,time1,time2,speed_counter1,speed_counter2) 
        pygame.display.update()
        clock.tick(60)


def score(x,y,v):
    if v:
        if y>783:return 70
        if y>647:return 60
        if y>530:return 55
        if y>472:return 45
        if y>356:return 40
        if y>188:return 30
        if y>132:return 25
        if y>126:return 15
        if y>18:return 10
    else:
        if y<76:return 70
        if y<121:return 60
        if y<249:return 55
        if y<289:return 45
        if y<415:return 40
        if y<461:return 30
        if y<589:return 25
        if y<635:return 15
        if y<759:return 10
    return 0

def score2(x,y,v):
    if v:
        if y>783:return 70
        if y>647:return 60
        if y>530:return 55
        if y>472:return 45
        if y>356:return 40
        if y>188:return 30
        if y>132:return 25
        if y>126:return 15
        if y>18:return 10
    else:
        if y<76:return 70
        if y<121:return 60
        if y<249:return 55
        if y<289:return 45
        if y<415:return 40
        if y<461:return 30
        if y<589:return 25
        if y<635:return 15
        if y<759:return 10
    return 0

game_loop1(0,0,0,0,2,2)
sys.exit()