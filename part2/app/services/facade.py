from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()


    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    #Rodrigo- metodo para actualizar usuario
    def update_user(self, user_id, new_info):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        if 'first_name' in new_info:
            user.first_name = new_info['first_name']
        if 'last_name' in new_info:
            user.last_name = new_info['last_name']
        if 'last_name' in new_info:
            user.last_name = new_info['last_name']
        if 'email' in new_info:
            user.email = new_info['email']
        self.user_repo.update(user_id, new_info)
        return user

    def create_amenity(self, amenity_data):
        """Crea un nuevo amenity."""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_all_amenities(self):
        """Obtiene todos los amenities."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Actualiza un amenity existente."""
        amenity = self.amenity_repo.get(amenity_id)
        
        if not amenity_id or not amenity_data:
            return None
        if 'name' in amenity_data:
            amenity.name = amenity_data['name']

        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity
    
    def get(self, amenity_id):
        """Get amenity details by ID"""
        return self.amenity_repo(amenity_id)

    def create_place(self, place_data):
        # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        pass

    def get_place(self, place_id):
        # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        pass

    def get_all_places(self):
        # Placeholder for logic to retrieve all places
        pass

    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        pass

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass

    def create_review(self, review_data):
        # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        pass

    def get_review(self, review_id):
        # Placeholder for logic to retrieve a review by ID
        pass

    def get_all_reviews(self):
        # Placeholder for logic to retrieve all reviews
        pass

    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        pass

    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review
        pass

    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        pass
