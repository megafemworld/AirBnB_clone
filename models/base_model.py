#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""Parent class for BaselModel"""


class BaseModel:
    """ All attributes & methods of BaselModel"""
    def __init__(self, *args, **kwargs):
        
        """ initilization of instance of BaselModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                else:
                    if 'at' in key:
                        value = datetime.fromisoformat(value)
                        setattr(self, key, value)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of an object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        
        """update instance attributes update_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
       
        """return dictionary containing all keys/values"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
