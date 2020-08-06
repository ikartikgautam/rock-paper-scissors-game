import random

choices = ['rock','paper','scissor']

def getMachineChoice():
    return choices[random.randrange(0,3)]

def getUserChoice():
    print("Choose One of the choices :- ")
    print("1. Rock\n2. Paper\n3. Scissor")
    res = int(input("Enter your choice:"))
    if (res==1 or res==2 or res==3):
        return choices[res-1]
    else:
        print("\nERROR !!\n")
        getUserChoice()

def compareChoices(usr,msc):
    if usr==msc:
        return 'Draw'
    elif usr=='rock':
        if msc=='paper':
            return 'paper'
        elif msc=='scissor':
            return 'rock'
    elif usr=='paper':
        if msc=='rock':
            return 'paper'
        elif msc=='scissor':
            return 'scissor'
    elif usr=='scissor':
        if msc=='paper':
            return 'scissor'
        elif msc=='rock':
            return 'rock'

def showResults(res):
    sum = 0
    for i in range(len(res)):
        sum = res[i]+sum
    score = sum/len(res)
    if(score>0.5):
        print("You Win")
    else:
        print("You Loose")

results = []
while input("y OR n ? ")=='y':
    usr = getUserChoice()
    res = compareChoices(usr,getMachineChoice())
    if res == usr:
        print(":) Congrats !! ===> You Win\n")
        results.append(1)
    elif res=='Draw':
        print(":\ Ahhh !! ===> its a DRAW\n")
    else:
        print(":( Alass !! ===> Your Machine is smarter than you, Try Harder\n")
        results.append(0)
# RESULTS
showResults(results)                                