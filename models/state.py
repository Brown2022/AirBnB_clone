#!/usr/bin/python3
""" State Class """
from models.base_model import BaseModel

Class State(BaseModel):
    """ State class inheriting from BaseModel

        Public class attributes:
        name: (str) - state name
        """
        name = ""

        def __init__(self, *args, **kwargs):

            """ Initializez class attributes
                Args:
                    *args: string list
                    **kwargs: string dictionary
                    """
                super().__init__(*args, **kwargs)
