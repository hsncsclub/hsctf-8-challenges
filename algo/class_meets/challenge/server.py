import os
import sys
import random
import time
import signal
from threading import Timer, Event

cases = os.listdir("saved")

answered = Event()

for file in cases:
   print(file)

def handler(signum, frame):
    if not answered.is_set():
        print("TLE. Good night.")
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)

for i in range(15):
    print("Please wait a moment for a case to be generated...")
    case = open("../saved/" + random.choice(cases)).read()
    time.sleep(3)
    signal.alarm(3)
    answered.clear()
    send, expect = case.split("\n\n")
    print("Here's case" + {i+1} + "!")
    print(send)
    s = input()
    if s == expect:
        print("Congrats, that's right!")
        answered.set()
    else:
        print("No, you're wrong, get out!")
        sys.exit(0)

print("Wow, you really know your scheduling!")
print("Take this flag!")
print(open("flag.txt").read())
