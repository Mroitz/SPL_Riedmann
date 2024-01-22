import random


sum = 0;

while True:
    Randomnumber = random.randint(0, 300)
    print(Randomnumber)
    sum += Randomnumber
    if Randomnumber == 15 or Randomnumber == 25:
        break
        print(sum)


