#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    x = len(argv)
    sum = 0
    for i in range(1, x):
        sum += int(argv[i])
    print("{}".format(sum))
