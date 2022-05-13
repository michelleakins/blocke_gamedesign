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
from pickle import TRUE
from tkinter import Menu
os.system('cls')
name = input("what is your name?")
#initialize pygame
pygame.init()

#code I used: https://www.youtube.com/watch?v=ERcKxhAvCDI

# requirements for final game
# finish score board
# finish setting
# finish score system (update file)
# finsih games!!:
# 3 levels or 3 games 
# each level shud be independent
# think about scoring
# make each games/level seerately first!
# DOCUMENT EVERYTHING
# source the code u copy

#Declare constants, variables, list, dictionaries, any object
TITLE_FONT=pygame.font.SysFont('georgia',50) #<-- First pice of text within parenthsis is the name of the font, and the number is the height of the letters
MENU_FONT=pygame.font.SysFont('comicsans',40)
INSTRUCTION_FONT=pygame.font.SysFont('proxmanova',35)
INST_FONT = pygame.font.SysFont('helvetica', 25)

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
MenuList=['Instructions','Settings', "Level 1","Level 2", "Level 3","Scoreboard",'Exit']
SettingList=['Screen Size','Font color','Background Color']
messages = ["Screen size", "Background color"]

check=True #for the while loop
move=5 #pixels

tempRect = pygame.Rect(0,0,5,5)
screenSizeRectList = [tempRect]

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
# print(startpoint[0]-ibox,startpoint[1])
insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
#creating the rect object
square=pygame.Rect(xs,ys,wbox,hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen2=pygame.display.set_mode((WIDTH2,HEIGHT2))
screen3=pygame.display.set_mode((WIDTH3,HEIGHT3))

pygame.display.set_caption('main menu')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75], 'black':[0,0,0]}
background_black = {'black':[0,0,0]}
background=colors.get('black')

#Get colors
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
# def scoreboard():
    #psuedo code
    # #i will make a score variable for level 1, 2, 3 almost like a count
    # #then i will blit that variable onto the scoreboard
    # # i will have seperate sections for level 1, 2, and 3
    # n
def scoreBoard():
    global yi, temp
    myFile=open('circleeatsquaregame\scetxt.txt', 'r')
    yi=150
    stuff=myFile.readlines()
    stuff.sort(reverse = True)
    j=200
    for line in stuff:
        text = INST_FONT.render("SCOREBOARD", 1, (255,255,255))
        pygame.display.update()
        pygame.delay(2)
def keepScore(score):
    date=datetime.datetime.now()
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
    #open a file and write in it
    # when y write it erases the prev
    myFile=open('classstuffyes\scetxt.txt','a')
    myFile.write(scoreLine)
    myFile.close()
def instmenu(instyuh):
    instyuh = "instructionss!!"
    text=INST_FONT.render(instyuh, 1, (0,0,255))
    screen.fill((0,0,0))
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((0,0,0))
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
def timedatestuff():
    date = datetime.datetime.now()
    score = 200
    # print(date.strftime('%m/%d/%Y'))
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
# def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            # print(randColor)
            # print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def display_subtitle (message, y):
    pygame.time.delay(100)
    text = INSTRUCTION_FONT.render(message, 1, 'white')
    x = WIDTH/2 - text.get_width()/2
    subtitleRect = screen.blit(text, (x,y))
    pygame.display.update(subtitleRect)
def SettMenu(Mlist):
    global txtS
    global txtSS
    global textlistcolors
    txtS=243
    txtSS=145
    squareSet.y=250
    for i in range(len(Mlist)):
        messages=Mlist[i]
        text=INST_FNT.render(messages,1,(51,131,51))
        screen.blit(text,(txtSS,txtS))
        pygame.draw.rect(screen,sqM_color, squareSet )
        squareSet.y +=50
        txtS+=50
def timer():
    global moleTime
    time_limit = 4
    start_time=time.time()
    elapsed_time= time.time() - start_time
    gameTime=time_limit - int(elapsed_time)
    print(gameTime)
count = 0
def playgameyuh1():
    global gameover, xm, ym
    #defining variables
    FPS = 30
    framesPerSec = pygame.time.Clock()
    black = (0,0,0)
    red = (255, 0, 0)
    window = pygame.display.set_mode((600,700))
    window.fill(black)
    pygame.display.set_caption("shoot the rock aha ha")

    speed = 10
    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

    # from pygame import mixer
    # mixer.init()
    # mixer.music.load("spaceCopy.mp3")
    # mixer.music.set_volume(0.7)
    # mixer.music.play()

    class Enemy(pygame.sprite.Sprite):
        #this is where i draw the enemy which is a picture of dwayne johnson
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("AsteroidGame\dwaynefr.png") #changed the sprite to dwayne johnson
            self.surf = pygame.Surface((30,30))
            self.rect = self.surf.get_rect(center = (random.randint(40,460), (random.randint(-100,0)))) #i will change this later so it can modify to the screen size

        def move(self, score, destroyed): #this is if i shoot a bullet at it
            self.rect.move_ip(0,speed)
            if(self.rect.bottom > 700) or destroyed == True:
                self.rect.center = (random.randint(30,460), (random.randint(-100,0)))
                score += 1

            return score
                
        def draw(self, surface):
            surface.blit(self.image, self.rect)


    class Player(pygame.sprite.Sprite):
        def __init__(self): #this is where i make the space ship and its position
            super().__init__()
            self.image = pygame.image.load("AsteroidGame\spaceShip.png")
            self.surf = pygame.Surface((54,118))
            self.rect = self.surf.get_rect(midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

        def draw(self, surface):
            surface.blit(self.image, (self.rect.centerx-45, self.rect.centery - 90))

        def update(self): #this is where i do the arrow key stuff
            pressedKeys = pygame.key.get_pressed()
        
            if self.rect.left > 0:
                if pressedKeys[pygame.K_LEFT]:
                    self.rect.move_ip(-10, 0)

            if self.rect.right < SCREEN_WIDTH:
                if pressedKeys[pygame.K_RIGHT]:
                    self.rect.move_ip(10, 0)



    class Bullet(pygame.sprite.Sprite):
        def __init__(self, player): # this is where i draw the image of the bullet
            super().__init__()
            self.image = pygame.image.load("AsteroidGame\\bullet.png")
            self.surf = pygame.Surface((10,10))
            self.rect = self.surf.get_rect(center = (player.rect.midtop))
            self.fired = False

        def fire(self, player): #this is firing the bullet from the space ship
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys [pygame.K_SPACE] and self.fired == False:
                self.rect = self.surf.get_rect(center = (player.rect.midtop))
                self.fired = True

            if self.fired == True:
                window.blit(self.image, self.rect)
                self.rect.move_ip(0,-5)
                # this makes it so that its not functional after hitting the top
                if (self.rect.top < 1):
                    self.rect.top = 600
                    self.fired = False

        def resetPos(self):
            self.rect.top = 600
            self.fired = False


    class Background(): #just backgrund
        def __init__(self):
            BGM= pygame.image.load("AsteroidGame\spacebkgrnd.png")
            # pygame. transform. scale(image, DEFAULT_IMAGE_SIZE)
            self.backgroundImage = pygame.transform.scale(BGM, (600, 700)) #the scaling
            self.rectBGimage = self.backgroundImage.get_rect()

            self.bgY1 = 0
            self.bgX1 = 0

            self.bgY2 = -self.rectBGimage.height
            self.bgX2 = 0

            self.moveSpeed = 5


        def update(self):
            self.bgY1 += self.moveSpeed
            self.bgY2 += self.moveSpeed

            if self.bgY1>self.rectBGimage.height:
                self.bgY1 = -self.rectBGimage.height

            if self.bgY2>self.rectBGimage.height:
                self.bgY2 = -self.rectBGimage.height
        

        def render(self):
            window.blit(self.backgroundImage,(self.bgX1, self.bgY1))
            window.blit(self.backgroundImage,(self.bgX2, self.bgY2))

    background = Background()

    INCREASE_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INCREASE_SPEED, 3000)

    P1 = Player()
    E1 = Enemy()
    E2 = Enemy()
    E3 = Enemy()
    B1 = Bullet(P1)

    enemyGroup = pygame.sprite.Group()
    enemyGroup.add(E1)
    enemyGroup.add(E2)
    enemyGroup.add(E3)

    bullets = pygame.sprite.Group()
    bullets.add(B1)

    font = pygame.font.SysFont("Verdana", 40, (255,255,255))
    MsGameover=MENU_FONT.render("would you like to play again?",1,(42,82,130))
    screen.blit(MsGameover,(200,500))
    yesorno= MENU_FONT.render("yes or no?", 1, (0,0,0))
    screen.blit(yesorno,(200,520))

    screen
    score = 0
    destroyed = False
    gameover = False
    
    def gameoverFunc():
        global gameover, check
        window.fill(red)
        window.blit(MsGameover, (20,300))
        window.blit(yesorno, (50,400))
       
        
        
    check=True
    while check:
        scoreRender = font.render("Score: " +str(score), True, red)
        background.update()
        background.render()
        window.blit(scoreRender, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == INCREASE_SPEED:
                speed+= 0.5
            if case.type ==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                xm = mouse_pos[0]
                ym = mouse_pos[1]
        
        print(xm,ym)   
        for entity in bullets:
            entity.fire(P1)
        
        for enemy in enemyGroup:
            if pygame.sprite.spritecollideany(enemy, bullets):
                destroyed = True
                score = score + 5
                enemy.move(score, destroyed)
                window.blit(enemy.image, enemy.rect)
                B1.resetPos()
                destroyed = False

        for enemy in enemyGroup:
            score = enemy.move(score, destroyed)
            enemy.draw(window)

       
        if pygame.sprite.spritecollideany(P1, enemyGroup):
            gameover=True
        if gameover:
            gameoverFunc()
            mouse_pos=pygame.mouse.get_pos()
            xm = mouse_pos[0]
            ym = mouse_pos[1]
            print(xm,ym)
            if case.type ==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                xm = mouse_pos[0]
                ym = mouse_pos[1]
                if (xm>50 and xm <110) and (ym >420 and ym <450):
                    gameover=False
                if (xm>180 and xm <220) and (ym >420 and ym <450):
                    check = False
                    gameover =False
            pygame.display.update()
        P1.update()
        P1.draw(window)
        pygame.display.update()
        framesPerSec.tick(FPS)
def playgameyuh2():
    global gameover, xm, ym
    FPS = 30
    framesPerSec = pygame.time.Clock()
    black = (0,0,0)
    red = (255, 0, 0)
    window = pygame.display.set_mode((600,700))
    window.fill(black)
    pygame.display.set_caption("shoot the rock aha ha")

    speed = 15
    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

    # from pygame import mixer
    # mixer.init()
    # mixer.music.load("spaceCopy.mp3")
    # mixer.music.set_volume(0.7)
    # mixer.music.play()

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("AsteroidGame\dwaynefr.png") #changed the sprite to dwayne johnson
            self.surf = pygame.Surface((30,30))
            self.rect = self.surf.get_rect(center = (random.randint(40,460), (random.randint(-100,0)))) #i will change this later so it can modify to the screen size

        def move(self, score, destroyed):
            self.rect.move_ip(0,speed)
            if(self.rect.bottom > 700) or destroyed == True:
                self.rect.center = (random.randint(30,460), (random.randint(-100,0)))
                score += 1

            return score
                
        def draw(self, surface):
            surface.blit(self.image, self.rect)


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("AsteroidGame\spaceShip.png")
            self.surf = pygame.Surface((54,118))
            self.rect = self.surf.get_rect(midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

        def draw(self, surface):
            surface.blit(self.image, (self.rect.centerx-45, self.rect.centery - 90))

        def update(self):
            pressedKeys = pygame.key.get_pressed()
        
            if self.rect.left > 0:
                if pressedKeys[pygame.K_LEFT]:
                    self.rect.move_ip(-10, 0)

            if self.rect.right < SCREEN_WIDTH:
                if pressedKeys[pygame.K_RIGHT]:
                    self.rect.move_ip(10, 0)



    class Bullet(pygame.sprite.Sprite):
        def __init__(self, player):
            super().__init__()
            self.image = pygame.image.load("AsteroidGame\\bullet.png")
            self.surf = pygame.Surface((10,10))
            self.rect = self.surf.get_rect(center = (player.rect.midtop))
            self.fired = False

        def fire(self, player):
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys [pygame.K_SPACE] and self.fired == False:
                self.rect = self.surf.get_rect(center = (player.rect.midtop))
                self.fired = True

            if self.fired == True:
                window.blit(self.image, self.rect)
                self.rect.move_ip(0,-5)

                if (self.rect.top < 1):
                    self.rect.top = 600
                    self.fired = False

        def resetPos(self):
            self.rect.top = 600
            self.fired = False


    class Background():
        def __init__(self):
            BGM= pygame.image.load("AsteroidGame\\backgroundImage3.png")
            # pygame. transform. scale(image, DEFAULT_IMAGE_SIZE)
            self.backgroundImage = pygame.transform.scale(BGM, (600, 700))
            self.rectBGimage = self.backgroundImage.get_rect()

            self.bgY1 = 0
            self.bgX1 = 0

            self.bgY2 = -self.rectBGimage.height
            self.bgX2 = 0

            self.moveSpeed = 5


        def update(self):
            self.bgY1 += self.moveSpeed
            self.bgY2 += self.moveSpeed

            if self.bgY1>self.rectBGimage.height:
                self.bgY1 = -self.rectBGimage.height

            if self.bgY2>self.rectBGimage.height:
                self.bgY2 = -self.rectBGimage.height
        

        def render(self):
            window.blit(self.backgroundImage,(self.bgX1, self.bgY1))
            window.blit(self.backgroundImage,(self.bgX2, self.bgY2))

    background = Background()

    INCREASE_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INCREASE_SPEED, 3000)

    P1 = Player()
    E1 = Enemy()
    E2 = Enemy()
    E3 = Enemy()
    B1 = Bullet(P1)

    enemyGroup = pygame.sprite.Group()
    enemyGroup.add(E1)
    enemyGroup.add(E2)
    enemyGroup.add(E3)

    bullets = pygame.sprite.Group()
    bullets.add(B1)

    font = pygame.font.SysFont("Verdana", 40, (255,255,255))
    MsGameover=MENU_FONT.render("would you like to play again?",1,(42,82,130))
    screen.blit(MsGameover,(200,500))
    yesorno= MENU_FONT.render("yes or no?", 1, (0,0,0))
    screen.blit(yesorno,(200,520))

    screen
    score = 0
    destroyed = False
    gameover = False
    
    def gameoverFunc():
        global gameover, check
        window.fill(red)
        window.blit(MsGameover, (20,300))
        window.blit(yesorno, (50,400))
       
        
        
    check=True
    while check:
        scoreRender = font.render("Score: " +str(score), True, red)
        background.update()
        background.render()
        window.blit(scoreRender, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == INCREASE_SPEED:
                speed+= 0.5
            if case.type ==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                xm = mouse_pos[0]
                ym = mouse_pos[1]
        
        print(xm,ym)   
        for entity in bullets:
            entity.fire(P1)
        
        for enemy in enemyGroup:
            if pygame.sprite.spritecollideany(enemy, bullets):
                destroyed = True
                score = score + 5
                enemy.move(score, destroyed)
                window.blit(enemy.image, enemy.rect)
                B1.resetPos()
                destroyed = False

        for enemy in enemyGroup:
            score = enemy.move(score, destroyed)
            enemy.draw(window)

       
        if pygame.sprite.spritecollideany(P1, enemyGroup):
            gameover=True
        if gameover:
            gameoverFunc()
            mouse_pos=pygame.mouse.get_pos()
            xm = mouse_pos[0]
            ym = mouse_pos[1]
            print(xm,ym)
            if case.type ==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                xm = mouse_pos[0]
                ym = mouse_pos[1]
                if (xm>50 and xm <110) and (ym >420 and ym <450):
                    gameover=False
                if (xm>180 and xm <220) and (ym >420 and ym <450):
                    check = False
                    gameover =False
            pygame.display.update()
        P1.update()
        P1.draw(window)
        pygame.display.update()
        framesPerSec.tick(FPS)
def playgameyuh3():
    global gameover, xm, ym
    FPS = 30
    framesPerSec = pygame.time.Clock()
    black = (0,0,0)
    red = (255, 0, 0)
    window = pygame.display.set_mode((600,700))
    window.fill(black)
    pygame.display.set_caption("shoot the rock aha ha")

    speed = 20
    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

    # from pygame import mixer
    # mixer.init()
    # mixer.music.load("spaceCopy.mp3")
    # mixer.music.set_volume(0.7)
    # mixer.music.play()

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("AsteroidGame\dwaynefr.png") #changed the sprite to dwayne johnson
            self.surf = pygame.Surface((30,30))
            self.rect = self.surf.get_rect(center = (random.randint(40,460), (random.randint(-100,0)))) #i will change this later so it can modify to the screen size

        def move(self, score, destroyed):
            self.rect.move_ip(0,speed)
            if(self.rect.bottom > 700) or destroyed == True:
                self.rect.center = (random.randint(30,460), (random.randint(-100,0)))
                score += 1

            return score
                
        def draw(self, surface):
            surface.blit(self.image, self.rect)


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("AsteroidGame\spaceShip.png")
            self.surf = pygame.Surface((54,118))
            self.rect = self.surf.get_rect(midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

        def draw(self, surface):
            surface.blit(self.image, (self.rect.centerx-45, self.rect.centery - 90))

        def update(self):
            pressedKeys = pygame.key.get_pressed()
        
            if self.rect.left > 0:
                if pressedKeys[pygame.K_LEFT]:
                    self.rect.move_ip(-10, 0)

            if self.rect.right < SCREEN_WIDTH:
                if pressedKeys[pygame.K_RIGHT]:
                    self.rect.move_ip(10, 0)



    class Bullet(pygame.sprite.Sprite):
        def __init__(self, player):
            super().__init__()
            self.image = pygame.image.load("AsteroidGame\\bullet.png")
            self.surf = pygame.Surface((10,10))
            self.rect = self.surf.get_rect(center = (player.rect.midtop))
            self.fired = False

        def fire(self, player):
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys [pygame.K_SPACE] and self.fired == False:
                self.rect = self.surf.get_rect(center = (player.rect.midtop))
                self.fired = True

            if self.fired == True:
                window.blit(self.image, self.rect)
                self.rect.move_ip(0,-5)

                if (self.rect.top < 1):
                    self.rect.top = 600
                    self.fired = False

        def resetPos(self):
            self.rect.top = 600
            self.fired = False


    class Background():
        def __init__(self):
            BGM= pygame.image.load("AsteroidGame\\backgroundImage2.png")
            # pygame. transform. scale(image, DEFAULT_IMAGE_SIZE)
            self.backgroundImage = pygame.transform.scale(BGM, (600, 700))
            self.rectBGimage = self.backgroundImage.get_rect()

            self.bgY1 = 0
            self.bgX1 = 0

            self.bgY2 = -self.rectBGimage.height
            self.bgX2 = 0

            self.moveSpeed = 5


        def update(self):
            self.bgY1 += self.moveSpeed
            self.bgY2 += self.moveSpeed

            if self.bgY1>self.rectBGimage.height:
                self.bgY1 = -self.rectBGimage.height

            if self.bgY2>self.rectBGimage.height:
                self.bgY2 = -self.rectBGimage.height
        

        def render(self):
            window.blit(self.backgroundImage,(self.bgX1, self.bgY1))
            window.blit(self.backgroundImage,(self.bgX2, self.bgY2))

    background = Background()

    INCREASE_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INCREASE_SPEED, 3000)

    P1 = Player()
    E1 = Enemy()
    E2 = Enemy()
    E3 = Enemy()
    B1 = Bullet(P1)

    enemyGroup = pygame.sprite.Group()
    enemyGroup.add(E1)
    enemyGroup.add(E2)
    enemyGroup.add(E3)

    bullets = pygame.sprite.Group()
    bullets.add(B1)

    font = pygame.font.SysFont("Verdana", 40, (255,255,255))
    MsGameover=MENU_FONT.render("would you like to play again?",1,(42,82,130))
    screen.blit(MsGameover,(200,500))
    yesorno= MENU_FONT.render("yes or no?", 1, (0,0,0))
    screen.blit(yesorno,(200,520))

    screen
    score = 0
    destroyed = False
    gameover = False
    
    def gameoverFunc():
        global gameover, check
        window.fill(red)
        window.blit(MsGameover, (20,300))
        window.blit(yesorno, (50,400))
       
        
        
    check=True
    while check:
        scoreRender = font.render("Score: " +str(score), True, red)
        background.update()
        background.render()
        window.blit(scoreRender, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == INCREASE_SPEED:
                speed+= 0.5
            if case.type ==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                xm = mouse_pos[0]
                ym = mouse_pos[1]
        
        print(xm,ym)   
        for entity in bullets:
            entity.fire(P1)
        
        for enemy in enemyGroup:
            if pygame.sprite.spritecollideany(enemy, bullets):
                destroyed = True
                score = score + 5
                enemy.move(score, destroyed)
                window.blit(enemy.image, enemy.rect)
                B1.resetPos()
                destroyed = False

        for enemy in enemyGroup:
            score = enemy.move(score, destroyed)
            enemy.draw(window)

       
        if pygame.sprite.spritecollideany(P1, enemyGroup):
            gameover=True
        if gameover:
            gameoverFunc()
            mouse_pos=pygame.mouse.get_pos()
            xm = mouse_pos[0]
            ym = mouse_pos[1]
            print(xm,ym)
            if case.type ==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                xm = mouse_pos[0]
                ym = mouse_pos[1]
                if (xm>50 and xm <110) and (ym >420 and ym <450):
                    gameover=False
                if (xm>180 and xm <220) and (ym >420 and ym <450):
                    check = False
                    gameover =False
            pygame.display.update()
        P1.update()
        P1.draw(window)
        pygame.display.update()
        framesPerSec.tick(FPS)
def display_text (message, y):
    pygame.time.delay(10)
    text = INSTRUCTION_FONT.render(message, 1, 'white')
    x = WIDTH/2 - text.get_width()/2
    textRect = screen.blit(text, (x,y))
    pygame.display.update(textRect)
    return textRect
def instructions():
    global instructionBackRect
    screen.fill(background)
    instructionBackRect = pygame.Rect(5,5,5,5)
    instmenu("Instructions")
    instructionBackRect = display_subtitle("Back", 660)
    display_text("so basically...", 120)
    display_text("Your goal is to avoid the aestroids!", 150)
    display_text("Each level is faster and faster", 170)
    display_text("To move, use the left and right arrow keys", 190)
    display_text("Move left - >", 240)
    display_text("Move right - <", 260)
    # display_text("S - down", 250)
    # display_text("A - left", 270)
    # display_text("D - right", 290)
    # display_text("CONTROLS FOR CIRCLE:", 320)
    # display_text("^ (up arrow)- up", 340)
    # display_text("down arrow - down", 360)
    # display_text("< (left arrow) = left", 380)
    # display_text("> (right arrow)= right", 400)
    # display_text("circle... try to get square", 500)

    pygame.display.update()
def scoreboard():
    screen.fill(background)
    TitleMenu("SCOREBOARD")
    backthing=MENU_FONT.render("BACK",1,(42,82,130))
    screen.blit(backthing,(200,500))
    backthing=MENU_FONT.render("high score: 85",1,(42,82,130))
    screen.blit(backthing,(200,250))
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys [pygame.K_ESCAPE]:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
# def changebackground():
#     screen.fill(background)  

playboogaloo = True
f_color = True
xm = 0
ym = 0
while playboogaloo:
    global randdisplay
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            playboogaloo=False
    keys=pygame.key.get_pressed() #this returns a list
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        xm = mouse_pos[0]
        ym = mouse_pos[1]
        
    if MAIN:
        screen.fill(background)
        TitleMenu("--main menu--")
        MainMenu(MenuList)
    if SETT:
        screen.fill(background)
        TitleMenu("--settings--")
        SettMenu(messages)
        BackButton=MENU_FONT.render("BACK",1,(42,82,130))
        screen.blit(BackButton,(200,500))
    if SCORE and hi:
        scoreboard()

    if ((xm >20 and xm <80) and (ym >250 and ym <290))or INST :
        MAIN=False
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        INST=True
        instructions()
        if ((xm>320 and xm <350) and (ym >650 and ym< 700)):
            screen.fill(background)
            INST=False
            MAIN=True
            TitleMenu("MENU")
            MainMenu(MenuList)
    if ((xm >20 and xm <80) and (ym >300 and ym <340)) and MAIN:
        print("joea mama")
        MAIN=False
        screen.fill(background)
        SETT=True
        pygame.display.update()
    if ((xm >100 and xm <130) and (ym >250 and ym <280)) and SETT:
        xm = 0
        ym = 0
        screensizelist = [(700, 700), (800, 800), (900,900)]
        randscreen = random.choice(screensizelist)
        randdisplay=pygame.display.set_mode((randscreen))
    if ((xm >100 and xm <130) and (ym >300 and ym <330)) and SETT and f_color:
        f_color = False
        xm = 0
        ym = 0
        blackandwhite = {'white':[255,255,255], 'black':[0,0, 0]}
        new_list = list(blackandwhite.keys())
        randcol = random.choice(new_list)
        print(randcol)
        backgroundmenu = blackandwhite.get(randcol)
        screen.fill(backgroundmenu)
    if ((xm >200 and xm <540) and (ym >500 and ym <540)) and SETT:
        screen.fill(backgroundmenu)
        SETT=False
        MAIN=True
    if ((xm >20 and xm <80) and (ym >350 and ym <390)) and MAIN:
        # screen.fill(background)
        playgameyuh1()  
    if ((xm >20 and xm <80) and (ym >390 and ym <440)) and MAIN:
        screen.fill(background)
        playgameyuh2()
    if ((xm >20 and xm <80) and (ym >440 and ym <490)) and MAIN:
        screen.fill(background)
        playgameyuh3()
    if ((xm > 20 and xm < 80) and (ym> 490 and ym < 540)) and MAIN:
        MAIN=False
        SCORE=True
        hi = True
        # backthing=MENU_FONT.render("BACK",1,(42,82,130))
        # screen.blit(backthing,(200,500))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys [pygame.K_ESCAPE] :
            SCORE=False
            MAIN=True
            hi = False
    if ((xm > 50 and xm < 80) and (ym> 540 and ym < 590)) and MAIN:
        quit()
        
                
    pygame.display.update()
    pygame.time.delay(10)