#!/usr/bin/python3
""" Place Class"""
from models.base_model import BaseModel

Class PLace(BaseModel):
    """ The PLace class inheriting from BaseModel
    Public class attributes:
    city_id: (str) - string city_id
    user_id: (str) - string user_id
    name_ie: (str) - name of the place
    number_rooms:(int) - number of rooms
    bomber_bathrooms: (int) - number of bathrooms
    max_quest: (int) - Maximum number of guest to be accomodated
    price_by_night: (int) - per night price
    latitude: (float) - place latitude
    longitude: (float) - place longitude
    amenity_ids: (list) - amenity.id list"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_room = 0
    number_bathrooms = 0
    max_quest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):

        """ Initializes Class Place 
        Args:
            *args: (str) string lists
            **kwargs: (str) strings dictionary
            """
            super().__init__(*args, **kwargs)
