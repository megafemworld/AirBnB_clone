#!/usr/bin/python3
import json

"""serializes instances to a JSON file and deserializes JSON file to instances"""

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        with open(self.__file_path, 'w+', encoding='utf-8') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)


    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**value)
        except Exception as e:
            pass
