#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
"""Parent class for BaselModel"""

class BaseModel:
    """ All attributes & methods of BaselModel"""
    def __init__(self):
        """ initilization of instance of BaselModel class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of an object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update instance attributes update_at"""
        self.update_at = datetime.now()

    def to_dict(self):
        """return dictionary containing all keys/values"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
