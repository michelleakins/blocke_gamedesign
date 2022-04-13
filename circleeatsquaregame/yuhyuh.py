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
name = input("what is your name?")
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
TITLE_FONT=pygame.font.SysFont('georgia',50) #<-- First pice of text within parenthsis is the name of the font, and the number is the height of the letters
MENU_FONT=pygame.font.SysFont('comicsans',40)
INSTRUCTION_FONT=pygame.font.SysFont('proxmanova',35)

#scree size
WIDTH=700
HEIGHT=700
WIDTH2 = 750
HEIGHT2= 750
WIDTH3 = 800
HEIGHT3 = 800
xMs=50
yMs=250
wb=30
hb=30
score = 0
#true/false for going to diff pages
MAIN=True
INST=False
SETT=False
GAME=False
LEV_I=False
EXIT = False
SCORE = False
# menu and setting list for pages 
MenuList=['Instructions','Settings', "Play Game","Exit",'Scoreboard']
SettingList=['Screen Size','Font color','Background Color']
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
screen2=pygame.display.set_mode((WIDTH2,HEIGHT2))
screen3=pygame.display.set_mode((WIDTH3,HEIGHT3))

pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
background_black = {'black':[0,0,0]}

#Get colors
background= background_black.get('black')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('purple')

check=True #<-- For while loop

#create fifferent type
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
WIN_FNT = pygame.font.SysFont('helvetica', 40)

#Create square fr menu
xSett=100
ySett=250
settW=30
SettH=30
squareM=pygame.Rect(xMs,yMs,wb,hb)
squareSet=pygame.Rect(xSett,ySett,settW,SettH)
#This is a function uses a parameter

#VARIABLES FOR COLLIDE, CIRCLE, AND MOVE
HitX=xc-15
HitY=yc-15
CRadius=15
HitLenght=CRadius*2
HitWidth=CRadius*2
hitbox=pygame.Rect(HitX,HitY,HitWidth,HitLenght)
move=5
ColorCheck=False

#random color and false statement for jump and jump count
sq_color=colors.get(randColor)
MAX=10
jumpCount=MAX
JUMP=False
hi = True
def scoreBoard():
    global yi, temp
    myFile=open('classstuffyes\scetxt.txt', 'r')
    yi=150
    stuff=myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=200
    for i in range(N, -1, -1):
        print(stuff[i])
        text=INST_FNT.render(stuff[i],1,(255,255,255))
        screen.blit(text,(20,j))
        j+=50
        pygame.display.update()
        pygame.time.delay(10)
def keepScore(score):
    date=datetime.datetime.now()
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
    #open a file and write in it
    # when y write it erases the prev
    myFile=open('classstuffyes\scetxt.txt','a')
    myFile.write(scoreLine)
    myFile.close()
def changebackground():
    global SETT, MAIN
    while check:
        if ((mouse_pos[0] >100 and mouse_pos[0] <130) and (mouse_pos[1] >350 and mouse_pos[1] <380)):
            screen.fill(0,0,0)
            BackButton=MENU_FONT.render("BACK",1,(255,255,255))
            screen.blit(BackButton,(200,500))
            if ((mouse_pos[0] >200 and mouse_pos[0] <540) and (mouse_pos[1] >500 and mouse_pos[1] <540)):
                    screen.fill(background)
                    SETT=False
                    MAIN=True
                    TitleMenu("MENU")
                    MainMenu(MenuList)
        pygame.display.update()
        pygame.time.delay(100000)
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((0,0,0))
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
def timedatestuff():
    date = datetime.datetime.now()
    score = 200
    print(date.strftime('%m/%d/%Y'))
    scoreline = str(score)+"\t"+name+ "\t"+ date.strftime('%m/%d/%Y'+"\n")
    myfile = open('classstuffyes\scetxt.txt', "r")
    myfile.write(scoreline)
    myfile.close() 
def MainMenu(Mlist):
    global txtx
    global txty
    global squareSet
    global nameprint
    #Create square fr menu
    xSett=100
    ySett=250
    settW=30
    SettH=30
    squareM=pygame.Rect(xMs,yMs,wb,hb)
    squareSet=pygame.Rect(xSett,ySett,settW,SettH)
    txty=243
    txtx=90
    squareM.y=250
    nameprint = MENU_FNT.render(name,1, (255, 0, 0))
    screen.blit(nameprint,(25, 650))
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(txtx,txty))
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
def SettMenu(Mlist):
    global txtS
    global txtSS
    global textlistcolors
    txtS=243
    txtSS=145
    squareSet.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(txtSS,txtS))
        pygame.draw.rect(screen,sqM_color, squareSet )
        squareSet.y +=50
        txtS+=50
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
def playgameyuh():
    global move
    global check
    check = True
    global screen
    global square
    global hitbox
    global c_color
    global background
    global Hit_color
    global s_color
    global jumpCount
    global JUMP
    global CRadius
    CRadius = 5
    global MAX
    global HitLenght
    global HitWidth
    global changeColor
    global HitX
    global HitY
    global ColorCheck
    global xc, yc
    global win
    global MAIN, hi, GAME

    #Create the screen
    pygame.display.set_mode((WIDTH,HEIGHT))

    #Define our colors in a dictionary
    colors={'white':[255,255,255], 'red':[255,0,0], 'orange':[255,85,0], 'purple':[48,25,52,],'pink': [200,3,75], 'black':[0,0,0], 'navy':[5,31,64]}

    #Getting a random color:
    RandColor=random.choice(list(colors))

    while RandColor == 'black':
        RandColor=random.choice(list(colors))

    #Call colors to get colors for our screen and shapes
    background=colors.get('black')
    # s_color=colors.get('navy') <--- Previous square color
    c_color=colors.get('white')
    Hit_color=colors.get('purple')
    # Creating a color check to make sure our colors are all different:

    changeColor()
    s_color=colors.get(RandColor) #<--- Getting a random color for the square


    #make a function for our game
    while check:
        GAME = True
        #Fill the screen and draw the shapes (for testing)
        screen.fill(background)
        #Checking for events in the pygame and allow for key inputs
        #For keys use K_(key value)
        #arrows for circle and wasd for squares
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                check=False
        keys=pygame.key.get_pressed() #<-- To check if a key gets pressed (classified as a list), the 'and move' part has to do with creating boundries
        # Movements for the square
        if keys[pygame.K_a] and square.x>=move:
            square.x-=move #subtract
        if keys[pygame.K_d] and square.x<=WIDTH-(wbox+move):
            square.x+=move
        #Jumping
        if not JUMP:
            if keys[pygame.K_w] and square.y>=move:
                square.y-=move
            if keys[pygame.K_s] and square.y<=HEIGHT-(hbox+move):
                square.y+=move
            if keys[pygame.K_SPACE]:
                JUMP=True
        else:
            if jumpCount>=-MAX:
                square.y-=jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False
        # Circle Movements
        if keys[pygame.K_LEFT] and xc>=move+CRadius:
            xc-=move #subtract
            hitbox.x-=move
        if keys[pygame.K_RIGHT] and xc<=WIDTH-(CRadius+move):
            xc+=move
            hitbox.x+=move
        if keys[pygame.K_UP] and yc>=move+CRadius:
            yc-=move
            hitbox.y-=move
        if keys[pygame.K_DOWN] and yc<=HEIGHT-(CRadius+move):
            yc+=move
            hitbox.y+=move
        #Making the collision
        checkCollide= square.colliderect(hitbox)
        if checkCollide==True:
            square.x=random.randint(wbox,WIDTH-wbox)
            square.y=random.randint(hbox,HEIGHT-hbox)
            CRadius+=move
            changeColor()
            ColorCheck=True
        pygame.draw.rect(screen,s_color,square)
        pygame.draw.rect(screen,Hit_color,hitbox)
        pygame.draw.circle(screen,c_color,(xc,yc),CRadius)
        if CRadius==30:
            mouse_pos=pygame.mouse.get_pos()
            print(mouse_pos)
            screen.fill(background)
            win = WIN_FNT.render("MUY BIEN! you won the game!!", 1, (149, 206, 255))
            screen.blit(win, (100, 350))
            win= WIN_FNT.render("want to play AGAIN?!", 1, (149, 206, 255))
            screen.blit(win,(150, 400))
            win = WIN_FNT.render("yes or no", 1, (149, 206, 255))
            screen.blit(win, (250, 500))
            if ((mouse_pos[0]> 250 and mouse_pos[0] < 300) and (mouse_pos[1]> 510 and mouse_pos[1]< 550)) and case.type ==pygame.MOUSEBUTTONDOWN:
                check = False
                GAME = False
                screen.fill(background)
                MAIN = True
                MainMenu(MenuList)
            
        #Display the screen and shapes via updating (for testing)
        pygame.display.update()
        #Add a delay so that we can see our shapes (for testing)
        pygame.time.delay(10)
def instructions():
    instructions = INST_FNT.render("so basically...", 1, (149, 206, 255))
    screen.blit(instructions,(75,160))
    instructions = INST_FNT.render("this is a two player game in which", 1, (149, 206, 255))
    screen.blit(instructions,(75,180))
    instructions = INST_FNT.render("one person is the circle and the other person is the square.", 1, (149, 206, 255))
    screen.blit(instructions,(75,200))
    instructions = INST_FNT.render('and the circle is trying to eat the sqaure by tagging it', 1, (149, 206, 255))
    screen.blit(instructions,(75,220))
    instructions = INST_FNT.render(' ', 1, (149, 206, 255))
    screen.blit(instructions,(75,260))
    instructions = INST_FNT.render('CONTROLS FOR SQUARE:', 1, (227, 111, 255))
    screen.blit(instructions,(75,290))
    instructions = INST_FNT.render('W - up', 1, (149, 206, 255))
    screen.blit(instructions,(75,310))
    instructions = INST_FNT.render('S - down', 1, (149, 206, 255))
    screen.blit(instructions,(75,330))
    instructions = INST_FNT.render('A - left', 1, (149, 206, 255))
    screen.blit(instructions,(75,350))
    instructions = INST_FNT.render('D - right', 1, (149, 206, 255))
    screen.blit(instructions,(75,370))
    instructions = INST_FNT.render('CONTROLS FOR CIRCLE:', 1, (227, 111, 255))
    screen.blit(instructions,(75,410))
    instructions = INST_FNT.render('up arrow (^) - up', 1, (149, 206, 255))
    screen.blit(instructions,(75,430))
    instructions = INST_FNT.render('down arrow - down', 1, (149, 206, 255))
    screen.blit(instructions,(75,450))
    instructions = INST_FNT.render('left arrow(<) - left', 1, (149, 206, 255))
    screen.blit(instructions,(75,470))
    instructions = INST_FNT.render('right arrow(>) - right', 1, (149, 206, 255))
    screen.blit(instructions,(75,490))
    instructions = INST_FNT.render('circle.... try to to get square!!', 1, (227, 111, 255))
    screen.blit(instructions,(75,540))
    instructions = INST_FNT.render('back', 1, (227, 111, 255))
    screen.blit(instructions,(50,650))
def scoreboard():
    while check:
        screen.fill(255,255,0)
        pygame.time.delay(100)
playboogaloo = True
while playboogaloo:
    print(GAME)
    global randdisplay
    if MAIN:
        screen.fill(background)
        TitleMenu("--main menu--")
        MainMenu(MenuList)
    if SETT:
        TitleMenu("--settings--")
        SettMenu(SettingList)
        BackButton=MENU_FONT.render("BACK",1,(42,82,130))
        screen.blit(BackButton,(200,500))
    if GAME:
        playgameyuh()
    if SCORE and hi:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        scoreBoard()
        backthing=MENU_FONT.render("BACK",1,(42,82,130))
        screen.blit(backthing,(200,500))
        if ((mouse_pos[0] >200 and mouse_pos[0] <540) and (mouse_pos[1] >500 and mouse_pos[1] <540)):
            screen.fill(background)
            SETT=False
            MAIN=True
            TitleMenu("MENU")
            MainMenu(MenuList)
    if SCORE:
        if keys[pygame.K_ESCAPE]:
            SCORE=False
            MAIN=True
            hi=True
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INST :
            MAIN=False
            screen.fill(background)
            TitleMenu("INSTRUCTIONS")
            INST=True
            instructions()
            if ((mouse_pos[0]>52 and mouse_pos[0] <113) and (mouse_pos[1] >660 and mouse_pos[1]< 684)):
                screen.fill(background)
                INST=False
                MAIN=True
                TitleMenu("MENU")
                MainMenu(MenuList)
        elif ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)) or SETT:
            MAIN=False
            screen.fill(background)
            SETT=True
            if ((mouse_pos[0] >200 and mouse_pos[0] <540) and (mouse_pos[1] >500 and mouse_pos[1] <540)):
                screen.fill(background)
                SETT=False
                MAIN=True
                TitleMenu("MENU")
                MainMenu(MenuList)
            if ((mouse_pos[0] >100 and mouse_pos[0] <130) and (mouse_pos[1] >250 and mouse_pos[1] <280)):
                screensizelist = [(700, 700), (800, 800), (900,900)]
                randscreen = random.choice(screensizelist)
                randdisplay=pygame.display.set_mode((randscreen))

        elif ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)) or GAME:
            screen.fill(background)
            playgameyuh()
        elif ((mouse_pos[0] > 20 and mouse_pos[0] < 80) and (mouse_pos[1]> 400 and mouse_pos[1] < 440)) or EXIT:
            check = False
        elif ((mouse_pos[0] > 50 and mouse_pos[0] < 80) and (mouse_pos[1]> 450 and mouse_pos[1] < 480)):
            MAIN=False
            SCORE=True
            backthing=MENU_FONT.render("BACK",1,(42,82,130))
            screen.blit(backthing,(200,500))
            if ((mouse_pos[0] >200 and mouse_pos[0] <540) and (mouse_pos[1] >500 and mouse_pos[1] <540)):
                screen.fill(background)
                SETT=False
                MAIN=True
                TitleMenu("MENU")
                MainMenu(MenuList)
      
                
    pygame.display.update()
    pygame.time.delay(10)