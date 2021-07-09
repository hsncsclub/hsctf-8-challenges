import random
import numpy.random as perm
import math
from pysat.solvers import Solver

flag = open('flag.txt','rb').read()
minN = 100
rangeN = 10
minM = 400
rangeM = 30
minTrials = 100
rangeT = 10

p = 0.75
trials = random.randint(minTrials, minTrials + rangeT)

def genLiteral(n):
    return (-1 if random.randint(0, 1) == 0 else 1) * random.randint(1, n)

def genGuess(n):
    guess = []
    for i in range(1, n + 1):
        guess.append((-1 if random.randint(0, 1) == 0 else 1) * i)

    return guess

probability = 0
print(trials)


for i in range(trials):
    n = random.randint(minN, minN + rangeN)
    m = random.randint(minM, minM + rangeM)

    print(n)
    print(m)

    clauses = []
    for j in range(m):
        clauses.append([genLiteral(n), genLiteral(n), genLiteral(n)])

    path = random.randint(0, 1)
    s1 = Solver(name='g3')
    s1.append_formula(clauses)
    guess = []

    if(path == 0):
        if(s1.solve()):
            guess = s1.get_model()
        else:
            guess = genGuess(n)
            path = 1
    else:
        guess = genGuess(n)
        if(s1.solve(assumptions=guess)):
            path = 0

    s1.delete()

    counter = 0
    req = "next"
    while req == "next":
        if counter > (math.log(p) / math.log(1 - 1/m)) + 30:
            print("Too many tries.")
            exit(0)
        temp = perm.permutation(clauses)
        print("permuted")
        clause = input(": ")
        try:
            clause = int(clause)
        except:
            print("bad input")
            exit(0)
        if not (clause in range(1, m + 1)):
            print("out of bounds")
            exit(0)

        clause = temp[clause - 1]
        output = [literal == guess[abs(literal) - 1] for literal in clause]
        print(output)
        counter += 1

        req = input()

    if (req == "true" and path == 0) or (req == "false" and path == 1):
        probability += 1
    
if probability >= (p * trials):
    print(flag)
else:
    print("Sorry, your rate of success was less than " + str(p))
    