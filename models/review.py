#!/usr/bin/python3
""" Review Class """
from models.base_model import BaseModel

Class Review(BaseModel):
    """ Review class inheriting from BaseModel
        
        Public attributes:
            place_id: (str) - string place_id
            user_id: (str) - string user_id
            text: (str) - reaview text """

            place_id = ""
            user_id = ""
            text = ""
            
            def __init__(self, *args, **kwargs):

                """ Review initialization 
                    Args:
                        *args: string list
                        **kwargs: string dictionary
                        """
                    super().__init__(*args, **kwargs)
