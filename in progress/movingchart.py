import os, time, random,math
from re import I
from shutil import move
import pygame as p

#initialize pygame
p.init()

WIDTH = 500
HEIGHT = 500
win = p.display.set_mode((WIDTH,HEIGHT))
p.display.set_caption("first game")

walkRight = [p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L9.png')]
char = p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\standing.png')
bg=p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\\bacroung image.jpg')

x = 50
y = 425
width = 64
height = 64
move = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redrawgamewindow():
    global walkCount
    win.blit(bg, (0,0))
    # win.blit(rip, (width-100, height-75))
    if walkCount + 1 > 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))

    p.display.update()

check = True
def death():
    global keys, check
    for case in p.event.get():
        if case.type==p.QUIT:
            check=False
    keys=p.key.get_pressed() #this returns a list
    if case.type ==p.MOUSEBUTTONDOWN:
        mouse_pos=p.mouse.get_pos()
        print(mouse_pos)
    
    # if ((mouse_pos[0] >100 and mouse_pos[0] <130) and (mouse_pos[1] >350 and mouse_pos[1] <380)):

clock = p.time.Clock()
MAX = 15
#mainloop
run = True
while run:
    clock.tick(27)
    redrawgamewindow()
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    keys = p.key.get_pressed()
    if keys[p.K_LEFT] and x >= -14:
        x -= move
        left = True
        right = False
    elif keys[p.K_RIGHT] and x < WIDTH - 50:
        x += move
        right = True
        left = False
    else:
        left = False
        right = False
        walkCount = 0

    #jumping
    if not (isJump):
        if keys[p.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -MAX:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= jumpCount*abs(jumpCount)/1
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = MAX
    
    for case in p.event.get():
        if case.type==p.QUIT:
            check=False
    
    # if (character position > 300) and (char pos < then 450):
    #       win.blit(char)
p.quit()
