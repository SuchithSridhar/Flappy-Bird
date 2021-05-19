'''Author : Suchith Sridhar
Last edited : 2018/09/07
Clean up on: 2021/05/19
Python Version coded with : 3.6 x64bit
program : Flappy Bird Game'''

#READ !!!!

import pygame
import time
import random
import os
import sys


pygame.init()

speed = 8
bird_speed = 1
bird_speed_up = -9
bird_velocity = 0

dirs = os.getcwd()
dirs = os.path.join(dirs, 'res')
os.chdir(dirs)
sys.path.append(dirs)

#SOUNDS-------

sound = pygame.mixer.Sound("sound_file.wav")
# pygame.mixer.music.load("jazz.wav")
# but does not play it--

# pygame.mixer.music.play(x)
# where x is the number of times it loops
# if x == -1 , it just keeps playing

# pygame.mixer.music.pause()
# pygame.mixer.music.unpause()
# pygame.mixer.music.stop()

dirs = os.path.join(dirs, 'game_images')
os.chdir(dirs)
sys.path.append(dirs)


dis_width = 800
dis_height = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bg_blue = (153,217,234)
crashed  = False

pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load("bird.png")
pygame.display.set_icon(icon)
gameDisplay = pygame.display.set_mode((dis_width,dis_height))



clock = pygame.time.Clock()

def background():
    x, y = 0, 0
    img = pygame.image.load('background.png')
    gameDisplay.blit(img,(x,y))

##    gameDisplay.fill(bg_blue)
    

def text_objects(text, font):
    textSurface = font.render(text, True, red)  # Renders font from pygame
                                                # True just has to stay True (RULE)

    return textSurface , textSurface.get_rect()  # A pygame / python function ()

def things_dodged(count):
    
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:"+str(count), True, black)
    gameDisplay.blit(text, (0,0))


def message_display(text):
    Ltext = pygame.font.Font("freesansbold.ttf", 90)
    textSurf , textRect = text_objects(text, Ltext)

    textRect.center = ((dis_width/2), (dis_height/2))

    gameDisplay.blit(textSurf , textRect)
    pygame.display.update()

    time.sleep(2)

    
def crashed_true():

    message_display('GAME OVER')
    intro()


def wall_dim(wall_choice):

    space = 0
    wall_up_height = 0
    wall_down_height = 0

    if wall_choice == 14:
        wall_up_height = 100
        wall_down_height = 400
        space = wall_up_height + wall_down_height - 600

    elif wall_choice == 13:
        wall_up_height = 100
        wall_down_height = 300
        space = wall_up_height + wall_down_height - 600

    elif wall_choice == 12:
        wall_up_height = 100
        wall_down_height = 200
        space = wall_up_height + wall_down_height - 600

    elif wall_choice == 11:
        wall_up_height = 100
        wall_down_height = 100
        space = wall_up_height + wall_down_height - 600

    elif wall_choice == 41:
        wall_up_height = 400
        wall_down_height = 100
        space = wall_up_height + wall_down_height - 600

    elif wall_choice == 31:
        wall_up_height = 300
        wall_down_height = 100
        space = wall_up_height + wall_down_height - 600

    elif wall_choice == 21:
        wall_up_height = 200
        wall_down_height = 100
        space = wall_up_height + wall_down_height - 600

    elif wall_choice == 22:
        wall_up_height = 200
        wall_down_height = 200
        space = wall_up_height + wall_down_height - 600

    elif wall_choice == 23:
        wall_up_height = 200
        wall_down_height = 300
        space = wall_up_height + wall_down_height - 600

    elif wall_choice == 32:
        wall_up_height = 300
        wall_down_height = 200
        space = wall_up_height + wall_down_height - 600



    if space < 0:
        space = space * -1

    if wall_up_height + wall_down_height + space != 600:
        print("Error")
        print(wall_up_height, wall_down_height, space)
        time.sleep(10)

    return wall_up_height, wall_down_height, space


def collision_check(x_bird, y_bird, x_wall, dis_height, crashed, wall_choice):

    if (y_bird < 0 ) or (y_bird + 30 > dis_height) :
        crashed = True
        # print("Crashed up or down")
        # This is for the bird not leaving the screen

    wall_up_height, wall_down_height, space = wall_dim(wall_choice)

    y_wall_up = 0
    x_wall_up = x_wall
    y_wall_down = y_wall_up + wall_up_height + space
    x_wall_down = x_wall_up
    wall_width = 100
    bird_width, bird_height = 30, 30

    c1 = (x_bird > x_wall) and (x_bird < (x_wall + wall_width))
    c2 = ((x_bird+bird_width) > x_wall) and ((x_bird+bird_width) < (x_wall + wall_width))
    c3 = (y_bird < (y_wall_up+wall_up_height))
    c4 = (y_bird+ bird_height > (y_wall_down))

    if (c1 and c3) or (c2 and c3):
        # print("crashed into upper wall")
        crashed = True

    if (c1 and c4) or (c2 and c4):
        # print("Crashed into lower wall")
        crashed = True

    

    return crashed


def random_wall():
    wall_h = [14,41,32,23]
    wall_m = [13,31,22]
    wall_e = [12,21]
    wall_d = [11]

    walls = wall_h + wall_m + wall_m +wall_m + wall_e + wall_d
    wall_choice = random.choice(walls)
    
    return wall_choice

def wall(x,wall_choice):
    y = 0
    img = pygame.image.load(str(wall_choice)+'.png')
    gameDisplay.blit(img,(x,y))


def bird(x,y):
    img = pygame.image.load('bird.png')
    gameDisplay.blit(img,(x,y))

def intro():
    
    x, y = 0, 0
    img = pygame.image.load('intro_bg.png')
    gameDisplay.blit(img,(x,y))
    
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            gameloop(dis_width, dis_height, speed, bird_speed, bird_speed_up)



def gameloop(dis_width, dis_height, speed, bird_speed, bird_speed_up):

    global bird_velocity

    x_wall = 1000
    x_wall2 = 1300
    x_wall3 = 1600
    x_wall4 = 1900
    opened = True
    crashed = False
    count = 0
    x_wall_check = True
    x_wall2_check = True
    x_wall3_check = True
    x_wall4_check = True
    

    x_bird = dis_width/2
    y_bird = dis_height/2


    while opened:

        for event in pygame.event.get():
            # Pressing / Clicking / any mouse movement

            if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE):

                pygame.quit()
                quit()
                # The x at the top right hand corner

                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(sound)
                    bird_velocity = bird_speed_up

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bird_speed = 0.75


            

        bird_velocity += bird_speed            
        y_bird = y_bird + bird_velocity

        background()
        
        #gameDisplay.fill(white)
        #Faster gameplay but less beautiful



        if x_wall == 1000:
            wall_choice = random_wall()

        if x_wall2 == 1300 or x_wall2 == 1000:
            wall_choice2 = random_wall()

        if x_wall3 == 1600 or x_wall3 == 1000:
            wall_choice3 = random_wall()

        if x_wall4 == 1900 or x_wall4 == 1000:
            wall_choice4 = random_wall()

        wall(x_wall,wall_choice)
        wall(x_wall2,wall_choice2)
        wall(x_wall3,wall_choice3)
        wall(x_wall4,wall_choice4)

        #Collision ---
        crashed = collision_check(x_bird, y_bird, x_wall, dis_height, crashed, wall_choice)
        crashed = collision_check(x_bird, y_bird, x_wall2, dis_height, crashed, wall_choice2)
        crashed = collision_check(x_bird, y_bird, x_wall3, dis_height, crashed, wall_choice3)
        crashed = collision_check(x_bird, y_bird, x_wall4, dis_height, crashed, wall_choice4)

        x_wall -= speed
        x_wall2 -= speed
        x_wall3 -= speed
        x_wall4 -= speed

        if x_wall_check:
            if x_bird>x_wall+100:
                count += 1
                x_wall_check = False
        if x_wall2_check:
            if x_bird>x_wall2+100:
                count += 1
                x_wall2_check = False
        if x_wall3_check:
            if x_bird>x_wall3+100:
                count += 1
                x_wall3_check = False
        if x_wall4_check:
            if x_bird>x_wall4+100:
                count += 1
                x_wall4_check = False
            
        

        if x_wall < -199 :
            x_wall = 1000
            x_wall_check = True

        if x_wall2 < -199 :
            x_wall2 = 1000
            x_wall2_check = True

        if x_wall3 < -199 :
            x_wall3 = 1000
            x_wall2_check = True

        if x_wall4 < -199 :
            x_wall4 = 1000
            x_wall2_check = True



        bird(x_bird, y_bird)
        things_dodged(count)

        if crashed:
            crashed_true()

        pygame.display.update()

        clock.tick(30)


intro()

        

        






