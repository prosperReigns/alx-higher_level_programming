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
        if list_dictionaries == None:
            return "{}"
        else:
            return json.dumps(list_dictionaries)
        
    @classmethod
    def save_to_file(cls, list_objs):
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
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod 
    def create(cls, **dictionary):
        my_list = []
        for key in dictionary.keys():
            if key in ["id", "width", "height", "x", "y"]:
                my_list.append(dictionary[key])
        return cls.update(my_list, **dictionary)
