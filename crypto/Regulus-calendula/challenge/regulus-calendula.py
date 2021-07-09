from collections import Counter
from Crypto.Util.number import *
import sys
import random
import sympy
flag = open('flag.txt','rb').read()
print("Loading... this may take a while.")
p,q = getPrime(4096),getPrime(4096)
e = 0x10001
n = p*q
m = random.randrange(0,n)
c = pow(m,e,n)
d = sympy.mod_inverse(e,(p-1)*(q-1))
def menu(guesses):
    print()
    print("1. Source")
    print("2. Public key")
    print("3. Decrypt")
    print("4. Play")
    print("\nYou have "+str(guesses)+" guesses left.")
    choice = input(": ").strip()
    if choice=="1":
        f = open(__file__)
        print()
        print(f.read())
        print()
        menu(guesses)
    elif choice=="2":
        print("\nn = "+str(n))
        print("e = 65537")
        menu(guesses)
    elif choice=="3":
        d_ = int(input("What is the private key?\n: "))
        if (pow(c,d_,n)==m):
            print("Congrats! Here is your flag:")
            print(flag)
            sys.exit()
        else:
            print("\nSorry, that is incorrect.")
            menu(guesses)
    elif choice=="4":
        if guesses==0:
            print("Sorry, you have no more guesses.")
            menu(0)
        else:
            if guesses>8:
                code = list(hex(p)[2:])
            else:
                code = list(hex(q)[2:])
            guess = input("Make a guess.\n: ")
            while len(guess)!=1024:
                guess = input("Try again.\n: ")
            guess = list(guess)
            a = "".join(["1" if guess[i]==code[i] else "0" for i in range(1024)])
            print(a)
            guesses-=1
            menu(guesses)
    else:
        print("That is not a valid choice.")
        menu(guesses)
while 1:
    menu(16)
