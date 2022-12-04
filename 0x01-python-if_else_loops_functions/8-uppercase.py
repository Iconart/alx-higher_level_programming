#!/usr/bin/python3
def uppercase(str):
    last = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            letter = ord(i) - 32
            last += chr(letter)
        else:
            last += i
    return(last)
