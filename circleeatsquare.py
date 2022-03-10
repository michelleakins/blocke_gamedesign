#michelle akins
#learning to draw circles and squares
#learning how to use keys to move objects
#learn about dictionary

#objective of the game: the rectangle to run away from the circle. if they collide the circle eats the square
#circle will get larger and new rectangle should appear somewhere on the screen

import os, random, time, pygame
os.system('cls')
#initialize pygame
pygame.init()

#declare constants, variables, init, dictionaries
#suare size
WIDTH = 700
HEIGHT = 500
check = True #for the while loop
move = 5 #5 pixels
#square variables
xs = 20
ys = 20
wbox = 30
hbox = 30
#circle variables
radius = 15
xc = random.randint(15, WIDTH-radius)
yc = random.randint(15, HEIGHT-radius)
#square
square = pygame.Rect(xs, ys, wbox, hbox)
#screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('cirlce eats square')
#define colors
colors= {'white':[255,255,255],'red':[255,0,0],'blueish':[102, 153, 255], 'orange':[255, 85, 0], 'purple': [48, 25, 52], 'navy': [5,31,64], 'pink':[200, 3, 75]}

background = colors.get('pink')
sq_color = colors.get('navy')
cr_color = colors.get('white')

while check:
    # pygame.draw.circle(screen, cr_color, (xc, yc), radius)
    screen.fill(background)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            check = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and square.x >= move:
        square.x -= move #subtract 5 from the x value
    if keys[pygame.K_d] and square.x < WIDTH - wbox:
        square.x += move 
    if keys[pygame.K_w] and square.y >= move:
        square.y -= move
    if keys[pygame.K_s] and square.y < HEIGHT - hbox:
        square.y += move
    #finished circle
    if keys[pygame.K_LEFT] and xc >=radius + move:
           xc -= move
    if keys[pygame.K_RIGHT] and xc < WIDTH - (radius +move):
           xc += move
    if keys[pygame.K_UP] and yc >=radius + move:
           yc -= move
    if keys[pygame.K_DOWN] and yc < HEIGHT - (radius + move):
           yc += move

    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc, yc), radius)
    pygame.display.update()
    pygame.time.delay(10)

    #  if xc and yc is equal to the position of the square, then end the game with "CIRCLE ATE SQUARE"