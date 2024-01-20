#!usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        number = my_list[0]
        list_len = len(my_list)
        for j in range(0, list_len - 1):
            if number < my_list[j + 1]:
                number = my_list[j + 1]

        return number
    else:
        return None
