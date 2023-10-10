#!/usr/bin/python3
""" In this module, we define a function that
returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object """


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    
    Args:
    	obj (Class): object
     
     Returns:
		dict: dictionary

    """

    return obj.__dict__
