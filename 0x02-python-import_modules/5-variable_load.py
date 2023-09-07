#!/usr/bin/python3
import variable_load_5

if __name__ == "__main__":
    names = dir(variable_load_5)
    for name in names:
        if not name.startswith("__"):
            print("{}".format(variable_load_5.a))
