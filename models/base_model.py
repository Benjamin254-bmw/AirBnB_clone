#!/usr/bin/python3
"""defines the base model class
"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """represents the BaseModel of the BnB project"""

    def __init__(self, *args, **kwargs):
        """initialize a new BaseModel"
        Args:
        *args (any): 
        **kwargs (dict): key, value pairs of attributes.
        """
        tmeform = %Y-%m-%dT%H:%M:%S.%f
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tmeform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.udate_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns dictionary containing all 
        keys/values of __dict__ of the instance:"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """ return the string representation of Basemodel instance"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
