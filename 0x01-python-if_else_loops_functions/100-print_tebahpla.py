#!/usr/bin/python3
i = 122
while i > 96:
    if i % 2 == 0:
        letter = chr(i)
        print("{}".format(letter), end="")
    else:
        letter = chr(i - 32)
        print("{}".format(letter), end="")
    i -= 1
