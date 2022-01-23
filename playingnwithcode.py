import numbers
import os, random
os.system('cls')

correct_number = random.randint
print("guessing number gaame boogaloo/playing with code")

letter_a = ("a")
letter_b = ("b")
letter_c = ("c")
letter_d = ("d")
letter_e = ("e")
letter_f = ("f")
letter_g = ("g")
letter_h = ("h")
letter_i = ("i")
letter_j = ("j")
letter_k = ("k")
letter_l = ("l")
letter_m = ("m")
letter_n = ("n")
letter_o = ("o")
letter_p = ("p")
letter_q = ("q")
letter_r = ("r")
letter_s = ("s")
letter_t = ("t")
letter_u = ("u")
letter_v = ("v")
letter_w = ("w")
letter_x = ("x")
letter_y = ("y")
letter_z = ("z")

print(" level 1: 1-100")
print(" level 2: 1-1000")
print(" level 1: 1-10000")

print("what level do you want")

def guessing(dif):
    if int(dif) == 1:
        Number= random.randint(1,100)
    if int(dif) == 2:
        Number= random.randint(1,1000)
    if int(dif) == 3:
        Number= random.randint(1,10000)
    if int(dif) >3:
        print("dummt! thats not a level. restart the game")
        quit()

difficulty= input("choose a level")
print("   ")
guessing(difficulty)

while True:
    guess = input("guess a number")
    if int(guess) > correct_number:
        print("that number is too big, guess again")
    if int(guess) < correct_number:
        print("sorry, that number is too small")
    if int(guess) == letter_a:
        print("that's not a number, silly")
    if int(guess) == letter_b:
        print("that's not a number, silly")
    if int(guess) == letter_c:
        print("that's not a number, silly")
    if int(guess) == letter_d:
        print("that's not a number, silly")
    if int(guess) == letter_e:
        print("that's not a number, silly")
    if int(guess) == letter_f:
        print("that's not a number, silly")
    if int(guess) == letter_g:
        print("that's not a number, silly")
    if int(guess) == letter_h:
        print("that's not a number, silly")
    if int(guess) == letter_i:
        print("that's not a number, silly")
    if int(guess) == letter_j:
        print("that's not a number, silly")
    if int(guess) == letter_k:
        print("that's not a number, silly")
    if int(guess) == letter_l:
        print("that's not a number, silly")
    if int(guess) == letter_m:
        print("that's not a number, silly")
    if int(guess) == letter_n:
        print("that's not a number, silly")
    if int(guess) == letter_o:
        print("that's not a number, silly")
    if int(guess) == letter_p:
        print("that's not a number, silly")
    if int(guess) == letter_q:
        print("that's not a number, silly")
    if int(guess) == letter_r:
        print("that's not a number, silly")
    if int(guess) == letter_s:
        print("that's not a number, silly")
    if int(guess) == letter_t:
        print("that's not a number, silly")
    if int(guess) == letter_u:
        print("that's not a number, silly")
    if int(guess) == letter_v:
        print("that's not a number, silly")
    if int(guess) == letter_w:
        print("that's not a number, silly")
    if int(guess) == letter_x:
        print("that's not a number, silly")
    if int(guess) == letter_y:
        print("that's not a number, silly")
    if int(guess) == letter_z:
        print("that's not a number, silly")  
    if int(guess) == correct_number:
        print("yayyyy that is correct")
        quit()
    
