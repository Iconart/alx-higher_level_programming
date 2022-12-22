#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_print_integer_err(value):
    try:
    	print("{:d}".format(value))
    except Exception as e:
        oke = file=sys.stderr
        print("Exception: {}".format(e), oke)
        return False
    return True
