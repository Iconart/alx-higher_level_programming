#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i is not x:
            print(my_list[i])
            i += 1
    expect IndexError:
        None
    print()
    return i
