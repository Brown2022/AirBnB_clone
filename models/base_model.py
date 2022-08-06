#!/usr/bin/python3
"""
A modules that implements the BaseModel python class and define all common attributes/methids for all other classes

"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize the base model
        """
        from models import storage

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ("created_at", "updated_at"):
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)


    def __str__(self):
        """
        This returns the string representation of BaseModel object [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        This updates updated_at with the current datetime
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This function returns a dictionary containing all keys/values of __dict__ of thw instance:
        - Only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        -created_at and updated_at must be converted to string object in ISO
        """

        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        for i, j in self.__dict__.items():
            if i in ("created_at", "updated_at"):
                j = self.__dict__[i].isoformat()
                dict_copy[i] = j
        return dict_copy
