import random
flag = open('flag.txt','r').read()
def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
fibs = [1,1]
for i in range(3,51):
    fibs.append(fibs[i-3]+fibs[i-2])
def lastEl(n):
    if n>50:
        return str(fibonacci(n))[-11:]
    a = ""
    while len(a)<11 and n>0:
        a=str(fibs[n-1])+str(a)
        n-=1
    return int(a[-11:])
def getSum(n):
    r = 0
    for i in range(1,n+1):
        r+=int(lastEl(i))
    return int(str(r)[-11:])
cases = [random.randint(1,1000) for i in range(20)]
print(cases)
for case in cases:
    answer = getSum(case)
    if input(": ")!=str(answer):
        print("Unfortunately, that is incorrect.")
        exit(0)
print(flag)
