import unittest  # Importamos la librería para hacer pruebas
from app import create_app  # Importamos la app Flask
from app.services.facade import HBnBFacade  # Importamos la Facade
import app.models



class TestHBnBFacade(unittest.TestCase):  # Creamos nuestra clase de pruebas
    test_user = 0
    def setUp(self):  # Esto se ejecuta ANTES de cada prueba
        self.app = create_app()  # Creamos la app de Flask
        self.client = self.app.test_client()  # Cliente para hacer peticiones
        self.facade = HBnBFacade()  # Creamos la Facade que maneja los datos


    def test_create_user(self):  
        """Prueba que se pueda crear un usuario"""
        user_data = {
            "first_name": "Jhon", 
            "last_name": "doe", 
            "email": "jhon.doe@example.com"
        }
        
        user = self.facade.create_user(user_data)  # Creamos un usuario
        test_user =user

        self.assertIsNotNone(user)  
        self.assertEqual(user.first_name, "Jhon")


    def test_create_user2(self):  
        """Prueba que no se pueda crear un usuario con el nombre vacío"""
        user_data = {
        "first_name": "", 
        "last_name": "Doe", 
        "email": "juan.doe@example.com"
    }
    
        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_user(user_data)
    
    def test_create_user3(self):  
        """Prueba que no se pueda crear un usuario con el nombre vacío"""
        user_data = {
        "first_name": "Jhon", 
        "last_name": "", 
        "email": "jhon.doe@example.com"
    }

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_user(user_data)

    def test_create_user4(self):  
        """Prueba que no se pueda crear un usuario con el nombre vacío"""
        user_data = {
        "first_name": "jhon", 
        "last_name": "doe", 
        "email": ""
    }

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_user(user_data)

    def test_create_user5(self):  
        """Prueba que no se pueda crear un usuario con el nombre vacío"""
        user_data = {
        "first_name": "jhon", 
        "last_name": "doe", 
        "email": "jhon.doeexample.com"
    }

    

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_user(user_data)

    
    def test_create_user6(self):  
        """Prueba que no se puede sin .com"""
        user_data = {
        "first_name": "jhon", 
        "last_name": "doe", 
        "email": "jhon.doeexample"
    }

    

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_user(user_data)

    def test_create_user_7(self):  
        """Prueba que no se puede sin .com"""
        user_data = {
        "first_name": "", 
        "last_name": "", 
        "email": ""
    }

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_user(user_data)
    

    def test_create_user7(self):  
        """Prueba que no se puede sin .com"""
        user_data = {
        "first_name": "123434234", 
        "last_name": "3232323", 
        "email": "7855665465456"
    }

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_user(user_data)

    def test_create_user_8(self):  
        """Prueba que no se puede sin .com"""
        user_data = {
        "first_name": "1234", 
        "last_name": "doe", 
        "email": "jhon.doeexample"
    }

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_user(user_data)


    def test_create_user_10(self):  
        """Prueba que no se puede sin .com"""
        user_data = {
        "first_name": "jhon", 
        "last_name": "12344", 
        "email": "jhon.doeexample"
    }

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_user(user_data)

    def test_create_user_12(self):  
        """Prueba que no se puede sin .com"""
        user_data = {
        "first_name": "Jhon", 
        "last_name": "doe", 
        "email": "1515654"
    }

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_user(user_data)



    def test_create_amenity(self):
        """Prueba que se pueda crear un amenity"""
        amenity_data = {"name": "WiFi"}  # Amenity de ejemplo
        
        amenity = self.facade.create_amenity(amenity_data)  # Creamos un amenity
        
        self.assertIsNotNone(amenity)  # Verificamos que se creó bien
        self.assertEqual(amenity.name, "WiFi")  # Verificamos que el nombre sea correcto
    

    def test_create_amenity2(self):
        """Prueba que no se pueda crear un amenity con el nombre vacío"""
        amenity_data = {"name": ""}  # Amenity de ejemplo
    
        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_amenity(amenity_data)

    def test_create_amenity3(self):
        """Prueba que no tengas mas de 50 caracteres"""
        amenity_data = {"name": "dasjdkasdkasjdkasjdkasdjaslkdjaskdjasdklasjdassadasdasdsadasd"}  # Amenity de ejemplo
    
        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_amenity(amenity_data)




    def test_create_place(self):
        """Prueba que se pueda crear un lugar"""
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

        
        

        place = self.facade.create_place(place_data)  # Creamos un lugar
        
        self.assertIsNotNone(place)  # Verificamos que se creó bien
        self.assertEqual(place.title, "Departamento pequeño")  # Verificamos el título

    def test_create_place_invalid_coordinates(self):
        """Prueba que no se pueda crear un lugar con coordenadas inválidas"""
        user_data = {
            "first_name": "Lu", 
            "last_name": "Rios", 
            "email": "lu.rios@example.com"
        }
        user = self.facade.create_user(user_data)

        # Datos del lugar con coordenadas inválidas
        place_data = {
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad", 
            "price": 50,
            "latitude": 200.0,  # Latitud inválida
            "longitude": -200.0,  # Longitud inválida
            "owner": user
        }

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_place(place_data)

    def test_create_place_with_empty_user_data(self):
        """Prueba que no se pueda crear un lugar con datos de usuario vacíos"""
        user_data = {
            "first_name": "", 
            "last_name": "", 
            "email": ""
        }
        
        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
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
        """Prueba que no se pueda crear un lugar con el campo owner vacío"""
        user_data = {
            "first_name": "Lu", 
            "last_name": "Rios", 
            "email": "lu.rios@example.com"
        }
        user = self.facade.create_user(user_data)

        # Datos del lugar con owner vacío
        place_data = {
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad", 
            "price": 50,
            "latitude": 40.0, 
            "longitude": -74.0,
            "owner": None  # Owner vacío
        }

        with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
            self.facade.create_place(place_data)

    def test_create_place_with_empty_first_name(self):
    """Prueba que no se pueda crear un lugar con el campo first_name vacío"""
    user_data = {
        "first_name": "", 
        "last_name": "Rios", 
        "email": "lu.rios@example.com"
    }
    
    with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
        self.facade.create_user(user_data)

def test_create_place_with_empty_last_name(self):
    """Prueba que no se pueda crear un lugar con el campo last_name vacío"""
    user_data = {
        "first_name": "Lu", 
        "last_name": "", 
        "email": "lu.rios@example.com"
    }
    
    with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
        self.facade.create_user(user_data)

def test_create_place_with_empty_email(self):
    """Prueba que no se pueda crear un lugar con el campo email vacío"""
    user_data = {
        "first_name": "Lu", 
        "last_name": "Rios", 
        "email": ""
    }
    
    with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
        self.facade.create_user(user_data)

def test_create_place_with_empty_title(self):
    """Prueba que no se pueda crear un lugar con el campo title vacío"""
    user_data = {
        "first_name": "Lu", 
        "last_name": "Rios", 
        "email": "lu.rios@example.com"
    }
    user = self.facade.create_user(user_data)

    place_data = {
        "title": "",  # Título vacío
        "description": "Un pequeño departamento en el centro de la ciudad", 
        "price": 50,
        "latitude": 40.0, 
        "longitude": -74.0,
        "owner": user
    }

    with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
        self.facade.create_place(place_data)

def test_create_place_with_empty_description(self):
    """Prueba que no se pueda crear un lugar con el campo description vacío"""
    user_data = {
        "first_name": "Lu", 
        "last_name": "Rios", 
        "email": "lu.rios@example.com"
    }
    user = self.facade.create_user(user_data)

    place_data = {
        "title": "Departamento pequeño",
        "description": "",  # Descripción vacía
        "price": 50,
        "latitude": 40.0, 
        "longitude": -74.0,
        "owner": user
    }

    with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
        self.facade.create_place(place_data)

def test_create_place_with_empty_price(self):
    """Prueba que no se pueda crear un lugar con el campo price vacío"""
    user_data = {
        "first_name": "Lu", 
        "last_name": "Rios", 
        "email": "lu.rios@example.com"
    }
    user = self.facade.create_user(user_data)

    place_data = {
        "title": "Departamento pequeño",
        "description": "Un pequeño departamento en el centro de la ciudad", 
        "price": None,  # Precio vacío
        "latitude": 40.0, 
        "longitude": -74.0,
        "owner": user
    }

    with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
        self.facade.create_place(place_data)

def test_create_place_with_empty_latitude(self):
    """Prueba que no se pueda crear un lugar con el campo latitude vacío"""
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
        "latitude": None,  # Latitud vacía
        "longitude": -74.0,
        "owner": user
    }

    with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
        self.facade.create_place(place_data)

def test_create_place_with_empty_longitude(self):
    """Prueba que no se pueda crear un lugar con el campo longitude vacío"""
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
        "longitude": None,  # Longitud vacía
        "owner": user
    }

    with self.assertRaises(ValueError):  # Esperamos que se lance una excepción
        self.facade.create_place(place_data)
    
    def test_get_all(self):
        """Prueba que se puedan obtener todos los elementos"""
        
        users = self.facade.get_all()  # Obtenemos todos los usuarios
        amenities = self.facade.get_all_amenities()  # Obtenemos todos los amenities
        places = self.facade.get_all_places()  # Obtenemos todos los lugares
        
        # Verificamos que cada uno sea una lista (aunque esté vacía)
        self.assertIsInstance(users, list)
        self.assertIsInstance(amenities, list)
        self.assertIsInstance(places, list)

    def test_get_by_id(self):
        """Prueba que se pueda obtener un usuario por su ID"""
        
        # Creamos un usuario de prueba
        user_data = {
            "first_name": "Test", 
            "last_name": "User", 
            "email": "test@example.com"
        }
        user = self.facade.create_user(user_data)
        
        # Lo buscamos por su ID
        fetched_user = self.facade.get_user(user.id)
        
        # Comprobamos que es el mismo usuario
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.email, "test@example.com")

    def test_update_user(self):
        """Prueba que se pueda actualizar un usuario"""
        
        # Creamos un usuario
        user_data = {
            "first_name": "Luis", 
            "last_name": "Gómez", 
            "email": "luis.gomez@example.com"
        }
        user = self.facade.create_user(user_data)
        
        # Actualizamos el nombre
        updated_user = self.facade.update_user(user.id, {"first_name": "Carlos"})
        
        # Comprobamos que el nombre cambió
        self.assertEqual(updated_user.first_name, "Carlos")

# Esto ejecuta las pruebas cuando corremos el archivo
if __name__ == '__main__':
    unittest.main()