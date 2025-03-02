from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

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
        """Crea un nuevo lugar."""
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """consulta un lugar por ID."""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Obtiene todos los lugares."""
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """actualiza un lugar existente."""
        updated_place = self.place_repo.update(place_id, place_data)
        return updated_place


	# Review
    def create_review(self, review_data):
        """Create a new review and add it to the repository."""
        user = self.user_repo.get(review_data['user_id'])
        place = self.place_repo.get(review_data['place_id'])

        if not user:
            raise ValueError("User not found")
        if not place:
            raise ValueError("Place not found")

        rating = review_data['rating']
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        review = Review(
            text=review_data['text'],
            rating=rating,
            user=user,
            place=place
        )

        self.review_repo.add(review)
        place.add_review(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        return place.reviews

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if review:
            review.update(review_data)
            return review
        return None

    def delete_review(self, review_id):
        review = self.get_review(review_id)
        if review:
            review.place.reviews.remove(review)
            self.review_repo.delete(review_id)
            return True
        return False
