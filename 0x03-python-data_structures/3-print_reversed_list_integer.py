#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in range(1, len(my_list)):
        print("{}".format(my_list[-i]))
    print("{}".format(my_list[0]))
