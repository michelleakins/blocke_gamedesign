import os, random

os.system('cls')

 

myNumber=0

def menu():

    print("-----------------------------------------------------------------")

    print("-                           WELCOME                             -")  

    print("-                      Guess a Number Game                      -")

    print("-                                                               -")

    print("-                        Level 1 = 1-10                         -")

    print("-                        Level 2 = 1-50                         -")

    print("-                        Level 3 = 1-100                        -")

    print("-                       Select Your Level                       -")

    print("-----------------------------------------------------------------")

#Checking for correct user input

menu()

# check=True

# while check:

#     try:

#         level=int(input("Level: "))

#         check= False

#     except ValueError:

#         print("Sorry thats not a level, please enter 1 to 3 only!")

 

def level(dif):

 

    if level(dif) == 1:

        myNumber= random.randint(1,10)

    elif level(dif) == 2:

        myNumber= random.randint(1,50)

    elif level(dif) == 3:

        myNumber= random.randint(1,100)

   

correct_number_10 = random.randint(1,10)

 

correct_number_50 = random.randint(1,50)

 

correct_number_100 = random.randint(1,100)

 

maxguess = 0

difficulty = input ("what level would you like")

 

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

os.system('cls')

menu()