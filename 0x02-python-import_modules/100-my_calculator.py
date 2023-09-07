#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    import sys
    ac = len(sys.argv)
    if not ac == 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    match sys.argv[2]:
        case "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
            sys.exit(0)
        case "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
            sys.exit(0)
        case "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
            sys.exit(0)
        case "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
            sys.exit(0)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
