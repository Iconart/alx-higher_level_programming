#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    element = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            element.append(True)
        else:
            element.append(False)
        i += 1
    return (element)
