import os, random
os.system('cls')

myNumber = random.randint
def menu():
    print("  _______________________________________________________________ ")
    print(" |                                                               |")
    print(" |     ╰(*°▽°*)╯ welcome to guess a number game!! ╰(*°▽°*)╯      |")
    print(" |                                                               |")
    print("  _______________________________________________________________ ")

print("Level 1: guess a number between 1-10")
print("Level 2: guess a number between 1-30")
print("Level 3: guess a number between 1-50")
print("  ")

menu() #calling the function menu

if choice == 1:
    myNumber = random.radint(1,10)
elif choice == 2:
    myNumber = random.radint(1,50)
elif choice == 3:
    myNumber = random.radint(1,100)

GameOn = True
while(GameOn):
    userGuess = choice(input("take a guess"))
    if myNumber > userGuess:
        print("too big, guess again")
    if myNumber < userGuess:
        print("too small, guess again")
    if myNumber == userGuess:
        print("correcto!!")
        GameOn =False

    os.system('cls')
    menu()