#!/usr/bin/python3

"""Defines a file storage module
"""
import json
from models import base_model


class FileStorage:
    """serializes instances to
    a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """returns the dictionary __objects
        """
        return type(self).__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
            Args:
                obj: dict stores the objects
        """
        key = type(obj).__name__ + "." + obj.id
        type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        d = {}
        for key, value in type(self).__objects.items():
            d[key] = value.to_dict()

        with open(type(self).__file_path, mode="w", encoding="UTF-8") as file:
            json.dump(d, file)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        d = {}
        try:
            with open(type(self).__file_path, encoding="UTF-8") as file:
                d = json.load(file)
        except FileNotFoundError:
            pass

        for value in d.values():
            obj = base_model.BaseModel(**value)
            self.new(obj)
