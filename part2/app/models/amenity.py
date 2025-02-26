#!/usr/bin/python3
""" Class User """

'''
Requiurements:
id (String): Unique identifier for each amenity.
name (String): The name of the amenity (e.g., "Wi-Fi", "Parking"). Required, maximum length of 50 characters.
created_at (DateTime): Timestamp when the amenity is created.
updated_at (DateTime): Timestamp when the amenity is last updated.
'''

from app.models.base import BaseModel

class Amenity(BaseModel):
    ''' Class Amenity, inherits from BaseModel '''
    
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or len(value) > 50:
            raise ValueError("Name is required and cannot exceed 50 characters")
        self._name = value
