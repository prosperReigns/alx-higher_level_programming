#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            pass
        else:
            n += 1

    print("", end="\n")
    return n
