import math
import random
flag = open('flag.txt','rb').read()
def getAns(n):
    onecounter = 0
    twocounter = 0
    tempN = n
    boards = 0
    if n%2==1:
        onecounter+=1
        tempN-=1
    twocounter = tempN//2
    while twocounter>=0:
        boards+=math.factorial(twocounter+onecounter)//(math.factorial(twocounter)*math.factorial(onecounter))
        boards%=10000
        twocounter-=1
        onecounter+=2
    return boards
cases = [random.randint(10,999) for i in range(20)]
for case in cases:
    ex, ans = case, getAns(case)
    print(ex)
    if input(": ")!=str(ans):
        print("Unfortunately, that is incorrect.")
        exit(0)
print(flag)
