#!/usr/bin/python3
def upppercase(str):
    for element in str:
        if ord(element) >= 97 and ord(element) <= 122:
            last = ord(element) - 32
            print("()".format(chr(last)), end="")
        else:
            print("{}".format(element), end="")
