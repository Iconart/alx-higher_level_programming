#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = int(a) / int(b)
    except (ZeroDivisionError, NameError, ValueError):
        result = "none"
    finally:
        print("Inside result: {}".format(result))
    return result
