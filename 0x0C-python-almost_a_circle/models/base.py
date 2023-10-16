#!/usr/bin/python3
""" In this module, we define Base class
that has a private attribute and a constructor
"""
import json


class Base:
    """ This class will be the “base”
    of all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes id """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """

        file_name = cls.__name__ + ".json"
        if list_objs is None:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write("[]")
        else:
            my_list = [obj.to_dictionary() for obj in list_objs]
            with open(file_name, 'w', encoding="utf-8") as f:
                json.dump(my_list, f)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """

        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """

        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                json_string = f.read()
                list_of_dict = cls.from_json_string(json_string)
                return [cls.create(**dict) for dict in list_of_dict]
        except FileNotFoundError:
            return []
