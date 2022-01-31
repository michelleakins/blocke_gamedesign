import numbers
import  os, random
os.system('cls')

# michelle akins
# game design e block
# 1/27/22

# steps:
#
# computer should geerate rock, paper, scissors, or as number
# computer should transfer the user input into numbers
# make "if" statements for scenerios
# loop yes or no, to restart or quit the game
# backup plan if they don't input rock, paper, or scissors
# mispellig scenerio

def menu():
    print("|    ☆*: .｡.｡.:*☆☆*: .｡.｡.:*☆           *           *        ")
    print("|                                           __    __            ")
    print("|    rock    paper    scissors          *  |  \  /  |    *      ")
    print("|                                  *        \  \/  /            ")
    print("|    ☆*: .｡.｡.:*☆☆*: .｡.｡.:*☆                \    /   *         ")
    print("|                                        *    \  /              ")
    print("|                                              \/               ")


menu() 

# winning Rules of the Rock paper and scissor game as follows:
# rock vs paper->paper wins
# rock vs scissors->rock wins
# paper vs scissors->scissors wins

#declaring variables: rock[r], paper[p], scissors[s]
p = 1
r = 2
s = 3

#this is the user input for the question
userInput = input("\nchoose: rock, paper, or scissors? \n")

#number randomizer [1-3]
randomthingy = random.randint(1,3)


# had a def tied to run when a player's choice matched the randomized number: random.randint(1,3)

#scenerios for user input's: paper
if userInput == "paper":
    if randomthingy == p:
        answer = input("Tie! do you wanna play again? [yes or no]")
        if answer == "yes":
            print("     cool!\n**restart game** ")
        elif answer == "no":
            quit()
    elif randomthingy == r:
        answer = input("You beat rock! do you wanna play again? [yes or no]")
        if answer == "yes":
            print("     cool!\n**restart game** ")
        elif answer == "no":
            quit()       
    elif randomthingy == s:
        answer = input("You got beat by scissors! Wanna play again? [yes or no]")
        if answer == "yes":
            print("     cool!\n**restart game** ")
        if answer == "no":
            quit()   

#scenerios for user input's: rock
if userInput == "rock":
    if randomthingy == r:
        answer = input("Tie! do you wanna play again? [yes or no]")
        if answer == "yes":
            print("     cool!\n**restart game** ")
        elif answer == "no":
            quit()
    elif randomthingy == s:
        answer = input("You beat scissors! do you wanna play again? [yes or no]")
        if answer == "yes":
            print("     cool!\n**restart game** ")
        elif answer == "no":
            quit()  
    elif randomthingy == p:
        answer = input("You got beat by paper! Wanna play again? [yes or no]")
        if answer == "yes":
            print("     cool!\n**restart game** ")
        if answer == "no":
            quit() 

#scenerios for user input's: scissors
if userInput == "scissors":
    if randomthingy == s:
        answer = input("Tie! do you wanna play again? [yes or no]")
        if answer == "yes":
            print("     cool!\n**restart game** ")
        elif answer == "no":
            quit()
    elif randomthingy == p:
        answer = input("You beat paper! do you wanna play again? [yes or no]")
        if answer == "yes":
            print("     cool!\n**restart game** ")
        elif answer == "no":
            quit()
    elif randomthingy == r:
        answer = input("You got beat by rock! Wanna play again? [yes or no]")
        if answer == "yes":
            print("     cool!\n**restart game** ")
        if answer == "no":
            quit()    
 
