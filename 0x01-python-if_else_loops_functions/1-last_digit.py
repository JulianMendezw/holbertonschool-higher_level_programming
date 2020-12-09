#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, "is", end=" ")

if number < 0:
    number = -(number)
number = number % 10
print(number, "and is", end=" ")
if number == 0:
    print("0")
elif number < 6:
    print("less than 6 and not 0")
else:
    print("greater than 5")
