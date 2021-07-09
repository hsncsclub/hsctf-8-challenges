import random
flag = open('flag.txt','rb').read()
def getKeithAns(s1):
    eqn = s1
    expression = []
    dig = []
    i = 0
    while i < len(eqn):
        if (eqn[i] == "a"):
            expression.append("a")
            i += 1
        elif (eqn[i] == "m"):
            expression.append("m")
            i +=1
        else:
            dig = []
            while i < len(eqn):
                if (eqn[i].isdigit()):
                    dig.append(eqn[i])
                else:
                    break
                i = i + 1
            expression.append(''.join(dig))
    while "a" in expression:
        idx = expression.index("a")
        expression[idx] = int(expression[idx-1]) + int(expression[idx+1])
        del expression[idx + 1]
        del expression[idx - 1]
    while "m" in expression:
        idx = expression.index("m")
        expression[idx] = int(expression[idx-1]) * int(expression[idx+1])
        del expression[idx + 1]
        del expression[idx - 1]
    return(int(expression[0]) % (2**32-1))
def gen(length,maxInt):
    e = str(random.randint(1,maxInt))
    while len(e)<length:
        rand = random.randint(0,1)
        i = str(random.randint(1,maxInt))
        if len(e)+1+len(i)<=length:
            e=e+"m"+i if rand==0 else e+"a"+i
        else:
            break
    return [e, getKeithAns(e)]
cases = [[10,3],[30,5],[30,100],[60,320],[200,3],[200,1000],[3000,31],[5000,5],[10000,5],[10000,100],[10000,1000],[10000,10000]]
for case in cases:
    ex, ans = gen(case[0],case[1])
    print(ex)
    if input(": ")!=str(ans):
        print("Unfortunately, that is incorrect.")
        exit(0)
print(flag)