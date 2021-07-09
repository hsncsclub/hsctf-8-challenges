from Crypto.Util.number import *
import random
import sympy
flag = open('flag.txt','rb').read()
p,q = getPrime(1024),getPrime(1024)
e = 0x10001
n = p*q
m = random.randrange(0,n)
c = pow(m,e,n)
d = sympy.mod_inverse(e,(p-1)*(q-1))
def menu():
    print()
    print("1. Key generation algorithm")
    print("2. Public key")
    print("3. Private key")
    print("4. Decrypt")
    choice = input(": ").strip()
    if choice=="1":
        f = open(__file__)
        print()
        print(f.read())
        print()
        menu()
    elif choice=="2":
        print("n = "+str(n))
        print("e = 65537")
        menu()
    elif choice=="3":
        print("d = "+str(d))
        menu()
    elif choice=="4":
        d_ = int(input("What private key you like to decrypt the message with?\n : "))
        if d_%((p-1)*(q-1))==d:
            print("You are not allowed to use that private key.")
            menu()
        if (pow(c,d_,n)==m):
            print("Congrats! Here is your flag:")
            print(flag)
            exit()
        else:
            print("Sorry, that is incorrect.")
            menu()
    else:
        print("That is not a valid choice.")
        menu()
while 1:
    menu()
