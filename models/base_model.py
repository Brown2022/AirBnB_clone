#!/usr/bin/python3
"""
A module that implements the BaseModel python class

"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """

    self.id = str(uuid4())
    self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        This returns the string representation of BaseModel object [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        This updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()


