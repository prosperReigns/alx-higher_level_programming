#!/usr/bin/python3
"""Idents texts in al line after a special sysbol is encountered"""


def text_indentation(text):
    """Idents a line after special symbole [".", "?", ":"]"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text.strip() == "":
        raise ValueError("text cannot be empty")

    for ch in text:
        if ch in [".", "?", ":"]:
            ch = "\n"
            print("", end="\n")

        print("{}".format(ch), end="")
    print("\n")
