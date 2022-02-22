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

def study():
    global randomvocab, userguess, correctanswer
    print("18 line reached")
    randomvocab = random.choice(vocabwords)
    userguess = input("okay, what is the correct vocab word to:", randomvocab, "?")
    correctanswer = randomvocab
    if userguess == correctanswer:
        print("yay that is correct, next question!")

def ready():
    userinputstudy = input("ready to study?? [yes or no]")
    if userinputstudy == "yes":
        print("it recognizes yes")
        study()
    if userinputstudy == "no":
        print("OH MY GOD, JUST STUDY!!!")

ready()             