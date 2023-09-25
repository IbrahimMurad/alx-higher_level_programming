#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
my_list = [1]
has_been_print = safe_print_integer(my_list)
if not has_been_print:
    print("{} is not an integer".format(my_list))

value = -89
has_been_print = safe_print_integer(my_list)
if not has_been_print:
    print("{} is not an integer".format(my_list))

value = "School"
has_been_print = safe_print_integer(my_list)
if not has_been_print:
    print("{} is not an integer".format(my_list))