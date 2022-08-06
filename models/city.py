#!/usr/bin/python3
""" Class City """
from models.base_model import BaseModel

Class City(BaseModel):

    """ City Class inheriting from BaseModel
        
        Public class attributes
        name: (str) - name of city
        state_id: (str) - state.id
        """
        state_id = ""
        name = ""

        def __init__(self, *args, **kwargs)
            """ Initializes city
                Args:
                    *args: (str) - list of strings
                    **kwargs: (str) - stings dictionary"""
                    super().__init__{*args, **kwargs)
