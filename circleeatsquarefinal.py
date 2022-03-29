#MAria I SUarez
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
#initialize pygame
import os, random, time, pygame, math
from pickle import TRUE

from circleeatsquare import mainmenu
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30
MAIN=TRUE
INST=False
SETT=False
LEV_I=False
#List f messages
MenuList=['Instructions','Settings', " ssfsdf","dasdas",'fdgdfg','asdasd','asdasd']
SettingList=['Screen Size','Font Size','C','BC']
check=True #for the while loop
move=5 #pixels
#square variables
xs=20
ys=20
wbox=30
hbox=30
#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)

#inscribed Square:
ibox=int(rad*math.sqrt(2))
startpoint = (int(xc-ibox/2),int(yc-ibox/2))
print(startpoint[0]-ibox,startpoint[1])
insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
#creating the rect object
square=pygame.Rect(xs,ys,wbox,hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors= {'light blue':[142,216,253],'baby blue':[104,159,203],'white':[255, 255, 255], 'orange':[255, 85, 0], 'purple': [48, 25, 52],
'navy': [5,31,64], 'pink':[200, 3, 75], 'black':[0,0,0]}

#Get colors
background= colors.get('black')
randColor=''
cr_color=colors.get('black')
sqM_color=colors.get('light blue')

#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)

#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (104,159,203))
    screen.fill((0,0,0))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))

#Create First button


#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#This is a function uses a parameter
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(255,111,246))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)

def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False

#sq_color=colors.get('navy')
#Making a rand c f the square
changeColor()
sq_color=colors.get(randColor)


def instructions():
    global instructions, keys, instructions1
    instructions1 = ['so basically, this is a two player game in which', 'one person is the circle and the other person is the square', 'and the circle is trying to eat the square by tagging it', '']
    check = True
    while check:
        instructions = INST_FNT.render("so basically...", 1, (149, 206, 255))
        screen.blit(instructions,(120,120))
        instructions = INST_FNT.render("this is a two player game in which", 1, (149, 206, 255))
        screen.blit(instructions,(120,160))
        instructions = INST_FNT.render("one person is the circle and the other person is the square.", 1, (149, 206, 255))
        screen.blit(instructions,(120,180))
        instructions = INST_FNT.render('and the circle is trying to eat the sqaure by tagging it', 1, (149, 206, 255))
        screen.blit(instructions,(120,200))
        instructions = INST_FNT.render(' ', 1, (149, 206, 255))
        screen.blit(instructions,(120,220))
        instructions = INST_FNT.render('CONTROLS FOR SQUARE:', 1, (227, 111, 255))
        screen.blit(instructions,(120,250))
        instructions = INST_FNT.render('W - up', 1, (149, 206, 255))
        screen.blit(instructions,(120,270))
        instructions = INST_FNT.render('S - down', 1, (149, 206, 255))
        screen.blit(instructions,(120,290))
        instructions = INST_FNT.render('A - left', 1, (149, 206, 255))
        screen.blit(instructions,(120,310))
        instructions = INST_FNT.render('D - right', 1, (149, 206, 255))
        screen.blit(instructions,(120,330))
        instructions = INST_FNT.render('CONTROLS FOR CIRCLE:', 1, (227, 111, 255))
        screen.blit(instructions,(120,370))
        instructions = INST_FNT.render('up arrow (^) - up', 1, (149, 206, 255))
        screen.blit(instructions,(120,390))
        instructions = INST_FNT.render('down arrow - down', 1, (149, 206, 255))
        screen.blit(instructions,(120,410))
        instructions = INST_FNT.render('left arrow(<) - left', 1, (149, 206, 255))
        screen.blit(instructions,(120,430))
        instructions = INST_FNT.render('right arrow(>) - right', 1, (149, 206, 255))
        screen.blit(instructions,(120,450))
        instructions = INST_FNT.render('circle.... try to to get square!!', 1, (227, 111, 255))
        screen.blit(instructions,(120,540))
        instructions = INST_FNT.render('back [< left arrow]', 1, (255, 255, 255))
        screen.blit(instructions,(50,600))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                mainmenu()
        for case in pygame.event.get():
                    if case.type == pygame.QUIT:
                        quit()
        pygame.display.update()
        pygame.time.delay(10)

MAX=10
jumpCount=MAX
JUMP=False

def playgameyuh():
    while check:
        if MAIN:
            screen.fill(background)
            TitleMenu("MENU")
            MainMenu(MenuList)
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                check=False

        keys=pygame.key.get_pressed() #this returns a list
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            print(mouse_pos)
            if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INST :
                MAIN=False
                # screen.fill(background)
                instructions()
                # TitleMenu("INSTRUCTIONS")
                INST=True
                pygame.display.update()

        if keys[pygame.K_a] and square.x >=move:
            square.x -= move #substract 5 from the x value
        if keys[pygame.K_d] and square.x <WIDTH-wbox:
            square.x += move  
        #Jumping part
        if not JUMP:
            if keys[pygame.K_w]:
                square.y -= move
            if keys[pygame.K_s]:
                square.y += move   
            if keys[pygame.K_SPACE]:
                JUMP=True
        else:
            if jumpCount >=-MAX:
                square.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False

    #Finish circle
        if keys[pygame.K_LEFT] and xc >=rad+move:
            xc -= move #substract 5 from the x value
            insSquare.x -= move
        if keys[pygame.K_RIGHT] and xc <=WIDTH -(rad+move):
            xc += move #substract 5 from the x value  
            insSquare.x += move
        if keys[pygame.K_DOWN] and yc <=HEIGHT-(rad+move):
            yc += move #substract 5 from the x value
            insSquare.y += move
        if keys[pygame.K_UP] and yc >=rad+move:
            yc -= move #substract 5 from the x value  
            insSquare.y -= move
            
        checkCollide = square.colliderect(insSquare)
        if checkCollide:
            square.x=random.randint(wbox, WIDTH-wbox)
            square.y=random.randint(hbox, HEIGHT-hbox)   
            changeColor()
            sq_color=colors.get(randColor)
            rad +=move
            ibox=int(rad*math.sqrt(2))
            startpoint = (int(xc-ibox/2),int(yc-ibox/2))
            insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
            
        
        pygame.draw.rect(screen, sq_color, square)
        pygame.draw.rect(screen,cr_color, insSquare )
        pygame.draw.circle(screen, cr_color, (xc,yc), rad)

        pygame.display.update()
        pygame.time.delay(10)

playgameyuh()