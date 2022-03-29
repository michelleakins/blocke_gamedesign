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
score = 345
name = 'Jay'
scoreline = str(score)+" "+name+ " "+ date.strftime('%m/%d/%Y')
print(scoreline)
#open a file and write
myfile = open('classstuffyes\scetxt.txt', "a")
myfile.write(scoreline)

myfile.close() 
