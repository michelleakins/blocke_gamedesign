#michelle akins
#learning to draw circles and squares
#learning how to use keys to move objects
#learn about dictionary

#objective of the game: the rectangle to run away from the circle. if they collide the circle eats the square
#circle will get larger and new rectangle should appear somewhere on the screen

#settings: screen size, color of circle, background color, circle color, sound on/off

import os, random, time, pygame
os.system('cls')
#initialize pygame
pygame.init()

#declare constants, variables, init, dictionaries
#suare size
WIDTH = 700
HEIGHT = 700
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

randColor = random.choice(list(colors))

TITLE_FNT = pygame.font.SysFont('hellvetica', 28)
MENU_FNT = pygame.font.SysFont('helvetica', 40)
SETTINGS_FNT = pygame.font.SysFont('helvetica',25 )
SCOREBOARD_FNT = pygame.font.SysFont('helvetica',25 )
LVL_FNT = pygame.font.SysFont('helvetica',25 )
INS_FNT = pygame.font.SysFont('helvetica', 25)

sq_color = colors.get(randColor)

fontsize = 12
coordx = 25
coordy = 26

background = colors.get('baby blue')
cr_color = colors.get('light blue')

MAX = 10
jumpcount = 10
JUMP = False

#square size
wb= 20
hb = 20
xs=75
ys=117
square = pygame.Rect(xs, ys, wb, hb)
sq_color = colors.get('light blue')
pygame.draw.rect(screen, sq_color, square)

def instructions():
    global instructions, keys
    check = True
    while check:
        instructions = INS_FNT.render("so basically...", 1, (149, 206, 255))
        screen.blit(instructions,(120,120))
        instructions = INS_FNT.render("this is a two player game in which", 1, (149, 206, 255))
        screen.blit(instructions,(120,160))
        instructions = INS_FNT.render("one person is the circle and the other person is the square.", 1, (149, 206, 255))
        screen.blit(instructions,(120,180))
        instructions = INS_FNT.render('and the circle is trying to eat the sqaure by tagging it', 1, (149, 206, 255))
        screen.blit(instructions,(120,200))
        instructions = INS_FNT.render(' ', 1, (149, 206, 255))
        screen.blit(instructions,(120,220))
        instructions = INS_FNT.render('CONTROLS FOR SQUARE:', 1, (227, 111, 255))
        screen.blit(instructions,(120,250))
        instructions = INS_FNT.render('W - up', 1, (149, 206, 255))
        screen.blit(instructions,(120,270))
        instructions = INS_FNT.render('S - down', 1, (149, 206, 255))
        screen.blit(instructions,(120,290))
        instructions = INS_FNT.render('A - left', 1, (149, 206, 255))
        screen.blit(instructions,(120,310))
        instructions = INS_FNT.render('D - right', 1, (149, 206, 255))
        screen.blit(instructions,(120,330))
        instructions = INS_FNT.render('CONTROLS FOR CIRCLE:', 1, (227, 111, 255))
        screen.blit(instructions,(120,370))
        instructions = INS_FNT.render('up arrow (^) - up', 1, (149, 206, 255))
        screen.blit(instructions,(120,390))
        instructions = INS_FNT.render('down arrow - down', 1, (149, 206, 255))
        screen.blit(instructions,(120,410))
        instructions = INS_FNT.render('left arrow(<) - left', 1, (149, 206, 255))
        screen.blit(instructions,(120,430))
        instructions = INS_FNT.render('right arrow(>) - right', 1, (149, 206, 255))
        screen.blit(instructions,(120,450))
        instructions = INS_FNT.render('circle.... try to to get square!!', 1, (227, 111, 255))
        screen.blit(instructions,(120,540))
        instructions = INS_FNT.render('back [< left arrow]', 1, (255, 255, 255))
        screen.blit(instructions,(50,600))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                mainmenu()
        for case in pygame.event.get():
                    if case.type == pygame.QUIT:
                        quit()
        pygame.display.update()
        pygame.time.delay(10)

def mainmenu():
    global menu, keys, check,xt, square, sq_color, i
    check = True
    while check:
        for case in pygame.event.get():
            if case.type == pygame.QUIT:
                check = False
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            screen.fill((0,0,0))
            instructions()            
            check = False
        #create square for menu
        square = pygame.Rect(xs, ys, wb, hb)
        sq_color = colors.get('light blue')
        text = TITLE_FNT.render('$*:...welcome to circle eats square game!!!...:*$', 1, (220, 240, 240))
        screen.fill((0,0,0))
        screen.blit(text,(120,50))
        pygame.draw.rect(screen, sq_color, square)
        menuList=['INSTRUCTIONS',"SETTINGS","LEVEL 1","LEVEL 2", "LEVEL 3",'Scoreboard','Exit']
        for i in range(5):
            pygame.draw.rect(screen, sq_color, square)
            square.y += 50

        menu = MENU_FNT.render("instructions[space bar]", 1, (227,111,255))
        screen.blit(menu, (100,100))

        menu = MENU_FNT.render("settings", 1, (255,137,236))
        screen.blit(menu, (100,150))
        menu = MENU_FNT.render("level select", 1, (137,156,255))
        screen.blit(menu, (100,200))
        menu = MENU_FNT.render("score board", 1, (137,212,255))
        screen.blit(menu, (100,250))
        menu = MENU_FNT.render("exit game", 1, (137,255,200))
        screen.blit(menu, (100,300))

        menu = MENU_FNT.render("   ___          ___", 1, (255,255,255))
        screen.blit(menu, (192,420))
        menu = MENU_FNT.render("   /       \___/        \ ", 1, (255,255,255))
        screen.blit(menu, (180,460))
        menu = MENU_FNT.render("|                        |", 1, (255,255,255))
        screen.blit(menu, (200,480))
        menu = MENU_FNT.render("\                       /", 1, (255,255,255))
        screen.blit(menu, (200,500))
        menu = MENU_FNT.render("  \                   /", 1, (255,255,255))
        screen.blit(menu, (200,520))
        menu = MENU_FNT.render("    \               /", 1, (255,255,255))
        screen.blit(menu, (200,540))
        menu = MENU_FNT.render("      \           /", 1, (255,255,255))
        screen.blit(menu, (200,560))
        menu = MENU_FNT.render("        \       /", 1, (255,255,255))
        screen.blit(menu, (200,580))
        menu = MENU_FNT.render("          \   /", 1, (255,255,255))
        screen.blit(menu, (200,600))
        menu = MENU_FNT.render("            \/", 1, (255,255,255))
        screen.blit(menu, (200,620))
    
        pygame.display.update()
    
        pygame.time.delay(10)

mainmenu()

def changecolor():
    global randColor
    colorcheck = True
    while colorcheck:
        randColor = random.choice(list(colors))
        if colors.get(randColor) == background:
            print(randColor)
            print(background)
            randColor = random.choice(list(colors))
        else:
            colorcheck = False


check = True
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
        changecolor()
        radius += move
    if radius > 200:
        quit()
    # if pos(square.x) == pos(square.y):
    #     print("CIRCLE ATE SQUARE")
    pygame.draw.rect(screen, sq_color, square)
    pygame.draw.circle(screen, cr_color, (xc, yc), radius)
    pygame.display.update()
    pygame.time.delay(10)

