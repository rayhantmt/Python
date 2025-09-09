import random


def userinput():
    firstvalue=input('enter first value')
    secondvalue=input('enter second value')
    userdata = [firstvalue,secondvalue]
    print(userdata)
    randomvalue1 = random.choice(userdata)
    print(randomvalue1)
    randomvalue2 = random.choice(userdata)
    print(randomvalue2)
    if randomvalue1 == randomvalue2:
        print(f'Random values are the same as input which is {randomvalue1}')
    else:
        print(f'Random values are not the same as input  {randomvalue1} is the first random value and {randomvalue2} is the second random value')
    return
userinput()
#def randomising1(userdata):
    ##return

