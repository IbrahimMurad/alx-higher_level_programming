#!/usr/bin/python3
def no_c(my_string):
    temp_str = ""
    for c in my_string:
        if not (c == 'c' or c == 'C'):
            temp_str = temp_str + c
    return temp_str
