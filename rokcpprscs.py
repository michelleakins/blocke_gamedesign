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


def menu2():
    print(" ")
    print("************************************************")
    print("|           wanna play again?🤨                |")
    print("|               [yes or no]                    |")
    print("************************************************")
    print(" ")
    if userInput == "yes":
        os.system('cls')
        menu()
        random.randint(1,3)
        print("\nchoose: rock, paper, or scissors? \n")
    if userInput == "no":
        quit()

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
        #since s is equal to 1, i made it so that if the random number is equal to p(paperthen I said it was a tie)
    if randomthingy == p:
        answer = input("Tie! press [enter]")
        menu2()
    elif randomthingy == r:
        answer = input("You beat rock! press [enter]")
        menu2()      
    elif randomthingy == s:
        answer = input("You got beat by scissors! press [enter]")
        menu2()  

#scenerios for user input's: rock
if userInput == "rock":
#since s is equal to 2, i made it so that if the random number is equal to r(rock then I said it was a tie)
    if randomthingy == r:
        answer = input("Tie! press [enter]")
        menu2()
    elif randomthingy == s:
        answer = input("You beat scissors! press [enter]")
        menu2() 
    elif randomthingy == p:
        answer = input("You got beat by paper! press [enter]")
        menu2()

#scenerios for user input's: scissors
if userInput == "scissors":
    #since s is equal to 3, i made it so that if the random number is equal to s(scissors then I said it was a tie)
    if randomthingy == s:
        answer = input("Tie! press [enter]")
        menu2()
    elif randomthingy == p:
        answer = input("You beat paper! press [enter]")
        menu2()
    elif randomthingy == r:
        answer = input("You got beat by rock! press [enter]")
        menu2()

