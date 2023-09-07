#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_len = len(sys.argv)
    if (args_len == 1):
        print("0 arguments.")
    elif args_len == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(args_len - 1))
        for i in range(1, args_len):
            print("{0:d}: {1}".format(i, sys.argv[i]))
