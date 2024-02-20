#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []

for lst in argv[1:]:
    my_list.append(lst)
save_to_json_file(my_list, "add_item.json")