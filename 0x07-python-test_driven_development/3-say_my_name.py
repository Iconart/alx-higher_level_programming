#!/usr/bin/python3
"""A module of Say my name"""

def say_my_name(first_name, last_name=""):
    """Say my name function

    Args:
        first_name: the first name must a string
        last_name: the second name must be a string
    
    Raises:
        TypeError: raise an error if the first_name or last_name is not a string

    Return:
        print( My name is <first name> <last name>
    """
    
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
