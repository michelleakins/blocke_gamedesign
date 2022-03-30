#michelle akins
#learning files
# -open/create a file
# -write a file 'w'
# -append a file 'a'
# -read a file 'r'
# -close a file 'o'


import pygame, os, datetime
os.system('cls')

date = datetime.datetime.now()
score = 200
name = 'Jesse'
scoreline = str(score)+"\t"+name+ "\t"+ date.strftime('%m/%d/%Y'+"\n")
print(scoreline)
#open a file and write
myfile = open('classstuffyes\scetxt.txt', "r")
lines = myfile.readline()
print(lines)
myfile.close() 

# date = datetime.datetime.now()
# score = 345
# name = 'Jay'
# scoreline = str(score)+"\t"+name+ "\t"+ date.strftime('%m/%d/%Y'+"\n")
# print(scoreline)
# #open a file and write
# myfile = open('classstuffyes\scetxt.txt', "r")
# myfile.write(scoreline)

# myfile.close() 