#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_keys = [k for k in list(a_dictionary) if a_dictionary[k] == value]
    if len(my_keys) == 0:
        return a_dictionary
    for key in my_keys:
        del a_dictionary[key]
    return a_dictionary
