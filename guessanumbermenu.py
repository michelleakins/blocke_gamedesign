import numbers
import os, random
os.system('cls')

# michelle akins
# game design block e
# 1/21/21

# we are going to learn about input() function,
# type casting, branching, looping

# declare a variable
#print("Enter a number from 1-10:")
#userInfo= int(input()) #input returns string, we must type cast bc we need a number
#print("The number is %.2f " %(userInfo/3)) #we use .2 float to get the thingy

#guess = int(input("Please give me a number"))
 
def menu():
    print("  _______________________________________________________________ ")
    print(" |                                                                |")
    print(" |     ╰(*°▽°*)╯ welcome to guess a number game!! ╰(*°▽°*)╯       |")
    print(" |              lvl 1: guess a number from 1-10                   |")
    print(" |              lvl 2: guess a number from 1-50                   |")
    print(" |              lvl 3: guess a number from 1-100                  |")
    print(" |              lvl 4: guess a number from 1-1000                  |")
    print("  _______________________________________________________________ ")
guess = 0    
menu()

# ValueError != int
check=True
while check:
    gameType=input("Please select a level of the game: ")
    try:
        gameType=int(gameType)
        if gameType >0 and gameType<5:
            check=False
        else:
            print("FROM 1-4 ONLY!")
    except ValueError:
        print("Sorry, wrong input try again")

number = 0
def difficulty():
    if gameType ==1:
        number = random.randint(1,10)
    if gameType ==2:
        number = random.randint(1,50)
    if gameType ==3:
        number = random.randint(1,100)


# difficulty = input("what level do you want: [1,2, or 3] \n")

maxguess = 0
correctGuess_10 = random.randint(1,10)
while int(gameType) == 1:
    guess = input("\ntake a guess: \n")
    if maxguess > 3:
        os.system('cls')
        menu()
        print("the correct guess was", correctGuess_10)
        print("too many guesses, restart game!")
        difficulty()
        quit()
    if int(guess) > correctGuess_10:
        print("oooof your number is too big, try a smaller number! \n☆*:.｡.｡.:*☆ \n")
        maxguess = maxguess + 1
    if int(guess) < correctGuess_10:
        print("oooof your number is too small, try a bigger number! \n☆*:.｡.｡.:*☆ \n")
        maxguess = maxguess + 1
    if int(guess) == correctGuess_10:
        answer = input("yay that is correct, wanna play again?? [yes OR no] ")
        if answer == "yes":
            os.system('cls')
            menu()
            difficulty()
        if answer == "no":
            quit()

maxguess = 0
correctGuess_50 = random.randint(1,50)
while int(gameType) == 2:
    guess = input("\ntake a guess: \n")
    if maxguess > 6:
        os.system('cls')
        menu()
        print("the correct guess was", correctGuess_50)
        print("too many guesses, restart game")
        difficulty()
        break
    if int(guess) > correctGuess_50:
        print("oooof your number is too big, try a smaller number! \n☆*:.｡.｡.:*☆ \n")
        maxguess = maxguess + 1
    if int(guess) <  correctGuess_50:
        print("oooof your number is too small, try a 2 bigger number! \n☆*:.｡.｡.:*☆ \n")
        maxguess = maxguess + 1
    if int(guess) ==  correctGuess_50:
        answer = input("yay that is correct, wanna play again?? [yes OR no] ")
        if answer == "yes":
            os.system('cls')
            menu()
            difficulty()
        if answer == "no":
            quit()

maxguess = 0
correctGuess_100 = random.randint(1,100)
while int(gameType) == 3:
    guess = input("\ntake a guess: \n")
    if maxguess >= 8:
        os.system('cls')
        menu()
        print("the correct guess was", correctGuess_100)
        print("too many guesses, restart game")
        difficulty()
        break
    if int(guess) >  correctGuess_100:
        print("oooof your number is too big, try a smaller number! \n☆*:.｡.｡.:*☆ \n")
        maxguess = maxguess + 1
    if int(guess) < correctGuess_100:
        print("oooof your number is too small, try a bigger number! \n☆*:.｡.｡.:*☆ \n")
        maxguess = maxguess + 1
    if int(guess) ==  correctGuess_100:
        answer = input("yay that is correct, wanna play again?? [yes OR no] ")
        if answer == "yes":
            os.system('cls')
            menu()
            difficulty()
        if answer == "no":
            print("next time:(")
            quit()

maxguess = 0
correctGuess_1000 = random.randint(1,1000)
while int(gameType) == 4:
    guess = input("\ntake a guess: \n")
    if maxguess >= 8:
        os.system('cls')
        menu()
        print("the correct guess was", correctGuess_1000)
        print("too many guesses, restart game")
        difficulty()
        break
    if int(guess) >  correctGuess_1000:
        print("oooof your number is too big, try a smaller number! \n☆*:.｡.｡.:*☆ \n")
        maxguess = maxguess + 1
    if int(guess) < correctGuess_1000:
        print("oooof your number is too small, try a bigger number! \n☆*:.｡.｡.:*☆ \n")
        maxguess = maxguess + 1
    if int(guess) ==  correctGuess_1000:
        answer = input("yay that is correct, wanna play again?? [yes OR no] ")
        if answer == "yes":
            os.system('cls')
            menu()
            difficulty()
        if answer == "no":
            quit()

