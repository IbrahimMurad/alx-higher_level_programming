#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_of_keys = [key for key in a_dictionary.keys() if a_dictionary[key] == value]
    if len(list_of_keys) == 0:
        return a_dictionary
    for key in list_of_keys:
        del a_dictionary[key]
    return a_dictionary
