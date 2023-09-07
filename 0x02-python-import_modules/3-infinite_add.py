#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    result = 0
    if argc == 1:
        print("0")
    elif argc == 2:
        print("{}".format(sys.argv[1]))
    else:
        for i in range(1, argc):
            result = result + int(sys.argv[i])
        print("{0:d}".format(result))
