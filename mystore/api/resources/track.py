from rajaongkir import RajaOngkirApi
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from mystore.models import Item
from mystore.extensions import ma, db


class OngkirSchema(ma.ModelSchema):
    api = RajaOngkirApi('182561962cf94cd52a5a013a6cc058fa')


class Province(Resource):
    def get(self):
        schema = OngkirSchema()
        api = schema.api
        province = api.provinces()
        return province


class City(Resource):
    def get(self):
        schema = OngkirSchema()
        api = schema.api
        cities = api.cities()
        return cities


class CityByProvince(Resource):
    def get(self, province_id):
        schema = OngkirSchema()
        api = schema.api
        cities = api.cities_by_province(province_id)
        return cities


class CityById(Resource):
    def get(self, city_id):
        schema = OngkirSchema()
        api = schema.api
        cities = api.city_by_id(city_id)
        return cities
