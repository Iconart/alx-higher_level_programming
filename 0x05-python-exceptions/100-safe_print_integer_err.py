#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    if __name__ = "__main__":
        try:
            print("{:d}".format(value))
            return True
        except Exception as e:
            print("Exception: ", e, file=sys.stderr)
            return False 
