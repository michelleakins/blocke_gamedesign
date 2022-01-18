import os
from tkinter import END
# michelle akins
# 1/14/22
# declare variables, print variable, print types of data, learn some operators

# this symbol is for comments, means the computer will ignore
# I want to clear my terminal
os.system('cls') 
#program is average of 3 tests

#declare and assign values
test1= 89
test2= 78.5
test3= 97
Flag=False
#to display things, we use print()
#print(type(test1), type(test2), type(Flag))

#declare sum to add tests, symbol for adding is +
sum = test1 + test2 + test3
# print(sum)

average = sum/3
# print(average)

# i wanna print the average of 3 tests is " number here"
print("The test scores are", end=": ")
print("test1=", test1, end=", ")
print("test2=", test2, end= ", ")
print("test3=", test3)
print("the average of 3 tests is", average)
