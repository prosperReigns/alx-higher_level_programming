#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    list_len = len(my_string)
    for i in range(list_len):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        else:
            new_str += my_string[i]

    return new_str
