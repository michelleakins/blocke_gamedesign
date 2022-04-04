#michelle akins
#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square,
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump

#C:\Users\AkinsM25\.vscode\blocke_gamedesign-1\circleeatsquaregame\yuhyuh.py

#initialize pygame
import os, random, time, pygame, math, datetime
os.system('cls')
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
TITLE_FONT=pygame.font.SysFont('georgia',50) #<-- First pice of text within parenthsis is the name of the font, and the number is the height of the letters
MENU_FONT=pygame.font.SysFont('comicsans',40)
INSTRUCTION_FONT=pygame.font.SysFont('proxmanova',35)

#scree size
WIDTH=700
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('final proj')
bg = pygame.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\\bacroung image.jpg')
chart = pygame.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L1.png')
screen.blit(chart, (300,300))
screen.blit(bg, (0,0))
pygame.display.update()
pygame.time.delay(3000)

for case in pygame.event.get():
    if case.type==pygame.QUIT:
        check=False

move = 5
keys=pygame.key.get_pressed() #<-- To check if a key gets pressed (classified as a list), the 'and move' part has to do with creating boundries
        # Movements for the square
if keys[pygame.K_a]:
    chart.x-=move #subtract
if keys[pygame.K_d]:
    chart.x+=move
if keys[pygame.K_w]:
    chart.y -= move
