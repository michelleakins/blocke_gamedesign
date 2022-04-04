#michelle akins
#lists and lists method
import random, os
os.system('cls')

fruits = ["mandarin", "orange", "orange", "blueberry", "mango", "cranberry", "papaya", "strawberry", "banana", "apple", "watermelon"]
animals = ["elephant", "kangaroo", "lion", "crab", "lizard", "snake", "deer", "toucan", "reindeer", "panda", "fox", "owl"]
computerparts = ["keyboard", "speakers", "screen", "ports", "power button", "circuit", "battery", "monitor",]


size = len(fruits)
print(size)
fruits.append("rambutan")
for i in range(size-1): # 11 is not included
    print(fruits[i])
print(fruits[size-1])
print(fruits[size-2])

# print(fruits.count('orange'))

# list2= [3,6,8,9,10]
# fruits.append(list2)

# print("append\n", fruits)
# fruits.pop(-1)
# fruits.extend(list2)
# print("extend\n",fruits)
# fruits.insert(2, "dragon fruits")
# print(fruits)