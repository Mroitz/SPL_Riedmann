import random

Randomnumber = random.randint(0, 100)
print(Randomnumber)

if Randomnumber < 20:
    print("mini")

if 20 <= Randomnumber <= 50:
    print("medium")

if Randomnumber > 50:
    print("Large")
