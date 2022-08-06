#!/usr/bin/python3
"""
This contains the FileStorage class model
"""

import json
from os import read
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
import os.path


class FileStorage:
    """
    This takes care of serializing instances to a JSON file and deserializing JSON file to instances
    """
    def __init__(self):
        """ Initializes FileStorage """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        This returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        This sets in obj the `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        This serializes objects to the JSON file
        """

        with open(self.__file_path, mode="w") as f:
            store_dict = {}
            for k, v in self.__objects.items():
                store_dict[k] = v.to_dict()
            json.dump(store_dict, f)

    def reload(self):
        """
        This deserializes the JSON file to __objects : only if it exists
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
