#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    import sys
    names = dir('hidden_4')
    for name in names:
        if not name.startwith("__"):
            print("{}".format(name))
