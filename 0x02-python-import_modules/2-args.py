#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print('0 arguments.')
    else:
        if num == 2:
            print("1 argument:")
            print("1: {}".format(sys.argv[1]))
        else:
            print('{} arguments:'.format(num - 1))
            x = 1
            while x < num:
                print("{}: {}".format(x, sys.argv[x]))
                x += 1
