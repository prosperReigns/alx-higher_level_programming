#!/usr/bin/python3
"""this program gives the full name of a person"""


def say_my_name(first_name, last_name=""):
    """
    says the user full name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name.strip() == "":
        raise ValueError("first name cannot be blank")

    print(f'My name is {first_name} {last_name}')
