import os, random
os.system('cls')
#michelle akins
# 1/31/22
# strings are an array of characters
# has many functions!


#if u put 3 quotation marks, it prints exactly how it is
myname = "michelle akins"
mystatement1 = """hVGBHJHHJB



jihfbhdYAYAYAYehb"""
print(myname[3])
print(myname[1])
print(mystatement1)
print("my last name begins with " +myname[9])

if 'yay' in mystatement1:
    print('true')
if 'michelle' in myname:
    print('RA')
print('expert' not in mystatement1)
#find functio will return the index ur looking for first instance
INDEX = myname.find("i")
print(INDEX)
#finding length of ur word
wordLen = len(myname)
print(wordLen -1) #your last index is len-1
#for loop in range 0 to limit
for i in range(wordLen-1):
    if "l" in myname[i]:
        print(i, end=", ")
print("done")
mystatement1=mystatement1.lower()
print(mystatement1) 

# if answer in mystatement1:
#     print("great")



for elem in myname:
    print(elem, end=",  ")

guess = random.choice(myname)
print(guess)
words = ["radio", "clues", "apple", "suite", "robot"]
word = random.choice(words)
print(word)
check =True
while check:
    answer = input("hey user, please give us a nice letter")
    if len(answer)>1 or not answer.isalpha():
        print("NOOOOO")
    else:
        check = False
print("ready for playing")

for i in range(len(word)):
    if answer == word[i]:
        print(answer, end=" ")
    else:
        print("_", end= " ")
