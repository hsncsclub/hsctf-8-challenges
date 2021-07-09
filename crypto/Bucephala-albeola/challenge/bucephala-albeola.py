import random
flag = open('/flag.txt','r').read().strip()
print("The flag is all lowercase. Wrap the flag in the flag format, flag{.*}")
square = list("abcdefghiklmnopqrstuvwxyz")
random.shuffle(square)
enc = []
for c in flag[5:-1]:
    if c=="j":
        ind = square.index("i")
    else: ind = square.index(c)
    row = ind//5+1
    col = (ind%5)+1
    enc.append(int(str(row)+str(col)))

def encrypt(pt, key):
    encrypted = []
    for char in range(len(pt)):
        encrypted.append(pt[char]+key[char%len(key)])
    return encrypted
def menu():
    key = input("key: ")
    while not key.isalpha():
        key = input("key: ")
    enc2 = []
    for c in key.lower():
        if c=="j":
            ind = square.index("i")
        else: ind = square.index(c)
        row = ind//5+1
        col = (ind%5)+1
        enc2.append(int(str(row)+str(col)))
    print("enc(flag,key):"," ".join([str(i) for i in encrypt(enc,enc2)]))
while 1:
    menu()
