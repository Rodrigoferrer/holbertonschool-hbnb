from app.persistence.repository import InMemoryRepository
from app.models.user import User

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
            user.first_name = new_info[first_name]
        if 'last_name' in new_info:
            user.last_name = new_info[last_name]
        if 'last_name' in new_info:
            user.last_name = new_info[last_name]
        if 'email' in new_info:
            user.email = new_info[email]
        return self.user_repo.update(user_id, new_info)

        
    

        







    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass


    