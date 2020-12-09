#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print("Last digit of", number, "is", end=" ")

num = number % 10

if number < 0:
    num = number % -10
print(num, "and is", end=" ")

if num == 0:
    print("0")
if num < 6:
    print("less than 6 and not 0")
else:
    print("greater than 5")
