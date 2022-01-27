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
    print("  _______________________________________________________________ ")
guess = 0    
menu()


def userInput(dif):
    if userInput(dif)==1:
        number_onetoten= random.randint(1,10)
    if userInput(dif)==2:
        number_onetofifty= random.randint(1,30)
    if userInput(dif)==3:
        number_onetohundred= random.randint(1,50) 
    if userInput(dif) > 3:
        print("FROM 1-3 ONLYYY")

correct_number_10 = random.randint(1,10)
correct_number_50 = random.randint(1,50)
correct_number_100 = random.randint(1,100)

# ValueError != int
# check = True
# while check:
#     try:
#         difficulty =int(("choice:"))
#         check = True
#     except ValueError:
#         print("that's not a level silly, please enter 1-3 ONLYY")
#         check = False
# ValueError != int

# if input == ValueError:
#     print('yogabagaba')

# def difficulty(int):
#     print("what level do you want?")

difficulty = input("what level do you want: [1,2, or 3] \n")

maxguess = 0
while int(difficulty) == 1:
        guess = input("\ntake a guess: \n")
        if maxguess > 3:
            os.system('cls')
            menu()
            print("too many guesses, restart game!")
            correct_number_10 = random.randint(1,10)
            correct_number_50 = random.randint(1,50)
            correct_number_100 = random.randint(1,100)
            quit()
        if int(guess) > correct_number_10:
            print("oooof your number is too big, try a smaller number! \n☆*:.｡.｡.:*☆ \n")
            maxguess = maxguess + 1
        if int(guess) < correct_number_10:
            print("oooof your number is too small, try a bigger number! \n☆*:.｡.｡.:*☆ \n")
            maxguess = maxguess + 1
        if int(guess) == correct_number_10:
            answer = input("yay that is correct, wanna play again?? [yes OR no] ")
            if answer == "yes":
                os.system('cls')
                menu()
                correct_number_10 = random.randint(1,10)
                correct_number_50 = random.randint(1,50)
                correct_number_100 = random.randint(1,100)
            if answer == "no":
                quit()

maxguess = 0
while int(difficulty) == 2:
        guess = input("\ntake a guess: \n")
        if maxguess > 6:
            os.system('cls')
            menu()
            print("too many guesses, restart game")
            correct_number_10 = random.randint(1,10)
            correct_number_50 = random.randint(1,50)
            correct_number_100 = random.randint(1,100)
            break
        if int(guess) > correct_number_50:
            print("oooof your number is too big, try a smaller number! \n☆*:.｡.｡.:*☆ \n")
            maxguess = maxguess + 1
        if int(guess) < correct_number_50:
            print("oooof your number is too small, try a bigger number! \n☆*:.｡.｡.:*☆ \n")
            maxguess = maxguess + 1
        if int(guess) == correct_number_50:
            answer = input("yay that is correct, wanna play again?? [yes OR no] ")
            if answer == "yes":
                os.system('cls')
                menu()
                correct_number_10 = random.randint(1,10)
                correct_number_50 = random.randint(1,50)
                correct_number_100 = random.randint(1,100)
            if answer == "no":
                quit()

maxguess = 0
while int(difficulty) == 3:
        guess = input("\ntake a guess: \n")
        if maxguess >= 8:
            os.system('cls')
            menu()
            print("too many guesses, restart game")
            correct_number_10 = random.randint(1,10)
            correct_number_50 = random.randint(1,50)
            correct_number_100 = random.randint(1,100)
            break
        if int(guess) > correct_number_100:
            print("oooof your number is too big, try a smaller number! \n☆*:.｡.｡.:*☆ \n")
            maxguess = maxguess + 1
        if int(guess) < correct_number_100:
            print("oooof your number is too small, try a bigger number! \n☆*:.｡.｡.:*☆ \n")
            maxguess = maxguess + 1
        if int(guess) == correct_number_100:
            answer = input("yay that is correct, wanna play again?? [yes OR no] ")
            if answer == "yes":
                os.system('cls')
                menu()
                correct_number_10 = random.randint(1,10)
                correct_number_50 = random.randint(1,50)
                correct_number_100 = random.randint(1,100)
            if answer == "no":
                quit()




# while int(difficulty) != 1 or 2 or 3:
#         guess = input("FROM 1-3 ONLY!!😡 RESTART THE GAME [enter]") 
#         quit()
