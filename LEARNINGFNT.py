#michelle akins
#3-23-22

#main menu for game and creating funtions

import pygame, time
pygame.init()
#variable

WIDTH = 700
HEIGHT = 700

#SCREEN
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('MAIN MENU')

#get colors
colors= {'light blue':[104,100,253],'baby blue':[104,159,203],'white':[255, 255, 255], 'orange':[255, 85, 0], 'purple': [48, 25, 52], 'navy': [5,31,64], 'pink':[200, 3, 75]}
background = colors.get('baby blue')
cr_color = colors.get('light blue')
randColor=''

TITLE_FNT= pygame.font.SysFont('helvetica', 80)
MENU_FNT = pygame.font.SysFont('helvetica', 40)
INS_FNT = pygame.font.SysFont('helvetica', 25)

# text = INS_FNT.render("Write y", 1, (0,255,0))
# wind.blit(text(220,220))

menulist = ["instructions", "settings", "levelselect", "scoreboard", "exit"]
#create square for menu
wb= 30
hb = 30
xs=75
ys=100
square = pygame.Rect(xs, ys, wb, hb)
sq_color = colors.get('light blue')
for i in range(7):
    pygame.draw.rect(screen, sq_color, square)
    square.y += 50

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
    global menu, keys, check, xt, ty
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

        ty = 243
        text = TITLE_FNT.render('$*:...welcome to circle eats square game!!!...:*$', 1, (220, 240, 240))
        screen.fill((0,0,0))
        screen.blit(text,(120,50))
        #x value= WIDTH/2 - wText/2
        xt=WIDTH/2-text.get_width
        #create first button
        message = menulist[i]
        menu = MENU_FNT.render(message, 1, (227,111,255))
        screen.blit(menu, (100,100))
        pygame.draw.rect(screen, sq_color, square)

        menu = MENU_FNT.render("- settings", 1, (255,137,236))
        screen.blit(menu, (100,150))
        menu = MENU_FNT.render("- level select", 1, (137,156,255))
        screen.blit(menu, (100,200))
        menu = MENU_FNT.render("- score board", 1, (137,212,255))
        screen.blit(menu, (100,250))
        menu = MENU_FNT.render("- exit game", 1, (137,255,200))
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

pygame.display.update()
pygame.time.delay(100000000)

mainmenu()