import unittest
from app.models.review import Review
from app.models.user import User
from app.models.place import Place

class TestReview(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.place = Place()
        self.review = Review("Great place!", 5, self.place, self.user)

    def test_review_initialization(self):
        self.assertEqual(self.review.text, "Great place!")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.place, self.place)
        self.assertEqual(self.review.user, self.user)

    def test_validate_text(self):
        with self.assertRaises(ValueError):
            self.review.validate_text("")
        with self.assertRaises(ValueError):
            self.review.validate_text("   ")
        with self.assertRaises(ValueError):
            self.review.validate_text(123)

    def test_validate_rating(self):
        with self.assertRaises(ValueError):
            self.review.validate_rating(0)
        with self.assertRaises(ValueError):
            self.review.validate_rating(6)
        with self.assertRaises(ValueError):
            self.review.validate_rating("five")

    def test_validate_place(self):
        with self.assertRaises(ValueError):
            self.review.validate_place("Not a place")
        with self.assertRaises(ValueError):
            self.review.validate_place(123)

    def test_validate_user(self):
        with self.assertRaises(ValueError):
            self.review.validate_user("Not a user")
        with self.assertRaises(ValueError):
            self.review.validate_user(123)

            def test_init_with_valid_data(self):
                review = Review("Nice place", 4, self.place, self.user)
                self.assertEqual(review.text, "Nice place")
                self.assertEqual(review.rating, 4)
                self.assertEqual(review.place, self.place)
                self.assertEqual(review.user, self.user)

            def test_init_with_invalid_text(self):
                with self.assertRaises(ValueError):
                    Review("", 4, self.place, self.user)
                with self.assertRaises(ValueError):
                    Review("   ", 4, self.place, self.user)
                with self.assertRaises(ValueError):
                    Review(123, 4, self.place, self.user)

            def test_init_with_invalid_rating(self):
                with self.assertRaises(ValueError):
                    Review("Nice place", 0, self.place, self.user)
                with self.assertRaises(ValueError):
                    Review("Nice place", 6, self.place, self.user)
                with self.assertRaises(ValueError):
                    Review("Nice place", "five", self.place, self.user)

            def test_init_with_invalid_place(self):
                with self.assertRaises(ValueError):
                    Review("Nice place", 4, "Not a place", self.user)
                with self.assertRaises(ValueError):
                    Review("Nice place", 4, 123, self.user)

            def test_init_with_invalid_user(self):
                with self.assertRaises(ValueError):
                    Review("Nice place", 4, self.place, "Not a user")
                with self.assertRaises(ValueError):
                    Review("Nice place", 4, self.place, 123)

if __name__ == '__main__':
    unittest.main()