#!/usr/bin/python3
"""Class Place"""

from .base import BaseModel
from .user import User


class Place(BaseModel):
    """Class Place, inherits from BaseModel"""

    def __init__(self, title: str, price: float, latitude: float, longitude: float, owner: str, description = None):
        BaseModel.__init__(self)
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    @property
    def title(self):
        return self.title
    
    @title.setter
    def title(self, value):
        if not value or len(value) > 100:
            raise ValueError("Title is required and cannot exceed 100 characters")

    @property
    def description(self):
        return self.description
    
    @description.setter
    def description_set(self, value):
        if len(value) > 100:
            raise ValueError("Title is required and cannot exceed 100 characters")
    
    @property
    def price(self):
        return self.price
    
    @price.setter
    def price_set(self, value):
        if value < 0:
            raise ValueError("Price must be a positive number")
    
    @property
    def latitude(self):
        return self.latitude
    
    @price.setter
    def latitude_set(self, value):
        if value < -90.0 or value > 90.0:
            raise ValueError("Must be within the range of -90.0 to 90.0.")
    
    @property
    def longitude(self):
        return self.longitude
    
    @price.setter
    def longitude_set(self, value):
        if value < -180.0 or value > 180.0:
            raise ValueError("Must be within the range of -180.0 to 180.0.")
    
    @property
    def owner(self):
        return self.owner
    
    @owner.setter
    def owner_set(self, value):
        if not isinstance(value, User):
            raise ValueError()
    
    def add_review(self, review):
        """Add a review to the place."""
        
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        
        self.amenities.append(amenity)