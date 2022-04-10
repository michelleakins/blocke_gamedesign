import mailbox
import os, time, random,math
from shutil import move
import pygame as p

#initialize pygame
p.init()
#variables, constants, and objects
WIDTH=700
HEIGHT=700
x=100
y=15
xc=random.randint(50, WIDTH-50)
yc=random.randint(50,HEIGHT-50)
hbox=20  #height if rect
wbox=20  #width of rect
#inscribe char
rad = 15
ibox=rad*math.sqrt(2)
xi= xc-ibox/2
yi= yc-ibox/2
inscSq=p.Rect(xi,yi, ibox,ibox)

walkRight = [p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R1.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R2.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R3.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R4.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R5.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R6.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R7.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R8.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L1.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L2.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L3.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L4.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L5.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L6.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L7.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L8.png'), p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\L9.png')]
char = p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\standing.png')
bg=p.image.load('classstuffyes\images\Pygame-Tutorials-master\Game\\bacroung image.jpg')


lock = p.time.Clock()

x = 50
y = 400
width = 64
height = 64
move = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
JUMP=False
MAX=10
#create screen
screen=p.display.set_mode((WIDTH,HEIGHT))

#define colors Dictionary dictio={key: values}
colors={'red':[255,0,0],'white':[255,255,255],'mag':[255,0,255],
'aqua':[51,153,255],'m':[47,192,229]}
#calling values from a dictionaty get('key')
background=colors.get('white')
blColor=colors.get('aqua')
randColor=''
def changeClr():
    print(background)
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        print("rand Clr = ", randColor)
        if colors.get(randColor)  == background:
            print("backgrnd = randclr")
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
sq_color=colors.get(randColor)    

p.display.set_caption("Circle eats Square")
jumpCount=7
COUNT=7

keys=p.key.get_pressed() #<-- To check if a key gets pressed (classified as a list), the 'and move' part has to do with creating boundries
RandColor=random.choice(list(colors))
#Call colors to get colors for our screen and shapes
background=colors.get('black')
# s_color=colors.get('navy') <--- Previous square color
c_color=colors.get('white')
Hit_color=colors.get('purple')
# Creating a color check to make sure our colors are all different:
changeClr()
s_color=colors.get(RandColor) 

#square variables
xs=20
ys=20
wbox=30
hbox=30

#VARIABLES FOR COLLIDE, CIRCLE, AND MOVE
HitX=xc-15
HitY=yc-15
CRadius=15
HitLenght=CRadius*2
HitWidth=CRadius*2
hitbox=pygame.Rect(HitX,HitY,HitWidth,HitLenght)
move=5
ColorCheck=False

def playgameyuh():
    #make a function for our game
    check = True
    while check:
        #Fill the screen and draw the shapes (for testing)
        screen.fill(background)
        keys=p.key.get_pressed() #<-- To check if a key gets pressed (classified as a list), the 'and move' part has to do with creating boundries
        # Movements for the square
        if keys[p.K_a] and char.x>=move:
            square.x-=move #subtract
        if keys[p.K_d] and char.x<=WIDTH-(wbox+move):
            square.x+=move
        #Jumping
        if not JUMP:
            if keys[p.K_w] and char.y>=move:
                char.y-=move
            if keys[p.K_s] and char.y<=HEIGHT-(hbox+move):
                char.y+=move
            if keys[p.K_SPACE]:
                JUMP=True
        else:
            if jumpCount>=-MAX:
                char.y-=jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False
        # Circle Movements
        if keys[p.K_LEFT] and xc>=move+CRadius:
            xc-=move #subtract
            walkCount.x-=move
        if keys[p.K_RIGHT] and xc<=WIDTH-(CRadius+move):
            xc+=move
            walkRight.x+=move
        # if keys[p.K_UP] and yc>=move+CRadius:
        #     yc-=move
        #     hitbox.y-=move
        # if keys[p.K_DOWN] and yc<=HEIGHT-(CRadius+move):
        #     yc+=move
        #     hitbox.y+=move
        #Making the collision
        checkCollide= char.colliderect(hitbox)
        if checkCollide==True:
            char.x=random.randint(wbox,WIDTH-wbox)
            char.y=random.randint(hbox,HEIGHT-hbox)
            CRadius+=move
            changeClr()
            ColorCheck=True