#!/usr/bin/python3
"""Class User"""

from  app.models.base import BaseModel
from email_validator import validate_email, EmailNotValidError


class User(BaseModel):
    """Class User, inherits from BaseModel"""
    
    def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Your name cannot include numbers, only letters")
        self._first_name = value





    