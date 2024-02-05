#!/usr/bin/python3

def safe_print_integer(value):
    try:
        val = int(value)
    except ValueError:
        pass
    else:
        print("{:d}".format(val), end="\n")
        return True
