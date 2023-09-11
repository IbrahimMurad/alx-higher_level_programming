#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [5, 3, 1, 7]
print_reversed_list_integer(my_list)
my_list = list(range(10))
print_reversed_list_integer(my_list)
my_list = [-1, -2, -3, -4, -5]
print_reversed_list_integer(my_list)
my_list = [-1, 0, 1, 2, 3]
print_reversed_list_integer(my_list)
print_reversed_list_integer([])
print_reversed_list_integer([13])
print_reversed_list_integer([0, 0, 0, 0, 0, 0])
my_list = list(range(1, 1001))
print_reversed_list_integer(my_list)
