#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    if num == 1:
        print('0')
    else:
        x = 1
        oke = 0
        while x < num:
            num1 = int(argv[x])
            oke += num1
            x += 1
        print(oke)
