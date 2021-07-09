import random
from fractions import Fraction
from math import gcd
#Script stolen from here: https://gist.github.com/ddddavidee/b34c2b67757a54ce75cb
def outputPrimes(a, n):
	p = gcd(a, n)
	q = int(n // p)
	if p > q:
		p, q = q, p
	return p,q
def RecoverPrimeFactors(n, e, d):
	k = d * e - 1
	if k % 2 == 1:
		failFunction()
		return 0, 0
	else:
		t = 0
		r = k
		while(r % 2 == 0):
			r = int(r // 2)
			t += 1
		for i in range(1, 101):
			g = random.randint(0, n) # random g in [0, n-1]
			y = pow(g, r, n)
			if y == 1 or y == n - 1:
				continue
			else:
				for j in range(1, t): # j \in [1, t-1]
					x = pow(y, 2, n)
					if x == 1:
						p, q = outputPrimes(y - 1, n)
						return p, q
					elif x == n - 1:
						continue
					y = x
					x = pow(y, 2, n)
					if  x == 1:
						p, q = outputPrimes(y - 1, n)
						return p, q
p,q = (RecoverPrimeFactors(n, 65537, d)) #Replace n and d with parameters from challenge
n = p*q
e = 65537
phi = (p-1)*(q-1)
d = inverse_mod(e,phi)
if (d+phi//2)>n:
    print (d-phi//2)
else:
    print(d+phi//2)
