#!/usr/bin/python3
"""Tests for the HBnB Facade"""

import unittest  # Import the unittest library
from app import create_app  # Import the Flask app
from app.services.facade import HBnBFacade  # Import the Facade
import app.models

class TestHBnBFacade(unittest.TestCase):  # Create our test class
    test_user = 0

    def setUp(self):  # This runs BEFORE each test
        self.app = create_app()  # Create the Flask app
        self.client = self.app.test_client()  # Client to make requests
        self.facade = HBnBFacade()  # Create the Facade that handles data


    def test_create_place(self):
            """Test that a place can be created"""
            user_data = {
                "first_name": "Lu", 
                "last_name": "Rios", 
                "email": "lu.rios@example.com"
            }
            user = self.facade.create_user(user_data)

            place_data = {
                "title": "Departamento pequeño",
                "description": "Un pequeño departamento en el centro de la ciudad", 
                "price": 50,
                "latitude": 40.0, 
                "longitude": -74.0,
                "owner": user
            }

            place = self.facade.create_place(place_data)  # Create a place
            
            self.assertIsNotNone(place)  # Verify it was created successfully
            self.assertEqual(place.title, "Departamento pequeño")  # Verify the title

    def test_create_place_with_invalid_coordinates(self):
        """Test that a place cannot be created with invalid coordinates"""
        user_data = {
            "first_name": "Lu", 
            "last_name": "Rios", 
            "email": "lu.rios@example.com"
        }
        user = self.facade.create_user(user_data)

        # Place data with invalid coordinates
        place_data = {
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad", 
            "price": 50,
            "latitude": 200.0,  # Invalid latitude
            "longitude": -200.0,  # Invalid longitude
            "owner": user
        }

        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_place(place_data)

        def test_create_place_with_empty_user_data(self):
            """Test that a place cannot be created with empty user data"""
            user_data = {
                "first_name": "", 
                "last_name": "", 
                "email": ""
            }
            
            with self.assertRaises(ValueError):  # Expect an exception to be raised
                user = self.facade.create_user(user_data)
                
                place_data = {
                    "title": "Departamento pequeño",
                    "description": "Un pequeño departamento en el centro de la ciudad", 
                    "price": 50,
                    "latitude": 40.0, 
                    "longitude": -74.0,
                    "owner": user
                }

                self.facade.create_place(place_data)
            
        def test_create_place_with_empty_owner(self):
            """Test that a place cannot be created with an empty owner field"""
            user_data = {
                "first_name": "Lu", 
                "last_name": "Rios", 
                "email": "lu.rios@example.com"
            }
            user = self.facade.create_user(user_data)

            # Place data with empty owner
            place_data = {
                "title": "Departamento pequeño",
                "description": "Un pequeño departamento en el centro de la ciudad", 
                "price": 50,
                "latitude": 40.0, 
                "longitude": -74.0,
                "owner": None  # Empty owner
            }

            with self.assertRaises(ValueError):  # Expect an exception to be raised
                self.facade.create_place(place_data)

        def test_create_place_with_empty_first_name(self):
            """Test that a place cannot be created with an empty first name"""
            user_data = {
                "first_name": "", 
                "last_name": "Rios", 
                "email": "lu.rios@example.com"
            }
        
            with self.assertRaises(ValueError):  # Expect an exception to be raised
                self.facade.create_user(user_data)

        def test_create_place_with_empty_last_name(self):
            """Test that a place cannot be created with an empty last name"""
            user_data = {
                "first_name": "Lu", 
                "last_name": "", 
                "email": "lu.rios@example.com"
            }
        
            with self.assertRaises(ValueError):  # Expect an exception to be raised
                self.facade.create_user(user_data)

        def test_create_place_with_empty_email(self):
            """Test that a place cannot be created with an empty email"""
            user_data = {
                "first_name": "Lu", 
                "last_name": "Rios", 
                "email": ""
            }
        
            with self.assertRaises(ValueError):  # Expect an exception to be raised
                self.facade.create_user(user_data)

        def test_create_place_with_empty_title(self):
            """Test that a place cannot be created with an empty title"""
            user_data = {
                "first_name": "Lu", 
                "last_name": "Rios", 
                "email": "lu.rios@example.com"
            }
            user = self.facade.create_user(user_data)

            place_data = {
                "title": "",  # Empty title
                "description": "Un pequeño departamento en el centro de la ciudad", 
                "price": 50,
                "latitude": 40.0, 
                "longitude": -74.0,
                "owner": user
            }

            with self.assertRaises(ValueError):  # Expect an exception to be raised
                self.facade.create_place(place_data)

        def test_create_place_with_empty_description(self):
            """Test that a place cannot be created with an empty description"""
            user_data = {
                "first_name": "Lu", 
                "last_name": "Rios", 
                "email": "lu.rios@example.com"
            }
            user = self.facade.create_user(user_data)

            place_data = {
                "title": "Departamento pequeño",
                "description": "",  # Empty description
                "price": 50,
                "latitude": 40.0, 
                "longitude": -74.0,
                "owner": user
            }

            with self.assertRaises(ValueError):  # Expect an exception to be raised
                self.facade.create_place(place_data)

        def test_create_place_with_empty_price(self):
            """Test that a place cannot be created with an empty price"""
            user_data = {
                "first_name": "Lu", 
                "last_name": "Rios", 
                "email": "lu.rios@example.com"
            }
            user = self.facade.create_user(user_data)

            place_data = {
                "title": "Departamento pequeño",
                "description": "Un pequeño departamento en el centro de la ciudad", 
                "price": None,  # Empty price
                "latitude": 40.0, 
                "longitude": -74.0,
                "owner": user
            }

            with self.assertRaises(ValueError):  # Expect an exception to be raised
                self.facade.create_place(place_data)

        def test_create_place_with_empty_latitude(self):
            """Test that a place cannot be created with an empty latitude"""
            user_data = {
                "first_name": "Lu", 
                "last_name": "Rios", 
                "email": "lu.rios@example.com"
            }
            user = self.facade.create_user(user_data)

            place_data = {
                "title": "Departamento pequeño",
                "description": "Un pequeño departamento en el centro de la ciudad", 
                "price": 50,
                "latitude": None,  # Empty latitude
                "longitude": -74.0,
                "owner": user
            }

            with self.assertRaises(ValueError):  # Expect an exception to be raised
                self.facade.create_place(place_data)

        def test_create_place_with_empty_longitude(self):
            """Test that a place cannot be created with an empty longitude"""
            user_data = {
                "first_name": "Lu", 
                "last_name": "Rios", 
                "email": "lu.rios@example.com"
            }
            user = self.facade.create_user(user_data)

            place_data = {
                "title": "Departamento pequeño",
                "description": "Un pequeño departamento en el centro de la ciudad", 
                "price": 50,
                "latitude": 40.0, 
                "longitude": None,  # Empty longitude
                "owner": user
            }

            with self.assertRaises(ValueError):  # Expect an exception to be raised
                self.facade.create_place(place_data)