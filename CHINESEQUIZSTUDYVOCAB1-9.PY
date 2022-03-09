from operator import truediv
import os, random
os.system('cls')

weather = "天气(tianqi n)"
comparedwith = "比（bi prep v)"
tosnow = "(xiaxue vo) 下雪"
tomakeanappointment = "(yue v) 约"
park = "(gongyuan n) 公园"
iceskate = "(hua bing vo) 滑冰"
will = "(hui mv) 会"
cold = "(leng adj) 冷"
justnowamomentago = "(gangcai t) 刚才"

vocabwords = [weather, comparedwith, tosnow, tomakeanappointment, park, iceskate, will, cold, justnowamomentago]

def playgame():
    gameon = True
    while gameon:
        global randomvocab, userguess, correctanswer
        userguess = input("okay, what is the correct vocab word to:", random, "?")
        correctanswer = random.choice(vocabwords)
        if userguess == correctanswer:
            print("yay that is correct, next question!")
        else:
            print("sorry that's wrong, guess again")

def ready():
    userinputstudy = input("ready to study?? [yes or no]")
    if userinputstudy == "yes":
        playgame()
    if userinputstudy == "no":
        print("OH MY GOD, JUST STUDY!!!")

ready()