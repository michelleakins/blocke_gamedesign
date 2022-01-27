import random, os

os.system('cls')

 

def menu():
    print("  _______________________________________________________________ ")
    print(" |                                                               |")
    print(" |     ╰(*°▽°*)╯ welcome to guess a number game!! ╰(*°▽°*)╯      |")
    print(" |              lvl 1: guess a number from 1-10                   |")
    print(" |              lvl 2: guess a number from 1-50                   |")
    print(" |              lvl 3: guess a number from 1-100                   |")
    print("  _______________________________________________________________ ")

choice=int(input("what level do you want: "))

if choice == 1:
    myNumber= random.randint(1,10)
elif choice == 2:
    myNumber= random.randint(1,50)
elif choice == 3:
    myNumber= random.randint(1,100)


GameOn=True
while(GameOn):
    userGuess=int(input("give me a number "))
    if myNumber ==userGuess:
        print("You guessed it!")
        GameOn=False
    elif myNumber > userGuess:
        print("thats tooooooo biggg!")
    elif myNumber > userGuess:
        print("thats tooooooo biggg!")

print("The number to guess was " + str(myNumber))