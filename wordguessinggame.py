from calendar import THURSDAY
import os, random
from unittest import result
os.system('cls')


def menu():
    print("  ")
print("´´´´´´´´´´´´´´´´´´´´´´´´¶´´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´´´´´´´´¶´´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´´´´¶´´´¶´´´´´´´´´¶´´´¶´´´´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´´´´¶´´¶¶´´´´´´´´´¶¶´´¶´´´´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶¶´´´´´´´¶¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´¶´´´´´´¶¶´´´¶¶¶´´´´´¶¶¶´´´¶¶´´´´´´¶´´´´´´´´´´´´´")
print("´´´´´´´´´´´´¶¶´´´´´´¶¶´´´¶¶¶´´´´´¶¶¶´´´¶¶´´´´´´¶¶´´´´´´´´´´´´")
print("´´´´´´´´´´´¶¶´´´´´´¶¶´´´´¶¶¶¶´´´¶¶¶¶´´´´¶¶´´´´´´¶¶´´´´´´´´´´´")
print("´´´´´´´´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶¶´´´´´´´´´´")
print("´´´´´´´¶´´¶¶¶´´´´¶¶¶¶´´´´¶¶¶¶´´´¶¶¶¶´´´´¶¶¶¶´´´¶¶¶¶´´¶´´´´´´´")
print("´´´´´´´¶¶´¶¶¶¶¶´´¶¶¶¶´´´¶¶¶¶¶´´´¶¶¶¶¶´´´¶¶¶¶´´¶¶¶¶¶´¶¶´´´´´´´")
print("´´´´´´´¶¶´¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶´¶¶´´´´´´´")
print("´´´´´´´¶¶´¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶´¶¶´´´´´´´")
print("´´´´´´¶¶¶´´¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶´´¶¶¶´´´´´´")
print("´´´´´¶¶¶¶´´¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶´´¶¶¶¶´´´´´")
print("´´´´¶¶¶¶´´´¶¶¶¶¶´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´¶¶¶¶´´´´")
print("´´´¶¶¶¶´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶´´´´")
print("´´´¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶´´´´")
print("´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´")
print("´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´")
print("´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´")
print("´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´")
print("´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´")
print("´´´´´¶¶¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶¶¶´´´´´")
print("´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´")
print("´´´´´´¶¶¶¶¶¶¶´´´´´´´´..´´´´´¶¶¶¶¶¶¶¶¶´´´´´..´´´´´´´´¶¶¶¶¶¶´´´´´")
print("´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´")
print("´´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´´´´")
print("´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´")
print("´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´¶¶´´¶¶¶¶´´¶¶¶¶¶´´¶¶¶¶´´¶¶´´´´´´´´´´´´´´´´´´")
print("´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´¶¶¶¶¶´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´")
print("````````````````````````````````````````````````````````````")
print("````````````````welcome to word guessing game````````````````")

menu()

listyes = "elephant, orange, baseball, sodapop, resilliant, academic, lifestyle"
words = ["elephant", "orange", "baseball", "sodapop", "resilliant", "academic", "lifestyle"]
wordanswer = random.choice(words)

name = input("what's  your name?")
print("hey",name, "\nthe words are: ",listyes,"\nyou have 5 tries to guess the word!!")

check =True
while check:
    answer = input("guess a letter!")
    if len(answer)>1 or not answer.isalpha():
        print("NOOOOO, guess ONE letter!!!😡")
    else:
        check = False

guesses = ''

#how many tries to input a character
trys = 7

while trys > 0:
    #each time a person guess a character
	result = 0
	for char in wordanswer:
        # when the perso guess the character right, it prints onto the little line thingy
		if char in guesses:
			print(char, end=" ")
		else:
			print("_")
            #every time the user guess, the result increases by 1
			result += 1

# if the person guesses the characters correctly with tries left over
	if result == 0:
		print("\nyayyyyyy you got it!!")
		break

	print()
	guess = input("guess a character:")
	
	guesses += guess
	
    #if the person doesnt gues the correct character
	if guess not in wordanswer:
        # tries will decrease each time the user guesses
		trys -= 1
		print("nope")
        #this lets the user know how many guesses they have
		print("You have", + trys, 'more guesses')
        # they will lose if they ran outta guesses
		if trys == 0:
			print("you ran outta guess :((")

print("the word is: ", wordanswer,)

# asks the user if they wanna play again
GameOn = True
while GameOn:
    userinput = input("\nwanna play again? [yes or no]")
    if userinput == "yes":
        menu()
        os.system('cls')
        wordanswer = random.choice(words)
    if userinput == "no":
        GameOn = False
        
# SOURCE!!! https://www.geeksforgeeks.org/python-program-for-word-guessing-game/ 






