#!/usr/bin/python3
if __name__ == "__main__":
    import sys, hidden_4
    names = dir('hidden_4')
    for name in names:
        if not name.startwith("__"):
            print("{}".format(name))
