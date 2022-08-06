#!/usr/bin/python3
""" Amenity Class """

from models.base_model import BaseModel

Class Amenity(BaseModel):
    """ Amenity Class that inherits from Base Model
        
        Public Class Attribute
        name: (str) - name of the amenity"""
    
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes the Amenity Class
        Args:
            *args: list of strings
            **kwargs: strings dictinnary
            """
            super().__init__(*args, **kwargs)
