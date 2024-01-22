import random

def adder(number1, number2):
    return number1 + number2

def randomnumber():
    return random.randint(100, 200)

def randomword(word_array):
    return random.choice(word_array)

number1 = 1;
number2 = 5;

result = adder(number1,number2)
print(result)

randomzahl = randomnumber()
print(randomzahl)

Liste = ("hallo", "ola", "grüezi", "hello")
randomwort = randomword(Liste)
print(randomwort)
