#!/usr/bin/python3

"""Defines a file storage module
"""
import json
import models


class FileStorage:
    """serializes instances to
    a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
            Args:
                obj: dict stores the objects
        """
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        d = {}
        for key, value in FileStorage.__objects.items():
            d[key] = value.to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as file:
            json.dump(d, file)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        d = {}
        try:
            with open(FileStorage.__file_path, encoding="UTF-8") as file:
                d = json.load(file)
        except FileNotFoundError:
            pass

        for value in d.values():
            obj = models.cls_names[value["__class__"]](**value)
            self.new(obj)
