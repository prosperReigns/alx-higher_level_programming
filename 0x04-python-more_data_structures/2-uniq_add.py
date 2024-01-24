#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_list = set(my_list)
    total = 0
    for i in my_list:
        total += i
    return total
