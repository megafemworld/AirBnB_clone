#!/usr/bin/python3
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)


    def reload(self):
        """deserializes the JSON file to __object"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    self.__objects[key] = obj_class(**value)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error loading data: {e}")
