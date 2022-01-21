import numbers
import os, random
os.system('cls')

# michelle akins
# game design block e
# 1/21/21

# we are going to learn about input() function,
# type casting, branching, looping

#  declare a variable
print("Enter a number from 1-10:")
#userInfo= int(input()) #input returns string, we must type cast bc we need a number
#print("The number is %.2f " %(userInfo/3)) #we use .2 float to get the thingy

#guess = int(input("Please give me a number"))

correct_number = random.randint(1,10)
# print("gcfvhjkloiujghfdghjklo;kljihgfdfghjkl;")
# print("blahshbhdw nem")

GameOn = True
while(GameOn):
    userGuess = int(input("Guess a number from 1-10"))
    if correct_number == userGuess:
        print("Yay!! That is correct!!")
        
    if userGuess > correct_number:
        print("Sorry, the number is too big, guess again")

    if userGuess < correct_number:
        print("Sorry, that number is too small, guess again")


