from flask_restful import Resource
from app.models.hotel import HotelModel
from app.resources.request_parser import RequestParser
from flask_jwt_extended import jwt_required


class Hotels(Resource):
    @jwt_required
    def get(self):
        hotels = HotelModel.fetch_all()
        return hotels, 200


class Hotel(Resource):
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel_by_id(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not %s found.' % hotel_id}, 404

    def post(self, hotel_id):
        body = RequestParser().get_body_args()
        hotel = HotelModel.find_hotel_by_id(hotel_id)
        if hotel:
            return {'message': 'Hotel id %s already exists.' % hotel_id}, 422
        new_hotel = HotelModel(hotel_id, **body)
        try:
            new_hotel.save_hotel()
        except:
            return {'message': 'cannot save hotel, internal server error.'}, 500
        return new_hotel.json(), 201

    def put(self, hotel_id):
        body = RequestParser().get_body_args()
        hotel = HotelModel.find_hotel_by_id(hotel_id)
        if hotel:
            hotel.update_hotel(**body)
            hotel.save_hotel()
            return hotel.json(), 200
        new_hotel = HotelModel(hotel_id, **body)
        try:
            new_hotel.save_hotel()
        except:
            return {'message': 'cannot save hotel, internal server error.'}, 500
        return new_hotel.json(), 201

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel_by_id(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'Hotel id %s deleted.' % hotel_id}, 200
        return {'message': 'Hotel id %s not found.' % hotel_id}, 404
