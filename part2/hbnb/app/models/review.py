import uuid
from datetime import datetime
from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        """
        Crea una nueva instancia de Review.
        Descubrí que:
        :param text: Contenido de la reseña (string).
        :param rating: Puntuación entre 1 y 5 (entero).
        :param place: Instancia de Place asociada a la reseña.
        :param user: Instancia de User que escribió la reseña.
        """
        super().__init__()
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)

    def validate_text(self, text):
        """Valida que el texto no esté vacío."""
        if not isinstance(text, str) or not text.strip():
            raise ValueError("El texto de la reseña no puede estar vacío.")
        return text

    def validate_rating(self, rating):
        """Valida que la calificación esté entre 1 y 5."""
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("La calificación debe estar entre 1 y 5.")
        return rating

    def validate_place(self, place):
        """Valida que la reseña esté asociada a un lugar válido."""
        if not isinstance(place, Place):
            raise ValueError("El objeto place debe ser una instancia de Place.")
        return place

    def validate_user(self, user):
        """Valida que la reseña tenga un usuario válido."""
        if not isinstance(user, User):
            raise ValueError("El objeto user debe ser una instancia de User.")
        return user

    def update_review(self, text=None, rating=None):
        """
        Permite actualizar el texto y/o la calificación de la reseña.

        :param text: Nuevo contenido de la reseña.
        :param rating: Nueva calificación entre 1 y 5.
        """
        if text is not None:
            self.text = self.validate_text(text)
        if rating is not None:
            self.rating = self.validate_rating(rating)
        self.save()

    def __str__(self):
        """Devuelve una representación legible de la reseña."""
        return f"Review(id={self.id}, text='{self.text}', rating={self.rating}, user={self.user.id}, place={self.place.id})"

    def __repr__(self):
        """Devuelve una representación en string que permite recrear la instancia."""
        return f"Review(text={repr(self.text)}, rating={self.rating}, place={repr(self.place)}, user={repr(self.user)})"
