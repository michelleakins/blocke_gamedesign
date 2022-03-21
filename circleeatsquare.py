#michelle akins
#learning to draw circles and squares
#learning how to use keys to move objects
#learn about dictionary

#objective of the game: the rectangle to run away from the circle. if they collide the circle eats the square
#circle will get larger and new rectangle should appear somewhere on the screen

#  K_SPACE FOR JUMP


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
colors= {'light blue':[104,100,253],'baby blue':[104,159,203],'white':[255, 255, 255], 'orange':[255, 85, 0], 'purple': [48, 25, 52], 'navy': [5,31,64], 'pink':[200, 3, 75]}

background = colors.get('baby blue')
sq_color = colors.get('white')
cr_color = colors.get('light blue')

fontsize = 12
coordx = 25
coordy = 26
# def writeText(screen, coordx, coordy, fontsize):
#   	#set the font to write with
#     font = pygame.font.Font('freesansbold.ttf', fontsize) 
#     #(0, 0, 0) is black, to make black text
#     text = font.render(screen, True, (0, 0, 0))
#     #get the rect of the text
#     textRect = text.get_rect()
#     #set the position of the text
#     textRect.center = (coordx, coordy)
#     #add text to window
#     screen.blit(text, textRect)
#     #update window
#     pygame.display.update()

MAX = 10
jumpcount = 10
JUMP = False
while check:
    # writeText()
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
    #jumping part
    if not JUMP:
        if keys[pygame.K_w] and square.y >= move:
            square.y -= move
        if keys[pygame.K_s] and square.y < HEIGHT - hbox:
            square.y += move
        if keys[pygame.K_SPACE]:
            JUMP = True
    else:
        if jumpcount >= -MAX:
            square.y -= jumpcount*abs(jumpcount)/2
            jumpcount -= 1
        else:
            jumpcount = MAX
            JUMP = False
    #finished circle
    if keys[pygame.K_LEFT] and xc >=radius + move:
           xc -= move
    if keys[pygame.K_RIGHT] and xc < WIDTH - (radius +move):
           xc += move
    if keys[pygame.K_UP] and yc >=radius + move:
           yc -= move
    if keys[pygame.K_DOWN] and yc < HEIGHT - (radius + move):
           yc += move

    checkcollide = square.collidepoint((xc, yc,))

    if checkcollide:
        square.x = random.randint(wbox, WIDTH-radius)
        square.y = random.randint(hbox, HEIGHT-radius)
        radius += move
    if radius > 200:
        quit()
    # if pos(square.x) == pos(square.y):
    #     print("CIRCLE ATE SQUARE")
    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc, yc), radius)
    pygame.display.update()
    pygame.time.delay(10)