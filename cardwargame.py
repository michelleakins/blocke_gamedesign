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
# 6. if the randomly generated card is less than users randomly generates input say "oh nooo you lost 2 points"
# 7. *subtract two points from their high score
# 8. then the computer is going to ask them "try again?"
# 9. if yes then the computer is going to keep going
# 10. if no the computer will quit the game and it will print their high score

cards= ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

def randomizedcards():
    global randomcarduser, randomcardcomputer
    randomcarduser= random.choice(cards)
    randomcardcomputer= random.choice(cards)

def menu():
    print("|    ☆*: .｡.｡.:*☆☆*: .｡.｡.:*☆           *           *        ")
    print("|                                           __    __            ")
    print("|    war    card    game          *        |  \  /  |    *      ")
    print("|                                  *        \  \/  /            ")
    print("|    ☆*: .｡.｡.:*☆☆*: .｡.｡.:*☆                \    /   *         ")
    print("|                                        *    \  /              ")
    print("|                                              \/               ")

def score():
    global scorec, scoreu, totalscore
    scoreu = randomcarduser*2
    scorec = randomcardcomputer*2
    totalscore = 0
    if totalscore > scorec or scoreu:
        print(totalscore)
    if scorec or scoreu > totalscore:
        

def score():
    global tries, letterGuessed, highscore
    score = len(randy)*2
    highscore=0
    if score> highscore:
        highscore = score
    print("\n|```````´´´´´´´´´´´´´´´´´´´´´´´´```````````````````````````````´´´´´´´´´´´´´´´´´´´´´´´´´|")
    print("|`````````your high score is...", score, "...wanna play again? ``````````````````````````|")
    print("|```````´´´´´´´´´´´´´´´´´´´´´´´´```````````````````````````````´´´´´´´´´´´´´´´´´´´´´´´´´|")
    userinput = input("[yes or no]")
    if userinput == "yes":
        ("\n\n--------THE CATEGORIES ARE: FRUITS, ANIMALS, AND DRINKS----------\n")
        print("\n")
        level()
        tries=0
        letterGuessed = ""
    elif userinput == "no":
        print(score)
        print("\nokie dokie!")
        quit()
    else:
        print("YES OR NO")

def win():
    global check
    userinput = input("\nYOU WONNN!\n☆*: .｡. the score is .｡.:*☆\n")
    if userinput == "yes":
        os.system('cls')
        menu()
        check = True
    if userinput == "no":
        quit()

def lost():
    global check
    userinput = input("\nHAHA YOU LOST!\n☆*: .｡. try again? [yes or no] .｡.:*☆\n")
    if userinput == "yes":
        os.system('cls')
        menu()
        check = True
    if userinput == "no":
        quit()

def userinput():
    global check, userinput
    check = True
    while check:
        userinput = input("|     typa 'card' if you want to pull out a card:\n\n")
        if userinput == "card":
            randomizedcards()
            print("you pulled out a", randomcarduser,",computer pulled out a",randomcardcomputer)
        if randomcarduser > randomcardcomputer:
            win()
        if randomcarduser < randomcardcomputer:
            lost()


menu()
userinput()

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