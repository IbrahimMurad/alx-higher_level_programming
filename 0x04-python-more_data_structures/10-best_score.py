#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is not dict:
        return "None"
    else:
        keys = list(a_dictionary.keys())
        values = list(a_dictionary.values())
        if len(keys) == 0 or len(values) == 0:
            return None
        max_value = max(values)
        max_value_index = values.index(max_value)
        key_of_max_value = keys[max_value_index]
        return key_of_max_value
