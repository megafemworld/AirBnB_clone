#!/usr/bin/python3i
import json
"""serializes instances to a JSON file and deserializes JSON file to instances"""

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @property
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    @objects.setter
    def new(self. obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump(self._object, f)


    def reload(self):
        """deserializes the JSON file to __objects"""
        if self.__file_path:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(self.__file_path)
