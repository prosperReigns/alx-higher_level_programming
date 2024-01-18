#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    hidden_func = dir()
    for names in hidden_func:
        if names.startswith("__"):
            continue
        print(f"{names}")
