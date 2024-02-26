#!/usr/bin/python3
"""a module for a base class"""
import json

class Base:
    """a base class"""

    __nb_objects = 0
    def __init__(self, id=None):
        self.id= id

        if (self.id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a python string to json

        Args:
            list_dicionary (list): a list of key value pair
        """
        if list_dictionaries == None:
            return "{}"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a json string to a file

        Args:
            cls (obj): the class itself
            list_objs (list): a list of square objects
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
               file.write("[]")
            else:
                my_dict = {}
                my_list = []

                for instance in list_objs:
                    my_dict["id"] = instance.id
                    my_dict["width"] = instance.width
                    my_dict["height"] = instance.height
                    my_dict["x"] = instance.x
                    my_dict["y"] = instance.y

                    my_list.append(my_dict)

                json.dump(my_list, file)

    @staticmethod
    def from_json_string(json_string):
        """ converts json to python object

        Args:
            json_string (str): python object
        """

        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)


    @classmethod 
    def create(cls, **dictionary):
        """converts json to python object

        Args:
            cls (obj): the class itself
            dictionary (dict): key value pair for the dimensions of a square
        """

        dummy_instance = cls(10, 10, 10, 10, 10)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
