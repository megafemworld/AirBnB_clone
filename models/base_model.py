#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
"""Parent class for BaselModel"""
class BaselModel:
    """ All attributes & methods of BaselModel"""
    def __init__(self, id, created_at, updated_at):
        """ initilization of instance of BaselModel class"""
        self.id = str(uuuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of an object"""
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        self.update_at = datetime()
