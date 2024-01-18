#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n = len(argv) - 1
    if n < 1:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} arguments.".format(n))
    else:
        print("{} arguments:".format(n))

    for i in range(n):
        print("{}: {}".format(i + 1, argv[i + 1]))
