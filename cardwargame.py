#card war game
#michelle akins
import os, random
os.system('cls')
#psuedo code
# 1. define my cards
# 2. the user inputs "card" to randomly generate a card that they use
# 3. have the computer randomly generate a card
# 4. if the randomly generate card is great than user's randomly generated input say "good job you gain 2 points"
# 5. *add the two points to their highscore
# 5. if the randomly generated card is less than users randomly generates input say "oh nooo you lost 2 points"
# 6. *subtract two points from their high score
# 6. then the computer is going to ask them "try again?"
# 7. if yes then the computer is going to keep going
# 7. if no the computer will quit the game and it will print their high score

def menu():
    print("|    ☆*: .｡.｡.:*☆☆*: .｡.｡.:*☆           *           *        ")
    print("|                                           __    __            ")
    print("|    war    card    game          *        |  \  /  |    *      ")
    print("|                                  *        \  \/  /            ")
    print("|    ☆*: .｡.｡.:*☆☆*: .｡.｡.:*☆                \    /   *         ")
    print("|                                        *    \  /              ")
    print("|                                              \/               ")
menu()

cards= ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

def userinput():
    global userinput, randomcarduser, randomcardcomputer
    userinput = input("type 'card' if you would like to play a card\n")
    if userinput == "card":
        randomcarduser= random.choice(cards)
        randomcardcomputer= random.choice(cards)
        print("you pulled out a", randomcarduser,",computer pulled out a",randomcardcomputer)
    if randomcarduser > randomcardcomputer:
        win()
    if randomcarduser < randomcardcomputer:
        lost()

userinput()

def playagain():
    if userinput == "yes":
        os.system('cls')
        menu()
        userinput()
    if userinput == "no":
        quit()

def win():
    global userinput
    userinput = input("\nYOU WONNN!\n☆*: .｡. try again? [yes or no] .｡.:*☆")
    playagain()

def lost():
    global userinput
    userinput = input("HAHA YOU LOST!\n☆*: .｡. try again? [yes or no] .｡.:*☆")
    playagain()





# size = len(cards)
# print(size)
# for i in range(size+1): # 11 is not included
#     print(cards[1])
# print(cards[size-1])
# print(cards[size-2])

# numbercards= []

# for i in range(2,14):
#     numbercards.append(i)
#     numbercards[i-2]= str(numbercards[i-2])
# print(numbercards)
# suits = ['s','d','g','d']
# royals = ['J','K', "Q", "A"]

#make a list from 2 to ace
# make a deck of cards adding each suite







