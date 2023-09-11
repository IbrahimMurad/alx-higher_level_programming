#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a == 0:
        temp_a = 0, 0
    elif len_a == 1:
        temp_a = tuple_a[0], 0
    else:
        temp_a = tuple_a[0], tuple_a[1]
    if len_b == 0:
        temp_b = 0, 0
    elif len_b == 1:
        temp_b = tuple_b[0], 0
    else:
        temp_b = tuple_b[0], tuple_b[1]
    t = temp_a[0] + temp_b[0], temp_a[1] + temp_b[1]
    return t
