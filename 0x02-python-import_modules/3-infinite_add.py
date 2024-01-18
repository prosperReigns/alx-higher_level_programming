#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    total = 0
    if len(argv) <= 1:
        total = 0
    else:
        for num in range(1, len(argv)):
            total += int(argv[num])

    print(f"{total}")
