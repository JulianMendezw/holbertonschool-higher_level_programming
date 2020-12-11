#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv as ar

    if len(ar) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if ar[2] == "+":
        print("{} + {} = {}".format(ar[1], ar[3], add(int(ar[1]), int(ar[3]))))

    elif ar[2] == "-":
        print("{} - {} = {}".format(ar[1], ar[3], sub(int(ar[1]), int(ar[3]))))

    elif ar[2] == "*":
        print("{} * {} = {}".format(ar[1], ar[3], mul(int(ar[1]), int(ar[3]))))

    elif ar[2] == "/":
        print("{} / {} = {}".format(ar[1], ar[3], div(int(ar[1]), int(ar[3]))))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
