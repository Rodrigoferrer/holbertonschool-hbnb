from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Adding the review model
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        data = api.payload
        existing_place = facade.get_place(data['title'])
        if existing_place:
            return {'error': 'Place already exists'}, 400
        owner = facade.get_user(data['owner_id'])
        if not owner:
            return {'error': 'Owner not found'}, 404
        data.pop('owner_id')
        data['owner'] = owner
        n_place = facade.create_place(data)
        return {'title': n_place.title, 'description': n_place.description, 'price': n_place.price, 'latitude': n_place.latitude, 'longitude': n_place.longitude, 'owner_id': owner.id}, 201
            

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [{'title': p.title, 'description': p.description, 'price': p.price, 'latitude': p.latitude, 'longitude': p.longitude, 'owner_id': p.owner.id} for p in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return {'title': place.title, 'description': place.description, 'price': place.price, 'latitude': place.latitude, 'longitude': place.longitude, 'owner': {'id': place.owner.id, 'first_name': place.owner.first_name, 'last_name': place.owner.last_name, 'email': place.owner.email}}, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        data = api.payload
        updated_place = facade.update_place(place_id, data)
        if not updated_place:
            return {'error': 'Place not found'}, 404
        return {'title': updated_place.title, 'description': updated_place.description, 'price': updated_place.price, 'latitude': updated_place.latitude, 'longitude': updated_place.longitude}, 200
    