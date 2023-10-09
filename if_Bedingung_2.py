import random

Randomnumber = random.randint(0, 100)
print(Randomnumber)

Randomnumber2 = random.randint(0, 100)
print(Randomnumber2)

if 50 > Randomnumber < Randomnumber2:
    print("Zahl 1 ist kleiner als Zahl 2")
    print("Mini")

if Randomnumber < 30 or Randomnumber2 <30:
    print("Eine der beiden ist kleiner als 30")

if Randomnumber < 50 and Randomnumber2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")