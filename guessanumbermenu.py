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


print("  _______________________________________________________________ ")
print(" |                                                               |")
print(" |     ╰(*°▽°*)╯ welcome to guess a number game!! ╰(*°▽°*)╯      |")
print(" |                                                               |")
print("  _______________________________________________________________ ")

print("Level 1: guess a number between 1-10")
print("Level 2: guess a number between 1-30")
print("Level 3: guess a number between 1-50")
print("  ")

def guessing(dif):
    if int(dif)==1:
        number_onetoten= random.randint(1,10)
    if int(dif)==2:
        number_onetothrity= random.randint(1,30)
    if int(dif)==3:
        number_onetofifty= random.randint(1,50)    
    if int(dif) > 3:
        print("hahaha that's not a level silly, restart the game😡")
        quit()

correct_number_10 = random.randint(1,10)
correct_number_30 = random.randint(1,30)
correct_number_50 = random.randint(1,50)

difficulty= input("Sooo what level do you want??")
print("   ")

while int(difficulty) == 1:
        guess = input("What's your guess??")
        if int(guess) > correct_number_10:
                print("Number is tooooo big, guess again")
        if int(guess) < correct_number_10:
                print("Number is tooooo small, guess again")
        if int(guess) == correct_number_10:
                print("Yayyy that is correct!!")
                quit()
                
while  int(difficulty) == 2:
        guess = input("What's your guess??")
        if int(guess) > correct_number_30:
            print("Number is tooooo big, guess again")
        if int(guess) < correct_number_30:
            print("Number is tooooo small, guess again")
        if str.isnumeric(guess) and int(guess) == correct_number_30:
            print("Yayyy that is correct!!")
            quit()
            
while int(difficulty) == 3:
        guess = input("What's your guess??")
        if int(guess) > correct_number_50:
            print("Number is tooooo big, guess again")
        if int(guess) < correct_number_50:
            print("Number is tooooo small, guess again")
        if str.isnumeric(guess) and int(guess) == correct_number_50:
            print("Yayyy that is correct!!")
            quit()
